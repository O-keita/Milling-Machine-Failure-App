from flask import Flask, render_template
import joblib
import pandas as pd
import xgboost as xgb
import numpy as np

from form import PredictiveForm




app = Flask(__name__)
app.config['SECRET_KEY'] = '15dabdhdh7dhwd7'


model = joblib.load('xgb_model.pkl')


feature_names = [
    "Air temperature K", "Process temperature K", "Rotational speed rpm",
    "Torque Nm", "Tool wear min", "power", "temperature_diff", "Type_L", "Type_M"
]


def predict_with_xgb_model(features):
    """
    Predict using the trained XGBoost model.

    Parameters:
    features (list): A list of features to make the prediction.
    
    Returns:
    tuple: A tuple containing the predicted probability and predicted class label.
    """

    input_data = pd.DataFrame([features], columns=feature_names)

    dmatrix = xgb.DMatrix(input_data)

    probability = model.predict(dmatrix)  # Get the predicted probability
    predicted_class = 1 if probability[0] >= 0.5 else 0  # Class label based on threshold

    return probability[0], predicted_class

dummy_input_features = [
    303,  # Air temperature K
    
    311,  # Process temperature K
    
    161,  # Rotational speed rpm
    
    33.2,   # Torque Nm
    
    155,  # Tool wear min
    
    54495,  # Power (in the appropriate units)
    
    7.7,  # Temperature difference
    
    0,    # Type_L True
    
    0     # Type_M 1 false
]






@app.route('/', methods=['GET', 'POST'])
def index():

    form = PredictiveForm()
    
    data = dummy_input_features

    if form.validate_on_submit():


        data = [
            form.Air_temp.data, 
            form.process_temp.data,
            form.Rotational_speed.data,
            form.Torque.data,
            form.Tool_wear.data,
            form.Torque.data * form.Rotational_speed.data,
            form.process_temp.data - form.Air_temp.data,
            0,
            0

    

  
        ]


  

    temperature_diff,  power  = round(data[6]),  round(data[5])

    predicted_probability, predicted_class = predict_with_xgb_model(data)

    predicted_probability = round(predicted_probability * 100)


    if predicted_probability < 10:
        status = "Excellent"

    elif predicted_probability < 30:
        status = "Good"

    elif predicted_probability < 50:
    
        status = "Average"

    elif predicted_probability < 65:
        status = "Poor"

    
    elif predicted_probability < 75:
        status = " Very Poor"

    else:
        status = "Bad"  


    return render_template('index.html',
                            predicted_probability=predicted_probability,
                              predicted_class=predicted_class,
                                status=status,
                                  form=form,
                                  power=power,
                                  temperature_diff=temperature_diff
                                  )

if __name__ == "__main__":
    app.run(debug=True)