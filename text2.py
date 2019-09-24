import json

today = \
{
 "早餐":{
       "space":"home",
       "time":"7-8",
       "items":{
               "bread":"1000cal",
               "boiled egg":"500cal"
               }
       },
 "午餐":{
       "space":"restrent",
       "time":"12-13",
       "items":{
               "steak":"5000cal"
               }
       },
 "dinner":{
         "space":"home",
         "time":"19-20",
         "items":{
                 "ramen":"4000cal"
                 }
         }
 }
today1 = json.dumps(today)
print(today1)
today2 = json.loads(today1)
print(today2)

       
       

