import pika
import json
from types import ImageCollectorMessage

class DataUploader:
    def __init__(self, rabbitmq_uri):
        self.rabbitmq_connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_uri))
        self.channel = self.rabbitmq_connection.channel()
        self.channel.queue_declare(queue='data_uploader_queue')

    def process_message(self, ch, method, properties, body):
        message = ImageCollectorMessage(**json.loads(body))
        # Here should be the logic for processing the received message
        print(f"Received message: {message}")

    def run(self):
        self.channel.basic_consume(
            queue='data_uploader_queue', 
            on_message_callback=self.process_message, 
            auto_ack=True
        )
        self.channel.start_consuming()

    def __del__(self):
        self.rabbitmq_connection.close()
