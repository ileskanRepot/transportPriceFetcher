import psycopg2
import dbSecret

from attributes import Trip

class Database:
	def __init__(self):
		self.lock = False
		self.conn = self.connect()
		self.cur = self.conn.cursor()

	def __del__(self):
		if hasattr(self, "cur"):
			self.cur.close()
		if hasattr(self, "conn"):
			self.conn.close()

	def connect(self):
		conn = psycopg2.connect(
			user = dbSecret.dbusername, 
			password = dbSecret.dbpassword,
			host = dbSecret.dbhost,
			port = dbSecret.dbport,
			dbname = dbSecret.dbname 
		)
		return conn
	def createTables(self):
		self.cur.execute("""
			CREATE TABLE trips (
				id serial PRIMARY KEY,
				departureTime TIMESTAMP,
                arrivalTime TIMESTAMP,
                fetchTime TIMESTAMP,
                
                departureStation VARCHAR(5),
                arrivalStation VARCHAR(5),
                
				totalPrice INT
			)
		""")
		self.conn.commit()

	def addTrip(self, trip:Trip):
		self.cur.execute(
			"INSERT INTO trips (departureTime, arrivalTime, fetchTime, departureStation, arrivalStation, totalPrice) VALUES (%s, %s, NOW(), %s, %s, %s)",
			(trip.departureTime, trip.arrivalTime, trip.departureStation, trip.arrivalStation, trip.totalPrice)
		)
		self.conn.commit()

db = Database()