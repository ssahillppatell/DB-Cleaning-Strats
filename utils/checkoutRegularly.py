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

def checkoutRegularly(id):
	result = {}
	try:
		conn = psycopg2.connect(user=dbUser, password=dbPass, host=dbHost, port=dbPort, database=dbName)

		with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
			cur.execute(f" \
				SELECT customer_id, inventory_id, rental_date FROM rental \
				WHERE rental_id = {id} \
			")
			rentalData = cur.fetchone()
			result['customer_id'], result['inventory_id'], result['rental_date'] = [rentalData[k] for k in ('customer_id', 'inventory_id', 'rental_date')]

			cur.execute(f" \
				SELECT film_id \
				FROM inventory \
				WHERE inventory_id = {result['inventory_id']} \
			")
			result['film_id'] = cur.fetchone()['film_id']

			cur.execute(f" \
				SELECT title, rental_duration, rental_rate \
				FROM film \
				WHERE film_id = {result['film_id']} \
			")
			filmData = cur.fetchone()
			result['film_title'], result['rental_duration'], result['rental_rate'] = [filmData[k] for k in ('title', 'rental_duration', 'rental_rate')]

			cur.execute(f" \
				SELECT first_name, last_name \
				FROM customer \
				WHERE customer_id = {result['customer_id']} \
			")
			name = cur.fetchone()
			firstName, lastName = [name[k] for k in ('first_name', 'last_name')]
			fullName = f"{firstName} {lastName}"
			result['full_name'] = fullName

			with open("daily.txt", "a") as myfile:
				myfile.write(f"{id}\n")
			return result
		
		conn.commit()

	except (Exception, Error) as error:
		print("Error while connecting to PostgreSQL", error)

	finally:
		if (conn):
			conn.close()
			print("PostgreSQL connection is closed")