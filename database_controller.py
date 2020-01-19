import psycopg2


class DatabaseController:
    def __init__(self):
        self.connection = psycopg2.connect("dbname=fiveringsdb user=fiveringsdbuser password=postgres")
        self.cursor = self.connection.cursor()

    def upsert(self, table, columns, values, key, update):
        query = """
            INSERT INTO {table} ({columns}) VALUES
            {values}
            ON CONFLICT ({key}) DO UPDATE SET
            {update}
        ;""".format(table=table, columns=columns, values=values, key=key, update=update)
        print("Executing Query: " + query)
        self.execute_query(query)

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()
        self.cursor.close()
