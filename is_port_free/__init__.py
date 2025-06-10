"""
is-port-free - Check if a port is free

Simple and minimalistic port checker.
"""

__version__ = "1.0.0"
__author__ = "Abderrahim GHAZALI"

import socket


def is_port_free(port, host='localhost'):
    """
    Check if a port is free (available for binding).
    
    Args:
        port (int): Port number to check
        host (str): Host to check on (default: 'localhost')
    
    Returns:
        bool: True if port is free, False if port is in use
    
    Example:
        >>> is_port_free(8000)
        True
        >>> is_port_free(8000, 'localhost')
        True
        >>> is_port_free(80, '127.0.0.1')
        False
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((host, port))
            return True
    except (socket.error, OSError):
        return False


def is_port_used(port, host='localhost'):
    """
    Check if a port is in use (opposite of is_port_free).
    
    Args:
        port (int): Port number to check
        host (str): Host to check on (default: 'localhost')
    
    Returns:
        bool: True if port is in use, False if port is free
    
    Example:
        >>> is_port_used(8000)
        False
        >>> is_port_used(80)
        True
    """
    return not is_port_free(port, host)


# Aliases for convenience
check_port = is_port_free
port_available = is_port_free
port_free = is_port_free

__all__ = [
    'is_port_free',
    'is_port_used', 
    'check_port',
    'port_available',
    'port_free'
]