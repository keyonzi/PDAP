from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)
dbs = SQLAlchemy(app)

class Factory(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  sprocket_production_actual = db.Column(db.Integer, nullable=False)
  sprocket_production_goal = db.Column(db.Integer, nullable=False)
  time = dbs.Column(dbs.DateTime, nullable=False)

  def __init__(self, sprocket_production_actual, sprocket_production_goal, time):
    self.sprocket_production_actual = sprocket_production_actual
    self.sprocket_production_goal = sprocket_production_goal
    self.time = time

db.create_all()

class Sprocket(dbs.Model):
  id = dbs.Column(dbs.Integer, primary_key=True)
  teeth = dbs.Column(dbs.Integer, nullable=False)
  pitch_diameter = dbs.Column(dbs.Integer, nullable=False)
  outside_diameter = dbs.Column(dbs.Integer, nullable=False)
  pitch = dbs.Column(dbs.Integer, nullable=False)
  time = dbs.Column(dbs.DateTime, nullable=False)


  def __init__(self, teeth, pitch_diameter, outside_diameter, pitch, time):
    self.teeth = teeth
    self.pitch_diameter = pitch_diameter
    self.outside_diameter = outside_diameter
    self.pitch = pitch
    self.time = time

dbs.create_all()

@app.route('/')
def home():
    return "PDAP RULES!"

# return factory data by id
@app.route('/factories/<id>', methods=['GET'])
def get_factory(id):
  factory = Factory.query.get(id)
  del factory.__dict__['_sa_instance_state']
  return jsonify(factory.__dict__)

# return all factory data
@app.route('/factories', methods=['GET'])
def get_factories():
  factories = []
  for factory in db.session.query(Factory).all():
    del factory.__dict__['_sa_instance_state']
    factories.append(factory.__dict__)
  return jsonify(factories)

# create factory
@app.route('/factories', methods=['POST'])
def create_factory():
  body = request.get_json()
  db.session.add(Factory(body['sprocket_production_actual'], body['sprocket_production_goal'], datetime.now()))
  db.session.commit()
  return "factory created"

# update factory by id
@app.route('/factories/<id>', methods=['PUT'])
def update_factory(id):
  body = request.get_json()
  db.session.query(Factory).filter_by(id=id).update(
    dict(sprocket_production_actual=body['sprocket_production_actual'], sprocket_production_goal=body['sprocket_production_goal'], time=datetime.now()))
  db.session.commit()
  return "factory updated"

# delete factory by id
@app.route('/factories/<id>', methods=['DELETE'])
def delete_factory(id):
  db.session.query(Factory).filter_by(id=id).delete()
  db.session.commit()
  return "factory deleted"


# Get Sprocket by id
@app.route('/sprockets/<id>', methods=['GET'])
def get_sprocket(id):
  sprocket = Sprocket.query.get(id)
  del sprocket.__dict__['_sa_instance_state']
  return jsonify(sprocket.__dict__)

# get all Sprockets
@app.route('/sprockets', methods=['GET'])
def get_sprockets():
  sprockets = []
  for sprocket in db.session.query(Sprocket).all():
    del sprocket.__dict__['_sa_instance_state']
    sprockets.append(sprocket.__dict__)
  return jsonify(sprockets)

# update sprocket by id
@app.route('/sprockets/<id>', methods=['PUT'])
def update_sprocket(id):
  body = request.get_json()
  db.session.query(Sprocket).filter_by(id=id).update(
    dict(teeth=body['teeth'], pitch_diameter=body['pitch_diameter'], outside_diameter=body['outside_diameter'], pitch=body['pitch'], time=datetime.now()))
  db.session.commit()
  return "factory updated"

# create sprocket
@app.route('/sprockets', methods=['POST'])
def create_sprocket():
  body = request.get_json()
  dbs.session.add(Sprocket(body['teeth'], body['pitch_diameter'], body['outside_diameter'], body['pitch'], datetime.now()))
  dbs.session.commit()
  return "sprocket created"

# delete sprocket by id
@app.route('/sprockets/<id>', methods=['DELETE'])
def delete_sprocket(id):
  db.session.query(Sprocket).filter_by(id=id).delete()
  db.session.commit()
  return "sprocket deleted"