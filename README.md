# Message Processor and KPI Integration
## Project Overview
This project involves building a message processing system that:

- Ingests messages from a file or a database.
- Processes them using equations defined either in code or fetched from a Django backend.
Saves the results into a database.

The project also includes a Django-based KPI app that handles KPI creation and asset-KPI linking.

## Features
- **Dynamic Equation Configuration**: The system loads equations dynamically from the `equation_config.json` file.
- **Message Processing**: Handles arithmetic and regex expressions.
- **Database Integration**: Saves processed results to a SQLite database.

## Setup and Configuration
### 1. Set Up the Django Backend
- Ensure you have Python installed and a virtual environment set up.
- Install the required dependencies:
```bash
pip install -r requirements.txt
```
- Apply the migrations for the Django project:
```bash
python manage.py migrate
```
- Start the Django server:
```bash
python manage.py runserver
```
### 2. Configure the Database
Make sure that your SQLite database is properly configured and contains the necessary tables (`processed_messages `, `kpi_kpi`, and `kpi_assetkpi`). You can inspect this with tools like `DBeaver`.

### 3. Running Tests
To run the unit tests for the message processor and KPI integration:
1. For the message processor:
```bash
python -m unittest discover -s tests
```
2. For the Django app:
```bash
python manage.py test
```
## API Endpoints
1. GET /api/kpi/: List all KPIs.
2. POST /api/kpi/: Create a new KPI.
3. POST /api/kpi/link/: Link an asset to a KPI.
