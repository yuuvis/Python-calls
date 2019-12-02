import requests

key = ""
object_id = ""

header_dict = {}
base_url = 'https' + '://' + 'api.yuuvis.io' + '/dms-core'

header_dict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

#id of the new repository for the content
repo_id = 'repoXXX'

response = session.post(str(base_url+'/objects/'+object_id+'/actions/move/contents/repositories/'+repo_id), data=open(new_content_file_path, 'rb'), headers=header_dict)
print(response.text)
