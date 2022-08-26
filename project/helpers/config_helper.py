import os
from decouple import config
from project.config import ConfigurationMode


class ConfigHelper:
    """
    Helper class for configuring the application. It has two config modes but the number could be expanded.
    """

    @staticmethod
    def config_app(app, test_mode):
        config_mode = config("CONFIG_MODE")
        if config_mode == ConfigurationMode.DEVELOPMENT.value and not test_mode:
            app.config.from_object("project.config.DevelopmentConfig")
        elif config_mode == ConfigurationMode.DEVELOPMENT.value and test_mode:
            app.config.from_object("project.config.TestConfig")

