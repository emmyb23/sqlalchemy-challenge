import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, desc

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/precipitation")
def date():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precips"""
    # Query all precips
    results = session.query(Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_precips = list(np.ravel(results))

    return jsonify(all_precips)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Query all stations
    results = session.query(Measurement.station).all()

    session.close()

    all_stations = list(np.ravel(results))

    return jasonfiy(all_stations)



@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    results = session.query(Measurement.tobs).all
    session.close()
    all_tobs = list(np.ravel(results))
    return jasonify(all_tobs)




if __name__ == '__main__':
    app.run(debug=True)
