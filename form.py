from flask_wtf import FlaskForm
from wtforms import  FloatField, SelectField
from wtforms.validators import DataRequired





class PredictiveForm(FlaskForm): 

    Air_temp = FloatField('Air temperature', validators=[DataRequired()]) 
    process_temp = FloatField('process temperature', validators=[DataRequired()])
    Rotational_speed = FloatField('Rotational speed', validators=[DataRequired()])
    Torque = FloatField('Torque', validators=[DataRequired()])
    Tool_wear = FloatField('Tool wear', validators=[DataRequired()])
