import requests

key = ""
#relative path to your new query file
query_file_path = '/path/to/your/query.json'

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/dms-core'

header_dict['Content-Type'] = 'application/json'

header_dict['Ocp-Apim-Subscription-Key'] = key

response = requests.post(str(base_url+'/objects/search'), data=open(query_file_path, 'rb'), headers=header_dict)
print(response.json())
