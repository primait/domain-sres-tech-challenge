# Domain SREs Tech Challenge

This repo contains the template of a working Python application, to be used as starting point for the tech challenge candidates should do during the hiring process for a Domain SRE position.

The application is exposing two essential endpoints:
- `GET /users`: Retrieve a list of all users.
- `POST /user`: Enable the creation of a new user

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
