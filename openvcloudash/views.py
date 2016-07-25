from openvcloudash import app, statusses
from collections import defaultdict
from flask import render_template

COLORMAP = defaultdict(lambda: 'deep-orange', {'WARNING': 'deep-orange',
                                          'ERROR': 'red',
                                          'OK': 'green'}
                       )

@app.route('/')
def index():
    return render_template('index.html', statusses=statusses, colormap=COLORMAP)
