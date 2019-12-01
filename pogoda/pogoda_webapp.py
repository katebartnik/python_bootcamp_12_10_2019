import io
import csv
import datetime

from flask import Flask, render_template, make_response
from flask_sqlalchemy import SQLAlchemy

from pogoda import get_location_id, get_location_weather, prepare_weather_report

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///C:\Users\kurs\workspace\python_bootcamp\zastosowania\pogoda\test.db"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "My Weather Page"


@app.route("/<location_name>")
def weather(location_name):
    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_weather = Weather(location_name=location_name, temperature=weather.the_temp, date=date)
    db.session.add(db_weather)
    db.session.commit()
    lista = [x ** 2 for x in range(10)]
    return render_template("index.html", weather=weather, lista=lista)


@app.route("/history")
def history():
    weathers = Weather.query.all()
    return render_template("history.html", weathers=weathers)


@app.route("/history/download")
def download_history():
    weathers = Weather.query.all()
    data = [["ID", "Miejscowosc", "temperatura", "data"]]
    for w in weathers:
        row = [w.id, w.location_name, w.temperature, w.date]
        data.append(row)
    f = io.StringIO()
    writer = csv.writer(f, delimiter=";")
    writer.writerows(data)
    output = make_response(f.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=result.csv"
    output.headers["Content-type"] = "text/csv"
    return output


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.Text, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Text, nullable=False)


if __name__ == "__main__":
    app.run()
