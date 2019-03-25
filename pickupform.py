from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask("PickUpForm")

# Display the form
@app.route("/")
def hello(name="World!!!"):
    return render_template("pickup_form.html", name=name)

app.run(debug=True)
