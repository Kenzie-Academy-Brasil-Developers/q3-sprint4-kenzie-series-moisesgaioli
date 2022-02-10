from flask import Flask
from http import HTTPStatus




class Series:
    def __init__(self, *args, **kwargs):
        self.serie = kwargs['series']
        self.seasons = kwargs['seasons']
        self.released_date = kwargs['released_date']
        self.genre = kwargs['genre']
        self.imdb_rating = kwargs['imdb_rating']
