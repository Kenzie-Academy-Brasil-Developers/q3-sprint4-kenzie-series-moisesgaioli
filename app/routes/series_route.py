from flask import Flask
from app.controllers import serie_controller


def serie_route(app: Flask):
    @app.get('/series')
    def retrieve():
        return serie_controller.get_series()