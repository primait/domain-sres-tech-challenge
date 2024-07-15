# Domain SREs Tech Challenge

This repo contains the template of a working Python application, to be used as starting point for the tech challenge candidates should do during the hiring process for a Domain SRE position.

The application is exposing three essential endpoints:
- `GET /users`: Retrieve a list of all users.
- `POST /user`: Enable the creation of a new user
- `POST /upload`: Providing an image of the user as avatar in an S3 bucket.

Additionally, you'll find a `/swagger` endpoint with a Swagger exposed, in order to provide documentation for the APIs and a UI for testing.

The application needs a set of AWS resources to work correctly, you can use both [Localstack CE](https://github.com/localstack/localstack) or an Official AWS Account (consider the Free Tier option).

In order to play locally with the application, you need some environment variables.
- edit the `.env-example` file
- change environment variables accordingly with your needs
- rename the `.env-example` file in `.env`

In order to start the application:

```
poetry install
cd prima-tech-challenge
poetry run flask run
```

## Tech Challenge Solution Overview:

### Task 1: Develop the Python API Server

Begin by developing a API Server using Python as the chosen programming language, with three essential endpoints:
- `GET /users`: Retrieve a list of all users.
- `POST /user`: Enable the creation of a new user
- `POST /upload`: Providing an image of the user as avatar in an S3 bucket.
If you aren't familiar with Python Web Development, you can start from the template `prima-tech-challenge` provided in this repo. Otherwise, you can write your own from scratch.

To enhance the reliability and maintainability of your application, please adhere to the following guidelines:
- Structure your application code in a well-organised manner, following coding standards and separation of concerns.
- Implement data persistence mechanisms with DynamoDB to securely store user information. This will not only extend the functionality of your application but will also provide an opportunity to demonstrate your commitment to reliability.
- Implement object storage mechanism with S3 to securely store your avatar

Apply basic error handling techniques to handle common scenarios, such as invalid requests or database errors.

### Task 2: Dockerise Your Application

Next, containerise your Python API server using Docker, ensuring that it can be seamlessly deployed in containerised environments.

### Task 3: Infrastructure as Code (IaC)

In this step, employ IaC principles and tools like Terraform or Pulumi to orchestrate the creation of the DynamoDB Table, S3 bucket and a role to access it. Provision all the essential resources, including roles and policies, required for the EKS cluster’s operation.

### Task 4: Kubernetes Deployment with Helm

Now, create a custom Helm Chart that includes templates for deploying your Python API server within the Kubernetes cluster. Define Helm Chart templates to encapsulate deployment, configuration, and scaling aspects of your application within the Kubernetes cluster. Focus on the reliability of the microservice (please consider autoscaling, healthchecks, and so on).

Please provide clear and concise documentation explaining the solution architecture, including how to use the scripts and any prerequisites.
