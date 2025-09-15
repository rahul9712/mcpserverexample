# /**
#  * A simple MCP server that allows us developers to do a deployment.
#  */
# 
# Commands to run this:
#    uv init
#    python3 -m venv .venv
#    source .venv/bin/activate
#    uv add mcp
#    pip install 'mcp[cli]'
#    mcp dev deployment.py
#

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Demo")

# Add an additional tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers.
    Args:
        a: The first number.
        b: The second number.
    Returns:
        The sum of the two numbers.
    """
    return a + b


