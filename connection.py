import os
import psycopg2
import psycopg2.extras
from psycopg2 import Error
from dotenv import load_dotenv

load_dotenv()
dbUser = os.environ.get('DB_USER')
dbPass = os.environ.get('DB_PASS')
dbHost = os.environ.get('DB_HOST')
dbPort = os.environ.get('DB_PORT')
dbName = os.environ.get('DB_NAME')

try:
	conn = psycopg2.connect(user=dbUser, password=dbPass, host=dbHost, port=dbPort, database=dbName)

	with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
		cur.execute("SELECT name FROM category;")
		print(cur.fetchall())
	
	conn.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if (conn):
        conn.close()
        print("PostgreSQL connection is closed")