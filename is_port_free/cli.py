"""
Command line interface for is-port-free
"""

import sys
import argparse
from . import is_port_free, __version__


def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description='Check if a port is free',
        prog='is-port-free'
    )
    
    parser.add_argument(
        'port', 
        type=int, 
        help='Port number to check'
    )
    
    parser.add_argument(
        '--host', 
        default='localhost',
        help='Host to check (default: localhost)'
    )
    
    parser.add_argument(
        '--version', 
        action='version', 
        version=f'is-port-free {__version__}'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Quiet mode - only return exit code'
    )
    
    args = parser.parse_args()
    
    try:
        free = is_port_free(args.port, args.host)
        
        if not args.quiet:
            status = "FREE" if free else "IN USE"
            print(f"Port {args.port} on {args.host}: {status}")
        
        # Exit code: 0 if free, 1 if in use
        sys.exit(0 if free else 1)
        
    except Exception as e:
        if not args.quiet:
            print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()