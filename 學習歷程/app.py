from flask import Flask, render_template
import requests

pm25_url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=5a3df95f-b379-4b15-8fcb-d23bc99ff1a9"

res = requests.get(pm25_url)

data = res.json()

record_list = data["records"]



app = Flask(__name__)


@app.route("/")
def home_page():

    return render_template("index.html", record_list=record_list)



if __name__ == "__main__":

    app.run(debug=True, port=5001)