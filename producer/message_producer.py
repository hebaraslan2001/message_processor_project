import sqlite3
from producer.base_producer import BaseProducer

class DatabaseProducer(BaseProducer):
    def __init__(self, db_path):
        self.db_path = db_path

    def setup_database(self):
        """Ensure the database and table are properly initialized."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id TEXT,
            attribute_id TEXT,
            timestamp TEXT,
            value TEXT
        )
        """)
        connection.commit()
        connection.close()

    def clear_table(self):
        """Clear the messages table for testing purposes."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM messages")  # Clear all rows
        connection.commit()
        connection.close()

    def save_to_database(self, message, processed_value):
        """Save processed messages to the database."""
        self.setup_database()  # Ensure the database is initialized
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO messages (asset_id, attribute_id, timestamp, value)
        VALUES (?, ?, ?, ?)
        """, (message["asset_id"], message["attribute_id"], message["timestamp"], str(processed_value)))
        connection.commit()
        connection.close()



# import sqlite3

# def save_to_database(message, processed_value):
#     # Connect to SQLite database (creates file if not exists)
#     connection = sqlite3.connect("message_processor.db")
#     cursor = connection.cursor()

#     # Create table if it doesn't exist
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS messages (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         asset_id TEXT,
#         attribute_id TEXT,
#         timestamp TEXT,
#         value TEXT
#     )
#     """)

#     # Insert the processed message
#     cursor.execute("""
#     INSERT INTO messages (asset_id, attribute_id, timestamp, value)
#     VALUES (?, ?, ?, ?)
#     """, (message["asset_id"], message["attribute_id"], message["timestamp"], str(processed_value)))

#     connection.commit()
#     connection.close()

# # # Example
# # if __name__ == "__main__":
# #     message = {"asset_id": "123", "attribute_id": "output_#", "timestamp": "2024-11-19T10:00:00Z"}
# #     processed_value = 42
# #     save_to_database(message, processed_value)
