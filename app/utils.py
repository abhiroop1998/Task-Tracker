from rest_framework.response import Response


def get_response_schema(schema, message, status_code):
    """ Utility: Standard response structure """

    return Response({
        'message': message,
        'status': status_code,
        'results': schema,
    }, status=status_code)


def get_global_success_messages():
    """ Utility: Get global success messages """
    data = {
        'CREDENTIALS_MATCHED': 'Login successful.',
        'RECORD_CREATED': 'Record created successfully.',
        "TASK_CREATED": "Task created successfully.",
        "LOGIN_SUCCESSFUL": "Login successful.",
        "LOGOUT_SUCCESSFUL": "Logout successful.",
        "NEW_USER_CREATED": "New user created successfully.",
        "RECORD_RETRIEVED": "Record retrieved successfully.",
        "RECORD_UPDATED": "Record updated successfully.",
        "RECORD_DELETED": "Record deleted successfully.",

    }

    return data


def get_global_error_messages():
    """ Utility: Get global error messages """
    data = {
        'SOMETHING_WENT_WRONG': 'Something went wrong. Please try again.',
        'BAD_REQUEST': 'Bad request. Please try again.',
        'INVALID_CREDENTIALS': 'Invalid credentials. Please try again.',
    }
    return data
