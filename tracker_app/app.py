import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, and_, desc, func


from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/updated_depletions4.sqlite3"
db = SQLAlchemy(app)



# Create database model
class DepletionData(db.Model):
    __tablename__ = 'dep'

    storenumber = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    area = db.Column(db.String)
    region = db.Column(db.String)
    distributor = db.Column(db.String)
    casesshipped = db.Column(db.Float)
    casesneeded = db.Column(db.Float)
    caseopportunity = db.Column(db.Float)
    status = db.Column(db.String)

    def __repr__(self):
        return '<DepletionData %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():

    db.create_all()


@app.route("/")
def home():
    # Render Home Page.
    return render_template("index.html")


@app.route("/data")
def data():
    # METHOD NUMBER 1
    # results = db.session.query(DepletionData.storenumber, DepletionData.address, DepletionData.city, DepletionData.state, DepletionData.latitude, DepletionData.longitude, DepletionData.area, DepletionData.region, DepletionData.distributor, DepletionData.casesshipped, DepletionData.casesneeded, DepletionData.caseopportunity, DepletionData.status).all()
    # df = pd.DataFrame(results, columns=["storenumber", "address", "city", "state", "latitude", "longitude", "area", "region", "distributor", "casesshipped", "casesneeded", "caseopportunity", "status"])
    # return jsonify(df.to_dict(orient="records"))   

    # METHOD NUMBER 2
    # results = db.session.query(DepletionData.storenumber, DepletionData.address, DepletionData.city, DepletionData.state, DepletionData.latitude, DepletionData.longitude, DepletionData.area, DepletionData.region, DepletionData.distributor, DepletionData.casesshipped, DepletionData.casesneeded, DepletionData.caseopportunity, DepletionData.status).all()
    # df = pd.DataFrame(results, columns=["storenumber", "address", "city", "state", "latitude", "longitude", "area", "region", "distributor", "casesshipped", "casesneeded", "caseopportunity", "status"])
    # df_dict = df.to_dict(orient="records")
    # total_store_list = {"all_stores": df_dict}
    # return jsonify(total_store_list)


    # METHOD NUMBER 3
    # Query for data
    results = db.session.query(DepletionData.storenumber, DepletionData.address, DepletionData.city, DepletionData.state, DepletionData.latitude, DepletionData.longitude, DepletionData.area, DepletionData.region, DepletionData.distributor, DepletionData.casesshipped, DepletionData.casesneeded, DepletionData.caseopportunity, DepletionData.status).all()

    # Create lists from the query results
    storenumber = [result[0] for result in results]
    address = [result[1] for result in results]
    city = [result[2] for result in results]
    state = [result[3] for result in results]
    latitude = [float(result[4]) for result in results]
    longitude = [float(result[5]) for result in results]
    area = [result[6] for result in results]
    region = [result[7] for result in results]    
    distributor = [result[8] for result in results]   
    casesshipped = [float(result[9]) for result in results]
    casesneeded = [float(result[10]) for result in results]
    caseopportunity = [float(result[11]) for result in results]
    status = [result[12] for result in results]      

    # Generate the plot trace
    trace = {
        "storenumber": storenumber,
        "address": address,
        "city": city,
        "state": state,
        "latitude": latitude,
        "longitude": longitude,
        "area": area,
        "region": region,
        "distributor": distributor,
        "casesshipped": casesshipped,
        "casesneeded": casesneeded,
        "caseopportunity": caseopportunity,
        "status": status
    }

    total_store_list = {"all_stores": trace}

    return jsonify(total_store_list)





@app.route("/national_view")
def area_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.caseopportunity).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    area = [result[0] for result in results]
    caseopportunity = [float(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": area,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)



@app.route("/national_region_view")
def nat_by_region_data():

    # Query for data
    results = db.session.query(DepletionData.region, DepletionData.caseopportunity).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    region = [result[0] for result in results]
    caseopportunity = [float(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": region,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)    



@app.route("/national_state_view")
def nat_by_state_data():

    # Query for data
    results = db.session.query(DepletionData.state, DepletionData.caseopportunity).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[0] for result in results]
    caseopportunity = [float(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)   



@app.route("/national_dist_view")
def nat_by_dist_data():

    # Query for data
    results = db.session.query(DepletionData.distributor, DepletionData.caseopportunity).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    distributor = [result[0] for result in results]
    caseopportunity = [float(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": distributor,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)




@app.route("/west_area")
def west_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.caseopportunity).\
        filter(DepletionData.region.in_(["SOUTHERN", "WESTERN"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    region = [result[1] for result in results]
    caseopportunity = [float(result[2]) for result in results]

    # Generate the plot trace
    trace = {
        "x": region,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/south_region")
def south_region_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.state, DepletionData.caseopportunity).\
        filter(DepletionData.state.in_(["AZ", "TX", "LA"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[2] for result in results]
    caseopportunity = [float(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/west_region")
def west_region_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.state, DepletionData.caseopportunity).\
        filter(DepletionData.state.in_(["CA", "NV", "OR", "WA"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[2] for result in results]
    caseopportunity = [float(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)









@app.route("/north_area")
def north_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.caseopportunity).\
        filter(DepletionData.region.in_(["CENTRAL", "MIDWEST", "NORTHEAST"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    region = [result[1] for result in results]
    caseopportunity = [float(result[2]) for result in results]

    # Generate the plot trace
    trace = {
        "x": region,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/central_region")
def central_region_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.state, DepletionData.caseopportunity).\
        filter(DepletionData.state.in_(["MI", "OH"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[2] for result in results]
    caseopportunity = [float(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/midwest_region")
def midwest_region_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.state, DepletionData.caseopportunity).\
        filter(DepletionData.state.in_(["IL", "IN", "MO", "WI"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[2] for result in results]
    caseopportunity = [float(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/n_east_region")
def northeast_region_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.state, DepletionData.caseopportunity).\
        filter(DepletionData.state.in_(["NH"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[2] for result in results]
    caseopportunity = [float(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)









@app.route("/east_area")
def east_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.caseopportunity).\
        filter(DepletionData.region.in_(["ATLANTIC", "SOUTHEAST"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    region = [result[1] for result in results]
    caseopportunity = [float(result[2]) for result in results]

    # Generate the plot trace
    trace = {
        "x": region,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/atlantic_region")
def atlantic_region_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.state, DepletionData.caseopportunity).\
        filter(DepletionData.state.in_(["DC", "NC", "SC", "VA"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[2] for result in results]
    caseopportunity = [float(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/s_east_region")
def southeast_region_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.state, DepletionData.caseopportunity).\
        filter(DepletionData.state.in_(["AL", "FL", "GA"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[2] for result in results]
    caseopportunity = [float(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)









@app.route("/mega_area")
def mega_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.caseopportunity).\
        filter(DepletionData.region.in_(["MEGA EAST", "MEGA WEST"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    region = [result[1] for result in results]
    caseopportunity = [float(result[2]) for result in results]

    # Generate the plot trace
    trace = {
        "x": region,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/mega_east")
def mega_east_region_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.state, DepletionData.caseopportunity).\
        filter(DepletionData.state.in_(["AR", "KY", "ME", "OK", "VT", "WV"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[2] for result in results]
    caseopportunity = [float(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/mega_west")
def mega_west_region_data():

    # Query for data
    results = db.session.query(DepletionData.area, DepletionData.region, DepletionData.state, DepletionData.caseopportunity).\
        filter(DepletionData.state.in_(["HI", "IA", "ID", "MT", "NE", "NM", "SD"])).\
        order_by(desc(DepletionData.caseopportunity)).\
        limit(10000).all()

    # Create lists from the query results
    state = [result[2] for result in results]
    caseopportunity = [float(result[3]) for result in results]

    # Generate the plot trace
    trace = {
        "x": state,
        "y": caseopportunity,
        "type": "bar"
    }
    return jsonify(trace)


if __name__ == '__main__':
    # render_template("index.html")
    app.run(debug=True)