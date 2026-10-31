from mcp.server.fastmcp import FastMCP

server = FastMCP()
context_store = {}

@server.tool()
async def share_context(agent: str, content: str):
    """
    Store context from a specified agent.
    """
    if agent not in context_store:
        context_store[agent] = []
    context_store[agent].append(content)
    return {"result": f"Context stored from {agent}: {content}"}


@server.tool()
async def retrieve_context(query: str):
    """
    Retrieve all stored context entries matching the query text.
    """
    matching = []
    for agent, contents in context_store.items():
        for content in contents:
            if query.lower() in content.lower():
                matching.append({"agent": agent, "content": content})
    if not matching:
        return {"result": f"No context found matching query: {query}"}
    return {"result": matching}

@server.tool()
async def list_all_context():
    """
    Return the full context store with contexts from all agents.
    """
    return context_store
