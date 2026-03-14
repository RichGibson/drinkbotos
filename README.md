# DrinkbotOS

> *Cocktail robotics made simple.*

DrinkbotOS is the open-source control software for the **Hello Drinkbot** hardware platform. It replaces earlier Bartendro-based systems with a modern, extensible, API-first foundation that supports both basic cocktail-making and delightfully weird robotic interfaces.

## Getting Started

```bash
conda env create -f environment.yml
conda activate drinkbotos
flask run
```

Then visit `http://127.0.0.1:5000`.

> **macOS note:** Port 5000 is used by AirPlay Receiver. Either disable it in System Settings → General → AirDrop & Handoff, or run on a different port: `flask run --port 5001`

## What is DrinkbotOS?

DrinkbotOS is designed to:
- Control pumps, relays, and valves to dispense liquids precisely
- Provide a RESTful API for programmatic drink requests
- Offer a friendly web interface for manual operation
- Support creative extensions like chatbot bartenders, physical controllers, or remote pour requests

## Core Features

- Ingredient & cocktail database with unit support
- API-first architecture for UI, hardware, and chat integrations
- Web interface with admin and user modes
- Modular backend in Python (Flask + SQLite)
- Personality hooks for custom bartender behaviors

## Cocktail Detail View

The cocktail customization page provides an interactive drink builder:

- **Per-ingredient sliders** grouped by type (Spirit, Mixer, etc.) with color-coded labels matching the glass visualization
- **Coupe glass visualization** — ingredient layers masked to the bowl shape of a coupe glass, with a concave meniscus on the top layer
- **Drink size selector** — Taster (1 oz), ½ Drink, Normal, and Double; the glass fill level adjusts proportionally
- **Keep total volume constant** — adjusting one ingredient proportionally rescales all others to maintain the same total volume
- **Live ABV estimate** and total volume display

## API Highlights

- `GET /api/cocktails` — List all cocktails
- `GET /api/ingredients/loaded` — Show what's currently on tap
- `POST /api/dispense` — Dispense a cocktail
- `GET /api/status` — System status and readiness

## Project Structure

```
drinkbotos/
├── app.py              # Flask app entrypoint
├── wsgi.py             # WSGI entry point for production
├── templates/          # Jinja2 HTML templates
├── static/
│   ├── themes/         # CSS themes (default implemented)
│   └── images/         # SVG glass assets and masks
├── api/                # RESTful endpoints (planned)
└── db/                 # Database utilities (planned)
```

## Acknowledgments

DrinkbotOS builds on the ideas and inspiration of the **Bartendro** project by Party Robotics. While no code was reused, Bartendro's open-source legacy helped spark the creation of Hello Drinkbot.

## License

MIT — free to use, remix, pour, and party responsibly.
