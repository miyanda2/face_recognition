import psycopg2
import logging

logger = logging.getLogger('django.server')

def create():
    conn = False
    try:
        logger.info('Begin creating table in DB')
        conn = psycopg2.connect(dbname='mylocaldb',
                                user='shumyk',
                                password='int20h',
                                host='localhost')
        cursor = conn.cursor()

        create_table_query = '''CREATE TABLE images
                            (ID INT PRIMARY KEY     NOT NULL,
                            URL             TEXT    NOT NULL,
                            IS_HAPPY        BOOLEAN);'''

        cursor.execute(create_table_query)
        conn.commit()
        logger.info('Table created successfully in PostgreSQL')
        return True
    except (Exception) as error:
        logger.error('Error while creating PostgreSQL table', error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            logger.info('PostgreSQL connection is closed')
