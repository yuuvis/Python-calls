import requests

key = ""

headerDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.get(str(baseUrl+'/dms/schema/native'), headers=headerDict)
print(response.text)
