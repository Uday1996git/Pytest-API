import requests
import json
import jsonpath

url = "https://thetestingworldapi.com/"


def test_addNewStudent():
    global id
    # id = 10292019
    base_path = "api/studentsDetails"
    obj = open("../Payload/addNewStudentPayload.json", "r")
    body = obj.read()
    request_body = json.loads(body)
    response = requests.post(url + base_path, request_body)
    id = jsonpath.jsonpath(response.json(), "id")
    print(response.json())


def test_addTechnicalSkills():
    base_path = "api/technicalskills"
    obj = open("..//Payload//addNewTechnicalSkills.json", 'r')
    body = obj.read()
    req_body = json.loads(body)
    req_body['id'] = int(id[0])
    req_body['st_id'] = id[0]
    response = requests.post(url + base_path, req_body)
    print(response.json())


def test_getTechnicalDetails():
    base_path = "api/technicalskills/" + str(id[0])
    response = requests.get(url + base_path)
    print(response.json())


def test_deleteStudentDetails():
    base_path = "api/studentsDetails/" + str(id[0])
    response = requests.delete(url + base_path)
    print(response.json())

