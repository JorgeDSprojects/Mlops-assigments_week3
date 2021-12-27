from flask import Flask, jsonify, request
from app.BMI import BodyMassIndex
 
# instantiate flask object
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_input():
   """
   A function to get request using flask, evluate and return result.
   """
   packet = request.get_json(force=True)
   height = packet['height']
   weight = packet['weight']

   BMI_Result = BodyMassIndex(height, weight)
 
   return jsonify(packet, BMI_Result)
