
import datetime

from State.Models.Report.Provider import Provider
from State.Models.Report.Level import Level
from State.Models.Report.Tag import Tag
from State.Models.Report.Task import Task
from State.Models.Report.Solution import Solution


class Report:
    def __init__(self,
        dir: str,
        name: str,
        alt_name: str,
        type: str | None = None,
        provider: Provider | None = None,
        level: Level | None = None,
        date: datetime.date | None = None,
        tags: list[Tag] = [],
        task: Task | None = None,
        solution: Solution | None = None
    ):
        self._dir = dir
        self._name = name
        self._alt_name = alt_name
        self._type= type
        self._provider = provider
        self._level = level
        self._date = date
        self._tags = tuple(tags)
        self._task = task
        self._solution = solution

    @property
    def dir(self):
        return self._dir
    
    @property
    def name(self):
        return self._name
    
    @property
    def alt_name(self):
        return self._alt_name
    
    @property
    def type(self):
        return self._type
    
    @property
    def provider(self):
        return self._provider
    
    @property
    def level(self):
        return self._level
    
    @property
    def date(self):
        return self._date
    
    @property
    def tags(self):
        return self._tags
    
    @property
    def task(self):
        return self._task
    
    @property
    def solution(self):
        return self._solution
    
    def __str__(self):
        data = {
            'dir': str(self._dir),
            'name': str(self._name),
            'alt_name': str(self._alt_name),
            'type': str(self._type),
            'provider': str(self._provider),
            'level': str(self._level),
            'date': str(self._date),
            'tags': [str(tag) for tag in self._tags],
            'task': str(self._task),
            'solution': str(self._solution)
        }
        return str(data)
