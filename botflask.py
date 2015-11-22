from flask import Flask, request, redirect
import twilio.twiml
 
yoo = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
    "+15102986731": "Curious George",
    "+14158675309": "Boots",
    "+14158675311": "Virgil",
}

 
@yoo.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    return "hi"
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
        print "hi"
    else:
        print "yo"
        message = "Monkey, thanks for the message!"
 
    resp = twilio.twiml.Response()
    resp.message(message)

 
    return str(resp) + "hi"
 
if __name__ == "__main__":

    yoo.run(debug=True)