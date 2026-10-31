# Execute the code

Run the inspector via the CLI, pointing it to your Python script using the STDIO transport:

npx.cmd @modelcontextprotocol/inspector python ai_engineering/mcp/mcp_server.py

This will launch a local web server (usually at http://localhost:5173). Navigate to the URL, and you will see the Inspector GUI.
Go to the Tools tab, select get_system_metrics, and execute it.
You should see your system's CPU and Memory stats returned in real-time.
