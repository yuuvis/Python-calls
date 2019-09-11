import requests

key = ""
objectId = ""

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.delete(str(baseUrl+'/dms/objects/'+objectId), headers=headerDict)
print(response)
