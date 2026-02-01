
from pydantic          import BaseModel
from typing_extensions import Self
from typing            import Literal
from pathlib           import Path

from Core.Report import Report


class Project(BaseModel):
    type   : Literal['project'] = 'project'
    path   : str
    reports: list[Report] = []

    @property
    def tags(self) -> list[str]:
        return list(set(t.lower() for r in self.reports for t in r.tags))
    
    @property
    def authors(self) -> list[str]:
        return list(set(a for r in self.reports for a in r.authors))
    
    @property
    def events(self) -> list[str]:
        return list(set(r.event for r in self.reports))
    
    def to_json(self, **kwargs) -> str:
        return self.model_dump_json(**kwargs)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.model_validate_json(json_str)
    
    @classmethod
    def load(cls, dirname) -> Self:
        project_dir = Path(dirname).resolve()

        if not project_dir.is_absolute():
            project_dir = Path.cwd() / project_dir
        
        if not project_dir.exists():
            msg = f'Path {project_dir} not found'
            raise FileNotFoundError(msg)

        reports = []
        
        for path in project_dir.iterdir():
            if not path.is_dir():
                continue
            try:
                report = Report.load(path)
                report.id = path.stem
            except Exception as err:
                print(err)
            else:
                reports.append(report)
        
        return Project(path=f'{project_dir}', reports=reports)
