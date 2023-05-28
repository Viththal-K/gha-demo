import requests
import pytest

endpoint = "https://todo.pixegami.io/"
# to check all endpoints/docs use -> https://todo.pixegami.io/docs

response = requests.get(endpoint)

# TESTS

def test_can_call_ep():
    response = requests.get(endpoint)
    assert response.status_code == 200

def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    create_res = create_task_response.json()
    print(create_res)

    task_id = create_res["task"]["task_id"]

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200

    get_res = get_task_response.json()
    assert get_res["content"] == payload["content"]
    assert get_res["user_id"] == payload["user_id"]
    assert get_res["is_done"] == payload["is_done"]
    assert get_res["task_id"] == task_id

def test_can_update_item():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id =  create_task_response.json()["task"]["task_id"]

    # update the task
    new_payload = {
                    "user_id": payload["user_id"],
                    "task_id": task_id,
                    "content": "Updated content",
                    "is_done": True
                }
    
    update_task_res = update_task(new_payload)

    # get and validate the change
    assert update_task_res.status_code == 200

    get_task_res = get_task(task_id)
    assert get_task_res.status_code == 200

def test_can_delete_task():
    # create task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id =  create_task_response.json()["task"]["task_id"]

    # delete task
    delete_task_res = delete_task(task_id)

    # get task and check that it's not found
    assert delete_task_res.status_code == 200

    get_task_res = get_task(task_id)
    assert get_task_res.status_code == 404


def create_task(payload):
    return requests.put(endpoint + "/create-task", json = payload)

def update_task(payload):
    return requests.put(endpoint + "/update-task", json = payload)

def get_task(task_id):
    return requests.get(endpoint + "/get-task/" + task_id)

def delete_task(task_id):
    return requests.delete(endpoint + "/delete-task/" + task_id)

def new_task_payload():
    return {
                "content": "Boring day",
                "user_id": "Human101",
                "is_done": False
            }
