import json


def load_data(filename, default):
    try:
        file = open(filename, "r")
        data = json.load(file)
        file.close()
        return data

    except:
        return default


def save_data(filename, data):
    file = open(filename, "w")
    json.dump(data, file, indent=4)
    file.close()
