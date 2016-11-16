import json

def getValue(outEntityName = None, inEntityName = None, inEntityValue = None):
	temp = ""
	if inEntityName != None and inEntityValue != None:
		for x in xrange(0,9):
			if data[x][inEntityName] == inEntityValue: 
				temp = temp +"\n"+ data[x][outEntityName]
	else:
		for x in xrange(0,9):
			temp = temp +"\n"+ data[x][outEntityName]
	return temp

if __name__ == "__main__" :
	json_data=open("data.json").read()
	data = json.loads(json_data)

	json_data1=open("result.json").read()
	data1 = json.loads(json_data1)
	
	print (data1["result"]["parameters"]["AirLine"])

	print (getValue("Departure City","Flight number","113"))
	print (getValue("Flight number"))
