import wattvision_api
	
#constants to test with
sensor_id='5679802'
api_id='6tg4yhb1zh7wav8krq7qyyrrfnshq6hl'
api_key='a0lk3ont0itzdt02kgxtja6d8e5x2k9x'
time='2014-05-21T12:32:03'
watts=545
watthours=654

#for get call	
type='rate'
start_time='2014-05-21T11:35:00'
end_time='2014-05-21T12:34:00'

print(wattvision_api.post(sensor_id,api_id,api_key,time,watts,watthours))
arr=wattvision_api.get(sensor_id,api_id,api_key,type,start_time,end_time)

for i in arr:
    print (i['v'])

