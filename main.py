from utils.URLHandler import URLHandler
from utils.DBConnector import execute_sql
from services.Service import Service
import requests
from services.xml import REQUEST
import xmltodict
import json

urlHandler = URLHandler(False)
url = urlHandler.get_url()

#db_config = urlHandler.get_db_config()

#db_data = execute_sql(config=db_config, query="SELECT * from taxpayer t where t.code = '790412330550'")

#print(db_data)

snrService = Service()
snrService.set_endpoint("/isnaregphysicalintegration/ws")
url = url + snrService.get_endpoint()

# date = "2023-03-02"
# taxpayerData = "010101000005"
# taxpayerType = "UL"

# data = {
#     "date": date,
#     "taxpayerData": taxpayerData,
#     "taxpayerType": taxpayerType
# }
# response = requests.get("https://arm.isna.kz/services/isnaregndsintegration/v2/api-docs")
# print(response.json()[paths])
headers = {'Content-Type': 'text/xml'}
print(url)
response = requests.post(url, data=REQUEST, headers=headers)

if response.status_code == 200:
    print('POST request was successful.')
    xml_dict = xmltodict.parse(response.text)
    json_data = json.dumps(xml_dict, indent=4)
    print('Response_xml:', xml_dict)
    print("Response_json:", json_data)
else:
    print(f'POST request failed with status code {response.status_code}.')

#response = requests.post(url=url, json=data)
#print(response.json())