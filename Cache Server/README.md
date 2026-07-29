# Cache Server System

A simple two-level file-serving system constructed entirely with pure Python sockets — no frameworks, no libraries, except for the standard library.

## How it works

- **Cache Server**: Receives client requests and checks the local cache first.
  - Cache hit → delivers the file straight away.
  - Cache miss → goes ahead and forwards the request to the Origin Server, keeps a local copy and serves the file to the client.
- **Origin Server**: Contains the original files. It can either send them on request or return a 404 error if the file is unavailable.

This is comparable to a CDN/caching architecture at a small level — the same straight idea of Cloudflare or Varnish, just without anything but the necessary elements.

## Why I built this

In order to practically grasp what goes on beneath the surface when a browser "requests a file" — sockets, TCP connections, manual request parsing — instead of sorting it out in `requests` or a web framework to hide it all.

## Usage

```bash
# Start the origin server
python origin_server.py -a 127.0.0.1 -p 9000

# Start the cache server
python cache_server.py -a 127.0.0.1 -p 8000

# Test it with the client
python client.py
```

## Files

| File | Purpose |
|---|---|
| `cache_server.py` | Cache tier; serves from local cache or falls through to origin |
| `origin_server.py` | Origin tier; source of truth for files |
| `fetchfile.py` | Shared helper; looks up a file locally |
| `client.py` | Basic test client |

## Roadmap
- [ ] Correct HTTP status lines/headers
- [ ] Origin host/port configurable (hardcoded right now)
- [ ] Cache expiry/invalidation
