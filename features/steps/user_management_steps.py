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

USERS_URL = f"http://localhost:{PORT}/users"
LOGIN_URL = f"http://localhost:{PORT}/login"


def create_auth_header(email, password):
    auth_string = f"{email}:{password}"
    auth_bytes = auth_string.encode("utf-8")
    auth_string_b64 = base64.b64encode(auth_bytes).decode("utf-8")
    return {"Authorization": f"Basic {auth_string_b64}"}


@given("I am not currently an user")
def step_impl(context):
    pass


@when("I create a new user")
def step_impl(context):
    request = requests.post(USERS_URL, json=DEFAULT_USER_DATA)
    context.response = request


@then("I am an user with the correct data")
def step_impl(context):
    assert context.response.status_code == 201
    assert context.response.json()["email"] == DEFAULT_USER_DATA["email"]
    assert context.response.json()["fullname"] == DEFAULT_USER_DATA["fullname"]
    assert context.response.json()["photo"] == DEFAULT_USER_DATA["photo"]


@then("I can login with my credentials")
def step_impl(context):
    auth_header = create_auth_header(
        DEFAULT_USER_DATA["email"], DEFAULT_USER_DATA["password"]
    )
    request = requests.post(LOGIN_URL, headers=auth_header)
    context.response = request

    assert context.response.status_code == 200


@given("I am an user with certain data")
def step_impl(context):
    request = requests.post(USERS_URL, json=DEFAULT_USER_DATA)
    context.response = request
    context.user_id = request.json()["id"]


@given("I am logged in")
def step_impl(context):
    headers = create_auth_header(
        DEFAULT_USER_DATA["email"], DEFAULT_USER_DATA["password"]
    )
    request = requests.post(LOGIN_URL, headers=headers)

    assert request.status_code == 200

@when("I get my data")
def step_impl(context):
    request = requests.get(f"{USERS_URL}/{context.user_id}", headers={"Authorization": f"Basic {DEFAULT_USER_DATA['email']}:{DEFAULT_USER_DATA['password']}"})
    context.response = request

@then("I get the correct data")
def step_impl(context):
    assert context.response.json()["email"] == DEFAULT_USER_DATA["email"]
    assert context.response.json()["fullname"] == DEFAULT_USER_DATA["fullname"]
    assert context.response.json()["photo"] == DEFAULT_USER_DATA["photo"]

