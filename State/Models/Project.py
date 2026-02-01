
from State.Models.Report.Report import Report


class Project:
    def __init__(self, dir: str, reports: list[Report]):
        self._dir = dir
        self._reports = reports
    
    @property
    def dir(self):
        return self._dir
     
    @property
    def reports(self):
        return self._reports[::]
