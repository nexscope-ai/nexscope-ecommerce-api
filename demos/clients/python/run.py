"""Run a catalog example with Python standard-library HTTP."""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, file_pointer, code, message, headers, new_url):
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("example", help="Path below demos/")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    folder = (ROOT / args.example).resolve()
    if not folder.is_relative_to((ROOT / "demos").resolve()):
        parser.error("Example must be inside demos/")
    config = json.loads((folder / "example.json").read_text(encoding="utf-8"))
    payload_path = (ROOT / config["payload"]).resolve()
    if not payload_path.is_relative_to(ROOT):
        parser.error("Payload must be inside repository")
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    def has_placeholder(value):
        if isinstance(value, dict):
            return any(has_placeholder(item) for item in value.values())
        if isinstance(value, list):
            return any(has_placeholder(item) for item in value)
        if not isinstance(value, str):
            return False
        host = (urllib.parse.urlsplit(value).hostname or "").lower()
        return host in ("example.com", "example.org", "example.net") or host.endswith(".example.com")
    if config["mode"] == "mcp":
        payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": config["mcpToolName"], "arguments": payload}}
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    print("POST", config["endpoint"])
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not args.execute:
        print("Preview only. Add --execute to send.")
        return
    if has_placeholder(payload):
        parser.error("Replace example.com/example.org/example.net URLs before executing")
    key = os.environ.get("NEXSCOPE_API_KEY")
    if not key:
        parser.error("NEXSCOPE_API_KEY is required")
    request = urllib.request.Request(config["endpoint"], data=body, headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, method="POST")
    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=120) as response:
            result = json.load(response)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            mcp_result = result.get("result")
            if result.get("code", 0) != 0 or result.get("error") or (isinstance(mcp_result, dict) and mcp_result.get("isError")):
                raise SystemExit(1)
    except urllib.error.HTTPError as error:
        print(error.read().decode("utf-8"), file=sys.stderr)
        raise SystemExit(error.code) from None


if __name__ == "__main__":
    main()
