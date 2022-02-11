from flask import jsonify, request
from http import HTTPStatus
from app.models.series_model import Series
from psycopg2.errors import UniqueViolation


def get_series():
    series = Series.read_series()

    series_list = Series.serialize_series(series)

    return {"data": series_list}, HTTPStatus.OK


def create_series():
    data = request.get_json()

    series = Series(**data)

    try:
        inserted_serie = series.create()

        serie_list = Series.serialize_series(inserted_serie)

        return jsonify(serie_list), HTTPStatus.CREATED
    
    except UniqueViolation:
        return jsonify({'msg': 'serie already exists'}), HTTPStatus.UNPROCESSABLE_ENTITY


def select_by_id(id: int):

    serie = Series.get_by_id(id)

    return {"data": serie}, HTTPStatus.OK



    

