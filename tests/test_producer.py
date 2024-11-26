import unittest
import sqlite3
from producer.message_producer import DatabaseProducer

class TestDatabaseProducer(unittest.TestCase):
    def setUp(self):
        """Clear the database before each test"""
        self.producer = DatabaseProducer("message_processor.db")
        self.producer.clear_table()  # Clear the database
        self.message = {"asset_id": "123", "attribute_id": "A1", "timestamp": "2024-11-19T10:00:00Z", "value": 100}

    def test_save_to_database(self):
        processed_value = 600.0
        self.producer.save_to_database(self.message, processed_value)

        # Check if the message is saved in the database
        connection = sqlite3.connect("message_processor.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM messages WHERE asset_id=?", (self.message["asset_id"],))
        row = cursor.fetchone()
        self.assertIsNotNone(row)  # Ensure the row is saved
        self.assertEqual(row[1], self.message["asset_id"])  # Check asset_id
        self.assertEqual(row[4], str(processed_value))  # Check processed value
        connection.close()
