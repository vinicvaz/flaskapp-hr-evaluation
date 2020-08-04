from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange


class MyForm(FlaskForm):
    projects = IntegerField('Number of Projects', description='The number of projects the employee works on throughout the year.', validators=[InputRequired()])
    avg_hours = IntegerField('Average Montly Hours', description='The average number of hours the employee works.', validators=[InputRequired()])
    time_spend = IntegerField('Time spend in company', description='Years of service.', validators=[InputRequired()])
    emp_identity = SelectField('Employee Identity', description='How the employee identifies themselves with the company.', choices=[1,2,3,4,5], validators=[InputRequired()])
    emp_role = SelectField('Employee Role', description='How the employee identifies themselves with the importance of their role in the company.', choices=[1,2,3,4,5], validators=[InputRequired()])
    percent_remote = FloatField('Percent Remote', description='The percentage of the employees work that is done remotely.', validators=[InputRequired(), NumberRange(0, 1, message='Must be between 0 and 1')])

    submit = SubmitField('Submit')