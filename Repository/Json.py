import json
from Models.Entry import Entry


class Json:
    @staticmethod
    def get_data(filepath):
        with open(filepath) as f:
            data = json.load(f)
            json_data = data["data"]

        return json_data # list of dicts

    @staticmethod
    def create_models(filepath):
        models_list = []

        for i in Json().get_data(filepath):
            models_list.append(Entry(i["key"], i["value"], i["ts"]))

        return models_list


