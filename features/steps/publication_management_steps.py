import base64
import requests
from behave import given, when, then, step
from decouple import config

PORT = config("FLASK_RUN_PORT", cast=int, default=5000)

DEFAULT_USER_DATA = {
    "email": "example@gmail.com",
    "password": "password",
    "fullname": "John Doe",
    "photo": "photo.jpg",
}

DEFAULT_PUBLICATION_DATA = {
    "title": "Example Publication",
    "description": "Example Publication Description",
    "priority": "high",
    "status": "open",
}


def get_publications_url(user_id):
    return f"http://localhost:{PORT}/users/{user_id}/publications"


def get_publication_url(user_id, publication_id):
    return f"http://localhost:{PORT}/users/{user_id}/publications/{publication_id}"

USER_POST_URL = f"http://localhost:{PORT}/users"
LOGIN_URL = f"http://localhost:{PORT}/login"
LOGOUT_URL = f"http://localhost:{PORT}/logout"


def create_auth_header(email, password):
    auth_string = f"{email}:{password}"
    auth_bytes = auth_string.encode("utf-8")
    auth_string_b64 = base64.b64encode(auth_bytes).decode("utf-8")
    return {"Authorization": f"Basic {auth_string_b64}"}


def determine_status_code(error_type):
    if error_type == "NotFound":
        return 404
    if error_type == "Ownership":
        return 403
    if error_type == "Authentication":
        return 401
    return 500

@given("I am an authenticated user")
def step_impl(context):
    request = requests.post(USER_POST_URL, json=DEFAULT_USER_DATA)
    context.user_id = request.json()["id"]

    auth_header = create_auth_header(
        DEFAULT_USER_DATA["email"], DEFAULT_USER_DATA["password"]
    )
    request = requests.post(LOGIN_URL, headers=auth_header)
    context.headers = {"Authorization": f"Bearer {request.json()['token']}"}


@when("I create a new publication")
def step_impl(context):
    request = requests.post(
        get_publications_url(context.user_id),
        json=DEFAULT_PUBLICATION_DATA,
        headers=context.headers,
    )
    context.response = request
    context.publication_id = request.json()["id"]


@then("the publication is created with the correct data")
def step_impl(context):
    assert context.response.status_code == 201
    assert context.response.json()["title"] == DEFAULT_PUBLICATION_DATA["title"]
    assert (
        context.response.json()["description"]
        == DEFAULT_PUBLICATION_DATA["description"]
    )
    assert context.response.json()["priority"] == DEFAULT_PUBLICATION_DATA["priority"]
    assert context.response.json()["status"] == DEFAULT_PUBLICATION_DATA["status"]


@when("I get the publication data")
def step_impl(context):
    request = requests.get(
        get_publication_url(context.user_id, context.publication_id),
        headers=context.headers,
    )
    context.response = request


@then("the publication data is correct")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json()["title"] == DEFAULT_PUBLICATION_DATA["title"]
    assert (
        context.response.json()["description"]
        == DEFAULT_PUBLICATION_DATA["description"]
    )
    assert context.response.json()["priority"] == DEFAULT_PUBLICATION_DATA["priority"]
    assert context.response.json()["status"] == DEFAULT_PUBLICATION_DATA["status"]


@given("I created a publication")
def step_impl(context):
    request = requests.post(
        get_publications_url(context.user_id),
        json=DEFAULT_PUBLICATION_DATA,
        headers=context.headers,
    )
    context.response = request
    context.publication_id = request.json()["id"]


@when("I update the publication")
def step_impl(context):
    context.new_data = {
        "title": "New Title",
        "description": "New Description",
        "priority": "low",
        "status": "closed",
    }
    request = requests.put(
        get_publication_url(context.user_id, context.publication_id),
        json=context.new_data,
        headers=context.headers,
    )
    context.response = request


@then("the publication data is updated")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json()["title"] == context.new_data["title"]
    assert context.response.json()["description"] == context.new_data["description"]
    assert context.response.json()["priority"] == context.new_data["priority"]
    assert context.response.json()["status"] == context.new_data["status"]


@when("I delete the publication")
def step_impl(context):
    request = requests.delete(
        get_publication_url(context.user_id, context.publication_id),
        headers=context.headers,
    )
    context.response = request


@then("the publication is deleted")
def step_impl(context):
    assert context.response.status_code == 204

    request = requests.get(
        get_publication_url(context.user_id, context.publication_id),
        headers=context.headers,
    )
    assert request.status_code == 404

@given("I login as another user")
def step_impl(context):
    alternative_user_data = {
        "email": "new@gmail.com",
        "password": "new password",
        "fullname": "New User",
        "photo": "new_photo.jpg",
    }
    request = requests.post(USER_POST_URL, json=alternative_user_data)
    context.user_id = request.json()["id"]

    auth_header = create_auth_header(
        DEFAULT_USER_DATA["email"], DEFAULT_USER_DATA["password"]
    )
    request = requests.post(LOGIN_URL, headers=auth_header)
    context.headers = {"Authorization": f"Bearer {request.json()['token']}"}


@then("I get a {error_type} error message")
def step_impl(context, error_type):
    expected_error_status = determine_status_code(error_type)
    assert context.response.status_code == expected_error_status


@given("I logout of the application")
def step_impl(context):
    headers = {"token": context.headers["Authorization"].split(" ")[1]}
    request = requests.post(
        LOGOUT_URL, headers=headers
    )
    assert request.status_code == 204