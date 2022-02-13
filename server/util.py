import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(Location, sqft, resale, bhk):
    try:
        loc_index = __data_columns.index(Location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = resale
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading Saved Artifacts... Start")
    global __data_columns
    global __locations
    global __model

    with open("/Users/mohamedinamulhassan/Desktop/Housing-Price-Prediction/server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("/Users/mohamedinamulhassan/Desktop/Housing-Price-Prediction/server/artifacts/chennai_housing.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading Artifacts Done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Medavakkam', 1000, 0, 3))
    print(get_estimated_price('Gopalapuram', 1000, 0, 3))
    print(get_estimated_price('Vadapalani', 1000, 0, 3))
    print(get_estimated_price('ABCG nagar', 1000, 0, 3))
