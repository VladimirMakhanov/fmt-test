import pika
import json
from datetime import datetime
from pymongo import MongoClient
from types import SchedulerMessage

class Scheduler:
    def __init__(self, mongodb_uri, rabbitmq_uri):
        self.mongo_client = MongoClient(mongodb_uri)
        self.rabbitmq_connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_uri))
        self.channel = self.rabbitmq_connection.channel()
        self.channel.queue_declare(queue='image_collector_queue')

    def get_schedule(self):
        # Here should be the logic for retrieving the schedule from MongoDB
        pass

    def send_message(self, camera_id, client_id):
        message = SchedulerMessage(camera_id=camera_id, client_id=client_id)
        self.channel.basic_publish(
            exchange='',
            routing_key='image_collector_queue',
            body=json.dumps(message.__dict__)
        )

    def run(self):
        while True:
            schedule = self.get_schedule()
            current_time = datetime.now()
            # Schedule verification and sending messages
            # ...

    def __del__(self):
        self.rabbitmq_connection.close()