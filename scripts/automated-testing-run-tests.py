# This file is ran by github workflows. There is no need to install any dependencies in this file or to run it manually.

import json
import unittest


class JSONTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results.append({"test": str(test), "outcome": "success"})

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.results.append({"test": str(test), "outcome": "failure", "error": self._exc_info_to_string(err, test)})

    def addError(self, test, err):
        super().addError(test, err)
        self.results.append({"test": str(test), "outcome": "error", "error": self._exc_info_to_string(err, test)})


class JSONTestRunner(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        return result

    def _makeResult(self):
        return JSONTestResult(self.stream, self.descriptions, self.verbosity)

    def generate_json_report(self, result, output_file):
        with open(output_file, "w") as f:
            json.dump({"results": result.results}, f, indent=2)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")

    runner = JSONTestRunner(verbosity=2)
    result = runner.run(suite)

    # Write the result to a JSON file
    runner.generate_json_report(result, "test_results/test_output.json")
