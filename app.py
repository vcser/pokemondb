from flask import Flask, json, render_template, jsonify, request, url_for
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
    try:
        conn = connect_db()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        cursor.execute("select * from pokedex.pokemon")
        '''
        select ip.num_pokedex, p.mote, p.sexop, p.nivel, p.factor_random
        from info_pokemon as ip, pokemon as p, representa as r
        where r.id_pokemon=p.id and r.num_info_pokemon=ip.num_pokedex
        '''
        result = cursor.fetchall()
        result = [row._asdict() for row in result]

        return result
    except:
        return []
    finally:
        cursor.close()
        conn.close()


def get_info_pokemon():
    try:
        conn = connect_db()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        cursor.execute("select * from pokedex.info_pokemon")
        result = cursor.fetchall()
        result = [row._asdict() for row in result]

        return result
    except:
        return []
    finally:
        cursor.close()
        conn.close()


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/_info_pokemon")
def info_pokemon():
    data = get_info_pokemon()
    return {
        "data": data
    }


@app.route("/_pokemon")
def pokemon():
    data = get_pokemon()
    return {
        "data": data
    }


@app.route("/acerca_de")
def acerca_de():
    return render_template("acerca_de.html")
