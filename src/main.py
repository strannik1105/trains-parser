from propan import PropanApp, RabbitBroker
from propan.brokers.rabbit import RabbitExchange, RabbitQueue

from service.service import MockService
from parser.parser import MockParser

rabbit_connect = 'connection data'
yadisk_token = 'token'
yadisk_url = 'url'

broker = RabbitBroker(rabbit_connect)
exch = RabbitExchange("exchange", auto_delete=True)
output = RabbitQueue("output_queue", auto_delete=True)
input = RabbitQueue("mock_queue", auto_delete=True)

service = MockService(yadisk_token, yadisk_url)
service.connect()
app = PropanApp(broker)
parser = MockParser()


@broker.handle(input, exch)
async def get_data():
    raw_data = service.get()
    result_data = parser.prepare_data(raw_data)
    await broker.publish(result_data, queue=output, exchange=exch)


