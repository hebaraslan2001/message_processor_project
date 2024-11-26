import json
from ingestor.base_ingestor import BaseIngestor

class FileIngestor(BaseIngestor):
    """
    Reads messages from a file.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def read_messages(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                yield json.loads(line)  # Convert each line to a dictionary
