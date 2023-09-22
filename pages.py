from threading import Thread
from flask import Flask, send_file

app = Flask(__name__, template_folder='pages', static_folder='static')


def run():
  app.run(host='0.0.0.0', port=8080)


def runwebsite():
  t = Thread(target=run)
  t.start()


@app.route('/')
@app.route('/home')
def index():
  return send_file('pages/index.html')


@app.errorhandler(404)
def page_not_found(e):
  return send_file('pages/error400.html')


@app.errorhandler(500)
def internal_server_error(e):
  return send_file('pages/error500.html')


@app.route('/news')
def news():
  return send_file('pages/news.html')


@app.route('/hire')
def hire():
  return send_file('pages/hire.html')


@app.route('/faqs')
def faqs():
  return send_file('pages/faqs.html')


@app.route('/contact')
def contact():
  return send_file('pages/contact.html')


@app.route('/login')
def login():
  return send_file('pages/login.html')


@app.route('/login/signup')
def silver():
  return send_file('pages/signup.html')

@app.route('/login/8iNk6yncgPwtRs5bgRA')
def admin():
  return send_file('pages/hidden/admin.html')