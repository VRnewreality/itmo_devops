from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests

addresses = ['0x74de5d4fcbf63e00296fd95d33236b9794016631',
     '0x0d0707963952f2fba59dd06f2b425ace40b492fe',
     '0xa1d8d972560c2f8144af871db508f0b0b10a3fbf',
     '0x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88',
     '0x28c6c06298d514db089934071355e5743bf21d60',
     '0x22f9dcf4647084d6c31b2765f6910cd85c178c18',
     '0x0000006daea1723962647b7e189d311d757fb793',
     '0xb9ee1e551f538a464e8f8c41e9904498505b49b0',
     '0x21a31ee1afc51d94c2efccaa2092ad1028285549',
     '0x4d246be90c2f36730bb853ad41d0a189061192d3',
     '0xdfd5293d8e347dfe59e90efd55b2956a1343963d',
     '0x0000000000007f150bd6f54c40a34d7c3d5e9f56',
     '0xe93381fb4c4f14bda253907b18fad305d799241a',
     '0x00000000003b3cc22af3ae1eac0440bcee416b40',
     '0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d',
     '0x9008d19f58aabd9ed0d60971565aa8510560ab41',
     '0x6cc5f688a315f3dc28a7781717a9a798a59fda7b',
     '0xe66b31678d6c16e9ebf358268a790b763c133750',
     '0x1bd435f3c054b6e901b7b108a0ab7617c808677b',
     '0x000000000035b5e5ad9019092c665357240f594e',
     "0x503828976d22510aad0201ac7ec88293211d23da",
     "0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511",
     "0x3cd751e6b0078be393132286c442345e5dc49699",
     "0xeb2629a2734e272bcc07bda959863f316f4bd4cf",
     "0x95a9bd206ae52c4ba8eecfc93d18eacdd41c88cc",
     "0xddfabcdc4d8ffc6d5beaf154f18b778f892a0740",
     "0xb739d0895772dbb71a89a3754a160269068f0d45",
     "0x71660c4005ba85c37ccec55d0c4493e66fe775d3",
     "0xf6874c88757721a02f47592140905c4336dfbc61",
     "0x881d4032abe4188e2237efcd27ab435e81fc6bb1",
     "0xa090e606e30bd747d4e6245a1517ebe430f0057e"]

api_key = "EK-uEiGr-CCiQu7A-uNyuY"

headers = {
    "Cache-Control": "no-cache, no-store, must-revalidate",
    "Pragma": "no-cache",
    "Expires": "0",
    "User-Agent": "XY"
    }

def fetch_ethplorer_data():
    response = requests.get(f'https://api.ethplorer.io/getAddressInfo/{addresses[0]}?apiKey={api_key}', headers=headers)
    js = response.json()
    print(js)

# Определение аргументов по умолчанию
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Определение DAG
with DAG(
    "ethplorer_fetcher_dag",
    default_args=default_args,
    description="DAG to fetch data from Ethplorer",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 9, 20),
    catchup=False,
) as dag:

    # Задача для выполнения функции fetch_ethplorer_data
    fetch_data_task = PythonOperator(
        task_id="fetch_ethplorer_data",
        python_callable=fetch_ethplorer_data
    )

