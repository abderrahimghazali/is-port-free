"""
Tests for is-port-free
"""

import pytest
import socket
import threading
import time
from is_port_free import is_port_free, is_port_used, check_port, port_available


class TestIsPortFree:
    """Test the is_port_free function"""
    
    def test_free_port(self):
        """Test with a port that should be free"""
        # Use a high port number that's likely to be free
        assert is_port_free(65432) == True
    
    def test_used_port_with_server(self):
        """Test with a port that we bind to"""
        # Create a server to occupy a port
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 0))  # Let OS choose port
        port = server.getsockname()[1]
        server.listen(1)
        
        try:
            # Port should be in use
            assert is_port_free(port) == False
        finally:
            server.close()
    
    def test_different_hosts(self):
        """Test with different host addresses"""
        port = 65433
        
        # Test localhost
        result_localhost = is_port_free(port, 'localhost')
        
        # Test 127.0.0.1
        result_127 = is_port_free(port, '127.0.0.1')
        
        # Should be consistent
        assert result_localhost == result_127
    
    def test_invalid_port(self):
        """Test with invalid port numbers"""
        # Port 0 might behave differently
        # Negative port should raise an error or return False
        assert is_port_free(-1) == False
        
        # Port > 65535 should return False
        assert is_port_free(70000) == False
    
    def test_is_port_used(self):
        """Test the is_port_used function"""
        port = 65434
        
        # Should be opposite of is_port_free
        free = is_port_free(port)
        used = is_port_used(port)
        
        assert free != used
    
    def test_aliases(self):
        """Test function aliases"""
        port = 65435
        
        # All should return the same result
        result1 = is_port_free(port)
        result2 = check_port(port)
        result3 = port_available(port)
        
        assert result1 == result2 == result3
    
    def test_with_threaded_server(self):
        """Test with a threaded server"""
        port = 0  # Let OS choose
        server_running = threading.Event()
        server_socket = None
        chosen_port = None
        
        def run_server():
            nonlocal server_socket, chosen_port
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('localhost', port))
            chosen_port = server_socket.getsockname()[1]
            server_socket.listen(1)
            server_running.set()
            
            # Keep server running briefly
            time.sleep(0.1)
            server_socket.close()
        
        # Start server in thread
        thread = threading.Thread(target=run_server)
        thread.start()
        
        # Wait for server to start
        server_running.wait(timeout=1.0)
        
        try:
            # Port should be in use while server is running
            assert is_port_free(chosen_port) == False
        finally:
            thread.join(timeout=1.0)