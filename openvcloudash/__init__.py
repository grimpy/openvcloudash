from flask import Flask
from openvcloudash.settings import connections
from openvcloudash.openvcloud.status import Status

app = Flask(__name__)
statusses = []
for name, connection in connections.items():
    statusses.append(Status(name, connection))

statusses.sort(key=lambda x: x.name)

import openvcloudash.views
app.run(debug=True)
