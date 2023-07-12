from threading import Thread
from flask import Flask, send_file

app = Flask(
  __name__,
  template_folder = 'pages',
  static_folder = 'static'
)

def run():
    app.run(host='0.0.0.0', port=8080)

def runwebsite():
    t = Thread(target=run)
    t.start()

@app.route('/')
def home():
    return send_file('pages/index.html')

@app.errorhandler(404)
def page_not_found(e):
    return send_file('pages/error.html')

@app.route('/bronze')
def bronze():
    return send_file('bronze.html')

@app.route('/bronze/expedition')
def bronze_exped():
    return send_file('bexpedition.html')

@app.route('/bronze/skill')
def bronze_skill():
    return send_file('BSkill.html')

@app.route('/bronze/volunteering')
def bronze_volunteer():
    return send_file('bvolunteering.html')

@app.route('/bronze/physical')
def bronze_physical():
    return send_file('bphysical.html')

@app.route('/silver')
def silver():
    return send_file('silver.html')

@app.route('/silver/expedition')
def silver_exped():
    return send_file('sexpedition.html')

@app.route('/silver/skill')
def silver_skill():
    return send_file('sskill.html')

@app.route('/silver/volunteering')
def silver_volunteer():
    return send_file('svolunteering.html')

@app.route('/silver/physical')
def silver_physical():
    return send_file('sphysical.html')

@app.route('/gold')
def gold():
  return send_file('gold.html')