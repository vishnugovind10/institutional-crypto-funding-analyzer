from sqlalchemy import create_engine

class DataStorage:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def save_funding_rates(self, data):
        data.to_sql('funding_rates', self.engine, if_exists='append', index=False)
