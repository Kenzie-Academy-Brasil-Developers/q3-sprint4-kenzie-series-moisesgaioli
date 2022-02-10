from flask import Flask
from app.routes.series_route import serie_route

def init_app(app: Flask):
    serie_route(app)