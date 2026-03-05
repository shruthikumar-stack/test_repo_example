"""
Utility functions for the application.
"""
import hashlib
import re
from datetime import datetime


def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def format_timestamp(dt: datetime) -> str:
    """Format a datetime object to ISO string."""
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def paginate(items: list, page: int = 1, per_page: int = 10) -> dict:
    """Paginate a list of items."""
    start = (page - 1) * per_page
    end = start + per_page
    return {
        "items": items[start:end],
        "total": len(items),
        "page": page,
        "per_page": per_page,
        "total_pages": (len(items) + per_page - 1) // per_page,
    }
