# is-odd

A simple Model Context Protocol (MCP) server that exposes a function to determine if a number is odd.

## Overview

This project demonstrates how to create a minimal MCP server that provides:
- An `is_odd` tool that checks if a number is odd
- Documentation and examples as resources
- Prompt templates for checking odd/even numbers

## Description

`is-odd` is a lightweight Python package that provides functionality to check if a number is odd. It's designed to be used with MCP, allowing AI assistants to easily determine if a number is odd when users ask questions like "Is 5 odd?" or "Check if 10 is odd."

## Features

- MCP server implementation for AI assistant integration
- Simple function to check if a number is odd
- Comprehensive documentation and examples

## Installation

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/scc-tw/is-odd-mcp.git
   cd is-odd-mcp
   ```

2. Install dependencies:
   ```bash
   # Using uv (recommended)
   uv init
   uv add "mcp[cli]"
   uv add --dev pytest pytest-cov
   ```

   Or using pip:
   ```bash
   pip install "mcp[cli]"
   pip install --dev pytest pytest-cov
   ```

## Usage

### Development Mode

Test the server with the MCP Inspector:
```bash
uv run mcp dev server.py
```

### Claude Desktop Integration

Install the server in Claude Desktop:
```bash
uv run mcp install server.py --name "IsOdd"
```

Once installed, you can use the tool in Claude:

- Ask Claude to check if a number is odd
- Claude will use your MCP server to perform the calculation

Example prompts you can try with Claude:

- "Is 42 an odd number?"
- "Filter out all the odd numbers from this list: 1,2,3,4,5,6,7,8,9,10"
- "What odd numbers are there between 10 and 20?"

### Direct Execution

```bash
uv run python server.py
# or
uv run mcp run server.py
```

## Server Capabilities

This MCP server provides:

| Type | Name | Description |
|------|------|-------------|
| Tool | `is_odd` | Determines if a number is odd |
| Resource | `documentation://usage` | Returns usage documentation |
| Resource | `examples://list` | Returns example usages |
| Prompt | `odd_checker_prompt` | Creates a prompt for checking odd/even numbers |
| Prompt | `odd_filter_prompt` | Creates a prompt for filtering odd numbers from a list |

## Development

### Testing

Run the tests with pytest:
```bash
uv run pytest
```

Or run tests directly:
```bash
uv run python -m tests.test_is_odd
```

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
