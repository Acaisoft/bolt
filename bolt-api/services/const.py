# Copyright (c) 2022 Acaisoft
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

SELFTEST_FLAG = 'BOLT_API_SELFTEST_FLAG'
HASURA_CLIENT_USER_ID = '7f1aab7a-e941-46a2-b63a-5b28b80ad384'
HASURA_DEVELOPMENT_ACCESS_KEY = 'devaccess'
HASURA_GQL = 'HASURA_GQL'
CLOUDSDK_CORE_PROJECT = 'CLOUDSDK_CORE_PROJECT'
IMAGE_REGISTRY_ADDRESS = 'IMAGE_REGISTRY_ADDRESS'
GOOGLE_LOGS_BUCKET = 'GOOGLE_LOGS_BUCKET'

# Auth
AUTH_PROVIDER = 'AUTH_PROVIDER'

JWT_ALGORITHM = 'JWT_ALGORITHM'
JWT_VALID_PERIOD = 'JWT_VALID_PERIOD'
AUTH_LOGIN = 'AUTH_LOGIN'
AUTH_PASSWORD = 'AUTH_PASSWORD'
AUTH_USER_ID = 'AUTH_USER_ID'
JWT_AUTH_PRIV_KEY = 'JWT_AUTH_PRIV_KEY'
JWT_AUTH_PUB_KEY = 'JWT_AUTH_PUB_KEY'

AUTH0_CLIENT_ID = 'AUTH0_CLIENT_ID'
AUTH0_CLIENT_SECRET = 'AUTH0_CLIENT_SECRET'
AUTH0_AUDIENCE = 'AUTH0_AUDIENCE'
AUTH0_BASE_URL = 'AUTH0_BASE_URL'

AUTH = {
    'BOLT': {
        'vars': [
            AUTH_LOGIN,
            AUTH_PASSWORD,
            AUTH_USER_ID,
            JWT_ALGORITHM,
            JWT_VALID_PERIOD,
            JWT_AUTH_PRIV_KEY
        ]
    },
    'AUTH0': {
        'vars': [
            AUTH0_CLIENT_ID,
            AUTH0_CLIENT_SECRET,
            AUTH0_AUDIENCE,
            AUTH0_BASE_URL
        ]
    }
}

# Argo
ARGO_KUBE_NAMESPACE = 'ARGO_KUBE_NAMESPACE'
ARGO_HELM_RELEASE_NAME = 'ARGO_HELM_RELEASE_NAME'
ARGO_CONTAINER_RESOURCES = 'ARGO_CONTAINER_RESOURCES'

# storage services
AZURE_ACCOUNT_NAME = "AZURE_ACCOUNT_NAME"
AZURE_ACCOUNT_KEY = "AZURE_ACCOUNT_KEY"
S3_KEY_ID = "S3_KEY_ID"
S3_ACCESS_KEY = "S3_ACCESS_KEY"
S3_REGION = "S3_REGION"
STORAGE_PROVIDERS = {
    'GCP': {
        'env': [
            "GOOGLE_APPLICATION_CREDENTIALS"
        ]
    },
    'AZURE': {
        'vars': [
            AZURE_ACCOUNT_NAME,
            AZURE_ACCOUNT_KEY
        ]
    },
    'S3': {
        'vars': [
            S3_KEY_ID,
            S3_ACCESS_KEY,
            S3_REGION
        ]
    }
}
STORAGE_SERVICE = 'STORAGE_SERVICE'
STORAGE_CONTAINER_NAME = 'STORAGE_CONTAINER_NAME'

ROLE_ADMIN = 'admin'
ROLE_TENANT_ADMIN = 'tenantadmin'
ROLE_MANAGER = 'manager'
ROLE_TESTER = 'tester'
ROLE_READER = 'reader'
ROLE_TESTRUNNER = 'testrunner'  # internal use
ROLE_REPORTGENERATOR = 'reportgenerator'  # internal use
ROLE_CHOICE = (ROLE_ADMIN, ROLE_TENANT_ADMIN, ROLE_MANAGER, ROLE_TESTER, ROLE_READER, ROLE_REPORTGENERATOR)

TENANT_ID = '1'

TESTRUN_INIT = 'INIT'
TESTRUN_PREPARING = 'PENDING'
TESTRUN_PREPARING_FAILED = 'PREPARING FAILED'
TESTRUN_STARTED = 'STARTED'
TESTRUN_RUNNING = 'RUNNING'
TESTRUN_CRASHED = 'CRASHED'
TESTRUN_FAILED = 'FAILED'
TESTRUN_ERROR = 'ERROR'
TESTRUN_TERMINATED = 'TERMINATED'
TESTRUN_FINISHED = 'FINISHED'
TESTRUN_SUCCEEDED = 'SUCCEEDED'

TESTTYPE_LOAD = 'load_tests'
TESTTYPE_CHOICE = (TESTTYPE_LOAD,)

TESTPARAM_USERS = 'load_tests_users'
TESTPARAM_USERS_PER_WORKER = 'load_tests_users_per_worker'
TESTRUN_MAX_USERS_PER_INSTANCE = 1000
TESTRUN_MAX_USERS = 500000
TESTRUN_MAX_DURATION = 28800

MONITORING_MIN_INTERVAL = 2

CONF_SOURCE_JSON = 'test_creator'
CONF_SOURCE_REPO = 'repository'
CONF_SOURCE_CHOICE = (CONF_SOURCE_JSON, CONF_SOURCE_REPO)

IMAGE_CONTENT_TYPES = ('image/png', 'image/jpg', 'image/jpeg', 'image/gif')
UPLOADS_MAX_SIZE_BYTES = 5000000
UPLOADS_PUBSUB_SUBSCRIPTION = 'uploads-bolt-acaisoft'

REQUIRED_BOLT_API_CONFIG_VARS = (
    'HASURA_GQL',
    'HASURA_GRAPHQL_ACCESS_KEY',
    'ARGO_CONTAINER_RESOURCES',
    'STORAGE_SERVICE',
    'STORAGE_CONTAINER_NAME',
)

REQUIRED_ENV_VARS = (
    'ARGO_KUBE_NAMESPACE',
    'ARGO_HELM_RELEASE_NAME',
    'CLOUDSDK_CORE_PROJECT',
    'IMAGE_REGISTRY_ADDRESS',
    'GOOGLE_LOGS_BUCKET',
)

# default testrunner image, override with IMAGE_BOLT_BUILDER
DEFAULT_IMAGE_BOLT_BUILDER = 'eu.gcr.io/acai-bolt/argo-builder:revival-v4'

# default report generator image, override with IMAGE_REPORT_BUILDER
DEFAULT_IMAGE_REPORT_BUILDER = 'eu.gcr.io/acai-bolt/bolt-reporting:os-test-05'

# allows load tests setup/teardown to work without getting ratelimited by repository hosting
MOCK_REPOSITORY = 'git@mockbitbucket.org:repo'

# configuration extensions
EXTENSION_NFS = 'nfs'
EXTENSION_NFS_MAX_MOUNTS_PER_WORKER = 100
EXTENSION_CHOICE = (EXTENSION_NFS,)

# executions graphs
MAX_GRAPH_POINTS = 1400

# argo images
IMAGE_BOLT_BUILDER = 'IMAGE_BOLT_BUILDER'
IMAGE_REPORT_BUILDER = 'IMAGE_REPORT_BUILDER'

# images upload
BUCKET_PRIVATE_STORAGE = "uploads-bolt-acaisoft"
BUCKET_PUBLIC_UPLOADS = "media.bolt.acaisoft.io"

# stat gathering interval
DEFAULT_STAT_GATHER_INTERVAL = 1
STAT_GATHER_INTERVAL = 2
