import requests
import json
import jsonpath

# def test_oAuth_Token():
#     token_url = "https://rahulshettyacademy.com/oauthapi/oauth2/resourceOwner/token"
#     data = {'grant_type': 'client_credentials', 'client_id': '692183103107-p0m7ent2hk7suguv4vq22hjcfhcr43pj.apps.googleusercontent.com', 'client_secret': 'erZOWM9g3UtwNRj340YYaK_W', 'scope':'trust'}
#     response = requests.post(token_url, data)
#     print(response.text)


def test_postStudentDetails():
    global id
    # id = 10292019
    url = "https://thetestingworldapi.com/api/studentsDetails"
    obj = open("../Payload/addNewStudentPayload.json", "r")
    body = obj.read()
    request_body = json.loads(body)
    response = requests.post(url, request_body)
    id = jsonpath.jsonpath(response.json(), "id")
    print(response.json())


def test_getStudentDetails():
    url = "https://thetestingworldapi.com/api/studentsDetails/" + str(id[0]) + ""
    print(url)
    response = requests.get(url)
    print(response.json())
    actual_id = jsonpath.jsonpath(response.json(), "data.id")
    print(actual_id[0])
    assert actual_id[0] == id[0]

def test_updateStudentDetails():
    url = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])+""
    obj = open("../Payload/updateStudentDetails.json", 'r')
    body = obj.read()
    req_body = json.loads(body)
    req_body['id'] = int(id[0])
    response = requests.put(url, req_body)
    print(response.json())

def test_getUpdatedStudentDetails():
    url = "https://thetestingworldapi.com/api/studentsDetails/" + str(id[0]) + ""
    response = requests.get(url)
    print(response.json())

def test_deleteStudentDetails():
    url = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])+""
    response = requests.delete(url)
    print(response.json())

# def test_JsonData():
#     obj = open("..//Payload//addNewStudentPayload.json", "r")
#     req_body = obj.read()
#     json_body = json.loads(req_body)
#     # json_body['last_name'] = 'Testing Sample'
#     print(json_body['last_name'])
