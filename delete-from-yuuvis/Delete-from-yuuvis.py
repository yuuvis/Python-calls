import requests

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = '{subscription key}'




session = requests.Session()




response = session.delete(str(baseUrl+'/dms/objects/{objectId}'), headers=headerDict)
print(response)
