from flask import Flask, jsonify
from http import HTTPStatus


def get_series():
    return jsonify({'msg': 'ok'}), HTTPStatus.OK