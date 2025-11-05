import yaml
from apiflask import APIFlask

app = APIFlask(__name__)

def read_yaml():
    with open("patients.yml") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        return yaml_data


def write_yaml():
    data = read_yaml()
    new = data.get("patients").get("id")
    new.setdefault(len(new) + 1, d)
    with open("patients.yml", "w") as y:
        yaml.dump(data, y)
    return new

app@route("/")
def home():
    return "Hello, World"