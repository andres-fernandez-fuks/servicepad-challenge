import requests
from decouple import config

PORT = config("FLASK_RUN_PORT", cast=int, default=5000)

RESET_URL = f"http://localhost:{PORT}/database/reset"

def before_scenario(scenario, context):
    requests.post(RESET_URL)