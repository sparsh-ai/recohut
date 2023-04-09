import bentoml
from bentoml.io import JSON
import pandas as pd

# This list was previous extracted from the data set
POSSIBLE_MODELS = {' Ka+', ' Grand C-MAX', ' Kuga', 'Other', ' C-MAX', ' Focus', 
                   ' Tourneo Custom', ' Escort', ' EcoSport', ' Edge', ' S-MAX',
                   ' Grand Tourneo Connect', ' Fiesta', ' Fusion', ' Mustang', 
                   ' B-MAX', ' KA', ' Streetka', ' Ranger', 'Focus', ' Tourneo Connect', 
                   ' Galaxy', ' Mondeo', ' Puma'}

# Loading the runner
ford_price_runner = bentoml.sklearn.get(
    "ford_price_predictor:latest",
).to_runner()

# Create the service
service = bentoml.Service(
    "ford_price_predictor",
    runners=[ford_price_runner]
)

# Define input and output types
@service.api(input=JSON(), output=JSON())
def predict(input):

    # If the model is not in the possible models, replace it with 'Other'
    if input['model'] not in POSSIBLE_MODELS:
        input['model'] = 'Other'

    # Transform the input data to a dataframe
    input_df = pd.DataFrame([input])
    result = ford_price_runner.run(input_df)

    return result[0]
