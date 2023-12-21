# Libraries.io

## Dependencies

- [python3](https://www.python.org/)
- [pipx](https://pipx.pypa.io/stable/)

## Installation

```bash
sunbeam extension install https://raw.githubusercontent.com/pomdtr/sunbeam-libraries/main/libraries.sh
```

## Setup

Get your token from <https://libraries.io>

## Development

```sh
python -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
sunbeam extension install ./.venv/bin/libraries
```
