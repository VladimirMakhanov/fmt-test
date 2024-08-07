# fmt-test

This is a test assignment for a Python developer position, focusing on image collection and processing using microservices architecture.

## Project Description

The project consists of three microservices that communicate via RabbitMQ:

1. **Scheduler**: Retrieves schedules from MongoDB and sends messages to the Image Collector at specified times.
2. **Image Collector**: Receives messages from the Scheduler, fetches images from an external API, uploads them to S3, and sends messages to the Data Uploader.
3. **Data Uploader**: Receives messages from the Image Collector and processes them.

The main focus of this assignment is on implementing the Image Collector service.

## Requirements

- Python 3.10+
- Poetry for dependency management
- RabbitMQ
- MongoDB
- AWS S3 account

## Local Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/fmt-test.git
cd fmt-test
```

2. Install dependencies using Poetry:
```bash
   poetry install --no-root --with=dev
```


## Project Structure

- `service/`: Contains the main service files
  - `scheduler.py`: Implements the Scheduler service
  - `image_collector.py`: Implements the Image Collector service
  - `data_uploader.py`: Implements the Data Uploader service
- `types/`: Contains type definitions
- `tests/`: Contains test files

## Implementation Tasks

As a candidate, you should focus on implementing the `ImageCollector` class in `service/image_collector.py`. Specifically:

1. Implement the `get_client_credentials` method to fetch client credentials from an external API.
2. Implement the `get_image` method to fetch an image from the client's API using the obtained credentials.
3. Complete the `upload_to_s3` method, ensuring it uses the correct bucket name and key structure.
4. Ensure all imports are correct and all necessary dependencies are installed.

## Setting up pre-commit hooks

This project uses pre-commit hooks to ensure code quality and consistency. To set up the pre-commit hooks:

1. Install pre-commit:
```bash
   poetry run pre-commit install
```

2. (Optional) Run pre-commit on all files:
```bash
   poetry run pre-commit run --all-files
```

Now, pre-commit will run automatically before each commit, checking your code for style violations, formatting issues, and performing static analysis.


## Code Formatting and Linting

This project uses Black for code formatting, isort for import sorting, and flake8 for linting. You can run these tools manually:
```bash
poetry run black .
poetry run isort .
poetry run flake8 .
```

Or let the pre-commit hooks handle it automatically when you commit your changes.
