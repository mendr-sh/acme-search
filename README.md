# acme-search

A small search API used to demonstrate [Mendr](https://www.mendr.sh).

> **This repository started with vulnerable dependencies on purpose.** They
> were pinned to releases from early 2021, so it has real, published
> advisories for Mendr to fix. Some can still be open. Do not deploy this code.

## What it does

- `search/views.py` serves the search API with **Django** and
  **djangorestframework**.
- `search/tokens.py` signs API tokens with **PyJWT** and encrypts page
  cursors with **cryptography**.
- `search/sql.py` formats slow queries for the logs with **sqlparse**.

Each module has tests in `tests/`, so a fix that breaks one of them fails CI.

```sh
pip install -r requirements-dev.txt
pytest
```
