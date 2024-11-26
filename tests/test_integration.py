import unittest
from ingestor.message_ingestor import FileIngestor
from engine.processing_engine import ProcessingEngine
from producer.message_producer import DatabaseProducer
import sqlite3

class TestIntegration(unittest.TestCase):
    def setUp(self):
        """Set up the test environment by clearing the database"""
        self.producer = DatabaseProducer("message_processor.db")
        self.producer.clear_table()  # Clear the database before each test
        self.ingestor = FileIngestor("messages.txt")

    def test_full_flow(self):
        # Process all messages and save to the database
        for message in self.ingestor.read_messages():
            if isinstance(message["value"], (int, float)):
                equation = "ATTR + 50 * (ATTR / 10)"
            elif isinstance(message["value"], str):
                equation = "Regex(ATTR, '^dog')"
            else:
                equation = None
            
            if equation:
                engine = ProcessingEngine(equation)
                processed_value = engine.process_message(message)
                self.producer.save_to_database(message, processed_value)

        # Verify data in the database
        connection = sqlite3.connect("message_processor.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM messages")
        rows = cursor.fetchall()
        self.assertGreater(len(rows), 0)  # Ensure at least one row is inserted
        connection.close()
