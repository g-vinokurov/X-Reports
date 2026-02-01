
import pathlib

from State.Models.Project import Project
from State.Utils.ReportLoader import ReportLoader

from Log import log


class ProjectLoader:
    @classmethod
    def load(cls, path_to_project_dir: str) -> Project:
        project_dir = pathlib.Path(path_to_project_dir).resolve()

        if not project_dir.is_absolute():
            project_dir = pathlib.Path.cwd() / project_dir
        log.debug(f'Load project from {project_dir}')
        
        if not project_dir.exists():
            msg = f'Path {project_dir} not found'
            log.error(msg)
            raise FileNotFoundError(msg)
        
        reports = []
        
        for path in project_dir.iterdir():
            if not path.is_dir():
                continue
            try:
                report = ReportLoader.load(path)
            except Exception as err:
                log.error(f'{err}')
                log.debug(f'{err}', exc_info=True)
                continue
            else:
                log.debug(str(report))
            reports.append(report)
        
        return Project(project_dir, reports)
