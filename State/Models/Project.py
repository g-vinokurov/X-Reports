
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
    
    def search(self, query: str):
        if not query:
            return self.reports
        query = query.strip().lower()

        result = []
        for r in self._reports:
            in_result = False
            for t in r.tags:
                if query in t.name.lower():
                    result += [r]
                    in_result = True
                    break
            if in_result:
                continue
            if r.level and r.level.name.lower() == query:
                result += [r]
                continue
            if r.provider and query in r.provider.name.lower():
                result += [r]
                continue
            if r.name and query in r.name.lower():
                result += [r]
                continue
        return result
