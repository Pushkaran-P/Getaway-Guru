import pandas as p
import psycopg2
#-----------------------/insert login/-------------------------------
#x=p.read_csv('login.csv')
#conn = psycopg2.connect(database = "sample", user = "postgres", password = "qwert", host = "127.0.0.1", port = "5432")
#cur=conn.cursor()
#for i in range(len(x['id'])):
#    a=int(x['id'][i])
#    b=str(x['Name'][i])
#    c=str(x['password'][i])
#    d=int(x['company id'][i])
    
#    cur.execute("insert into login values (%s,%s,%s,%s)",(a,b,c,d))
#    conn.commit()
#cur.execute('select * from company;')
#print(cur.fetchall())
#conn.close()


#---------------------/insert path/-----------------------------------
x=p.read_csv('path.csv')
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "qwert", host = "127.0.0.1", port = "5432")
cur=conn.cursor()
for i in range(len(x['id'])):
    a=int(x['id'][i])

    b=str(x['Start point'][i])
    c=str(x['End point'][i])
    q=str(x['Via'][i])
    w=str(x['Up/Down'][i])
    d=str(x['Company'][i])
    e=int(x['Cost of travel'][i])
    f=int(x['Cost of Food'][i])
    g=int(x['company id'][i])
    
    cur.execute("insert into path values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,q,w,d,e,f,g))
    conn.commit()
cur.execute('select * from path;')
print(cur.fetchall())
conn.close()

#----------------------/insert bus/-------------------------------------
#x=p.read_csv('bus.csv')
#conn = psycopg2.connect(database = "sample", user = "postgres", password = "qwert", host = "127.0.0.1", port = "5432")
#cur=conn.cursor()
#for i in range(len(x['company_name'])):
#    a=str(x['company_name'][i])
#    b=int(x['no of A/C+semi bus'][i])
#    c=int(x['no of A/C bus'][i])
#    q=int(x['no of semi buss'][i])
#    w=int(x['no of normal bus'][i])
#    d=int(x['no of student per bus'][i])
#    e=int(x['rating '][i])
#    f=int(x['company_id'][i])
#   
#    cur.execute("insert into bus values(%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,q,w,d,e,f))
#    conn.commit()
#cur.execute('select * from bus;')
#print(cur.fetchall())
#conn.close()

#-----------------------/insert hotel/------------------------------------
#x=p.read_csv('hotel.csv')
#conn = psycopg2.connect(database = "postgres", user = "postgres", password = "qwert", host = "127.0.0.1", port = "5432")
#cur=conn.cursor()
#for i in range(0,175):
#    a=int(x['hotel_id'][i])
#    b=str(x['address'][i])
#    b=b[0:55]
#    c=int(x['hotel_star_rating'][i])
#    q=int(x['rating'][i])
#    w=str(x['pageurl'][i])
#    w=w[0:55]
#    d=int(x['room_count'][i])+20
#    e=int(x['no_per_room'][i])
#    f=str(x['room_type'][i])
#    g=str(x['similar_hotel'][i])
#    g=g[0:55]
#    h=int(x['path ref id'][i])
#    i=int(x['cost'][i])
#    cur.execute("insert into hotel values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,q,w,d,e,f,g,h,i))
#    conn.commit()
#cur.execute('select * from path;')
#print(cur.fetchall())
#conn.close()


