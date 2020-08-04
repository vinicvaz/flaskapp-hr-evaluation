from flask import render_template, request
from app import model
from app.Forms import MyForm
import pandas as pd


def home():

    form = MyForm()

    if form.validate_on_submit():
        data = {
            'projects':[form.data['projects']],
            "avg_hours": [form.data['avg_hours']],
            "time": [form.data['time_spend']],
            'emp_identity': [form.data['emp_identity']],
            "emp_role":[form.data['emp_role']],
            'percent_remote': [form.data['percent_remote']]
        }
        features = pd.DataFrame(data)

        p = model.predict(features)
        evaluation_result = p[0]
    else:
        evaluation_result = ''

    return render_template('home/home.html', form=form, evaluation_result=evaluation_result)