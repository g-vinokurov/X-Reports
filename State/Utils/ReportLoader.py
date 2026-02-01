
import pathlib
import bs4
import datetime

from State.Models.Report.Report import Report
from State.Models.Report.Provider import Provider
from State.Models.Report.Level import Level
from State.Models.Report.Tag import Tag
from State.Models.Report.Task import Task
from State.Models.Report.Solution import Solution

from State.Utils.ContentParser import ContentParser

from Logger import log


class ReportLoader:
    @classmethod
    def load(cls, path_to_report_dir: str) -> Report:
        report_dir = pathlib.Path(path_to_report_dir).resolve()

        if not report_dir.is_absolute():
            report_dir = pathlib.Path.cwd() / report_dir
        log.debug(f'Load report from {report_dir}')
        
        if not report_dir.exists():
            raise FileNotFoundError(f'Path {report_dir} not found')
        
        return cls.__parse_report(report_dir)
    
    @classmethod
    def __parse_report(cls, report_dir: pathlib.Path) -> Report:
        report_alt_name = str(report_dir.name)

        report_file_name = 'report.xml'
        report_file_path = report_dir / report_file_name
        if not report_file_path.exists():
            raise FileNotFoundError(f'{report_alt_name}: File {report_file_name} not found, skipped!')
    
        with open(report_file_path, 'r', encoding='utf-8') as report_file:
            report_xml = bs4.BeautifulSoup(report_file.read(), 'xml')
         
        report_head = report_xml.find('head', recursive=True)
        if report_head is None:
            raise ValueError('Report Head not found, skipped!')
        
        report_body = report_xml.find('body', recursive=True)
        if report_body is None:
            raise ValueError('Report Body not found, skipped!')
        
        report_name = cls.__parse_report_metadata_item(report_head, 'name', report_alt_name)
        report_provider = cls.__parse_report_provider(report_head)
        report_type = cls.__parse_report_metadata_item(report_head, 'type')
        report_date = cls.__parse_report_date(report_head)
        report_level = cls.__parse_report_level(report_head)
        report_tags = cls.__parse_report_tags(report_head)

        report_task = cls.__parse_report_task(report_body)
        report_solution = cls.__parse_report_solution(report_body)

        return Report(
            report_dir,
            report_name,
            report_alt_name,
            report_type,
            report_provider,
            report_level,
            report_date,
            report_tags,
            report_task,
            report_solution
        )
    
    @classmethod
    def __parse_report_metadata_item(cls, report_head: bs4.Tag, key: str, default = None):
        report_metadata_item = report_head.find(key, recursive=False)
        if report_metadata_item is not None:
            report_metadata_item = str(report_metadata_item.text).strip()
        else:
            report_metadata_item = default
            log.warning('Report parameter "{key}" not defined: set default')
        return report_metadata_item
    
    @classmethod
    def __parse_report_provider(cls, report_head: bs4.Tag) -> Provider | None:
        provider = cls.__parse_report_metadata_item(report_head, 'provider')
        if not provider or provider is None:
            return None
        return Provider(provider)
    
    @classmethod
    def __parse_report_date(cls, report_head: bs4.Tag) -> datetime.date | None:
        date = cls.__parse_report_metadata_item(report_head, 'date')
        try:
            date = datetime.datetime.strptime(date, "%d.%m.%Y").date()
        except Exception:
            log.warning('Could not recognize report date')
            date = None
        return date
    
    @classmethod
    def __parse_report_level(cls, report_head: bs4.Tag) -> Level | None:
        level = cls.__parse_report_metadata_item(report_head, 'level')
        try:
            level = Level[level]
        except Exception:
            log.warning('Could not recognize report level')
            level = None
        return level
    
    @classmethod
    def __parse_report_tags(cls, report_head: bs4.Tag) -> list[Tag]:
        tags = report_head.find('tags', recursive=False)
        if tags is not None:
            tags = tags.find_all('tag', recursive=False)
        else:
            tags = []
        for i in range(len(tags)):
            tags[i] = str(tags[i].text).strip()
        tags = [Tag(tag) for tag in tags if tag]
        return tags

    @classmethod
    def __parse_report_task(cls, report_body: bs4.Tag) -> Task | None:
        task = report_body.find('task', recursive=False)
        if task is None:
            log.warning('Report Task not found')
            return None
        return Task(ContentParser.parse(task))
    
    @classmethod
    def __parse_report_solution(cls, report_body: bs4.Tag) -> Solution | None:
        solution = report_body.find('solution', recursive=False)
        if solution is None:
            log.warning('Report Solution not found')
            return None
        return Solution(ContentParser.parse(solution))
