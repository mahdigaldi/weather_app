import requests
import time
import sqlite3
def sql_contector():
    con=sqlite3.connect("mydata.db")
    cur=con.cursor()
    return con,cur
def create_table(con,cur):
    cur.execute("CREATE TABLE weather (name TEXT,time TEXT")
    con.commit()
def insert_data(con,cur,data):
    cur.execute("INSET INTO weather(?,?)",tuple([v for k,v in data.items()]))
    con.commit()
    
def get_weather_data(city="tehran",api="6c726da3ead24560dae740093921589a"):
    city=city
    api=api
    Url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,api)
    r=requests.get(url=Url)
    return r.json()
count=0
con,cur=sql_contector()
create_table(con,cur )
while True:
    city="tehran"
    name1=get_weather_data(city)["name"]
    name2="country of {} is :".format(name1)
    print(name2+get_weather_data(city)["sys"]["country"])
    real_time=time.ctime(get_weather_data(city)["dt"])
    print("last recive in : ",real_time)
    count+=1
    time.sleep(5)
    if (count==3):break
    

