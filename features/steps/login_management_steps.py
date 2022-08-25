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

@given("I am a registered user")
def step_impl(context):
    request = requests.post(USER_POST_URL, json=DEFAULT_USER_DATA)
    context.user_id = request.json()["id"]

@when("I login with valid credentials")
def step_impl(context):
    auth_header = create_auth_header(
        DEFAULT_USER_DATA["email"], DEFAULT_USER_DATA["password"]
    )
    context.response = requests.post(LOGIN_URL, headers=auth_header)

@then("I receive an authentication token")
def step_impl(context):
    assert context.response.status_code == 200
    assert "token" in context.response.json()

@when("I login with invalid credentials")
def step_impl(context):
    auth_header = create_auth_header(
        DEFAULT_USER_DATA["email"], "invalid"
    )
    context.response = requests.post(LOGIN_URL, headers=auth_header)

@when("I logout of the application")
def step_impl(context):
    headers = {"token": context.headers["Authorization"].split(" ")[1]}
    context.response = requests.post(LOGOUT_URL, headers=headers)

@then("I receive a successful response")
def step_impl(context):
    assert context.response.status_code == 204