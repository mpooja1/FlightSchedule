import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

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
    FlightNumber = parameters.get("FlightNumber")

    AirLine = {'113':'AjaxAir', '114':'AjaxAir', '121':'BakerAir', '122':'BakerAir', '124':'BakerAir', '522': 'CarsonAir','679':'CarsonAir','670':'CarsonAir','671':'CarsonAir','672':'CarsonAir'}
    
    speech = "The airline for " + FlightNumber + " is " + str(AirLine[FlightNumber]) + " euros."

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