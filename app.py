from flask import Flask, jsonify, render_template
from dbviewer import db_view
import sqlite3
from collections import defaultdict

app = Flask(__name__)

DB_PATH = "cocktail_robot.db"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/status")
def status():
    return jsonify({
        "status": "ready",
        "ingredients_loaded": 4
    })

def get_cocktail_recipes():
    """" return all cocktails and their recipes, an example of all of the queries needed """
    return [1,2,3]


def get_cocktails_with_ingredients_and_types(db_path="cocktail_robot.db"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Query all cocktails
    cursor.execute("SELECT * FROM cocktails")
    cocktails = cursor.fetchall()

    result = {}

    for cocktail in cocktails:
        cocktail_id = cocktail["id"]
        cocktail_name = cocktail["name"]
        description = cocktail["description"]

        # Query ingredients for this cocktail
        cursor.execute("""
            SELECT ci.quantity, ci.unit, ci.note,
                   i.name AS ingredient_name, i.id AS ingredient_id
            FROM cocktail_ingredients ci
            JOIN ingredients i ON ci.ingredient_id = i.id
            WHERE ci.cocktail_id = ?
        """, (cocktail_id,))
        ingredients = cursor.fetchall()

        ingredient_list = []
        for ing in ingredients:
            ingredient_id = ing["ingredient_id"]

            # Query types for this ingredient
            cursor.execute("""
                SELECT t.name
                FROM ingredient_types it
                JOIN types t ON it.type_id = t.id
                WHERE it.ingredient_id = ?
            """, (ingredient_id,))
            types = [row["name"] for row in cursor.fetchall()]

            ingredient_list.append({
                "name": ing["ingredient_name"],
                "quantity": ing["quantity"],
                "unit": ing["unit"],
                "note": ing["note"],
                "types": types
            })

        result[cocktail_name] = {
            "description": description,
            "ingredients": ingredient_list
        }

    conn.close()
    return result

@app.route("/show_table/<table_name>")
def show_table(table_name):
    conn = sqlite3.connect("cocktail_robot.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
    except sqlite3.Error as e:
        rows = []
        print(f"Error reading {table_name}: {e}")
    finally:
        conn.close()
    return render_template("show_table.html", table_name=table_name, rows=rows)

def get_database_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()

        table_info = []
        for (table_name,) in tables:
            cursor.execute(f"PRAGMA table_info({table_name});")
            schema = cursor.fetchall()

            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
            rows = cursor.fetchall()

            table_info.append({
                "name": table_name,
                "schema": schema,
                "rows": rows
            })
        return table_info

@app.route("/db/tables")
def db_view():
    tables = get_database_tables()
    recipes = get_cocktail_recipes()
    recipes=get_cocktails_with_ingredients_and_types()
    return render_template("tables.html", tables=tables, recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)


