from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_PATH = "cocktail_robot.db"

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
    return render_template("tables.html", tables=tables)

if __name__ == "__main__":
    app.run(debug=True)
