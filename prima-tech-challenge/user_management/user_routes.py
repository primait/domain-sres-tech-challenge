from flask import Blueprint, jsonify, request

from .user_service import create_user, get_all_users, uploader

user_blueprint = Blueprint("user", __name__)

REQUIRED_FIELDS = ["name", "email"]


def validate_user_data(data):
    """
    Validates the user data.

    This function checks if the provided user data contains all the required fields.
    It returns an error message and HTTP status code if any required field is missing.

    Args:
        data (dict): The user data to be validated.

    Returns:
        Tuple[str, int]: Error message and HTTP status code if validation fails, otherwise (None, None).
    """

    if not data:
        return "Missing required data", 400
    for field in REQUIRED_FIELDS:
        if field not in data:
            return f"Missing required data: {field}", 400
    return None, None


@user_blueprint.route("/users", methods=["GET"])
def get_users():
    """
    Endpoint to get all users.

    This endpoint handles GET requests to fetch all users from the DynamoDB table.

    Returns:
        Tuple[Response, int]: JSON response containing the list of users and HTTP status code.
    """

    return get_all_users()


@user_blueprint.route("/user", methods=["POST"])
def post_user():
    """
    Endpoint to create a new user.

    This endpoint handles POST requests to create a new user in the DynamoDB table.
    It validates the user data before attempting to create the user.

    Returns:
        Tuple[Response, int]: JSON response indicating success or failure and HTTP status code.
    """

    user_data = request.json
    error_message, status_code = validate_user_data(user_data)

    if error_message:
        return jsonify({"error": error_message}), status_code

    return create_user(user_data)


@user_blueprint.route("/upload", methods=["POST"])
def upload_file():
    """
    Endpoint to upload a file.

    This endpoint handles POST requests to upload a file to an S3 bucket.
    It checks if a file is included in the request before attempting the upload.

    Returns:
        Tuple[Response, int]: JSON response indicating success or failure and HTTP status code.
    """

    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]

    message, status = uploader(file)

    return message, status
