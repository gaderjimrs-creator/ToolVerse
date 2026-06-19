import json


class jsontools:
    """
    JSON utility class
    """

    def read_json(self, file_path):
        """
        Read JSON file and return data
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def write_json(self, file_path, data):
        """
        Write data to JSON file
        """
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def pretty_print(self, data):
        """
        Return formatted JSON string
        """
        return json.dumps(data, indent=4)

    def validate_json(self, json_string):
        """
        Validate JSON string
        """
        try:
            json.loads(json_string)
            return True
        except json.JSONDecodeError:
            return False

    def json_to_string(self, data):
        """
        Convert Python object to JSON string
        """
        return json.dumps(data)

    def string_to_json(self, json_string):
        """
        Convert JSON string to Python object
        """
        return json.loads(json_string)
    
    def merge_json(self, data1, data2):
        return json.merge(data1, data2)

# Aliases
JsonTools = jsontools
JSONTOOLS = jsontools
