# astockevent-mcp — public front door

## What this repository is

The **public face** of AStockEvent: what the server is, how to connect to it, and the
[`server.json`](./server.json) descriptor used by the MCP registry.

🔴 **There is no server implementation here, and there should not be one.**
AStockEvent's MCP server is **remote** (Streamable HTTP) — callers point a client at
`https://astockevent.com/mcp/` rather than installing code. A server implementation
published here would (a) be pointless, since nobody runs it, and (b) not even start,
since it imports a private service layer.

## What lives in the private repository

`NengjiangLunpi/astockevent` (private) holds the extraction engines, crawlers, parsers,
schemas, deployment and everything else. Nothing about how extraction works belongs here.

## Rules for anyone editing this repo

- ❌ **No extractor / pipeline / crawler logic**, and no references to private code paths.
- ❌ **No internal tooling.** This repo previously shipped an admin console, an extraction
  review UI and a cost report — they exposed our extraction methodology (regex-vs-LLM
  arbitration) and LLM spend, which the public API deliberately strips. Removed 2026-08-20.
  Do not add anything of that kind back.
- ❌ **Nothing that describes an API we do not serve.** The MVP-era stdio server sat here
  for 80 days describing a backend that no longer existed; anyone following it would have
  wired up to nothing. Public docs going stale is a correctness bug, not a chore.
- ✅ Connection instructions, coverage statements, `server.json`, license.
- ✅ Keep coverage claims in sync with what `list_coverage` actually returns —
  the tool is the source of truth, this README is a copy.
