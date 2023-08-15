from utils.URLHandler import URLHandler
from utils.DBConnector import execute_sql
from services.Service import Service
import requests


urlHandler = URLHandler(True)
url = urlHandler.get_url()

db_config = urlHandler.get_db_config()

db_data = execute_sql(config=db_config, query="SELECT * from taxpayer t where t.code = '790412330550'")

print(db_data)

snrService = Service()
snrService.set_endpoint("/isnaregsnrintegration/open-api/tax-regimes/taxpayer")
url = url + snrService.get_endpoint()

date = "2023-03-02"
taxpayerData = "010101000005"
taxpayerType = "UL"

data = {
    "date": date,
    "taxpayerData": taxpayerData,
    "taxpayerType": taxpayerType
}
requests.post
response = requests.post(url=url, json=data)
print(response.json())