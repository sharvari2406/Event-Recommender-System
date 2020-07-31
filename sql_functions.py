import sqlite3 as sq

class sql_func:
	def __init__(self):
		self.conn = sq.connect('employee_data.db')
		self.conn.execute("CREATE TABLE IF NOT EXISTS \
			employee_interest(name TEXT,domain TEXT,event1 TEXT,event2 TEXT)")

	def insert_data(self,uname,dom,ev1,ev2):       ### can try with *args
		self.conn.execute("INSERT INTO employee_interest (name,domain,event1,event2) \
			VALUES (?,?,?,?)",(uname,dom,ev1,ev2))
		self.conn.commit()

	def close(self):
		self.conn.close()
