#!/usr/bin/env python3

import json
import sys

import requests
import sunbeam

manifest: sunbeam.Manifest = {
    "title": "Sunbeam",
    "preferences": [{"label": "API Key", "name": "api_key", "type": "text"}],
    "commands": [
        {"name": "platforms", "title": "List all platforms", "mode": "filter"},
        {
            "name": "search",
            "title": "Search for a package",
            "mode": "search",
            "params": [{"name": "platform", "label": "Platform", "type": "text"}],
        },
    ],
}


def main():
    if len(sys.argv) == 1:
        print(json.dumps(manifest))
        sys.exit(0)

    payload = json.loads(sys.argv[1])
    command = payload["command"]
    prefs = payload["preferences"]
    params = payload["params"]

    if command == "platforms":
        data = requests.get(
            "https://libraries.io/api/platforms", params={"api_key": prefs["api_key"]}
        ).json()
        res: sunbeam.List = {
            "items": [
                {
                    "title": item["name"],
                    "accessories": [f"{item['project_count']} projects available"],
                    "actions": [
                        {
                            "title": "Search",
                            "type": "run",
                            "run": {
                                "command": "search",
                                "params": {"platform": item["name"]},
                            },
                        },
                        {
                            "title": "Open Homepage",
                            "type": "open",
                            "open": {"url": item["homepage"]},
                        },
                    ],
                }
                for item in data
            ]
        }
        json.dump(res, sys.stdout)
    elif command == "search":
        if not payload.get("query"):
            json.dump(
                sunbeam.List({"emptyText": "Enter a query to search for"}), sys.stdout
            )
            sys.exit(0)
        data = requests.get(
            "https://libraries.io/api/search",
            params={
                "api_key": prefs["api_key"],
                "platforms": params["platform"],
                "q": payload.get("query"),
            },
        ).json()
        res: sunbeam.List = {
            "items": [
                {
                    "title": item["name"],
                    "actions": [
                        {
                            "title": "Open Homepage",
                            "type": "open",
                            "open": {"url": item["homepage"]},
                        }
                    ],
                }
                for item in data
            ]
        }
        json.dump(res, sys.stdout)


if __name__ == "__main__":
    main()
