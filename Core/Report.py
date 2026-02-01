
import datetime
import re

from enum              import StrEnum
from pydantic          import BaseModel
from typing_extensions import Self
from typing            import Literal
from pathlib           import Path


class Level(StrEnum):
    Baby   = 'Baby'
    Easy   = 'Easy'
    Medium = 'Medium'
    Hard   = 'Hard'
    Insane = 'Insane'

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


class P(BaseModel):
    type: Literal['p'] = 'p'
    text: str

    def to_md(self) -> str:
        return f"{self.text}\n\n"


class Pre(BaseModel):
    type: Literal['pre'] = 'pre'
    text: str
    lang: str = ''

    def to_md(self) -> str:
        return f"```{self.lang}\n{self.text}\n```\n\n"


class Quote(BaseModel):
    type: Literal['quote'] = 'quote'
    text: str

    def to_md(self) -> str:
        return f'> {self.text}\n\n'


class Img(BaseModel):
    type: Literal['img'] = 'img'
    src: str
    alt: str = ''

    def to_md(self) -> str:
        return f'![{self.alt}]({self.src})\n\n'


class File(BaseModel):
    type: Literal['file'] = 'file'
    path: str
    name: str

    def to_md(self) -> str:
        return f'{self.name}: [{self.path}]({self.path} "{self.path}")\n\n'


class HR(BaseModel):
    type: Literal['hr'] = 'hr'

    def to_md(self) -> str:
        return '---\n\n'


class Doc(BaseModel):
    type : Literal['doc'] = 'doc'
    items: list[P | Pre | Img | File | Quote | HR] = []

    def to_json(self, **kwargs) -> str:
        return self.model_dump_json(**kwargs)
    
    def to_md(self) -> str:
        return ''.join(item.to_md() for item in self.items)
    
    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.model_validate_json(json_str)
    
    @classmethod
    def from_md(cls, md_str: str) -> Self:
        patterns = {
            'image'      : re.compile(r'!\[(.*?)\]\((.*?)\)'),
            'file_link'  : re.compile(r'(.+)\s*:\s*\[(.+?)\]\((.*?)(?:\s*"(.+?)")?\)'),
            'code_block' : re.compile(r'^```(\w+)?$'),
            'quote_block': re.compile(r'^> (.+)$'),
            'hr'         : re.compile(r'^---\s*$|^___\s*$|^\*\*\*\s*$')
        }

        lines = md_str.strip().split('\n')
        doc = Doc()

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines
            if not line:
                i += 1
                continue

            # Handle horizontal rules
            hr_match = patterns['hr'].match(line)
            if hr_match:
                doc.items.append(HR())
                i += 1
                continue
            
            # Handle code blocks
            code_match = patterns['code_block'].match(line)
            if code_match:
                lang = code_match.group(1) or ''
                code_lines = []
                i += 1
                
                while i < len(lines) and not patterns['code_block'].match(lines[i].strip()):
                    code_lines.append(lines[i])
                    i += 1
                
                if i < len(lines):  # Skip closing ```
                    i += 1
                
                if code_lines:
                    doc.items.append(Pre(
                        text='\n'.join(code_lines),
                        lang=lang
                    ))
                continue
            
            # Handle quote blocks
            quote_match = patterns['quote_block'].match(line)
            if quote_match:
                quote_lines = [quote_match.group(1)]
                i += 1
                
                # Continue reading quote lines
                while i < len(lines):
                    next_quote_match = patterns['quote_block'].match(lines[i].strip())
                    if next_quote_match:
                        quote_lines.append(next_quote_match.group(1))
                        i += 1
                    else:
                        break
                
                doc.items.append(Quote(
                    text='\n'.join(quote_lines)
                ))
                continue
            
            # Handle images
            img_match = patterns['image'].match(line)
            if img_match:
                alt, src = img_match.groups()
                doc.items.append(Img(
                    src=src,
                    alt=alt or ''
                ))
                i += 1
                continue

            # Handle file links
            file_match = patterns['file_link'].search(line)
            if file_match:
                title, link_text, path, _ = file_match.groups()
                doc.items.append(File(
                    path=path,
                    name=title or link_text or path
                ))
                i += 1
                continue

            paragraph_lines = []
            while i < len(lines):
                line = lines[i].strip()

                if not line:
                    break
                
                if patterns['code_block'].match(line):
                    break

                if patterns['quote_block'].match(line):
                    break

                if patterns['image'].match(line):
                    break
                
                paragraph_lines.append(line)
                i += 1
                
            if paragraph_lines:
                doc.items.append(P(
                    text='\n'.join(paragraph_lines).strip()
                ))
            continue
        return doc


class Report(BaseModel):
    type    : Literal['report'] = 'report'
    name    : str
    event   : str = 'CTF'
    id      : str | None = None
    date    : datetime.date = datetime.date.today()
    lvl     : Level = Level.Baby
    tags    : list[str] = []
    authors : list[str] = []
    task    : Doc = Doc()
    solution: Doc = Doc()

    def to_json(self, **kwargs) -> str:
        return self.model_dump_json(**kwargs)
    
    def to_md(self) -> str:
        md = ''
        md += f'# {self.event} :: {self.name}\n\n'
        md += f'**Уровень**: {self.lvl}\n\n'
        md += f'**Теги**: {", ".join(self.tags)}\n\n'
        md += f'**Авторы**: {", ".join(self.authors)}\n\n'
        md += f'**Дата**: {self.date.strftime("%d.%m.%Y")}\n\n'
        md += f'## Задача\n'
        md += self.task.to_md()
        md += f'## Решение\n'
        md += self.solution.to_md()
        return md
    
    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.model_validate_json(json_str)
    
    @classmethod
    def from_md(cls, md_str: str) -> Self:
        patterns = {
            'header' : re.compile(r'^# (.+?) :: (.+)$'),
            'level'  : re.compile(r'^\*\*Уровень\*\*: (.+)$'),
            'tags'   : re.compile(r'^\*\*Теги\*\*: (.+)$'),
            'authors': re.compile(r'^\*\*Авторы\*\*: (.+)$'),
            'date'   : re.compile(r'^\*\*Дата\*\*: (.+)$'),
            'section': re.compile(r'^## (.+)$')
        }

        lines = md_str.strip().split('\n')
        
        # Parse header and metadata
        event = 'CTF'
        name = ''
        level = Level.Baby
        tags = []
        authors = []
        date_str = ''
        
        task_lines = []
        solution_lines = []
        current_section = None
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Parse header
            header_match = patterns['header'].match(line)
            if header_match:
                event, name = header_match.groups()
                i += 1
                continue
            
            # Parse level
            level_match = patterns['level'].match(line)
            if level_match:
                level_str = level_match.group(1)
                try:
                    level = Level(level_str)
                except ValueError:
                    level = Level.Baby
                i += 1
                continue
            
            # Parse tags
            tags_match = patterns['tags'].match(line)
            if tags_match:
                tags_str = tags_match.group(1)
                tags = [tag.strip() for tag in tags_str.split(',')]
                i += 1
                continue

            # Parse authors
            authors_match = patterns['authors'].match(line)
            if authors_match:
                authors_str = authors_match.group(1)
                authors = [author.strip() for author in authors_str.split(',')]
                i += 1
                continue
            
            # Parse date
            date_match = patterns['date'].match(line)
            if date_match:
                date_str = date_match.group(1)
                i += 1
                continue
            
            # Parse sections
            section_match = patterns['section'].match(line)
            if section_match:
                section_name = section_match.group(1)
                if section_name.lower() in ['задача', 'task']:
                    current_section = 'task'
                if section_name.lower() in ['решение', 'solution']:
                    current_section = 'solution'
                i += 1
                continue
            
            # Collect content based on current section
            if current_section == 'task':
                task_lines.append(lines[i])
            if current_section == 'solution':
                solution_lines.append(lines[i])
            
            i += 1
        
        # Parse date
        try:
            date = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
        except ValueError:
            date = datetime.date.today()
        
        # Parse task and solution docs
        task_doc     = Doc.from_md('\n'.join(task_lines))
        solution_doc = Doc.from_md('\n'.join(solution_lines))
        
        return Report(
            name=name,
            event=event,
            date=date,
            lvl=level,
            tags=tags,
            authors=authors,
            task=task_doc,
            solution=solution_doc
        )
    
    @classmethod
    def load_md(cls, filename) -> Self:
        with open(filename, 'r', encoding='utf-8') as file:
            md = file.read()
        return cls.from_md(md)
    
    @classmethod
    def load_json(cls, filename) -> Self:
        with open(filename, 'r', encoding='utf-8') as file:
            json_data = file.read()
        return cls.from_json(json_data)
    
    @classmethod
    def load(cls, dirname) -> Self:
        report_dir = Path(dirname).resolve()

        if not report_dir.is_absolute():
            report_dir = Path.cwd() / report_dir
        
        if not report_dir.exists():
            raise FileNotFoundError(f'Path {report_dir} not found')
        
        report_path_json = report_dir / 'report.json'
        report_path_md   = report_dir / 'report.md'

        if report_path_json.exists():
            return Report.load_json(report_path_json)
        if report_path_md.exists():
            return Report.load_md(report_path_md)
        raise FileNotFoundError(f'{report_dir.name}: Report file not found, skipped!')
