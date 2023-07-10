# prefect sample

This Python application retrieves data from an external API, performs data manipulation, and generates a markdown report.

## Overview

The application performs the following steps:

1. Retrieves data from an external API.
2. Updates the data by modifying specific fields and adding a unique identifier.
3. Generates a markdown report containing selected fields.

## Prerequisites

- Assumes docker is installed

## How to Run

1. Clone the repo.

2. Navigate to project root dir.

3. Run the following command to build and start the Docker containers:

   ```bash
   docker-compose up
   ```

This will build the necessary Docker images and start the containers.

- Monitor the logs in the terminal to ensure that the containers are running without any errors.

- The application will run once prefect is up and will generate the markdown report.

- Open the web browser to `127.0.0.1:4200`.

