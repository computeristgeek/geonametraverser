from geopy.geocoders import GeoNames
import urllib,json
#geoc = GeoNames(country_bias='EG',username='username')
#Location((27.0, 30.0, 0.0))
#loc=geoc.geocode('egypt')
#json.dumps(loc.raw,indent=4)
#egypt=loc.raw['geonameId']
#357994
username='username'
egypt=357994
parentchild={'parent':None,'child':None}
parentchilddict=[]
with open('geonames2.json','w') as f:
	url="http://api.geonames.org/childrenJSON?username="+username+"&geonameId="
	response=urllib.urlopen(url+str(egypt))
	level1 = response.read()
	f.write(level1)
	level1 = json.loads(level1)
	#for geoname in data['geonames']: print d
	traversallist=[]
	geonameId=egypt
	parentchild['parent']=geonameId
	print 'retrieving children of '+str(geonameId)+'...'
	response=urllib.urlopen(url+str(geonameId))
	resjson=response.read()
	print '\tresponse received, writing to file...'
	f.write(resjson)
	children=json.loads(resjson)
	print '\twritten and converted to json, retrieving children list...'
	if 'geonames' in children:
		for child in children['geonames']:
			parentchild['child']=child['geonameId']
			parentchilddict.append({'parent':parentchild['parent'],'child':parentchild['child']});
			traversallist.append(child)
			print parentchilddict
	while traversallist:
		geo=traversallist.pop();
		if 'geonameId' in geo:
			geonameId=geo['geonameId']
			parentchild['parent']=geonameId
			print 'retrieving children of '+str(geonameId)+'...'
			response=urllib.urlopen(url+str(geonameId))
			resjson=response.read()
			print '\tresponse received, writing to file...'
			f.write(resjson)
			children=json.loads(resjson)
			print '\twritten and converted to json, retrieving children list...'
			if 'geonames' in children:
				for child in children['geonames']:
					if 'geonameId' in child:
						parentchild['child']=child['geonameId']
						parentchilddict.append({'parent':parentchild['parent'],'child':parentchild['child']});
						traversallist.append(child)
						print parentchilddict
	f.write(str(parentchilddict))
	print parentchilddict
