from flask import current_app

class DatabaseInitializer:
    """
    Helper that should only be used for testing purposes.
    """
    @staticmethod
    def initialize_db(db):
        with current_app.app_context():
            db.drop_all()
            db.create_all()
      
