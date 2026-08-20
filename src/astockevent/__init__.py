"""AStockEvent — now a **remote** MCP server.

This package no longer contains an implementation. AStockEvent is served over
Streamable HTTP at https://astockevent.com/mcp/ — point your MCP client at that URL
instead of installing anything.

Why the change: version 0.2.x shipped a stdio MCP server that talked to a REST backend
which no longer exists. Rather than leave a package that fails in a confusing way, this
version says so plainly and tells you where to go.
"""

__version__ = "0.3.0"

MCP_URL = "https://astockevent.com/mcp/"
DOCS_URL = "https://astockevent.com/docs"

_MESSAGE = f"""\
AStockEvent is now a REMOTE MCP server — there is nothing to install.

  Point your MCP client at:  {MCP_URL}

  Example (Claude Desktop and other clients that accept a remote URL):

      {{
        "mcpServers": {{
          "astockevent": {{
            "url": "{MCP_URL}"
          }}
        }}
      }}

  REST API and docs:  {DOCS_URL}

No API key and no sign-up. This package (0.3.0) is a pointer, not an implementation;
version 0.2.x shipped a stdio server whose backend no longer exists.
"""


def _cli() -> int:
    """Entry point kept from 0.2.x so the old command prints guidance, not a traceback."""
    print(_MESSAGE)
    return 0


def __getattr__(name: str):
    # 🔴 老代码里 `from astockevent import ...` 会走到这里 —— 给一句能看懂的话，
    #    而不是一个 AttributeError（那会让人以为是自己装错了）。
    raise AttributeError(
        f"astockevent has no attribute {name!r}. This package is now a pointer only — "
        f"AStockEvent is a remote MCP server at {MCP_URL}. See {DOCS_URL}."
    )
