import os
import tkinter as tk

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

def checkoutOne(id):
	try:
		conn = psycopg2.connect(user=dbUser, password=dbPass, host=dbHost, port=dbPort, database=dbName)

		with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
			cur.execute(f" \
				SELECT * FROM rental \
				WHERE rental_id = {id} \
			")
			print(cur.fetchall())
		
		conn.commit()

	except (Exception, Error) as error:
		print("Error while connecting to PostgreSQL", error)

	finally:
		if (conn):
			conn.close()
			print("PostgreSQL connection is closed")

root = tk.Tk()

canvas = tk.Canvas(root, width = 400, height = 300)
canvas.grid(columnspan = 3, rowspan = 3)

rentalId = tk.Entry(root)
rentalId.grid(column = 1, row = 0)

actionBtn = tk.Button(root, text="Transact", command = lambda:checkoutOne(rentalId.get()))
actionBtn.grid(column = 1, row = 1)

root.mainloop()