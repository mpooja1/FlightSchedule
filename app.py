import urllib
import json
import os

from flask import *

def getValue(outEntityName, inEntityName = None, inEntityValue = None):
    temp = ""
    if inEntityName != None and inEntityValue != None:
        for x in xrange(0,9):
            if data[x][inEntityName] == inEntityValue: 
                temp = temp +"\n"+ data[x][outEntityName]
    else:
        for x in xrange(0,9):
            temp = temp +"\n"+ data[x][outEntityName]
	return temp

#from flask import request
#from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
"""def webhook():
    req = request.get_json(silent=True, force=True)
    json_data1=open(req).read()
    data1 = json.loads(json_data1)
    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r"""
	
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

	result = req.get("result")
    parameters = result.get("parameters")
	
	 stuff.setdefault('AirLine', None)
	 stuff.setdefault('FlightNumber', None)
	 stuff.setdefault('DepartureCity', None)
	 stuff.setdefault('DepartureTime', None)
	 stuff.setdefault('ArrivalCity', None)
	 stuff.setdefault('ArrivalTime', None)
	 stuff.setdefault('Status', None)

	stuff = {'AirLine': parameters.get("AirLine"), 'FlightNumber': parameters.get("FlightNumber"), 'DepartureCity': parameters.get("DepartureCity"), 'ArrivalCity': parameters.get("ArrivalCity"),'ArrivalTime': parameters.get("ArrivalTime"),'Status': parameters.get("Status"),'DepartureTime': parameters.get("DepartureTime")}

	"""arr=[[]]
    for x in xrange(0,7):
        arr[1,x]=None
        x = x + 1

    result = req.get("result")
    parameters = result.get("parameters")
    
   
    array=[]
    arr[0,0] = "AirLine"
    arr[0,1] = "FlightNumber"
    arr[0,2] = "DepartureCity"
    arr[0,3] = "ArrivalCity"
    arr[0,4] = "ArrivalTime"
    arr[0,5] = "Status"
    arr[0,6] = "DepartureTime"
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
            array[y]=arr[1,x]
            y = y + 1

	y = y-1

"""    

    if req.get("result").get("action") == "AirLine":
	   #print getValue("AirLine", arr[0][y], arr[1][y])
	   speech = "The FlightNumber of  to is " + str(stuff[FlightNumber]) + "."
	   #speech = "The airline for " + FliNumber + " is " + str(AirLine[FliNumber]) + "."
    #if req.get("result").get("action") == "FlightNumber":
		
	
    #if req.get("result").get("action") == "Status":

		
    #if req.get("result").get("action") == "ArrivalTime":
	
	
	
    #if req.get("result").get("action") == "ArrivalCity":
	
	
	
    #if req.get("result").get("action") == "DepartureTime":
	
	
	
    #if req.get("result").get("action") == "DepartureCity":
	

#    if req.get("result").get("action") != "bookticket":
###   parameters = result.get("parameters")
  #  FliNumber = parameters.get("FlightNumber")
#	Aire = parameters.get("AirLine")

#	FlightNumber = {'AjaxAir':'113', 'AjaxAir':'114', 'BakerAir':'121', 'BakerAir':'122', 'BakerAir':'124', 'CarsonAir':'522','CarsonAir':'679','CarsonAir':'670','CarsonAir':'671','CarsonAir':'672'}
	
 #   AirLine = {'113':'AjaxAir', '114':'AjaxAir', '121':'BakerAir', '122':'BakerAir', '124':'BakerAir', '522': 'CarsonAir','679':'CarsonAir','670':'CarsonAir','671':'CarsonAir','672':'CarsonAir'}
  #DepartureCity = {'113':'Portland', '114':'Atlanta', '121':'Atlanta', '122':'NewYork', '124':'Portland', '522': 'Portland','679':'NewYork','670':'NewYork','671':'Atlanta','672':'Portland'}
  #DepartureTime = {'113':'8:03AM', '114':'2:05PM', '121':'5:14PM', '122':'9:00PM', '124':'9:03AM', '522':'2:15AM','679':'9:30AM','670':'9:30AM','671':'1:20PM','672':'1:25PM'}
  #ArrivalCity = {'113': 'Atlanta', '114': 'Portland', '121': 'NewYork', '122': 'Portland', '124': 'Atlanta', '522': 'NewYork', '679': 'Atlanta' , '670': 'Portland' , '671': 'NewYork' , '672': 'NewYork'}
  #ArrivalTime = {'113': '12:51AM', '114': '4:44PM', '121', '7:20PM', '122': '12:13AM', '124': '12:52PM', '522': '4:58PM', '679': '11:30AM' , '670': '12:05PM' , '671': '2:55PM' , '672': '8:36PM'}
  ## 
    #   speech = "The flights for " + Aire + " is " + str(FlightNumber[Aire]) + "."
   # speech = "The airline for " #+ FliNumber + " is " + str(AirLine[FliNumber]) + "."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        "source": "apiai-flight-schedule"
    }


if __name__ == '__main__':

    json_data=open("data.json").read()
    data = json.loads(json_data)

	
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')