from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class EquipoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    modelo_id = IntegerField('Modelo ID', validators=[DataRequired()])
    categoria_id = IntegerField('Categoría ID', validators=[DataRequired()])
    costo = FloatField('Costo', validators=[DataRequired()])
    submit = SubmitField('Guardar')
