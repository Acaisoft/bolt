import xml.etree.ElementTree as ET
from apps.bolt_api.app.external_tests.loader import ExternalTestsLoader


class BaseXMLParser:
    def __init__(self, file, data):
        self.project_id = str(data["scenario_id"])
        self.scenario_id = str(data["scenario_id"])
        self.custom_fields = data["custom_fields"]
        self.report_format = data["report_format"]
        self.root = ET.parse(file).getroot()
        self.groups_objects = {}
        self.test_cases_objects = []
        self.test_result_objects = []
        self.test_run_object = {}
        self.loader = ExternalTestsLoader()

