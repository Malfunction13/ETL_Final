import psycopg2


class Database:

    def write_data(self, data, host, database, user, password, port):
        connection = psycopg2.connect(host=host,
                                      database=database,
                                      user=user,
                                      password=password,
                                      port=port)
        cursor = connection.cursor()

        for i in data:
            cursor.execute("INSERT INTO etl_db VALUES(%s, %s,%s)", (i.key, i.value, i.ts))
            connection.commit()
        cursor.close() # close cursor
        connection.close() #close connection
        print(f"Writing to {database} complete")


