# %%

import asyncio
import psutil
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

app = Server("System-Monitor-MCP") # Create the MPC server

@app.list_tools()
async def list_tools() -> list[Tool]:
    """
    When an MPC client asks which tools are available, this method is executed to provide the list of tools.
    Register the tools exposed by this server.
    """
    return [
        Tool(
            name="get_system_metrics",
            description="Fetches real-time CPU and Memory usage of the host machine.",
            inputSchema={
                "type": "object",
                "properties": {
                    "verbose": {
                        "type": "boolean",
                        "description": "If true, returns detailed memory statistics."
                    }},
                "required": []
            })]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """
    When an MCP client calls a tool, execute this function to handle the request.
    Handle the execution of registered tools.
    """
    if name == "get_system_metrics":
        verbose = arguments.get("verbose", False)
        
        cpu_usage = psutil.cpu_percent(interval=0.5)
        memory = psutil.virtual_memory()
        
        if verbose:
            result = f"CPU Usage: {cpu_usage}%\nTotal Memory: {memory.total / (1024**3):.2f} GB\nAvailable Memory: {memory.available / (1024**3):.2f} GB\nMemory Used: {memory.percent}%"
        else:
            result = f"CPU: {cpu_usage}%, Mem: {memory.percent}%"
            
        return [TextContent(type="text", text=result)]
    
    raise ValueError(f"Unknown tool: {name}")

async def main():
    """
    Run the server using STDIO transport.
    """
    print("Starting System Monitor MCP Server...", flush=True)
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options())
if __name__ == "__main__":
    asyncio.run(main())