import psycopg2
import logging
import json

logger = logging.getLogger('django.server')

def createTable():
    conn = False
    try:
        logger.info('Begin creating table in DB')
        conn = psycopg2.connect(dbname='mylocaldb',
                                user='shumyk',
                                password='int20h',
                                host='localhost')
        cursor = conn.cursor()

        # faceCoords array of strings containing width/top/left/height
        create_table_query = '''CREATE TABLE images
                            (id             SERIAL PRIMARY KEY  NOT NULL,
                             url            TEXT    NOT NULL,
                             faceToken      TEXT,
                             faceCoords     VARCHAR[],
                             hasHappiness   BOOLEAN,
                             hasSadness     BOOLEAN,
                             hasNeutral     BOOLEAN,
                             hasDisgust     BOOLEAN,
                             hasAnger       BOOLEAN,
                             hasSurprise    BOOLEAN,
                             hasFear        BOOLEAN);'''

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

def deleteTable():
    try:
        logger.info('Deleting table in DB')
        conn = psycopg2.connect(dbname='mylocaldb',
                                user='shumyk',
                                password='int20h',
                                host='localhost')
        cursor = conn.cursor()

        drop_table_query = 'DROP TABLE images;'

        cursor.execute(drop_table_query)
        conn.commit()
        logger.info('Table dropped successfully in PostgreSQL')
        return True
    except Exception as error:
        logger.error('Error while deleting PostgreSQL table', error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            logger.info('PostgreSQL connection is closed')

def selectData():
    try:
        logger.info('Fetching data from DB')
        conn = psycopg2.connect(dbname='mylocaldb',
                                user='shumyk',
                                password='int20h',
                                host='localhost')
        cursor = conn.cursor()

        drop_table_query = 'SELECT * FROM images;'

        cursor.execute(drop_table_query)
        images_records = cursor.fetchall()

        logger.info('Data fetched successfully in PostgreSQL')
        return json.dumps(images_records)
    except Exception as error:
        logger.error('Error while fetching data from PostgreSQL table', error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            logger.info('PostgreSQL connection is closed')

def insertData(request):
    try:
        logger.info('Inserting data from DB')
        conn = psycopg2.connect(dbname='mylocaldb',
                                user='shumyk',
                                password='int20h',
                                host='localhost')
        cursor = conn.cursor()

        insert_query = """INSERT INTO images
            (url, faceToken, hasHappiness, hasSadness, hasNeutral, hasDisgust, hasAnger, hasSurprise, hasFear)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        for key in request.GET:
            logger.info('key: ' + key + ', value: ' + request.GET[key])

        for key in request:
            logger.info('request object:')
            logger.info('key: ' + key + ', value: ' + request[key])

        record_to_insert = (request.GET.get('url'),
                            request.GET.get('facetoken'),
                            request.GET.get('happiness'),
                            request.GET.get('sadness'),
                            request.GET.get('neutral'),
                            request.GET.get('disgust'),
                            request.GET.get('anger'),
                            request.GET.get('surprise'),
                            request.GET.get('fear'))
        cursor.execute(insert_query, record_to_insert)
        conn.commit()

        logger.info('Data inserted successfully in PostgreSQL', cursor.rowcount)
        return True
    except Exception as error:
        logger.error('Error while inserted data in PostgreSQL table', error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            logger.info('PostgreSQL connection is closed')
