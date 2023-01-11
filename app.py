from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI
origin = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True
    allow_methods=['*']
    allow_headers = ["*"]
)

class model_input(BaseModel):
    Rainfall: float
    Max-Temprature : float
    Min-temperature : float
    Relative humidity 1(0800hrs): float
    Relative humidity 2(1400hrs): float
    mosquito population: int
    Cases: int


malaria_model = pickle.load(open('best_model(1).pkl', 'rb'))

@app.post('/malaria_predictor')
def malaria_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary=json.loads(input_data)

    rain = input_dictionary['Rainfall']
    maxt = input_dictionary['Max-Temperature']
    mint = input_dictionary['Min-temperature']
    rel1 = input_dictionary['Relative humidity 1(0800hrs)']
    rel2 = input_dictionary['Relative humidity 2(1400hr)']
    mosqp = input_dictionary['Mosquito population']
    cas = input_dictionary['Cases']

input_list = [rain,maxt,mint,rel1,rel2,mosqp,cas]


if prediction[0]==1:
    return 'moderate threat'
else:
    return 'outbreak'
