import sys
import os
import time

import pygame

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import Qt, QUrl, QTimer

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from mutagen.easyid3 import EasyID3

from ui import Ui_MainWindow

class DraggableLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.window != None:
                self.window.start_drag(event)

    def mouseMoveEvent(self, event):
        if self.window != None:
            self.window.drag(event)

    def mouseReleaseEvent(self, event):
        if self.window != None:
            self.window.stop_drag(event)

class VolumeLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0
        self.setText(f"{self.counter}%")
        self.setMouseTracking(True)
        self.hovered = False

    def enterEvent(self, event):
        self.hovered = True
        self.setText(f"{self.counter}%")
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.hovered = False
        self.setText(f"{self.counter}%")
        super().leaveEvent(event)

    def wheelEvent(self, event):
        if self.hovered:
            delta = event.angleDelta().y() // 25
            if self.counter < 100 and delta > 0:
                self.counter += delta
            elif self.counter > 0 and delta < 0:
                self.counter += delta
            
            if self.counter > 100:
                self.counter = 100
            if self.counter < 0:
                self.counter = 0

            self.setText(f"{self.counter}%")

            pygame.mixer.music.set_volume(self.counter / 100)

class ClickableLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.function = None
        self.arg = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.function and self.arg:
                self.function(self.arg)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resize(400, 50)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.dragging = False
        self.drag_position = QtCore.QPoint()

        self.mousePressEvent = self.start_drag
        self.mouseMoveEvent = self.drag
        self.mouseReleaseEvent = self.stop_drag

        # drag label
        self.ui.compact_name = DraggableLabel("Name")
        self.ui.compact_name.window = self
        self.ui.compact_name.setGeometry(QtCore.QRect(140, 150, 62, 56))
        self.ui.compact_name.setMaximumSize(QtCore.QSize(16777215, 56))
        self.ui.compact_name.setStyleSheet(u"font-size:14px;")
        self.ui.compact_name.setTextFormat(Qt.TextFormat.MarkdownText)
        self.ui.compact_name.setScaledContents(True)
        self.ui.compact_name.setWordWrap(True)
        self.ui.compact_layout_name.addWidget(self.ui.compact_name)

        self.start_play = False
        self.is_playing = False
        self.repeat = False
        self.list = False
        self.lenght = 0
        self.position = 0
        self.start_position = 0
        self.file_loaded = False
        self.current_music_file = None
        self.folder_music = sys.argv[1]
        self.files_list = sorted(os.listdir(self.folder_music))

        # audio connect
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)

        #self.load_file(self.current_music_file)
        self.ui.compact_slider_time.sliderMoved.connect(self.seek)

        # connect buttons
        self.ui.compact_btn_repeat.clicked.connect(self.toggle_repeat)
        self.ui.compact_btn_back.clicked.connect(self.back_music)
        self.ui.compact_btn_play.clicked.connect(self.toggle_play)
        self.ui.compact_btn_next.clicked.connect(self.next_music)
        self.ui.compact_btn_list.clicked.connect(self.toggle_list)
        self.ui.compact_btn_exit.clicked.connect(self.close)

        # add volume label
        self.ui.compact_volume = VolumeLabel()
        self.ui.compact_volume.setObjectName(u"compact_volume")
        self.ui.compact_volume.setGeometry(QtCore.QRect(130, 110, 100, 56))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.compact_volume.sizePolicy().hasHeightForWidth())
        self.ui.compact_volume.setSizePolicy(sizePolicy)
        self.ui.compact_volume.setMinimumSize(QtCore.QSize(100, 56))
        self.ui.compact_volume.setMaximumSize(QtCore.QSize(100, 56))
        self.ui.compact_volume.setStyleSheet("""
            QLabel {
                background: rgba(0, 0, 0, 0);
                color: rgba(0, 0, 0, 0);
                font-size: 22px;
            }
            QLabel::hover {
                background: rgba(0, 0, 0, 100);
                color: rgba(255, 255, 255, 255);
            }
        """)
        self.ui.compact_volume.setTextFormat(Qt.TextFormat.MarkdownText)
        self.ui.compact_volume.setScaledContents(True)
        self.ui.compact_volume.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.compact_volume.setWordWrap(True)
        self.ui.compact_layout_volume.addWidget(self.ui.compact_volume)
        self.ui.compact_volume.counter = 50

        self.create_list()

        self.timer = QTimer(self)
        self.timer.setInterval(16)
        self.timer.timeout.connect(self.update)
        self.timer.start()
    
    def update(self):
        if not self.list and self.size().height() > 95:
            self.resize(400,50)
        if self.list and self.size().height() < 400:
            self.resize(400,450)

        self.position = self.start_position + pygame.mixer.music.get_pos() / 1000
        pos = self.position
        dur = self.lenght
        if pos >= 0 and dur > 0:
            self.ui.compact_slider_time.setValue(int(pos))
            self.ui.compact_label_time.setText(f"{self.sec_to_str(pos)} / {self.sec_to_str(dur)}")

            if pos >= dur*0.998:
                if self.repeat:
                    self.load_file(self.current_music_file)
                else:
                    self.next_music()
    
    def start_drag(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def drag(self, event):
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.drag_position)

    def stop_drag(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
    
    def load_file(self, file_path):
        self.current_music_file = file_path
        try:
            pygame.mixer.music.load(self.current_music_file)
            self.file_loaded = True
        except Exception:
            self.file_loaded = False
        self.start_position = 0
        self.position = 0
        
        audio = MP3(self.current_music_file)
        duration = audio.info.length
        self.update_duration(duration)

        audio = MP3(self.current_music_file, ID3=EasyID3)
        title = audio.get("title", [os.path.basename(self.current_music_file).split('.')[0]])[0]
        self.ui.compact_name.setText(title)

        self.set_bacground_preview()

        if self.start_play and self.is_playing:
            pygame.mixer.music.play(start=0)
        else:
            self.start_play = False
            self.is_playing = False
    
    def toggle_play(self):
        self.is_playing = not self.is_playing
        
        if not self.file_loaded:
            return

        if not self.start_play:
            self.start_play = True
            self.ui.compact_btn_play.setText("||")
            pygame.mixer.music.play()

        elif self.is_playing:
            self.ui.compact_btn_play.setText("||")
            pygame.mixer.music.unpause()

        else:
            self.ui.compact_btn_play.setText("|>")
            pygame.mixer.music.pause()
    
    def next_music(self):
        try:
            i = self.files_list.index(os.path.basename(self.current_music_file))
            if i < len(self.files_list)-1:
                self.load_file(os.path.join(self.folder_music, self.files_list[i+1]))
            else:
                self.load_file(os.path.join(self.folder_music, self.files_list[0]))
        except Exception:
            pass
    def back_music(self):
        try:
            i = self.files_list.index(os.path.basename(self.current_music_file))
            if i > 0:
                self.load_file(os.path.join(self.folder_music, self.files_list[i-1]))
            else:
                self.load_file(os.path.join(self.folder_music, self.files_list[len(self.files_list)-1]))
        except Exception:
            pass
    
    def toggle_repeat(self):
        self.repeat = self.ui.compact_btn_repeat.isChecked()
    
    def seek(self, position):
        self.start_position = position
        if self.file_loaded and self.is_playing:
            pygame.mixer.music.play(start=position)

    def update_duration(self, duration):
        self.lenght = duration
        self.ui.compact_slider_time.setRange(0, int(self.lenght))
    
    def toggle_list(self):
        self.list = not self.list
        if self.list:
            self.ui.compact_btn_list.setText("^")

            current_sizePolicy = self.ui.scrollArea.sizePolicy()
            current_sizePolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
            self.ui.scrollArea.setSizePolicy(current_sizePolicy)

            self.ui.scrollArea.setMaximumSize(400, 1000)
            self.resize(400,450)
            

        else:
            self.ui.compact_btn_list.setText("V")

            current_sizePolicy = self.ui.scrollArea.sizePolicy()
            current_sizePolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Ignored)
            self.ui.scrollArea.setSizePolicy(current_sizePolicy)

            self.ui.scrollArea.setMaximumSize(0, 0)
            self.resize(400,50)
    
    def sec_to_str(self, sec):
        return f"{int(sec//60):02}:{int(sec%60):02}"
    
    def set_bacground_preview(self):
        try:
            self.ui.compact_preivew_img.setStyleSheet("background: rgba(0,0,0,255);")

            audio = MP3(self.current_music_file, ID3=ID3)
            for tag in audio.tags.values():
                if isinstance(tag, APIC):
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(tag.data)

                    scaled = pixmap.scaled(
                        self.ui.compact_preivew_img.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    scaled.save("temp_preview.png")
                    self.ui.compact_preivew_img.setStyleSheet(f"""
                        QWidget {{
                            background-image: url(temp_preview.png) 0 0 0 0 stretch stretch;
                            background-repeat: no-repeat;
                            background-position: center;
                        }}
                    """)
        except Exception:
            pass
    
    def create_list(self):
        for f in self.files_list:
            horizontalLayoutWidget = QtWidgets.QWidget()
            horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 321, 71))
            horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
            horizontalLayout.setContentsMargins(0, 0, 0, 0)
            horizontalLayout.setSpacing(5)
            label_preview_img = QtWidgets.QLabel(horizontalLayoutWidget)
            label_preview_img.setMinimumSize(QtCore.QSize(100, 56))
            label_preview_img.setMaximumSize(QtCore.QSize(56, 16777215))

            horizontalLayout.addWidget(label_preview_img)

            label_name = ClickableLabel(horizontalLayoutWidget)
            label_name.setScaledContents(True)
            label_name.setWordWrap(True)
            label_name.setStyleSheet("""
                QLabel {
                    background: rgba(0, 0, 0, 0);
                    color: #fff;
                }
                QLabel::hover {
                    background: rgba(255, 255, 255, 25);
                }
            """)


            def function(file_path):
                self.load_file(file_path)

            label_name.function = function
            label_name.arg = os.path.join(self.folder_music, f)

            horizontalLayout.addWidget(label_name)

            audio = MP3(os.path.join(self.folder_music, f), ID3=EasyID3)
            title = audio.get("title", [f.split('.')[0]])[0]
            
            label_name.setText(title)
            self.ui.compact_layout_list.addWidget(horizontalLayoutWidget)
            
            try:
                audio = MP3(os.path.join(self.folder_music, f), ID3=ID3)
                for tag in audio.tags.values():
                    if isinstance(tag, APIC):
                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(tag.data)

                        label_preview_img.setPixmap(pixmap.scaled(
                            label_preview_img.size(), 
                            aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                        ))
            except Exception:
                pass
            
            self.ui.compact_layout_list.addWidget(horizontalLayoutWidget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
