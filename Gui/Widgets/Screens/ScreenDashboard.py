
import pathlib

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QImage

from PyQt5.QtCore import Qt

from Gui.Widgets.Screens.Screen import Screen
from Gui.Widgets.Scroll import Scroll
from Gui.Widgets.Scroll import ScrollSecondary

from Gui.Colors import COLOR_VSC_PRIMARY
from Gui.Colors import COLOR_VSC_SECONDARY
from Gui.Colors import COLOR_VSC_TERTIARY
from Gui.Colors import COLOR_BS_LIGHT
from Gui.Colors import COLOR_BS_DARK
from Gui.Colors import COLOR_BS_SECONDARY
from Gui.Colors import COLOR_BS_GRAY_200

from Gui.Fonts import FONT_JET_BRAINS_MONO_NL_BOLD
from Gui.Fonts import FONT_JET_BRAINS_MONO_NL_REGULAR
from Gui.Fonts import FONT_JET_BRAINS_MONO_NL_REGULAR
from Gui.Fonts import FONT_SEGOE_UI_EMOJI

from Gui.Images import IMG_WELCOME

from State.Models.Project import Project
from State.Models.Report.Report import Report
from State.Models.Report.Solution import Solution
from State.Models.Report.Task import Task

from State.Models.Content.Content import Content
from State.Models.Content.File import File
from State.Models.Content.Img import Img
from State.Models.Content.P import P
from State.Models.Content.Pre import Pre

from Logger import log

from App import app


class ReportFileWidget(QWidget):
    def __init__(self, dir: str, file: File, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__dir = dir
        self.__file = file
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            background: none;
            border: none;
        ''')

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 8)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignLeft)

        self._report_file_emoji = ReportParameterEmoji('📌', self)
        self._report_file = ReportParameter(f'{self.__file.name}:', self)
        self._report_file_value = ReportLinkValue(f'{self.__file.src}', self)

        self._layout.addWidget(self._report_file_emoji)
        self._layout.addWidget(self._report_file)
        self._layout.addWidget(self._report_file_value)

        self._layout.setStretch(2, 1)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._report_file_value.updateUI(self.__file.src)


class ReportImageContent(QWidget):
    def __init__(self, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__path = path
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._pixmap = QPixmap.fromImage(QImage(str(self.__path)))
        
        # This code allows show image via QLabel in layout
        # If image is too large it will fit to layout size
        # Usage: if we need scale image to full layout width
        self._image = QLabel("", self)
        self._image.setMinimumSize(1, 1)
        self._image.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._image.setAlignment(Qt.AlignCenter)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignCenter)

        self._layout.addWidget(self._image)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._image.setPixmap(self._pixmap)
        pass

    def resizeEvent(self, event):
        self._image.setPixmap(self._pixmap.scaledToWidth(self._image.width()))


class ReportImageTitle(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 10))
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.IBeamCursor))
    
    def updateUI(self, *args, **kwargs):
        pass


class ReportImageWidget(QWidget):
    def __init__(self, report_dir: str, img: Img, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dir = report_dir
        self.__src = img.src
        self.__text = img.name
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        path = pathlib.Path(self.__dir) / pathlib.Path(self.__src)

        self._image = ReportImageContent(path, self)
        self._image_title = ReportImageTitle(self.__text, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignCenter)

        self._layout.addWidget(self._image)
        self._layout.addWidget(self._image_title)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._image.updateUI(*args, **kwargs)
        self._image_title.updateUI(*args, **kwargs)


class ReportParagraph(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 8)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 10))
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.IBeamCursor))
    
    def updateUI(self, *args, **kwargs):
        pass


class ReportPreformattedWidgetContent(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setContentsMargins(8, 8, 8, 8)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 9))
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.IBeamCursor))
    
    def updateUI(self, *args, **kwargs):
        pass


class ReportPreformattedWidget(QWidget):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__text = text
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._content = ReportPreformattedWidgetContent(self.__text, self)

        self._scroll = ScrollSecondary(self)
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(self._content)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._scroll)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._content.updateUI(*args, **kwargs)


class ReportPreformatted(QWidget):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__text = text
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.IBeamCursor))
        self.setStyleSheet(f'''
            padding: 0px;
            background-color: {COLOR_BS_GRAY_200};
            border-radius: 16px;
            border-color: none;
            color: {COLOR_BS_DARK};
        ''')

        self._widget = ReportPreformattedWidget(self.__text, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)
        
        self._layout.addWidget(self._widget)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._widget.updateUI(*args, **kwargs)


class ReportWidgetInnerContent(QWidget):
    def __init__(self, report: Report, content: Content, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.__content = content
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            background: none;
            border: none;
        ''')

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignTop)

        for item in self.__content.items:
            if isinstance(item, P):
                widget = ReportParagraph(item.text, self)
                self._layout.addWidget(widget)
                continue
        
            if isinstance(item, Pre):
                widget = ReportPreformatted(item.text, self)
                self._layout.addWidget(widget)
                continue

            if isinstance(item, Img):
                widget = ReportImageWidget(self.__report.dir, item, self)
                self._layout.addWidget(widget)
                continue
            
            if isinstance(item, File):
                widget = ReportFileWidget(self.__report.dir, item, self)
                self._layout.addWidget(widget)
                continue

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        for i in reversed(range(self._layout.count())):
            widget = self._layout.itemAt(i).widget()
            if widget is None:
                continue
            widget.updateUI(*args, **kwargs)


class ReportWidgetSolution(QWidget):
    def __init__(self, report: Report, solution: Solution, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.__solution = solution
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            background: none;
            border: none;
        ''')

        self._content = ReportWidgetInnerContent(self.__report, self.__solution.content, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._content)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._content.updateUI(*args, **kwargs)


class ReportWidgetTask(QWidget):
    def __init__(self, report: Report, task: Task, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.__task = task
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            background: none;
            border: none;
        ''')

        self._content = ReportWidgetInnerContent(self.__report, self.__task.content, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._content)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._content.updateUI(*args, **kwargs)


class ReportWidgetSubtitle(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 16, 0, 8)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_BOLD), 10))
    
    def updateUI(self, *args, **kwargs):
        pass


class ReportCardTitle(QLabel):
    def __init__(self, report: Report, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__report = report
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_BOLD), 11))
    
    def updateUI(self, *args, **kwargs):
        report = self.__report
        if report.provider is not None and report.provider.name:
            text = f'{report.provider.name}. '
        else:
            text = ''
        if report.name:
            text = text + f'{report.name}'
        else:
            text = f'{report.alt_name}'
        self.setText(text)


class ReportWidgetTitle(QLabel):
    def __init__(self, report: Report, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__report = report
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_BOLD), 12))
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.IBeamCursor))
    
    def updateUI(self, *args, **kwargs):
        report = self.__report
        if report.provider is not None and report.provider.name:
            text = f'{report.provider.name}. '
        else:
            text = ''
        if report.name:
            text = text + f'{report.name}'
        else:
            text = f'{report.alt_name}'
        self.setText(text)


class ReportCardAltName(QLabel):
    def __init__(self, report: Report, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__report = report
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_SECONDARY};
        ''')
        self.setContentsMargins(0, 0, 0, 8)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 9))

        self.setText(str(self.__report.alt_name))
    
    def updateUI(self, *args, **kwargs):
        pass


class ReportParameterEmoji(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        font = QFont(str(FONT_SEGOE_UI_EMOJI), 12)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.setFont(font)
    
    def updateUI(self, emoji: str, *args, **kwargs):
        self.setText(emoji)


class ReportParameter(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_BOLD), 10))
    
    def updateUI(self, text: str, *args, **kwargs):
        self.setText(text)


class ReportParameterValue(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 10))
        self.adjustHeight()
    
    def adjustHeight(self):
        # Without this method after word-wrapping QLabel will hide last content rows
        font_metrics = self.fontMetrics()
        width = self.width()
        text = self.text()
        text_rect = font_metrics.boundingRect(0, 0, width, 0, Qt.TextWordWrap, text)
        required_height = text_rect.height()
        self.setMinimumHeight(required_height)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustHeight()
    
    def updateUI(self, text: str, *args, **kwargs):
        self.setText(text)


class ReportLinkValue(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        font = QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 10)
        font.setUnderline(True)
        self.setFont(font)
    
    def updateUI(self, text: str, *args, **kwargs):
        self.setText(text)


class ReportWidgetAltName(QLabel):
    def __init__(self, report: Report, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__report = report
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_SECONDARY};
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 9))
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.IBeamCursor))

        self.setText(str(self.__report.alt_name))
    
    def updateUI(self, *args, **kwargs):
        pass


class ReportCardParameters(QWidget):
    def __init__(self, report: Report, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            background: none;
            border: none;
        ''')

        self._layout = QGridLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignTop)

        self._report_type_emoji = ReportParameterEmoji('🚩', self)
        self._report_type = ReportParameter('Тип:', self)
        self._report_type_value = ReportParameterValue(self)

        self._report_level_emoji = ReportParameterEmoji('☢️', self)
        self._report_level = ReportParameter('Уровень:', self)
        self._report_level_value = ReportParameterValue(self)

        self._report_tags_emoji = ReportParameterEmoji('🌵', self)
        self._report_tags = ReportParameter('Теги:', self)
        self._report_tags_value = ReportParameterValue(self)

        self._report_date_emoji = ReportParameterEmoji('☄️', self)
        self._report_date = ReportParameter('Дата:', self)
        self._report_date_value = ReportParameterValue(self)

        self._layout.addWidget(self._report_type_emoji, 0, 0)
        self._layout.addWidget(self._report_type, 0, 1)
        self._layout.addWidget(self._report_type_value, 0, 2)

        self._layout.addWidget(self._report_level_emoji, 1, 0)
        self._layout.addWidget(self._report_level, 1, 1)
        self._layout.addWidget(self._report_level_value, 1, 2)

        self._layout.addWidget(self._report_tags_emoji, 2, 0)
        self._layout.addWidget(self._report_tags, 2, 1)
        self._layout.addWidget(self._report_tags_value, 2, 2)

        self._layout.addWidget(self._report_date_emoji, 3, 0)
        self._layout.addWidget(self._report_date, 3, 1)
        self._layout.addWidget(self._report_date_value, 3, 2)

        self._layout.setColumnStretch(2, 1)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        report = self.__report

        report_type = str(report.type) if report.type is not None else 'Undefined'
        report_level = str(report.level) if report.level is not None else 'Undefined'
        report_tags = [str(tag) for tag in report.tags]
        report_tags = ', '.join(report_tags) if report_tags else 'No tags'
        report_date = str(report.date) if report.date is not None else 'Undefined'

        self._report_type_value.updateUI(report_type)
        self._report_level_value.updateUI(report_level)
        self._report_tags_value.updateUI(report_tags)
        self._report_date_value.updateUI(report_date)


class ReportWidgetParameters(ReportCardParameters):
    def __init__(self, report, parent, *args, **kwargs):
        super().__init__(report, parent, *args, **kwargs)
        self._report_type_value.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self._report_level_value.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self._report_tags_value.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self._report_date_value.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self._report_type_value.setCursor(QCursor(Qt.IBeamCursor))
        self._report_level_value.setCursor(QCursor(Qt.IBeamCursor))
        self._report_tags_value.setCursor(QCursor(Qt.IBeamCursor))
        self._report_date_value.setCursor(QCursor(Qt.IBeamCursor))


class ReportCard(QWidget):
    def __init__(self, report: Report, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            border-radius: 16px;
            background-color: {COLOR_BS_LIGHT};
            border-color: none;
            padding: 0px
        ''')
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self._report_title = ReportCardTitle(self.__report, self)
        self._report_alt_name = ReportCardAltName(self.__report, self)
        self._report_parameters = ReportCardParameters(self.__report, self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._report_title)
        self._layout.addWidget(self._report_alt_name)
        self._layout.addWidget(self._report_parameters)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        self._report_title.updateUI(*args, **kwargs)
        self._report_alt_name.updateUI(*args, **kwargs)
        self._report_parameters.updateUI(*args, **kwargs)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            app.gui.navigator.update('dashboard', current_report=self.__report)


class ReportsList(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.ArrowCursor))

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(16)
        self._layout.setAlignment(Qt.AlignTop)

        self.setLayout(self._layout)

    def updateUI(self, reports: list[Report] = [], **kwargs):
        for i in reversed(range(self._layout.count())):
            widget = self._layout.itemAt(i).widget()
            if widget is None:
                continue
            widget.setParent(None)
        for report in reversed(sorted(reports, key=lambda r: r.alt_name)):
            report_card = ReportCard(report, self)
            report_card.updateUI()
            self._layout.addWidget(report_card)


class ReportsListSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.ArrowCursor))

        self._reports_list = ReportsList(self)

        self._scroll = Scroll(self)
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(self._reports_list)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        
        self._layout.addWidget(self._scroll)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        project : Project | None = app.state.project
        if project is None:
            log.error(f'Project is not defined')
            return
        self._reports_list.updateUI(reports=project.reports)


class ReportWidgetContent(QWidget):
    def __init__(self, report: Report, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            border-radius: 16px;
            background-color: {COLOR_BS_LIGHT};
            border-color: none;
            padding: 0px
        ''')
        self.setCursor(QCursor(Qt.ArrowCursor))

        self._report_title = ReportWidgetTitle(self.__report, self)
        self._report_alt_name = ReportWidgetAltName(self.__report, self)
        self._report_parameters = ReportWidgetParameters(self.__report, self)

        if self.__report.task is not None:
            self._report_task_title = ReportWidgetSubtitle('Задача', self)
            self._report_task = ReportWidgetTask(self.__report, self.__report.task, self)

        if self.__report.solution is not None:
            self._report_solution_title = ReportWidgetSubtitle('Решение', self)
            self._report_solution = ReportWidgetSolution(self.__report, self.__report.solution, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(64, 64, 64, 64)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._report_title)
        self._layout.addWidget(self._report_alt_name)
        self._layout.addWidget(self._report_parameters)

        if self.__report.task is not None:
            self._layout.addWidget(self._report_task_title)
            self._layout.addWidget(self._report_task)

        if self.__report.solution is not None:
            self._layout.addWidget(self._report_solution_title)
            self._layout.addWidget(self._report_solution)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._report_title.updateUI(*args, **kwargs)
        self._report_alt_name.updateUI(*args, **kwargs)
        self._report_parameters.updateUI(*args, **kwargs)

        if self.__report.task is not None:
            self._report_task_title.updateUI(*args, **kwargs)
            self._report_task.updateUI(*args, **kwargs)

        if self.__report.solution is not None:
            self._report_solution_title.updateUI(*args, **kwargs)
            self._report_solution.updateUI(*args, **kwargs)


class ReportWidget(QWidget):
    def __init__(self, report: Report, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.ArrowCursor))

        self._report_content = ReportWidgetContent(self.__report, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._report_content)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._report_content.updateUI(*args, **kwargs)


class ReportSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._report_widget = None

        self._scroll = Scroll(self)
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(None)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)
        
        self._layout.addWidget(self._scroll)

        self.setLayout(self._layout)

    def updateUI(self, *args, report: Report | None = None, **kwargs):
        if report is None:
            self._scroll.setWidget(None)
            self._report_widget = None
            return
        self._report_widget = ReportWidget(report, self)
        self._report_widget.updateUI(*args, **kwargs)
        self._scroll.setWidget(self._report_widget)


class Header(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(32, 32, 32, 32)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        pass


class Body(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._reports_list_section = ReportsListSection(self)
        self._report_section = ReportSection(self)
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._reports_list_section, stretch=34)
        self._layout.addWidget(self._report_section, stretch=55)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        current_report = kwargs.pop('current_report', None)
        self._reports_list_section.updateUI(*args, **kwargs)
        self._report_section.updateUI(*args, report=current_report, **kwargs)


class Footer(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        pass


class ScreenDashboard(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self._background = QPixmap(IMG_WELCOME)

        self._header = Header(self)
        self._body = Body(self)
        self._footer = Footer(self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._header)
        self._layout.addWidget(self._body)
        self._layout.addWidget(self._footer)

        self._layout.setStretch(1, 1)
        
        self.setLayout(self._layout)

    def updateUI(self, *args, current_report: Report | None = None, **kwargs):
        kwargs['current_report'] = current_report
        self._header.updateUI(*args, **kwargs)
        self._body.updateUI(*args, **kwargs)
        self._footer.updateUI(*args, **kwargs)
        app.gui.setWindowTitle('The X-Files | Dashboard')
    
    def paintEvent(self, event):
        screen_size = self.size()
        screen_width = screen_size.width()
        screen_height = screen_size.height()
        screen_ratio = screen_width / screen_height

        image_width = self._background.width()
        image_height = self._background.height()
        image_ratio = image_width / image_height

        painter = QPainter(self)

        if image_ratio > screen_ratio:
            w = int(screen_height * image_ratio)
            h = screen_height
            x = (w - screen_width) // -2
            y = 0
        else:
            w = screen_width
            h = int(screen_width / image_ratio)
            x = 0
            y = (h - screen_height) // -2
        painter.drawPixmap(x, y, w, h, self._background)