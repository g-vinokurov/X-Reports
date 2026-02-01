
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name


class Highlighter:
    @classmethod
    def highlight(cls, text: str, lang: str | None = None):
        lexer = get_lexer_by_name('python', stripall=True)
        formatter = HtmlFormatter(linenos=False, cssclass='code-highlight', style='xcode')
        style = formatter.get_style_defs('.code-highlight')
        text = highlight(text, lexer, formatter)
        text = f'<!DOCTYPE html><html><style>{style}</style><body>{text}</body></html>'
        return text
