from flask import Flask 
app = Flask()

@app.route("/", methods = ["GET"])
def health():
    print("The audioProcessing service is up and running!")


