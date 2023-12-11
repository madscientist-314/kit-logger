'''
  GNU AGPLv3.0 2023 
  Software: v0.0.8
  Kit Logger - DofE Kit Management System
  Copyright (C) 2023 Thomas Kirby

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  
  You should have received a copy of the GNU General Public License
  along with this program [LICENSE.txt].  If not, see <https://www.gnu.org/licenses/>.
'''
from threading import Thread
from flask import Flask, send_file

app = Flask(__name__, template_folder='pages', static_folder='static')


def run():
  app.run(host='0.0.0.0', port=8080)


def runwebsite():
  t = Thread(target=run)
  t.start()

def keep_alive():
  Thread(target=run).start()

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