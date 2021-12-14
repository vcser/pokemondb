from flask import Flask, json, render_template, jsonify, request, url_for
from flask.helpers import make_response
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
        with connect_db() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) as cursor:
                cursor.execute('''
                select ip.num_pokedex, p.mote, p.sexop, p.nivel, p.factor_random, null as entrenador
                from pokedex.pokemon as p, pokedex.info_pokemon as ip, pokedex.representa as r
                where r.id_pokemon=p.id and r.num_info_pokemon=ip.num_pokedex and not exists
                (select 1
                from pokedex.mochila as m, pokedex.contiene as c
                where c.id_pokemon=p.id and c.id_mochila=m.id
                )
                union
                select ip.num_pokedex, p.mote, p.sexop, p.nivel, p.factor_random, e.nombre as entrenador
                from pokedex.entrenador as e, pokedex.tiene as t, pokedex.mochila as m, pokedex.contiene as c, pokedex.pokemon as p, pokedex.info_pokemon as ip, pokedex.representa as r
                where t.id_entrenador=e.id and t.id_mochila=m.id and c.id_mochila=m.id and c.id_pokemon=p.id and r.id_pokemon=p.id and r.num_info_pokemon=ip.num_pokedex
                ''')
                result = cursor.fetchall()
                result = [row._asdict() for row in result]
                return result
    except:
        return []


def get_info_pokemon():
    try:
        with connect_db() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) as cursor:
                cursor.execute("select * from pokedex.info_pokemon")
                result = cursor.fetchall()
                result = [row._asdict() for row in result]
                return result
    except:
        return []


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/_info_pokemon")
def info_pokemon():
    data = get_info_pokemon()
    response = make_response({"data": data})
    if (not data):
        response.status_code = 404
    return response


@app.route("/_pokemon")
def pokemon():
    data = get_pokemon()
    response = make_response({"data": data})
    if (not data):
        response.status_code = 404
    return response


@app.route("/acerca_de")
def acerca_de():
    return render_template("acerca_de.html")
