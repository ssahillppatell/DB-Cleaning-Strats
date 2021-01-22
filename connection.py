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
		cur.execute(" \
			WITH t1 AS (Select *, DATE_PART('day', return_date - rental_date) AS date_difference FROM rental), \
			t2 AS (SELECT rental_duration, date_difference, \
						CASE \
							WHEN rental_duration > date_difference THEN 'Returned early' \
							WHEN rental_duration = date_difference THEN 'Returned on Time' \
							ELSE 'Returned late' \
						END AS Return_Status \
					FROM film f \
					JOIN inventory i \
					USING(film_id) \
					JOIN t1 \
					USING (inventory_id)) \
			SELECT Return_status, count(*) AS total_no_of_films \
			FROM t2 \
			GROUP BY 1 \
			ORDER BY 2 DESC; \
		")
		print(cur.fetchall())
	
	conn.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if (conn):
        conn.close()
        print("PostgreSQL connection is closed")