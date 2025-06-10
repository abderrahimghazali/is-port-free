# is-port-free

🔍 Check if a port is free - simple and minimalistic.

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/is-port-free.svg)](https://badge.fury.io/py/is-port-free)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why?

Sometimes you just need to check if a port is available. That's it. No complex features, no dependencies, just a simple function that returns `True` or `False`.

## Installation

```bash
pip install is-port-free
```

## Usage

### Basic Usage

```python
from is_port_free import is_port_free

# Check if port 8000 is free on localhost
if is_port_free(8000):
    print("Port 8000 is available!")
else:
    print("Port 8000 is in use")

# Check specific host
if is_port_free(8000, 'localhost'):
    print("Port 8000 is free on localhost")

if is_port_free(80, '127.0.0.1'):
    print("Port 80 is free on 127.0.0.1")
```

### Alternative Functions

```python
from is_port_free import is_port_used, check_port, port_available

# Check if port is in use (opposite of is_port_free)
if is_port_used(8000):
    print("Port 8000 is busy")

# Function aliases (all do the same thing as is_port_free)
check_port(8000)        # Returns True/False
port_available(8000)    # Returns True/False
```

### Command Line

```bash
# Check if port is free
is-port-free 8000

# Check specific host  
is-port-free 8000 --host localhost

# Quiet mode (only exit codes)
is-port-free 8000 --quiet
echo $?  # 0 = free, 1 = in use, 2 = error
```

## API Reference

### `is_port_free(port, host='localhost')`

Check if a port is free (available for binding).

**Parameters:**
- `port` (int): Port number to check
- `host` (str, optional): Host to check on. Defaults to 'localhost'

**Returns:**
- `bool`: `True` if port is free, `False` if port is in use

**Example:**
```python
is_port_free(8000)              # True
is_port_free(8000, 'localhost') # True  
is_port_free(80, '127.0.0.1')   # False (usually)
```

### `is_port_used(port, host='localhost')`

Check if a port is in use (opposite of `is_port_free`).

**Returns:**
- `bool`: `True` if port is in use, `False` if port is free

## Common Use Cases

### Starting a Development Server

```python
from is_port_free import is_port_free

def start_server(preferred_port=8000):
    port = preferred_port
    
    # Find next available port
    while not is_port_free(port):
        port += 1
        if port > 65535:
            raise Exception("No available ports")
    
    print(f"Starting server on port {port}")
    # start your server here
    return port
```

### Testing

```python
import pytest
from is_port_free import is_port_free

def test_my_server():
    # Make sure test port is available
    test_port = 8080
    assert is_port_free(test_port), f"Test port {test_port} is not available"
    
    # Start your test server
    server = start_test_server(test_port)
    
    # Port should now be in use
    assert not is_port_free(test_port)
    
    # Clean up
    server.stop()
```

### Docker Health Checks

```python
from is_port_free import is_port_used

def health_check():
    """Check if application is running"""
    if is_port_used(8000, 'localhost'):
        return "healthy"
    else:
        return "unhealthy"
```

### Port Allocation

```python
from is_port_free import is_port_free

def allocate_ports(count=3, start_port=8000):
    """Allocate multiple free ports"""
    ports = []
    port = start_port
    
    while len(ports) < count:
        if is_port_free(port):
            ports.append(port)
        port += 1
        
        if port > 65535:
            break
    
    return ports

# Get 3 free ports starting from 8000
free_ports = allocate_ports(3, 8000)
print(f"Available ports: {free_ports}")
```

## How It Works

The package uses Python's built-in `socket` library to attempt to bind to the specified port. If the bind succeeds, the port is free. If it fails, the port is in use.

```python
import socket

def is_port_free(port, host='localhost'):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((host, port))
            return True
    except (socket.error, OSError):
        return False
```

## Notes

- **No dependencies** - Uses only Python standard library
- **Cross-platform** - Works on Windows, macOS, and Linux  
- **Fast** - Minimal overhead, just a socket bind attempt
- **Safe** - Uses context managers to ensure proper socket cleanup
- **IPv4 only** - Currently only supports IPv4 addresses

## Edge Cases

- **Port 0**: Returns `True` (OS will assign an available port)
- **Invalid ports** (< 0 or > 65535): Returns `False`
- **Privileged ports** (< 1024): May require admin rights on some systems
- **Firewall**: Function checks if port can be bound, not if it's accessible externally

## Contributing

This package is intentionally minimal. If you need more features, consider:
- [portpicker](https://pypi.org/project/portpicker/) - More advanced port selection
- [python-port-for](https://pypi.org/project/port-for/) - Port testing utilities

For bug fixes or small improvements, pull requests are welcome!