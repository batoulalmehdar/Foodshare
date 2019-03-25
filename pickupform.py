from flask import Flask, render_template, flash, request
import requests
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask("PickUpForm")

# Display the form
@app.route("/")
def hello(name="World!!!"):
    return render_template("pickup_form.html", name=name)

@app.route("/my-handling-form-page", methods=["POST"])
def sign_up():
    form_data = request.form
    # Print out all the form data
    print(form_data)

    #Send the email
    requests.post(
        "https://api.mailgun.net/v3/sandboxd21d655ac64e48d08c7c0e245e620ae0.mailgun.org/messages",
        auth=("api", "7df13535b905f6f58d8b1f9b3aae0874-acb0b40c-c59e0ed6"),
        data={"from": "Excited User <mailgun@sandboxd21d655ac64e48d08c7c0e245e620ae0.mailgun.org>",
        "to": form_data["user_mail"],
                  "subject": "Pick Up Meals",
                  "html": form_data["user_name", "user_mail", "user_number", "postcode", "address1", "address2", "address3", "town",
                  "user_date", "user_meals", "user_comments"]})

    return "Thank you and we will be picking up the meal/s shortly."
app.run(debug=True)
