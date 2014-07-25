import os
from flask import Flask

from main import Main

app = Flask(__name__)

app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])


app.debug = True
app.run()