from flask import Flask, json, render_template, jsonify
import psycopg2
import psycopg2.extras


def connect_db():
    conn = psycopg2.connect(
        host="plop.inf.udec.cl",
        user="bdi2021cb",
        password="bdi2021cb",
        database="bdi2021cb"
    )
    return conn

def get_pokemon():
    conn = connect_db()
    cursor = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

    cursor.execute("select * from pokedex.pokemon")
    result = cursor.fetchall()
    result = [row._asdict() for row in result]

    cursor.close()
    conn.close()
    return result

app = Flask(__name__)

@app.route("/")
def index():
    data = get_pokemon()
    return render_template("index.html", datos=data)

