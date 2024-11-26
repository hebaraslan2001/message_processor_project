import json
from ingestor.message_ingestor import FileIngestor
from engine.processing_engine import ProcessingEngine
from producer.message_producer import DatabaseProducer
import time
import requests

INPUT_FILE = "messages.txt"
DB_PATH = "message_processor.db"
CONFIG_FILE = "config/equation_config.json"
KPI_API_URL = "http://127.0.0.1:8000/api/kpi/" 

def get_kpi_equations():
    try:
        response = requests.get(f"{KPI_API_URL}kpi/")  # Correct URL for fetching KPIs
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()  # Parse and return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch KPIs: {e}")
        return []

def load_equations(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    # Load the equations dynamically from the config file
    equations = load_equations(CONFIG_FILE)
    
    # Get equations from the API
    # equations = get_kpi_equations()
    if not equations:
        print("No equations found, exiting.")
        exit(1)

    ingestor = FileIngestor(INPUT_FILE)
    producer = DatabaseProducer(DB_PATH)

    for message in ingestor.read_messages():
        print("Reading message:", message)
        time.sleep(5)  # Wait 5 seconds before reading the next message

        # Decide which equation to use based on the message content
        if isinstance(message["value"], (int, float)):
            equation = equations["arithmetic"]  # Use arithmetic for numeric values
        elif isinstance(message["value"], str):
            equation = equations["regex"]  # Use regex for string values
        else:
            print("Unsupported message value type:", type(message["value"]))
            continue

        if not equation:
            print("No suitable equation found for the message type.")
            continue

        # Process the message
        engine = ProcessingEngine(equation)
        processed_value = engine.process_message(message)
        print("Processed value:", processed_value)

        # Save to the database
        producer.save_to_database(message, processed_value)
        print("Saved to database!")



# from ingestor.message_ingestor import FileIngestor
# from engine.processing_engine import ProcessingEngine
# from producer.message_producer import DatabaseProducer
# import time

# INPUT_FILE = "messages.txt"
# DB_PATH = "message_processor.db"
# # Example equations
# ARITHMETIC_EQUATION = "ATTR + 50 * (ATTR / 10)"  # Example arithmetic equation
# REGEX_EQUATION = 'Regex(ATTR, "^dog")'          # Example regex equation

# if __name__ == "__main__":
#     ingestor = FileIngestor(INPUT_FILE)
#     producer = DatabaseProducer(DB_PATH)
    
#     for message in ingestor.read_messages():
#         print("Reading message:", message)
#         time.sleep(5)  # Wait 5 seconds before reading the next message

#         # Decide which equation to use based on the message content
#         if isinstance(message["value"], (int, float)):
#             equation = ARITHMETIC_EQUATION  # Use arithmetic for numeric values
#         elif isinstance(message["value"], str):
#             equation = REGEX_EQUATION  # Use regex for string values
#         else:
#             print("Unsupported message value type:", type(message["value"]))
#             continue

#         # Process the message
#         engine = ProcessingEngine(equation)
#         processed_value = engine.process_message(message)
#         print("Processed value:", processed_value)

#         # Save to the database
#         producer.save_to_database(message, processed_value)
#         print("Saved to database!")
