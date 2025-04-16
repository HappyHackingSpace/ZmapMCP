"""
ZMap Scanner FastMCP Server
--------------------------------
A FastMCP server that provides a structured API for ZMap network scanning.
"""

from typing import Any, List, Dict, Optional
import httpx
import json
import ipaddress
import logging
from zmapsdk import ZMap
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("zmap-mcp")

# Initialize FastMCP server
mcp = FastMCP("ZmapMCP")

# Initialize ZMap
zmap = ZMap()

@mcp.tool()
def scan(target: str, port: int) -> Any:
    """
    Scan a target subnet for a specific open port.
    
    Args:
        target (str): Target subnet in CIDR notation (e.g., "192.168.1.0/24").
        port (int): Target port number to scan.
        
    Returns:
        dict: Scan results containing discovered hosts with the port open.
    """
    # Validate subnet format
    try:
        ipaddress.IPv4Network(target)
    except ValueError:
        raise ValueError("Invalid subnet format. Expected format: 192.168.1.0/24")
    
    # Validate port
    if not (0 < port <= 65535):
        raise ValueError("Invalid port number. Must be between 1 and 65535.")

    logger.info(f"Starting scan of {target} on port {port}")
    
    # Attempt scan
    try:
        return zmap.scan(
            target_port=port,
            subnets=[target],
            bandwidth="1M"
        )
    except Exception as e:
        logger.error(f"Scan failed: {str(e)}")
        return {"error": str(e)}

# Run the server
if __name__ == "__main__":
    # Log server startup
    logger.info("Starting ZMap MCP server...")
    
    # Check ZMap version on startup
    try:
        version = zmap.get_version()
        logger.info(f"ZMap version: {version}")
    except Exception as e:
        logger.warning(f"Warning: Could not determine ZMap version: {e}")
    
    # Start server
    mcp.run()  # or remove 'transport' if you prefer default
