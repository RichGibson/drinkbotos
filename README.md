# DrinkbotOS


TODO: fix license


#drinkbotos
#robot
#cocktail

> *Cocktail robotics made simple.*

DrinkbotOS is the open-source control software for the **Hello Drinkbot** hardware platform. It replaces earlier Bartendro-based systems with a modern, extensible, API-first foundation that supports both basic cocktail-making and delightfully weird robotic interfaces.

## What is DrinkbotOS?
DrinkbotOS is designed to:
- Control pumps, relays, and valves to dispense liquids precisely
- Provide a RESTful API for programmatic drink requests
- Offer a friendly web interface for manual operation
- Support creative extensions like chatbot bartenders, physical controllers, or remote pour requests

## Core Features
- Ingredient & Cocktail database (with unit support)
- API-first architecture for UI, hardware, and chat integrations
- Web interface with admin & user modes
- Modular backend in Python (Flask + SQLite)
- Personality hooks for custom bartender behaviors

## 📁 Project Structure
```
📦 drinkbotos/
├── api/                # RESTful endpoints
├── static/             # CSS, JavaScript
├── templates/          # Jinja2 HTML
├── db/                 # SQLite and schema
├── scripts/            # Setup, calibration
└── app.py              # Flask app entrypoint
```

## Getting Started
```bash
$ conda env create -f environment.yml
$ conda activate drinkbotos
$ flask run
```

## API Highlights
- `GET /api/cocktails` — List all cocktails
- `GET /api/ingredients/loaded` — Show what's currently on tap
- `POST /api/dispense` — Dispense a cocktail
- `GET /api/status` — System status and readiness

## Acknowledgments
DrinkbotOS builds on the ideas and inspiration of the **Bartendro** project by Party Robotics. While no code was reused, Bartendro's open-source legacy helped spark the creation of Hello Drinkbot.

## License
MIT — free to use, remix, pour, and party responsibly.
