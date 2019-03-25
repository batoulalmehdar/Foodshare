from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(PickUpForm)
app.config.from_object(PickUpForm)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

print form.errors
if request.method == 'POST':
<<<<<<< HEAD
    name=request.form['name']
=======
    name = request.form['name']
>>>>>>> a04cb420d060bf73e554e3df978b06dcb1593f8a
print name

if form.validate():
# Save the comment here.
flash('Hello ' + name)
else:
flash('All the form fields are required. ')

return render_template('pickup_form.html', form=form)

if PickUpForm == "PickUpForm":
app.run()