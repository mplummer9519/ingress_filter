from flask import Flask


app = Flask(__name__)

#@app.route("/")
#def index():
#    return "Congrats its a web app"

@app.route("/")
def GetIngressFilterData(filter_name):
    headers={"X-Auth-Token":"6cc3c907948d4ca3e92416067c08bc7fa57c7125"}
    ingress_url="https://192.168.2.134/api/v1/ingress_whitelist/SvchostFilter" + filter_name
    responses = requests.get(ingress_url,headers=headers,verify=False)        
    data = json.loads(responses.text)
    hit_rate_current = " "
    if responses.status_code == 200:
       hit_rate_current = data['hit_rate']
       return str(hit_rate_current)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

