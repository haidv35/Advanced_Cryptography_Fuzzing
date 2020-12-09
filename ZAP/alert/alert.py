import json, csv

data_list = [["Alert", "Riskcode", "Riskdesc", "Confidence", "URI", "Method", "Param"]]

with open('alert.json') as json_file:
    data = json.load(json_file)
    for p in data['site'][0]['alerts']:
    	if(int(p['riskcode']) > 1):
	    	for instance in p['instances']:
	    		uri = instance['uri']
	    		method = instance['method']
	    		if('param' in instance):
	    			param = instance['param']
	    		else:
	    			param = instance['evidence']
		    	data_list.append([
		    		p['alert'],
		    		p['riskcode'],
		    		p['riskdesc'],
		    		p['confidence'],
		    		uri,
		    		method,
		    		param
		    	])
with open('alert.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(data_list)