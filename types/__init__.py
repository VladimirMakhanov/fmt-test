from dataclasses import dataclass
from datetime import datetime

@dataclass
class SchedulerMessage:
    camera_id: str
    client_id: str

@dataclass
class ImageCollectorMessage:
    client_id: str
    camera_id: str
    image_path: str
    collection_time: datetime

@dataclass
class ClientCredentials:
    api_key: str
    api_secret: str