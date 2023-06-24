from django.shortcuts import render
from flask import Flask

app = Flask(__name__, static_folder="./frontend/build", static_url_path="/")


@app.route('/')
def indexPage(request):
   return app.send_static_file('index.html')
