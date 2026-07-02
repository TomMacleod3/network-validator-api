# Network Validator API
A FastAPI-based backend project for validating and generating network device configuration data.

Network Validator API provides endpoints for validating network configuration input and generating basic configuration output from structured data.

The project currently includes:

FastAPI application structure

Pydantic models for request validation

Service-layer validation logic

Configuration generation logic

API routes for validation and generation

Automated tests using pytest

Test coverage reporting using pytest-cov

## Run locally
Running the Project Locally

Clone the repository:

git clone <your-repository-url>
cd network-validator-api

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate

### Install dependencies:

pip install -r requirements.txt


### Run the FastAPI application:

uvicorn app.main:app --reload

Open the API documentation in your browser:

http://127.0.0.1:8000/docs


## Running Tests
Running Tests

Run the full test suite:

pytest

Run tests with coverage:

pytest --cov=app --cov-report=term-missing

### Current test status:
13 passed
95% total test coverage

