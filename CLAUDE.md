# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

DrinkbotOS is open-source control software for the "Hello Drinkbot" cocktail robotics platform. It's an API-first Flask app with a SQLite backend for managing cocktail recipes and dispensing.

## Development Commands

**Setup:**
```bash
conda env create -f environment.yml
conda activate drinkbotos
```

**Run (development):**
```bash
flask run
```
Uses `FLASK_APP=app.py` and `FLASK_DEBUG=1` from `.env`.

**Run (production):**
```bash
gunicorn app:app
# or
python wsgi.py
```

There are no tests or linting tools configured.

## Architecture

Single-file Flask app (`app.py`) with Jinja2 templates and SQLite (`cocktail_robot.db`).

**Routes:**
- `GET /` — Home page, shows featured cocktails
- `GET /cocktail_detail/<id>` — Interactive cocktail customization with ingredient sliders
- `GET /api/status` — System readiness status
- `GET /db/tables` — Admin view of DB schema and recipes
- `GET /show_table/<table_name>` — View a specific DB table

**Database schema (5 tables):**
- `ingredients` — Catalog with `name`, `brand`, `description`, `abv`
- `types` — Categories (Spirit, Mixer, Juice, etc.)
- `ingredient_types` — Many-to-many join for ingredients ↔ types
- `cocktails` — Recipe definitions (`name`, `description`)
- `cocktail_ingredients` — Recipe composition with `quantity`, `unit`, `note`

**Theme system:** Theme name is resolved via `get_theme()` → CSS loaded from `static/themes/<theme>/style.css`. Eight themes are defined but only `default` is implemented.

**Frontend (`cocktail_detail.html`):** Vanilla JS with real-time sliders for per-ingredient quantity adjustment, volume-constraint rebalancing, ABV calculation, and a stacked visual glass representation.

## Key Notes

- The `api/` and `db/` directories are empty stubs for planned future development.
- `show_table` route uses an f-string with the table name directly in SQL — avoid extending this pattern to user-supplied input.
- `dbviewer.py` is a standalone utility for inspecting the database outside the web app.
