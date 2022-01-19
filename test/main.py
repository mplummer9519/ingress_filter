
import requests
import json
from flask import Flask
from flask import request


app = Flask(__name__)

#@app.route("/")
#def index():
#    return "Congrats its a web app"

@app.route("/")
def GetIngressFilterData():
    headers={"X-Auth-Token":"6cc3c907948d4ca3e92416067c08bc7fa57c7125"}
    ingress_url="https://192.168.2.134/api/v1/ingress_whitelist/SvchostFilter"
    responses = requests.get(ingress_url,headers=headers,verify=False)        
    data = json.loads(responses.text)
    hit_rate_current = " "
    if responses.status_code == 200:
       hit_rate_current = data['hit_rate']
       return str(hit_rate_current)

@app.route("/name")
def name():
    first_name = request.args.get("firstname")
    return str(first_name)


@app.route("/webpage")
def webpage():
    return render_template('test.html')




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

