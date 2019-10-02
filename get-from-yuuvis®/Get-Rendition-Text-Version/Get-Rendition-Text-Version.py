import requests

key = ""
object_id = ""
versionNr = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/dms-view'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.get(str(base_url+'/objects/'+object_id+'/versions/'+versionNr+'/contents/renditions/text'), headers=header_dict)
print(response.text)
