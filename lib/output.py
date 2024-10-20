import csv
import json


class outputWriter:
    """
    This class is made to write the output of parse_ functions to either CSV or JSON (Json is W.I.P)
    the write_csv function takes a list like this [["column","column2"],["row1_col1","row1_col2"]] and writes it to a csv like this
    column1,column2
    row1_col1,row1_col2

    This is to reduce code reuse in the parsing functions
    """

    def __init__(self, output: str, user: str, browser: str, profile: str = ""):
        self.output_directory = output
        self.user = user
        self.browser = browser
        self.profile = profile
        if self.profile:
            self.filename = f"{self.output_directory}{self.user}_{self.browser}_{self.profile}"
        else:
            self.filename = f"{self.output_directory}{self.user}_{self.browser}"

    def write_csv(self, datatype: str, content: list):
        with open(f"{self.filename}_{datatype}.csv", "w+", newline="", encoding="UTF-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            for line in content:
                csv_writer.writerow(line)

    def write_json(self, datatype: str, content: list):
        headers = content.pop(0)  # Remove the first element to remove the headers
        try:
            with open(f"{self.filename}_{datatype}.json", "r") as file:
                existing_json = json.load(file)
        except FileNotFoundError:
            existing_json = []

        new_json = []
        # Loop through the entries and add them to new JSON
        for entry in content:
            json_data = {}
            for header, value in zip(headers, entry):
                json_data[header] = value
            new_json.append(json_data)

        existing_json.extend(new_json)

        # Write updated JSON to file:
        with open(f"{self.filename}_{datatype}.json", "w", encoding="UTF-8") as file:
            json.dump(existing_json, file, indent=4)
