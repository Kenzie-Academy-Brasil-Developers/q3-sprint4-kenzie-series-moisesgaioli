from app.models import DatabaseConnector



class Series(DatabaseConnector):

    series_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']

    def __init__(self, *args, **kwargs):
        self.serie = kwargs['serie'].title()
        self.seasons = kwargs['seasons']
        self.released_date = kwargs['released_date']
        self.genre = kwargs['genre'].title()
        self.imdb_rating = kwargs['imdb_rating']

    @staticmethod
    def serialize_series(data, keys=series_keys):
        if type(data) is tuple:
            return dict(zip(keys, data))
        if type(data) is list:
            return [dict(zip(keys, serie)) for serie in data]



    @classmethod
    def read_series(cls):
        cls.get_conn_cur()

        query_create_table = """CREATE TABLE IF NOT EXISTS ka_series (
            id BIGSERIAL PRIMARY KEY,
            serie VARCHAR(200) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULL
        );"""

        cls.cur.execute(query_create_table)

        query = 'SELECT * FROM ka_series;'

        cls.cur.execute(query)

        series = cls.cur.fetchall()

        cls.commit_and_close()

        return series

    
    
    def create(self):
        self.get_conn_cur()

        query = """
            INSERT INTO
                ka_series (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """

        query_values = list(self.__dict__.values())

        self.cur.execute(query, query_values)

        inserted_serie = self.cur.fetchall()

        self.commit_and_close()

        return inserted_serie

    @classmethod
    def get_by_id(cls, id: int):
        cls.get_conn_cur()

        query_create_table = """CREATE TABLE IF NOT EXISTS ka_series (
            id BIGSERIAL PRIMARY KEY,
            serie VARCHAR(200) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULL
        );"""

        cls.cur.execute(query_create_table)

        query = 'SELECT * FROM ka_series;'

        cls.cur.execute(query)

        series = cls.cur.fetchall()

        series_list = Series.serialize_series(series)

        cls.commit_and_close()

        for serie in series_list:
            if serie['id'] == id:
                return serie



