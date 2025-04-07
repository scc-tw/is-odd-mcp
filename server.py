from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("IsOdd")


@mcp.tool()
def is_odd(num: int) -> bool:
    """
    Determines if a number is odd.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is odd, False otherwise
    """
    return num % 2 != 0


@mcp.resource("documentation://usage")
def get_usage_docs() -> str:
    """Get usage documentation for the is_odd function"""
    return """
    # IsOdd MCP Module
    
    This module provides a simple tool to determine if a number is odd.
    
    ## Usage
    
    Use the `is_odd` tool to check if a number is odd:
    
    ```
    is_odd(5)  # Returns: True
    is_odd(10)  # Returns: False
    ```
    
    The function takes an integer as input and returns a boolean value.
    """


@mcp.resource("examples://list")
def get_examples() -> str:
    """Get example usage of is_odd function"""
    return """
    # Examples
    
    ## Basic usage
    
    ```python
    # Check if 5 is odd
    is_odd(5)  # Returns: True
    
    # Check if 10 is odd
    is_odd(10)  # Returns: False
    ```
    
    ## Using with lists
    
    ```python
    # Filter odd numbers from a list
    numbers = [1, 2, 3, 4, 5]
    odd_numbers = list(filter(is_odd, numbers))  # [1, 3, 5]
    ```
    """


@mcp.prompt()
def odd_checker_prompt(number: int) -> str:
    """Create a prompt for checking if a number is odd"""
    return f"""
    Please determine if the number {number} is odd or even.
    Explain your reasoning step by step.
    """


@mcp.prompt()
def odd_filter_prompt(numbers: str) -> str:
    """Create a prompt for filtering odd numbers from a list"""
    return f"""
    Given this list of numbers: {numbers}
    Please filter out all the odd numbers and return only the odd ones.
    Explain your process step by step.
    """


if __name__ == "__main__":
    mcp.run()

