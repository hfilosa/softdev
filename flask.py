from flask import Flask

app = Flask(__name__)

#Flask generates html webpages when given a string, so all routes must ultimately return a string

#This says if the person is connecting to the home "route"(page) run the home function
#The name of the home function doesn't matter it will run the function if any of the routes above it are the same
@app.route("*/home")
def home():
    return "<h1>Home Page</h1>"

#In this example, whenever a user connects to the /blerg extension, the bleh function is run
@app.route("/blerg")
def bleh():
    return "Lark"

# "/" means that whenever a user doesn't put an extension, this route will be actvated
#Multiple routes can activate the same function
@app.route("/")
@app.route("/Gah!")
def heh():
    return "I am a webpage!"

#This says if this function is being called to run as the main program then do this
if __name__ == "__main__":
    app.debug = true
    #setting debug to true allows better error messages
    #This says who can connect. 0.0.0.0 allows anyone to connect, port is how the connection is made
    app.run(hosts='0.0.0.0', port=8000)    
