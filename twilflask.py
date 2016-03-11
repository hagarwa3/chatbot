from flask import Flask, request, redirect, Response
import twilio.twiml
import json
import random

app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {}
 



@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    print "hii"
    message = ""

    string = request.query_string
    string = string.split("%20")
    print str(string)
    string = ' '.join(string)
    print string
    print "lalalala"
    s = string.encode('ascii',errors='ignore')
    #from_number = request.values.get('From', None)
    #if from_number in callers and s=="STOP_1":
        #del d[from_number]
    #    message = "You have switched. Send another message to start chattimg with jaden. send, STOP_2 to switch to donald trump."
    #    callers[from_number]="jaden"
    #elif from_number in callers and s=="STOP_2":
    #    #del d[from_number]
    #    message = "You have switched. Send another message to start chattimg with trump. send STOP_1 to switch to jaden smith."
    #    callers[from_number]="trump"
    #elif from_number not in callers:
    #    message = "You are at a default of donald trump messages. Send another text to start chatting with donald trump. send STOP_1 to switch to jaden smith."
    #    callers[from_number]="trump"
    if 0:
        lalalala = 1
    else:

    #from_number = request.values.get('From', None)
        
        person = "trump" #callers[from_number]
        outfile = open((person+'combined.json'), 'r')
        start = open((person+'startpoints.txt'),'r')
        start = random.choice(start.readlines())
        data = json.load(outfile)
        #start = random.choice(data.keys())
        #print start
        length = random.randint(3,20)
        print length
        listsofar = start.split()
        while len(listsofar)<=length:
            prev = listsofar[-2]+" "+ listsofar[-1]
            #print prev
            get = data[prev]
            string = random.choice(get)
            listsofar.append(string)
            if len(listsofar)==length and ("." != listsofar[-1][-1] and length<40):
                length+=1
        listsofar.pop()
        listsofar = ' '.join(listsofar)
        print "here"
        message = listsofar
    print message
        #print listsofar
    #"""Respond and greet the caller by name."""
     
        # from_number = request.values.get('From', None)
        # if from_number in callers:
        #     message = callers[from_number] + ", thanks for the message!"
        # else:
        #     message = "Monkey, thanks for the message!"
        #message = listsofar 
    #resp = twilio.twiml.Response()
    #resp.message(message)
    message = message.encode('ascii',errors='ignore')
    #message = {"message": message}
    #print message
    #message = json.loads(message)
    print str(message)
    resp = Response(response=str(message),
    status=200)
    return (resp)
 
if __name__ == "__main__":
    app.run(debug=True)
