import requests
import json

url='https://www.wattvision.com/api/v0.2/elec' #main wattvision url

#post
def post(sensor_id,api_id,api_key,time,watts,watthours):
    data=str.encode("{\"sensor_id\":\""+sensor_id+"\",\"api_id\":\""+api_id+"\",\"api_key\":\""+api_key+"\",\"time\":\""+time+"\",\"watts\":"+str(watts)+",\"watthours\":"+str(watthours)+"}")
    req=requests.post(url,data)
    return req.content

#get	
def get(sensor_id,api_id,api_key,type,start_time,end_time):
    data= {'sensor_id':sensor_id,'api_id':api_id,'api_key':api_key,'type':type,'start_time':start_time,'end_time':end_time}
    req=requests.get(url,params=data)
	
    #parse response to dict, and print
	
    return req.json()['data']