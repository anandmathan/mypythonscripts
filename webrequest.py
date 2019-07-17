# importing the requests library 
import requests
import json
import sys

# api-endpoint 
URL = "https://jsonplaceholder.typicode.com/posts"
r=requests.get(url = URL, params=None)
a =  json.loads(r.content)
#print(a['userId'])
outfile={}
with open("web.json", 'w') as outfile:
	json.dump(a, outfile)
json_file={}
with open("web.json") as json_file:
	data = json.load(json_file)
	userid=sys.argv[1]
	for d in data:
		ruser=str(d['userId'])
		# print(userid)
		if userid == ruser:
			title=str(d['title'])
			magic=len(title)
			star=magic*"x"
			print ("userId:"+str(d['userId']) + "\n" +"id:" + str(d['id']) + "\n" +"title:"+ d['title'] + "\n" + star)


"""
for c in a:
	fp=open("web.json", 'w')
	fp.write(str(c))
fp.close()
r=[]
with open("web.json", 'r+') as fr:
	r = fr.read()
	print(str(r))
	#for u in r:
	#	print(u)
fr.close()

# for userID in a:
# print (userID)
"""