import os

import boto3
from flask import jsonify

from .utils import check_env_vars

required_env_vars = [
    "DYNAMODB_TABLE",
    "S3_BUCKET",
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
]
if os.getenv("LOCALSTACK_HOST"):
    required_env_vars.remove("AWS_ACCESS_KEY_ID")
    required_env_vars.remove("AWS_SECRET_ACCESS_KEY")

if not check_env_vars(*required_env_vars):
    raise EnvironmentError("Required environment variables are not set")

DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE")
S3_BUCKET = os.getenv("S3_BUCKET")
LOCALSTACK_HOST = os.getenv("LOCALSTACK_HOST")
AWS_REGION = os.getenv("AWS_REGION", "eu-west-1")
AWS_ACCESS_KEY_ID = os.getenv(
    "AWS_ACCESS_KEY_ID", "fakeAccessKeyId" if LOCALSTACK_HOST else None
)
AWS_SECRET_ACCESS_KEY = os.getenv(
    "AWS_SECRET_ACCESS_KEY", "fakeSecretAccessKey" if LOCALSTACK_HOST else None
)


def get_all_users():
    """
    Fetches all users from the DynamoDB table.

    This function scans the specified DynamoDB table and returns all items (users).
    It handles any exceptions that occur during the scan operation and returns an
    appropriate JSON response.

    Returns:
        Tuple[Response, int]: JSON response containing the list of users and HTTP status code.
    """

    dynamodb = boto3.resource(
        "dynamodb",
        region_name=AWS_REGION,
        endpoint_url=LOCALSTACK_HOST,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    table = dynamodb.Table(DYNAMODB_TABLE)

    try:
        response = table.scan()
        return jsonify(response.get("Items", [])), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def create_user(user_data):
    """
    Creates a new user in the DynamoDB table.

    This function inserts a new item (user) into the specified DynamoDB table.
    It handles any exceptions that occur during the put_item operation and returns an
    appropriate JSON response.

    Args:
        user_data (dict): A dictionary containing the user data to be inserted.

    Returns:
        Tuple[Response, int]: JSON response indicating success or failure and HTTP status code.
    """

    dynamodb = boto3.resource(
        "dynamodb",
        region_name=AWS_REGION,
        endpoint_url=LOCALSTACK_HOST,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    table = dynamodb.Table(DYNAMODB_TABLE)

    try:
        table.put_item(Item=user_data)
        return jsonify({"success": "User created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def uploader(file, filename):
    """
    Uploads a file to an S3 bucket.

    This function uploads a given file to the specified S3 bucket and makes it publicly readable.
    It handles any exceptions that occur during the upload operation and returns an
    appropriate JSON response.

    Args:
        file: The file to be uploaded.

    Returns:
        Tuple[Response, int]: JSON response indicating success or failure and HTTP status code.
    """

    s3_client = boto3.client(
        "s3",
        region_name=AWS_REGION,
        endpoint_url=LOCALSTACK_HOST,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    try:
        s3_client.upload_fileobj(
            file, S3_BUCKET, filename, ExtraArgs={"ACL": "public-read"}
        )
        return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"
    except Exception as e:
        return jsonify({"error": str(e)}), 500
