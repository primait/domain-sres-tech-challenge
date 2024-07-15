import os


def check_env_vars(*env_vars):
    """
    Check if the specified environment variables are set.

    Parameters:
    env_vars (str): Environment variable names to check.

    Returns:
    bool: True if all specified environment variables are set, False otherwise.
    """
    missing_vars = [var for var in env_vars if not os.getenv(var)]
    if missing_vars:
        print(f"Missing environment variables: {', '.join(missing_vars)}")
        return False
    return True
