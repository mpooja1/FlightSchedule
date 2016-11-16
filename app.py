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
	
	"""
	arr=[[]]
	for x in xrange(0,7):
		arr[1,x]=None
		x = x + 1

	result = req.get("result")
	parameters = result.get("parameters")
    
    
	array=[[]]
	arr[0,0] = "Airline"
	arr[0,1] = "Flight number"
	arr[0,2] = "Departure City"
	arr[0,3] = "Arrival City"
	arr[0,4] = "Arrival Time"
	arr[0,5] = "Status"
	arr[0,6] = "Departure time"
	arr[1,0] = parameters.get("AirLine")
	arr[1,1] = parameters.get("FlightNumber")
	arr[1,2] = parameters.get("DepartureCity")
	arr[1,3] = parameters.get("ArrivalCity")
	arr[1,4] = parameters.get("ArrivalTime")
	arr[1,5] = parameters.get("Status")
	arr[1,6] = parameters.get("DepartureTime")
	y = 0
	for x in xrange(0,7):
		if arr[1,x]!=None:
			array[0,y]=arr[0,x]
			array[1,y]=arr[1,x]
			y = y + 1
	y = y-1

	if y == 1:
		temp = getValue("Airline",array[0,0],array[1,0],array[1,0],array[1,1])
	if y == 0:
		temp = getValue("Airline",array[0,0],array[1,0])
	"""
	
  	
	
	if req.get("result").get("action") == "bookticket":
	    
		result = req.get("result")
		parameters = result.get("parameters")
		FlightNumber = parameters.get("FlightNumber")
		temp = getValue("Airline","Flight number",FlightNumber)
    
	if req.get("result").get("action") == "Status":
	    
		result = req.get("result")
		parameters = result.get("parameters")
		FlightNumber = parameters.get("FlightNumber")
		temp = getValue("Status","Flight number",FlightNumber)
	"""
	if req.get("result").get("action") == "Flightnumber":
	    
		result = req.get("result")
		parameters = result.get("parameters")
		Airline = parameters.get("AirLine")
		temp = getValue("Flight number","Airline",Airline)
	"""	
 
	

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