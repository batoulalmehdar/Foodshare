from flask import Flask, render_template, request
import requests

app = Flask("PickUpForm")

# Display the form
@app.route("/")
    return render_template("Application.html", name=name)

# Handle form submission
@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    # Print out all the form data
    print(form_data)

    #Send the email
    requests.post(
        "https://api.mailgun.net/v3/sandboxd21d655ac64e48d08c7c0e245e620ae0.mailgun.org/messages",
        auth=("api", "7df13535b905f6f58d8b1f9b3aae0874-acb0b40c-c59e0ed6"),
        data={"from": "Excited User <mailgun@sandboxd21d655ac64e48d08c7c0e245e620ae0.mailgun.org>",
        "to": form_data["recipient"],
                  "subject": "Hello",
                  "text": form_data["body"]})

    return "All OK"

app.run(debug=True)
