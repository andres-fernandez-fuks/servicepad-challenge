from flask_openapi3 import APIBlueprint
from project import db
from flask import jsonify

RESET_ENDPOINT = "/database/reset"

EXPECTED_RESPONSES = {}

reset_blueprint = APIBlueprint("reset_blueprint", __name__)

@reset_blueprint.post(
    f"{RESET_ENDPOINT}"
)
def reset_database():
    db.drop_all()
    db.create_all()
    return jsonify({"message": "Database reset"})