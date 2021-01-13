import psycopg2
import psycopg2.extras
from psycopg2 import Error

try:
	conn = psycopg2.connect(user="postgres", password="Sahil@123", host="127.0.0.1", port="5432", database="dvdrental")

	with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
		cur.execute("SELECT name FROM category;")
		print(cur.fetchall());
	
	conn.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if (conn):
        conn.close()
        print("PostgreSQL connection is closed")