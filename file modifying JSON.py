import json
x = {"Industry":"TATA",
	"period" : 60,
	"city" : "Pune"}
with open("GHJ.json",'w') as file1:
	json.dump(x,file1)