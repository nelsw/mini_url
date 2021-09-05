import os
from hashids import Hashids
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath("db.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'cyphotilapiafrontosa'
db = SQLAlchemy(app)
hashids = Hashids(min_length=6, salt=app.config['SECRET_KEY'])


class Url(db.Model):
    __tablename__ = "url"

    id = db.Column(db.Integer, primary_key=True)
    decoded = db.Column(db.String(512), nullable=False)
    encoded = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return '<Url %r>' % self.value


db.drop_all()
db.create_all()
db.session.commit()


@app.route('/', methods=('PUT',))
def encode():

    d = request.form['encode']
    if len(d) < 1:
        abort(400, "No URL provided to encode")

    url = Url.query.filter_by(decoded=d).first()
    if url is not None:
        return url.encoded

    i = 0
    url = Url.query.order_by(Url.id.desc()).first()
    if url is not None:
        i = url.id + 1

    e = hashids.encode(i)
    url = Url(decoded=d, encoded=e)
    db.session.add(url)
    db.session.commit()

    return 'http://localhost:5050/' + url.encoded


@app.route('/<string:value>', methods=('GET',))
def decode(value):

    if len(value) < 1:
        abort(400, "No URL provided to decode")

    url = Url.query.filter_by(encoded=value).first()
    if url is None:
        abort(404, "No URL found for given decode value")

    return url.decoded


if __name__ == '__main__':
    app.run()
