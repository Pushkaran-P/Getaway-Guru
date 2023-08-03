import psycopg2
conn = psycopg2.connect(database = "sample", user = "postgres", password = "qwert", host = "127.0.0.1", port = "5432")
cur=conn.cursor()
cur.execute("select admin('Nivedh Auswin','16pd23');")
x=cur.fetchall()
print(x)
conn.close()
a=list(x[0])
print(a[0])