from .client import Client
import time

class Status:
    def __init__(self, name, connection):
        self.name = name
        self.url = connection['url']
        self.api = Client(self.url, connection['login'], connection['password'])
        self._status = None
        self._status_time = 0

    @property
    def status(self):
        if time.time() - self._status_time > 10:
            try:
                status = self.api.system.health.getOverallStatus()['state']
            except:
                status = 'ERROR'
            self._status = status
            self._status_time = time.time()
        return self._status
