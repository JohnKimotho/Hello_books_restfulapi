#app/__init__.py

from flask import Flask

from config import app_config

def create_app(config_name):
	
	app = Flask (__name__,instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app_config[config_name].init_app(app)
	
	return app

