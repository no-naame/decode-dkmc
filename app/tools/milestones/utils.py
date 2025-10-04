from typing import Any, Dict


def format_response(data: Any, message: str = "Success") -> Dict[str, Any]:
    """Format API response in a consistent structure"""
    return {
        "success": True,
        "message": message,
        "data": data
    }


def format_error_response(message: str, error_code: str = "ERROR") -> Dict[str, Any]:
    """Format error response in a consistent structure"""
    return {
        "success": False,
        "message": message,
        "error_code": error_code,
        "data": None
    }
