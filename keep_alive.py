from flask import Flask
from threading import Thread
 
app = Flask('')
 
@app.route('/')
def home():
    return "Bot is online"
 
def run():
    app.run(host='0.0.0.0',port=8080)
 
def keep_alive():
    t = Thread(target=run)
    t.start()

@app.route('/user')
def user():
  return "유저 페이지"