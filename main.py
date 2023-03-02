from flask import Flask,render_template
from picker import pick, pull_info

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
    place = pick()
    info = pull_info(place)
    return render_template('index.html', place=place, info=info, image=info[2])

app.run(host='0.0.0.0', port=81)
