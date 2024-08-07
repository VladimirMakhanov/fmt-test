import pika
import json
import boto3
from datetime import datetime
from types import SchedulerMessage, ImageCollectorMessage, ClientCredentials
from settings import S3_CREDENTIALS

class ImageCollector:
    def __init__(self, rabbitmq_uri):
        self.rabbitmq_connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_uri))
        self.channel = self.rabbitmq_connection.channel()
        self.channel.queue_declare(queue='image_collector_queue')
        self.channel.queue_declare(queue='data_uploader_queue')
        
        self.s3_client = boto3.client('s3', 
                                      aws_access_key_id=S3_CREDENTIALS['access_key'],
                                      aws_secret_access_key=S3_CREDENTIALS['secret_key'])

    def get_client_credentials(self, client_id: str) -> ClientCredentials:
        # Here should be a request to an external API to retrieve client credentials
        pass

    def get_image(self, credentials: ClientCredentials, camera_id: str) -> bytes:
        # Here should be a request to the client's API to retrieve an image
        pass

    def upload_to_s3(self, image_bytes: bytes, client_id: str, camera_id: str) -> str:
        key = ''
        # Generate a unique key for the image in S3
        self.s3_client.put_object(Bucket='your-bucket-name', Key=key, Body=image_bytes)
        return f"s3://your-bucket-name/{key}"

    def process_message(self, ch, method, properties, body):
        message = SchedulerMessage(**json.loads(body))
        
        credentials = self.get_client_credentials(message.client_id)
        image_bytes = self.get_image(credentials, message.camera_id)
        
        image_path = self.upload_to_s3(image_bytes, message.client_id, message.camera_id)
        
        uploader_message = ImageCollectorMessage(
            client_id=message.client_id,
            camera_id=message.camera_id,
            image_path=image_path,
            collection_time=datetime.now()
        )
        
        self.channel.basic_publish(
            exchange='',
            routing_key='data_uploader_queue',
            body=json.dumps(uploader_message.__dict__)
        )

    def run(self):
        self.channel.basic_consume(
            queue='image_collector_queue', 
            on_message_callback=self.process_message, 
            auto_ack=True
        )
        self.channel.start_consuming()

    def __del__(self):
        self.rabbitmq_connection.close()
