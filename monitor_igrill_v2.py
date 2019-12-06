import time
import os
from google.oauth2 import service_account
from google.cloud import pubsub_v1
import datetime

from igrill import IGrillPeripheral

ADDRESS = os.environ['IGRILL_ADDRESS']
SERVICE_ACCOUNT_KEY = os.environ['SERVICE_ACCOUNT_KEY']
PUBSUB_TOPIC = os.environ['PUBSUB_TOPIC']
# DATA_FILE = '/tmp/igrill.json'
INTERVAL = 15

if __name__ == '__main__':
 credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY)
 scoped_credentials = credentials.with_scopes('https://www.googleapis.com/auth/pubsub')

 publisher = pubsub_v1.PublisherClient(credentials=credentials)

 periph = IGrillV2Peripheral(ADDRESS)
 while True:
  temperature=periph.ReadTemperature()
  publisher.publish(PUBSUB_TOPIC,b"bbq/temp", probe1=str(temperature[0]), probe2=str(temperature[1]), probe3=str(temperature[2]), probe4=str(temperature[3]), batt=str(periph.ReadBattery()),time=datetime.now().isoformat())

  time.sleep(INTERVAL)
