import unittest
from ingestor.message_ingestor import FileIngestor

class TestFileIngestor(unittest.TestCase):
    def test_read_messages(self):
        # Use the existing messages.txt file
        ingestor = FileIngestor("messages.txt")
        messages = list(ingestor.read_messages())
        
        # Adjust assertions based on messages.txt content
        self.assertEqual(len(messages), 4)  # Assuming there are 4 messages
        self.assertEqual(messages[0]["asset_id"], "123")  # Example assertion
