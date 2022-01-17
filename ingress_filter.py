# This is to gather the hit rate from a EDR Server
#
#-------------------------------------------------
from http.client import responses
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import time
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def GetIngressFilterData(filter_name):

    headers={"X-Auth-Token":"6cc3c907948d4ca3e92416067c08bc7fa57c7125"}
    ingress_url="https://192.168.2.134/api/v1/ingress_whitelist/" + filter_name
    responses = requests.get(ingress_url,headers=headers,verify=False)
        
    data = json.loads(responses.text)
    hit_rate_current = " "


    if responses.status_code == 200:
       #print("success")

       hit_rate_current = data['hit_rate']

    return hit_rate_current
num = 1 
while 0 < num:

   current_rate = GetIngressFilterData("SvchostFilter")
   print(current_rate)
   time.sleep(5)









