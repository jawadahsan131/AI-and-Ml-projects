from flask import Flask, render_template,jsonify
import requests

app = Flask(__name__)

NASA_API = "SRBcd2mqP3ooPJwI1bbMyB08zmBLVQ29OiShXb7t"
EPIC_URL = "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"

@app.route("/",methods= ["GET"])
def index():
    par = {"api_key":NASA_API}
    response = requests.get(EPIC_URL, params=par)
    if response.status_code == 200:
        epic_data = response.json()[:4]
        print(epic_data)
        return render_template("index.html", EP = epic_data)

    else:
        return render_template("index.html", EP=None, error="Failed to fetch data from NASA API.")
    
if __name__ == "__main__":
    app.run(debug=True)



