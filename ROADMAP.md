# DrinkbotOS Roadmap

## 1. Admin UI
Nav links are currently placeholders.
- Edit Cocktails — add, edit, delete recipes
- Edit Ingredients — manage the ingredient catalog (name, brand, ABV, type)
- Ingredient "loaded" management — mark which ingredients are currently on tap

## 2. Index / Browse Page
- Cocktail cards link to detail pages (currently no href)
- Filter/search by ingredient or type
- Show only cocktails makeable from loaded ingredients

## 3. Core API
The `api/` directory is currently empty.
- `GET /api/cocktails` — list all cocktails
- `GET /api/ingredients/loaded` — what's currently on tap
- `POST /api/dispense` — trigger a pour (the "Make This Cocktail" button currently shows an alert)
- `GET /api/status` — system readiness

## 4. Hardware Integration
- Pump/relay control layer
- Calibration tool (ml-per-second per pump)
- Dispense sequencing (order of pours, timing)
- Hardware status monitoring

## 5. Themes
Seven themes are named but only `default` is implemented.
- Build out at least one or two alternates (dark, neon_nightclub)
- Theme selector in the UI

## 6. Polish & Stability
- Remove debug output (`<pre id="debug-output">`, `console.log` statements)
- Error handling for missing cocktails / empty DB
- Tests
