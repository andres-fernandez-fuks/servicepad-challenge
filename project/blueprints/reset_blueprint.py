from flask_openapi3 import APIBlueprint, Info
from project import db
from flask import jsonify
from decouple import config

info = Info(title='Reset endpoint', description="Resets the DB, must be used only for testing purposes")

RESET_ENDPOINT = "/database/reset"

EXPECTED_RESPONSES = {}

reset_blueprint = APIBlueprint("reset_blueprint", __name__)

@reset_blueprint.post(
    f"{RESET_ENDPOINT}"
)
def reset_database():
    reset_allowed = config("ALLOW_DB_RESET", cast=bool, default=False)

    if reset_allowed:
        db.drop_all()
        db.create_all()
        return jsonify({"message": "Database reset"})
    else:
        return jsonify({"message": "Database reset not allowed"}), 403