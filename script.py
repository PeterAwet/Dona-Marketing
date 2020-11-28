import psycopg2

conn = psycopg2.connect(
     host ='localhost',
     database ='marketing',
     user ='postgres',
     password ='peter123',
     port ='5432'
    )
#print("connected to postgreSQL DB")
conn.close()