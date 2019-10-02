import requests

key = ""
object_id = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/dms-core'

header_dict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

#relative path to your new content file
new_content_file_path = '/path/to/your/new/content.pdf'

response = session.post(str(base_url+'/objects/'+object_id+'/contents/file'), data=open(new_content_file_path, 'rb'), headers=header_dict)
print(response.text)
