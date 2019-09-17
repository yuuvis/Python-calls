import requests

key = ""
objectId = ""

headerDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.get(str(baseUrl+'/dms/objects/'+objectId+'/contents/renditions/text'), headers=headerDict)
print(response.text)
