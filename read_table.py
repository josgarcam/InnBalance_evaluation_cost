import configparser

import psycopg2

config = configparser.ConfigParser()
config.read('config.ini')

database_host = config['DATABASE']['DB_HOST']
database_user = config['DATABASE']['DB_USER']
database_name = config['DATABASE']['DB_NAME']
database_password = config['DATABASE']['DB_PASSWORD']

def Read_table(query):
    data = []

    try:
        conn = psycopg2.connect(host=database_host, database=database_name, user=database_user, password=database_password)

        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            data.append(list(row))

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return data


def Update_table(query):
    try:
        conn = psycopg2.connect(host=database_host, database=database_name, user=database_user, password=database_password)

        cur = conn.cursor()
        cur.execute(query)
        # updated_rows = cur.rowcount
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()