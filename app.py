import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

def getValue(outEntityName = None, inEntityName = None, inEntityValue = None):
	temp = ""
	if inEntityName != None and inEntityValue != None:
		for x in xrange(0,9):
			if data[x][inEntityName] == inEntityValue: 
				temp = temp +"\n"+ data[x][outEntityName]
	else:
		for x in xrange(0,9):
			temp = temp +"\n"+ data[x][outEntityName]
	speech = "The airline for "
	return temp

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
   # if req.get("result").get("action") != "bookticket":
    #    return {}
    FlightNumber = None
    Airline = None
	Status = None
	ArrivalCity = None
	
    if req.get("result").get("action") == "bookticket":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        FlightNumber = parameters.get("FlightNumber")
        temp = getValue("Airline","Flight number",FlightNumber)
		
    if req.get("result").get("action") == "bookticket":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        Airline = parameters.get("AirLine")
        temp = getValue("Flight number","Airline",Airline)	
    
    if req.get("result").get("action") == "Status":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        FlightNumber = parameters.get("FlightNumber")
        temp = getValue("Status","Flight number",FlightNumber)
	
    if req.get("result").get("action") == "Status":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        Status = parameters.get("Status")
        temp = getValue("Flight number","Status",Status)
			
     
	
    if req.get("result").get("action") == "Arrivaltime":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        FlightNumber = parameters.get("FlightNumber")
        temp = getValue("Arrival Time","Flight number",FlightNumber)
		
    if req.get("result").get("action") == "Arrivaltime":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        ArrivalTime = parameters.get("Arrivaltime")
        temp = getValue("Flight number","Arrival Time",ArrivalTime)	
		
    if req.get("result").get("action") == "Departuretime":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        FlightNumber = parameters.get("FlightNumber")
        temp = getValue("Departure time","Flight number",FlightNumber)
   
    if req.get("result").get("action") == "Departurecity":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        FlightNumber = parameters.get("FlightNumber")
        temp = getValue("Departure City","Flight number",FlightNumber)
		
    if req.get("result").get("action") == "Arrivalcity":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        FlightNumber = parameters.get("FlightNumber")
        temp = getValue("Arrival City","Flight number",FlightNumber)
		
   
    if req.get("result").get("action") == "Arrivalcity":
	    
        result = req.get("result")
        parameters = result.get("parameters")
        ArrivalCity = parameters.get("Arrivalcity")
        temp = getValue("Flight number","Arrival City",ArrivalCity)   

	

    print("Response:")
    print(temp)

    return {
        "speech": temp,
        "displayText": temp,
        "source": "apiai-flight-schedule"
    }


if __name__ == '__main__':
    
    json_data=open("data.json").read()
    data = json.loads(json_data)	
	
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')