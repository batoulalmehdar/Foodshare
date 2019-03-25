from flask import Flask, render_template, flash, request
import requests
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask("PickUpForm")

# Display the form
@app.route("/")
def hello(name="World!!!"):
    return render_template("pickup_form.html", name=name)

@app.route("/my-handling-form-page", methods=["POST"])
def send_simple_message():
    name = request.forms.get('user_name')
    email =  request.forms.get('user_mail')
    number =  request.forms.get('user_number')
    postcode =  request.forms.get('postcode')
    address1 =  request.forms.get('address1')
    address2 =  request.forms.get('address2')
    address3 =  request.forms.get('address3')
    city =  request.forms.get('town')
    date =  request.forms.get('user_date')
    meals =  request.forms.get('user_meals')
    comment =  request.forms.get('user_comments')
    text = "Name: "+ name + "Email: " + email + "Mobile No.: " + number + "Postcode: " + postcode + "Address: " +
    address1 + ", " + address2 + ", " + address3 + ", " + city + "Date: " + date + "No. of Meals: " +
    meals + "Comments: " + comment
    print(text)

    #Send the email
    requests.post(
        "https://api.mailgun.net/v3/sandboxd21d655ac64e48d08c7c0e245e620ae0.mailgun.org/messages",
        auth=("api", "7df13535b905f6f58d8b1f9b3aae0874-acb0b40c-c59e0ed6"),
        data={"from": "Excited User <mailgun@sandboxd21d655ac64e48d08c7c0e245e620ae0.mailgun.org>",
        "to": form_data["user_mail"],
                  "subject": "Pick Up Meals",
                  "text": form_data["text"]})

    return "Thank you and we will be picking up the meal/s shortly."
app.run(debug=True)
