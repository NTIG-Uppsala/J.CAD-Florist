# This file is ran by github workflows. There is no need to install any dependencies in this file or to run it manually.

import xmltodict, json
import os


def convert_xml_to_json(xml_path, json_path):
    with open(xml_path) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        with open(json_path, "w") as json_file:
            json.dump(data_dict, json_file, indent=4)


if __name__ == "__main__":
    xml_report = "test-reports/TESTS-TestSuite.xml"
    json_report = "test.results.json"

    if os.path.exists(xml_report):
        convert_xml_to_json(xml_report, json_report)
        print(f"Test results saved to {json_report}")
    else:
        print(f"XML report not found: {xml_report}")
