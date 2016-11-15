import urllib
import json
import os

from flask import *

#from flask import request
#from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "bookticket":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("FlightNumber")

    AirLine = {'113':AjaxAir, '114':AjaxAir, '121':BakerAir, '122':BakerAir, '124':BakerAir, '522': CarsonAir,'679':CarsonAir,'670':CarsonAir,'671':CarsonAir,'672':CarsonAir}
    DepartureCity = {'113':Portland, '114':Atlanta, '121':Atlanta, '122':NewYork, '124':Portland, '522': Portland,'679':NewYork,'670':NewYork,'671':Atlanta,'672':Portland}
    DepartureTime = {'113':'8:03AM', '114':'2:05PM', '121':'5:14PM', '122':'9:00PM', '124':'9:03AM', '522':'2:15AM','679':'9:30AM','670':'9:30AM','671':'1:20PM','672':'1:25PM'}
    ArrivalCity = {'113': Atlanta, '114': Portland, '121': NewYork, '122': Portland, '124': Atlanta, '522': NewYork, '679': Atlanta , '670': Portland , '671': NewYork , '672': NewYork}
    ArrivalTime = {'113': '12:51AM', '114': '4:44PM', '121': '7:20PM', '122': '12:13AM', '124': '12:52PM', '522': '4:58PM', '679': '11:30AM' , '670': '12:05PM' , '671': '2:55PM' , '672': '8:36PM'}
    ArrivalCity = {'113': landed, '114': boarding, '121': departed, '122': scheduled, '124': delayedto955, '522': scheduled, '679': departed , '670': departed , '671': scheduled , '672': scheduled}

    speech = "The airline for " + FlightNumber + " is " + str(AirLine[FlightNumber]) + "."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        "source": "apiai-flight-schedule"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')