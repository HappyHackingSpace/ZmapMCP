# ZMap MCP 

A FastMCP wrapper for ZMap network scanner that provides a simple interface for scanning networks through a structured API.

## Install
```
> sudo apt install zmap -y
> uv venv
> uv add "mcp[cli]" httpx
> pip install zmapsdk
> pip install FastMCP
> pip install ipaddress
```

## Requirements

- Python 3.13+
- ZMap network scanner (installed locally or via Docker)
- FastMCP
- zmapsdk

## Usage

### Running the Server

Start the FastMCP server:

```
fastmcp install server.py
python server.py
Run Claude desktop
```

### Available Tools

The server exposes the following tools:

- `scan(target, port)`: Scan a specific subnet for open ports
  - `target`: Target subnet in CIDR notation (e.g., "192.168.1.0/24")
  - `port`: Target port number to scan



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer
This project is intended for educational and authorized security testing purposes only. Unauthorized scanning of networks that you do not own or have explicit permission to test is strictly prohibited and may be illegal in your jurisdiction.

By using this software, you agree that you are solely responsible for your actions. The authors and contributors of this project assume no liability for any misuse or damage caused by the use of this tool.