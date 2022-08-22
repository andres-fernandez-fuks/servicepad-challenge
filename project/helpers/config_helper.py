
import os
from decouple import config
from project.config import ConfigurationMode


class ConfigHelper:
    @staticmethod
    def config_app(app):
        config_mode = config('CONFIG_MODE')
        if config_mode == ConfigurationMode.DEVELOPMENT.value:
            app.config.from_object('project.config.DevelopmentConfig')
        elif config_mode == ConfigurationMode.TESTING.value:
            app.config.from_object('project.config.TestConfig')

