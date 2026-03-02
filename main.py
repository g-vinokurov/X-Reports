import sys
import json
import os
import re
import asyncio
import requests
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTreeView, QTextEdit, QPushButton, QLabel, QComboBox,
    QLineEdit, QFileSystemModel, QSplitter, QTabWidget,
    QGroupBox, QFormLayout, QCheckBox, QMessageBox, QProgressBar,
    QMenu, QMenuBar, QStatusBar, QToolBar, QDialog, QDialogButtonBox,
    QSpinBox, QTextBrowser
)
from PySide6.QtCore import (
    Qt, QDir, QThread, Signal, QSettings, QTimer, 
    QPropertyAnimation, QEasingCurve, QRect, QPoint, Slot, QUrl
)
from PySide6.QtGui import (
    QIcon, QAction, QFont, QColor, QPalette, 
    QSyntaxHighlighter, QTextCharFormat, QFontDatabase,
    QDesktopServices, QPixmap
)
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

import ollama
from duckduckgo_search import DDGS

# Константы
APP_NAME = "CTF Reports Analyzer"
APP_VERSION = "1.0.0"
SETTINGS_FILE = "settings.json"
REPORTS_DIR = r"D:\Write-Ups"

# ==================== Модели данных ====================

class SearchEngine(Enum):
    DUCKDUCKGO = "DuckDuckGo"
    # GOOGLE = "Google"  # для будущего расширения
    # BING = "Bing"

@dataclass
class AppSettings:
    """Настройки приложения"""
    ollama_base_url: str = "http://localhost:11434"
    model_name: str = "qwen2.5-coder:7b"
    search_engine: str = SearchEngine.DUCKDUCKGO.value
    max_search_results: int = 5
    enable_web_search: bool = False
    auto_index_reports: bool = True
    theme: str = "system"  # system, light, dark
    
    def save(self, filepath: str = SETTINGS_FILE):
        """Сохранить настройки в JSON"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(asdict(self), f, indent=4, ensure_ascii=False)
    
    @classmethod
    def load(cls, filepath: str = SETTINGS_FILE) -> 'AppSettings':
        """Загрузить настройки из JSON"""
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return cls(**data)
            except:
                return cls()
        return cls()

@dataclass
class ReportInfo:
    """Информация о райтапе"""
    folder_name: str
    folder_path: str
    report_file: Optional[str] = None
    has_report: bool = False
    files: List[str] = None
    title: str = ""
    description: str = ""
    ctf_name: str = ""
    challenge_name: str = ""
    date: Optional[datetime] = None
    tags: List[str] = None
    error: Optional[str] = None
    
    def __post_init__(self):
        if self.files is None:
            self.files = []
        if self.tags is None:
            self.tags = []

# ==================== Потоки для асинхронных операций ====================

class OllamaWorker(QThread):
    """Поток для работы с Ollama"""
    finished = Signal(str)
    error = Signal(str)
    progress = Signal(str)
    models_loaded = Signal(list)
    
    def __init__(self):
        super().__init__()
        self.base_url = None
        self.model = None
        self.prompt = None
        self.context = None
        self.action = "chat"  # chat, list_models
    
    def set_chat_params(self, base_url: str, model: str, prompt: str, context: str = ""):
        self.base_url = base_url
        self.model = model
        self.prompt = prompt
        self.context = context
        self.action = "chat"
    
    def set_list_models(self, base_url: str):
        self.base_url = base_url
        self.action = "list_models"
    
    def run(self):
        try:
            client = ollama.Client(host=self.base_url)
            
            if self.action == "list_models":
                try:
                    models = client.list()
                    model_names = [m['name'] for m in models.get('models', [])]
                    self.models_loaded.emit(model_names)
                except Exception as e:
                    self.error.emit(f"Не удалось получить список моделей: {str(e)}")
                return
            
            # Формируем промпт с контекстом
            full_prompt = f"""
Ты - ассистент для анализа CTF-райтапов (writeups). 
Используй предоставленный контекст из файлов райтапов для ответа на вопрос.

Контекст из файлов:
{self.context}

Вопрос пользователя: {self.prompt}

Дай подробный, структурированный ответ на русском языке, ссылаясь на конкретные райтапы.
"""
            
            response = client.chat(
                model=self.model,
                messages=[{"role": "user", "content": full_prompt}]
            )
            
            self.finished.emit(response['message']['content'])
            
        except Exception as e:
            self.error.emit(f"Ошибка Ollama: {str(e)}")

class SearchWorker(QThread):
    """Поток для веб-поиска"""
    finished = Signal(str)
    error = Signal(str)
    progress = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.query = None
        self.max_results = 5
    
    def set_search_params(self, query: str, max_results: int = 5):
        self.query = query
        self.max_results = max_results
    
    def run(self):
        try:
            self.progress.emit("Поиск в интернете...")
            
            with DDGS() as ddgs:
                results = list(ddgs.text(self.query, max_results=self.max_results))
                
                if not results:
                    self.finished.emit("Ничего не найдено.")
                    return
                
                formatted = "🌐 Результаты поиска:\n\n"
                for i, r in enumerate(results, 1):
                    formatted += f"{i}. {r.get('title', 'Без названия')}\n"
                    formatted += f"   {r.get('body', '')}\n"
                    formatted += f"   Источник: {r.get('href', '')}\n\n"
                
                self.finished.emit(formatted)
                
        except Exception as e:
            self.error.emit(f"Ошибка поиска: {str(e)}")

# ==================== Кастомные виджеты ====================

class MarkdownHighlighter(QSyntaxHighlighter):
    """Подсветка синтаксиса Markdown"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []
        
        # Заголовки
        header_format = QTextCharFormat()
        header_format.setFontWeight(QFont.Weight.Bold)
        header_format.setForeground(QColor("#569CD6"))
        header_format.setFontPointSize(14)
        self.highlighting_rules.append((re.compile(r"^#{1,6} .+"), header_format))
        
        # Жирный текст
        bold_format = QTextCharFormat()
        bold_format.setFontWeight(QFont.Weight.Bold)
        self.highlighting_rules.append((re.compile(r"\*\*.+?\*\*"), bold_format))
        self.highlighting_rules.append((re.compile(r"__.+?__"), bold_format))
        
        # Курсив
        italic_format = QTextCharFormat()
        italic_format.setFontItalic(True)
        self.highlighting_rules.append((re.compile(r"\*.+?\*"), italic_format))
        self.highlighting_rules.append((re.compile(r"_.+?_"), italic_format))
        
        # Код
        code_format = QTextCharFormat()
        code_format.setFontFamily("Courier New")
        code_format.setBackground(QColor("#F5F5F5"))
        self.highlighting_rules.append((re.compile(r"`[^`]+`"), code_format))
        self.highlighting_rules.append((re.compile(r"^ {4}.*"), code_format))
        self.highlighting_rules.append((re.compile(r"^\t.*"), code_format))
        
        # Ссылки
        link_format = QTextCharFormat()
        link_format.setForeground(QColor("#0000FF"))
        link_format.setUnderlineStyle(QTextCharFormat.UnderlineStyle.SingleUnderline)
        self.highlighting_rules.append((re.compile(r"\[.+?\]\(.+?\)"), link_format))
    
    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            for match in pattern.finditer(text):
                self.setFormat(match.start(), match.end() - match.start(), format)

class ClickableTextBrowser(QTextBrowser):
    """Текстовый браузер с поддержкой кликабельных ссылок на файлы"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOpenExternalLinks(True)
        self.setOpenLinks(True)
        self.base_path = None
    
    def set_base_path(self, path: str):
        """Устанавливает базовый путь для относительных ссылок"""
        self.base_path = path
    
    def load_resource(self, type: int, name: QUrl):
        """Загружает ресурсы (изображения) из локальных файлов"""
        if type == QTextBrowser.ImageResource:
            if self.base_path:
                file_path = Path(self.base_path) / name.toString()
                if file_path.exists():
                    return QPixmap(str(file_path))
        return super().load_resource(type, name)

# ==================== Диалоги ====================

class SettingsDialog(QDialog):
    """Диалог настроек"""
    
    def __init__(self, settings: AppSettings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self.setWindowTitle(f"Настройки - {APP_NAME}")
        self.setMinimumWidth(500)
        self.setup_ui()
        self.load_settings()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Форма настроек
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)
        
        # Ollama URL
        self.ollama_url_edit = QLineEdit()
        self.ollama_url_edit.setPlaceholderText("http://localhost:11434")
        form_layout.addRow("Ollama Base URL:", self.ollama_url_edit)
        
        # Модель
        self.model_combo = QComboBox()
        self.model_combo.setEditable(True)
        self.model_combo.addItem("qwen2.5-coder:7b")
        self.model_combo.addItem("llama3.2:3b")
        self.model_combo.addItem("llama3.1:8b")
        self.model_combo.addItem("mistral:7b")
        form_layout.addRow("Модель:", self.model_combo)
        
        # Кнопка обновления списка моделей
        refresh_btn = QPushButton("🔄 Обновить список")
        refresh_btn.clicked.connect(self.refresh_models)
        form_layout.addRow("", refresh_btn)
        
        # Поисковый движок
        self.search_combo = QComboBox()
        self.search_combo.addItems([e.value for e in SearchEngine])
        form_layout.addRow("Поисковый движок:", self.search_combo)
        
        # Максимум результатов поиска
        self.max_results_spin = QSpinBox()
        self.max_results_spin.setRange(1, 20)
        self.max_results_spin.setValue(5)
        form_layout.addRow("Макс. результатов:", self.max_results_spin)
        
        # Автоиндексация
        self.auto_index_check = QCheckBox("Автоматически индексировать райтапы")
        self.auto_index_check.setChecked(True)
        form_layout.addRow("", self.auto_index_check)
        
        # Тема
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["system", "light", "dark"])
        form_layout.addRow("Тема:", self.theme_combo)
        
        layout.addWidget(form_widget)
        
        # Кнопки
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
    
    def load_settings(self):
        """Загружает настройки в UI"""
        self.ollama_url_edit.setText(self.settings.ollama_base_url)
        self.model_combo.setCurrentText(self.settings.model_name)
        self.search_combo.setCurrentText(self.settings.search_engine)
        self.max_results_spin.setValue(self.settings.max_search_results)
        self.auto_index_check.setChecked(self.settings.auto_index_reports)
        self.theme_combo.setCurrentText(self.settings.theme)
    
    def get_settings(self) -> AppSettings:
        """Возвращает обновлённые настройки"""
        return AppSettings(
            ollama_base_url=self.ollama_url_edit.text().strip(),
            model_name=self.model_combo.currentText().strip(),
            search_engine=self.search_combo.currentText(),
            max_search_results=self.max_results_spin.value(),
            auto_index_reports=self.auto_index_check.isChecked(),
            theme=self.theme_combo.currentText()
        )
    
    def refresh_models(self):
        """Обновляет список доступных моделей из Ollama"""
        try:
            client = ollama.Client(host=self.ollama_url_edit.text())
            models = client.list()
            
            self.model_combo.clear()
            for m in models.get('models', []):
                self.model_combo.addItem(m['name'])
            
            QMessageBox.information(self, "Успех", "Список моделей обновлён!")
            
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось получить список моделей: {str(e)}")

# ==================== Главное окно ====================

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = AppSettings.load()
        self.reports: Dict[str, ReportInfo] = {}
        self.current_report: Optional[ReportInfo] = None
        
        # Инициализация потоков
        self.ollama_worker = OllamaWorker()
        self.search_worker = SearchWorker()
        
        self.setup_ui()
        self.load_reports()
        self.setup_connections()
        self.apply_theme()
        
        # Автоматическая индексация при запуске
        if self.settings.auto_index_reports:
            QTimer.singleShot(500, self.index_reports)
    
    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.setGeometry(100, 100, 1400, 800)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Главный layout
        main_layout = QHBoxLayout(central_widget)
        
        # Создаём сплиттер
        splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(splitter)
        
        # ===== Левая панель =====
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        
        # Заголовок
        title_label = QLabel("📁 CTF Райтапы")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 5px;")
        left_layout.addWidget(title_label)
        
        # Дерево файлов
        self.tree_view = QTreeView()
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath(REPORTS_DIR)
        self.file_model.setFilter(QDir.Filter.AllDirs | QDir.Filter.Files | QDir.Filter.NoDotAndDotDot)
        
        self.tree_view.setModel(self.file_model)
        self.tree_view.setRootIndex(self.file_model.index(REPORTS_DIR))
        self.tree_view.setColumnWidth(0, 250)
        self.tree_view.hideColumn(1)  # Size
        self.tree_view.hideColumn(2)  # Type
        self.tree_view.hideColumn(3)  # Date Modified
        
        left_layout.addWidget(self.tree_view)
        
        # Кнопки управления
        btn_layout = QHBoxLayout()
        
        self.index_btn = QPushButton("🔄 Индексировать")
        self.index_btn.setToolTip("Переиндексировать все райтапы")
        btn_layout.addWidget(self.index_btn)
        
        self.open_folder_btn = QPushButton("📂 Открыть папку")
        self.open_folder_btn.setToolTip("Открыть папку Reports")
        btn_layout.addWidget(self.open_folder_btn)
        
        left_layout.addLayout(btn_layout)
        
        # Информация о райтапе
        info_group = QGroupBox("Информация")
        info_layout = QFormLayout(info_group)
        
        self.info_title = QLabel("-")
        self.info_title.setWordWrap(True)
        info_layout.addRow("Название:", self.info_title)
        
        self.info_ctf = QLabel("-")
        info_layout.addRow("CTF:", self.info_ctf)
        
        self.info_challenge = QLabel("-")
        info_layout.addRow("Задание:", self.info_challenge)
        
        self.info_date = QLabel("-")
        info_layout.addRow("Дата:", self.info_date)
        
        self.info_tags = QLabel("-")
        self.info_tags.setWordWrap(True)
        info_layout.addRow("Теги:", self.info_tags)
        
        left_layout.addWidget(info_group)
        
        splitter.addWidget(left_widget)
        
        # ===== Центральная панель =====
        center_widget = QWidget()
        center_layout = QVBoxLayout(center_widget)
        center_layout.setContentsMargins(0, 0, 0, 0)
        
        # Табы
        self.tab_widget = QTabWidget()
        
        # Таб с просмотром файлов
        self.file_viewer = ClickableTextBrowser()
        self.file_viewer.set_base_path(REPORTS_DIR)
        self.tab_widget.addTab(self.file_viewer, "📄 Просмотр")
        
        # Таб с вопросом к LLM
        self.qa_widget = QWidget()
        qa_layout = QVBoxLayout(self.qa_widget)
        
        # Текущий контекст
        context_group = QGroupBox("Контекст анализа")
        context_layout = QVBoxLayout(context_group)
        
        self.context_text = QTextEdit()
        self.context_text.setMaximumHeight(150)
        self.context_text.setPlaceholderText("Здесь будет контекст из выбранных файлов...")
        self.context_text.setReadOnly(True)
        context_layout.addWidget(self.context_text)
        
        qa_layout.addWidget(context_group)
        
        # Вопрос
        question_group = QGroupBox("Вопрос")
        question_layout = QVBoxLayout(question_group)
        
        self.question_edit = QTextEdit()
        self.question_edit.setMaximumHeight(100)
        self.question_edit.setPlaceholderText("Введите ваш вопрос о райтапах...")
        question_layout.addWidget(self.question_edit)
        
        qa_layout.addWidget(question_group)
        
        # Кнопки управления
        ctrl_layout = QHBoxLayout()
        
        self.web_search_check = QCheckBox("🌐 Искать в интернете")
        ctrl_layout.addWidget(self.web_search_check)
        
        self.search_first_check = QCheckBox("Сначала искать, потом анализировать")
        self.search_first_check.setChecked(True)
        ctrl_layout.addWidget(self.search_first_check)
        
        ctrl_layout.addStretch()
        
        self.ask_btn = QPushButton("🚀 Спросить")
        self.ask_btn.setMinimumWidth(150)
        self.ask_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        ctrl_layout.addWidget(self.ask_btn)
        
        qa_layout.addLayout(ctrl_layout)
        
        # Прогресс
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        qa_layout.addWidget(self.progress_bar)
        
        # Ответ
        answer_group = QGroupBox("Ответ")
        answer_layout = QVBoxLayout(answer_group)
        
        self.answer_browser = ClickableTextBrowser()
        self.answer_browser.setOpenExternalLinks(True)
        answer_layout.addWidget(self.answer_browser)
        
        qa_layout.addWidget(answer_group)
        
        self.tab_widget.addTab(self.qa_widget, "🤖 Анализ")
        
        center_layout.addWidget(self.tab_widget)
        
        splitter.addWidget(center_widget)
        
        # ===== Правая панель (история) =====
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        
        history_label = QLabel("📋 История вопросов")
        history_label.setStyleSheet("font-size: 14px; font-weight: bold; padding: 5px;")
        right_layout.addWidget(history_label)
        
        self.history_list = QTextEdit()
        self.history_list.setReadOnly(True)
        self.history_list.setMaximumWidth(250)
        right_layout.addWidget(self.history_list)
        
        splitter.addWidget(right_widget)
        
        # Устанавливаем пропорции
        splitter.setSizes([300, 700, 200])
        
        # Создаём меню
        self.create_menu()
        
        # Создаём статусбар
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Готов")
    
    def create_menu(self):
        """Создаёт меню приложения"""
        menubar = self.menuBar()
        
        # Меню Файл
        file_menu = menubar.addMenu("Файл")
        
        index_action = QAction("🔄 Индексировать райтапы", self)
        index_action.triggered.connect(self.index_reports)
        file_menu.addAction(index_action)
        
        open_folder_action = QAction("📂 Открыть папку Reports", self)
        open_folder_action.triggered.connect(self.open_reports_folder)
        file_menu.addAction(open_folder_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("🚪 Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Меню Настройки
        settings_menu = menubar.addMenu("Настройки")
        
        settings_action = QAction("⚙️ Параметры", self)
        settings_action.triggered.connect(self.show_settings)
        settings_menu.addAction(settings_action)
        
        models_action = QAction("🤖 Управление моделями", self)
        models_action.triggered.connect(self.manage_models)
        settings_menu.addAction(models_action)
        
        # Меню Помощь
        help_menu = menubar.addMenu("Помощь")
        
        about_action = QAction("ℹ️ О программе", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def setup_connections(self):
        """Настройка сигналов и слотов"""
        self.tree_view.clicked.connect(self.on_file_clicked)
        self.index_btn.clicked.connect(self.index_reports)
        self.open_folder_btn.clicked.connect(self.open_reports_folder)
        self.ask_btn.clicked.connect(self.ask_question)
        
        # Сигналы от рабочих потоков
        self.ollama_worker.finished.connect(self.on_ollama_response)
        self.ollama_worker.error.connect(self.on_ollama_error)
        self.ollama_worker.progress.connect(self.on_progress)
        self.ollama_worker.models_loaded.connect(self.on_models_loaded)
        
        self.search_worker.finished.connect(self.on_search_response)
        self.search_worker.error.connect(self.on_search_error)
        self.search_worker.progress.connect(self.on_progress)
    
    def apply_theme(self):
        """Применяет выбранную тему"""
        if self.settings.theme == "dark":
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QWidget {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QGroupBox {
                    border: 2px solid #555;
                    border-radius: 5px;
                    margin-top: 10px;
                    font-weight: bold;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 10px;
                    padding: 0 5px 0 5px;
                }
                QTextEdit, QTreeView {
                    background-color: #3b3b3b;
                    color: #ffffff;
                    border: 1px solid #555;
                }
                QPushButton {
                    background-color: #4a4a4a;
                    color: white;
                    border: 1px solid #555;
                    padding: 5px;
                    border-radius: 3px;
                }
                QPushButton:hover {
                    background-color: #5a5a5a;
                }
            """)
    
    def load_reports(self):
        """Загружает информацию о райтапах"""
        reports_path = Path(REPORTS_DIR)
        if not reports_path.exists():
            reports_path.mkdir(exist_ok=True)
            self.status_bar.showMessage("Создана папка Reports")
    
    def index_reports(self):
        """Индексирует все райтапы в папке Reports"""
        self.reports.clear()
        reports_path = Path(REPORTS_DIR)
        
        if not reports_path.exists():
            return
        
        self.status_bar.showMessage("Индексация райтапов...")
        
        for folder in reports_path.iterdir():
            if folder.is_dir():
                report = self.scan_report_folder(folder)
                self.reports[report.folder_name] = report
        
        self.status_bar.showMessage(f"Проиндексировано райтапов: {len(self.reports)}")
        
        # Обновляем дерево
        self.tree_view.setRootIndex(self.file_model.index(REPORTS_DIR))
    
    def scan_report_folder(self, folder_path: Path) -> ReportInfo:
        """Сканирует папку с райтапом"""
        report = ReportInfo(
            folder_name=folder_path.name,
            folder_path=str(folder_path)
        )
        
        # Ищем report.md
        report_file = folder_path / "report.md"
        if report_file.exists():
            report.has_report = True
            report.report_file = str(report_file)
            
            # Парсим report.md для извлечения метаданных
            try:
                content = report_file.read_text(encoding='utf-8')
                self.parse_report_metadata(content, report)
            except:
                report.error = "Ошибка чтения report.md"
        
        # Собираем все файлы в папке
        for f in folder_path.iterdir():
            if f.is_file() and f.name != "report.md":
                report.files.append(f.name)
        
        return report
    
    def parse_report_metadata(self, content: str, report: ReportInfo):
        """Парсит метаданные из report.md"""
        lines = content.split('\n')
        
        for line in lines[:20]:  # Смотрим только первые 20 строк
            if line.startswith('# '):
                report.title = line[2:].strip()
            elif line.startswith('CTF:'):
                report.ctf_name = line[4:].strip()
            elif line.startswith('Challenge:'):
                report.challenge_name = line[10:].strip()
            elif line.startswith('Date:'):
                try:
                    date_str = line[5:].strip()
                    report.date = datetime.strptime(date_str, "%Y-%m-%d")
                except:
                    pass
            elif line.startswith('Tags:'):
                tags = line[5:].strip().split(',')
                report.tags = [t.strip() for t in tags]
    
    def on_file_clicked(self, index):
        """Обработчик клика по файлу в дереве"""
        path = self.file_model.filePath(index)
        
        if os.path.isfile(path):
            self.show_file_content(path)
            
            # Если это report.md, показываем информацию о райтапе
            if path.endswith('report.md'):
                folder_name = os.path.basename(os.path.dirname(path))
                if folder_name in self.reports:
                    self.current_report = self.reports[folder_name]
                    self.update_report_info()
    
    def show_file_content(self, file_path: str):
        """Показывает содержимое файла"""
        try:
            ext = Path(file_path).suffix.lower()
            
            if ext in ['.md', '.txt', '.py', '.sh', '.c', '.cpp', '.json', '.xml']:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if ext == '.md':
                    # Конвертируем Markdown в HTML
                    import markdown
                    html = markdown.markdown(content)
                    self.file_viewer.setHtml(html)
                else:
                    self.file_viewer.setPlainText(content)
                    
                self.file_viewer.set_base_path(os.path.dirname(file_path))
                
            elif ext in ['.png', '.jpg', '.jpeg', '.gif']:
                # Показываем изображение
                html = f'<img src="{file_path}" style="max-width: 100%;">'
                self.file_viewer.setHtml(html)
                
            else:
                # Для бинарных файлов показываем сообщение
                self.file_viewer.setPlainText(f"Файл {ext} не может быть отображён")
                
            self.tab_widget.setCurrentIndex(0)  # Переключаемся на вкладку просмотра
            
        except Exception as e:
            self.file_viewer.setPlainText(f"Ошибка открытия файла: {str(e)}")
    
    def update_report_info(self):
        """Обновляет информацию о текущем райтапе"""
        if not self.current_report:
            return
        
        self.info_title.setText(self.current_report.title or "-")
        self.info_ctf.setText(self.current_report.ctf_name or "-")
        self.info_challenge.setText(self.current_report.challenge_name or "-")
        self.info_date.setText(
            self.current_report.date.strftime("%Y-%m-%d") if self.current_report.date else "-"
        )
        self.info_tags.setText(", ".join(self.current_report.tags) if self.current_report.tags else "-")
    
    def ask_question(self):
        """Обработчик кнопки 'Спросить'"""
        question = self.question_edit.toPlainText().strip()
        
        if not question:
            QMessageBox.warning(self, "Предупреждение", "Введите вопрос!")
            return
        
        # Собираем контекст из текущего райтапа или всех
        context = self.gather_context()
        
        if not context and not self.web_search_check.isChecked():
            reply = QMessageBox.question(
                self, "Подтверждение",
                "Нет контекста из райтапов. Всё равно продолжить?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return
        
        self.context_text.setPlainText(context if context else "Контекст не выбран")
        
        # Добавляем вопрос в историю
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.history_list.append(f"[{timestamp}] {question[:50]}...")
        
        # Блокируем кнопку
        self.ask_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # Бесконечный прогресс
        
        # Определяем порядок действий
        if self.web_search_check.isChecked() and self.search_first_check.isChecked():
            # Сначала ищем, потом анализируем
            self.status_bar.showMessage("Выполняется поиск...")
            self.search_worker.set_search_params(question, self.settings.max_search_results)
            self.search_worker.start()
        elif self.web_search_check.isChecked():
            # Сначала анализ, потом поиск
            self.ask_llm_with_context(question, context)
        else:
            # Только анализ
            self.ask_llm_with_context(question, context)
    
    def gather_context(self) -> str:
        """Собирает контекст из выбранных файлов"""
        context_parts = []
        
        if self.current_report:
            # Добавляем информацию о текущем райтапе
            report = self.current_report
            context_parts.append(f"=== Райтап: {report.folder_name} ===\n")
            
            if report.has_report and report.report_file:
                try:
                    with open(report.report_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    context_parts.append(f"Содержимое report.md:\n{content[:2000]}")
                except:
                    context_parts.append("Ошибка чтения report.md")
            
            # Добавляем другие файлы
            for file in report.files[:5]:  # Ограничиваем количество
                file_path = Path(report.folder_path) / file
                try:
                    if file_path.suffix in ['.py', '.txt', '.md', '.sh']:
                        content = file_path.read_text(encoding='utf-8')[:1000]
                        context_parts.append(f"\nФайл {file}:\n{content}")
                except:
                    pass
        
        return "\n\n".join(context_parts)
    
    def ask_llm_with_context(self, question: str, context: str):
        """Задаёт вопрос LLM с контекстом"""
        self.status_bar.showMessage("Обращение к LLM...")
        
        self.ollama_worker.set_chat_params(
            base_url=self.settings.ollama_base_url,
            model=self.settings.model_name,
            prompt=question,
            context=context
        )
        self.ollama_worker.start()
    
    def on_search_response(self, results: str):
        """Обработчик результатов поиска"""
        # Сохраняем результаты поиска
        search_results = results
        
        # Получаем вопрос
        question = self.question_edit.toPlainText().strip()
        
        # Собираем контекст
        context = self.gather_context()
        
        # Формируем новый промпт с результатами поиска
        enhanced_prompt = f"""
Вопрос: {question}

Результаты веб-поиска:
{search_results}

Контекст из райтапов:
{context}

На основе всей доступной информации дай подробный ответ.
Если информация противоречива, укажи это.
"""
        
        # Отправляем в LLM
        self.ask_llm_with_context(question, enhanced_prompt)
    
    def on_search_error(self, error: str):
        """Обработчик ошибки поиска"""
        QMessageBox.warning(self, "Ошибка поиска", error)
        self.ask_btn.setEnabled(True)
        self.progress_bar.setVisible(False)
    
    def on_ollama_response(self, response: str):
        """Обработчик ответа от Ollama"""
        self.answer_browser.setPlainText(response)
        self.status_bar.showMessage("Ответ получен")
        self.ask_btn.setEnabled(True)
        self.progress_bar.setVisible(False)
        
        # Сохраняем ответ в историю
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.history_list.append(f"[{timestamp}] Ответ получен")
        
        # Переключаемся на вкладку с ответом
        self.tab_widget.setCurrentIndex(1)
    
    def on_ollama_error(self, error: str):
        """Обработчик ошибки Ollama"""
        QMessageBox.critical(self, "Ошибка Ollama", error)
        self.ask_btn.setEnabled(True)
        self.progress_bar.setVisible(False)
    
    def on_progress(self, message: str):
        """Обновление прогресса"""
        self.status_bar.showMessage(message)
    
    def on_models_loaded(self, models: list):
        """Обработчик загрузки списка моделей"""
        # Можем обновить комбобокс в настройках
        pass
    
    def open_reports_folder(self):
        """Открывает папку Reports в файловом менеджере"""
        path = os.path.abspath(REPORTS_DIR)
        QDesktopServices.openUrl(QUrl.fromLocalFile(path))
    
    def show_settings(self):
        """Показывает диалог настроек"""
        dialog = SettingsDialog(self.settings, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.settings = dialog.get_settings()
            self.settings.save()
            self.apply_theme()
            self.status_bar.showMessage("Настройки сохранены")
    
    def manage_models(self):
        """Управление моделями Ollama"""
        # Здесь можно добавить диалог для управления моделями
        pass
    
    def show_about(self):
        """Показывает информацию о программе"""
        QMessageBox.about(
            self,
            f"О программе {APP_NAME}",
            f"""
            <h2>{APP_NAME} v{APP_VERSION}</h2>
            <p>Приложение для анализа CTF-райтапов с использованием локальных LLM.</p>
            <p><b>Возможности:</b></p>
            <ul>
                <li>Просмотр и индексация райтапов</li>
                <li>Анализ через Ollama (Qwen 2.5 Coder 7B)</li>
                <li>Поиск в интернете через DuckDuckGo</li>
                <li>Поддержка Markdown и подсветка синтаксиса</li>
                <li>Сохранение настроек</li>
            </ul>
            <p>Сделано с ❤️ для CTF-сообщества</p>
            """
        )

# ==================== Запуск приложения ====================

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName("CTF Tools")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
