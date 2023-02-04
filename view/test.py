import psycopg2
conn = psycopg2.connect(host='124.70.11.121', port=26000, user='jack', password='123qwe!@#', dbname='library')
conn.set_client_encoding('utf8')
cur = conn.cursor()


admin=1
sql = "select * from {} where {}='{}'".format("users", "id", admin)

# sql="select * from users where id=1"

count = cur.execute(sql)

res = cur.fetchall()

print(count,res)
conn.close()
