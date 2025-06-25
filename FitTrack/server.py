from flask import Flask, request
from database import execute_query
from database import execute_select_query

import paho.mqtt.client as mqtt

server = Flask(__name__)

@server.route("/health", methods=['POST'])
def insert_db():
    name = request.get_json('name')
    age = request.get_json('age')
    city=request.get_json('city')
    steps=request.get_json('steps')
    pulse=request.get_json('pulse')
    oxygen=request.get_json('oxygen')
    temp=request.get_json('temp')

    query = f"insert into health (name, age, city, steps, pulse, oxygen, temp) values('{name}', {age}, '{city}', {steps}, {pulse}, {oxygen}, {temp});"

    execute_query(query)

    method =request.method
    
    publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    publisher.connect("localhost")
    publisher.publish("health/status", "Post operated successfully")
    publisher.disconnect()

    return f"{name}query insarted successfully"


@server.route("/health", methods=['GET'])
def disp_db():
    

    query = f"select * from health;"

    health=execute_select_query(query)

    method =request.method
    publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    publisher.connect("localhost")
    publisher.publish("health/status", "GET operated successfully")
    publisher.disconnect()

    return health


@server.route("/health", methods=['PUT'])
def update_db():
    name=request.form.get('name')
    city=request.form.get('city')


    query = f"update health SET city = '{city}' where name = '{name}';"
    method =request.method

    execute_query(query)

    publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    publisher.connect("localhost")
    publisher.publish("health/status", "Put operated successfully")
    publisher.disconnect()

    return f"query updated successfully for '{name}"


@server.route("/health_info", methods=['GET'])
def info_db():
    name = request.get_json().get('name')

    query = f"select * from health where name = '{name}';"

    health=execute_select_query(query)    
    method =request.method
    
    publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    publisher.connect("localhost")
    publisher.publish("health/status", "Get_Info operated successfully")
    publisher.disconnect()

    return health

@server.route("/health_info", methods=['POST'])
def steps_db():
    name ="ssk"

    query = f"select * from health order by steps DESC limit 1;"

    health=execute_select_query(query)
    method =request.method

    publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    publisher.connect("localhost")
    publisher.publish("health/status", "Post_steps operated successfully")
    publisher.disconnect()

    return health


if __name__ == "__main__":
    server.run(host='0.0.0.0',port=4000,debug=True)
