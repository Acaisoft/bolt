import datetime
from enum import Enum

from apps.bolt_api.app.utils.storage_client import StorageClient
from apps.bolt_api.app.workflow import WorkflowsResource, KubernetesService
from services import const
from services.hasura import hce
from services.hasura.hasura import generate_hasura_token
from services.logger import setup_custom_logger

logger = setup_custom_logger(__name__)


class Status(Enum):
    STATUS_ERROR = 'error'
    STATUS_NOT_GENERATED = 'not_generated'
    STATUS_GENERATING = 'generating'
    STATUS_READY = 'ready'

def generate_report(app_config, execution_id: str) -> str:
    """
    If report for given execution exists, will return signed download url.
    Otherwise, will return a proper message
    """
    logger.info("Report Generation")

    client = StorageClient(app_config)
    file_name = f'reports/{execution_id}.pdf'

    report_status = hce(app_config, '''query ($executionId: uuid!) {
        execution(
            where: { id: { _eq: $executionId } }
        ) {
            report
            }
    }''', variable_values={
        "executionId": execution_id
    })

    if report_status == Status.STATUS_READY:
        if client.file_exists(file_name):
            return client.generate_download_url(blob_name=file_name)
        else:
            trigger_report_generator(client, file_name, execution_id, app_config)
            return "Report was not found. Generating new report."
    elif report_status in [Status.STATUS_NOT_GENERATED, Status.STATUS_ERROR]:
        trigger_report_generator(client, file_name, execution_id, app_config)
        return "Generating report."
    elif report_status == Status.STATUS_GENERATING:
        return "Generating report."

def trigger_report_generator(client: StorageClient, file_name: str, execution_id: str, app_config):
    url = client.generate_upload_url(blob_name=file_name)
    try:
        hasura_token, _ = generate_hasura_token(app_config, const.ROLE_READER)
        workflow_data = {
            'tenant_id': '1',
            'project_id': "",
            'repository_url': "",
            'branch': "",
            'execution_id': str(execution_id),
            'auth_token': hasura_token,
            'duration_seconds': 123,
            'job_pre_start': None,
            'job_load_tests': None,
            'job_monitoring': None,
            'job_post_stop': None,
            'job_report': {
                "env_vars": {
                    "UPLOAD_URL": url
                }
            },
            'no_cache': True,
        }
    except Exception as ex:
        logger.error(f'Failure during Argo workflow data preparation: {ex}')
        raise ex
    try:
        workflow = WorkflowsResource(KubernetesService(app_config))
        workflow_state = workflow.generate_report(workflow_data)
    except Exception as ex:
        logger.error(f'Failure during Argo workflow triggering: {ex}')
        raise ex