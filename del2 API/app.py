import yaml
from apiflask import APIFlask, Schema
from apiflask.fields import Integer, String

app = APIFlask(__name__)

class PatientIn(Schema):
    first_name = String(required=True)
    last_name = String(required=True)
    age = Integer()
    bloodtype = String(required=True)
    allergies = String(required=True)


def read_yaml():
    with open("patients.yml") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        return yaml_data


def write_yaml(data):
    with open("patients.yml", "w") as y:
        yaml.dump(data, y)


@app.post("/add_patient")
@app.input(PatientIn)
def add_new_patient(json_data):
    print(json_data)
    data = read_yaml()
    new = data.get("patients").get("id")
    new.setdefault(len(new) + 1, json_data)
    write_yaml(data)
    return {"message": "created"}, 201