__author__ = 'adamb'
import os

class StyleSheet(object):

    def __init__(self):
        pass

    def styleSheet( self, production):

        fileName = ['launcherDev', 'launcher'][production]
        imageTypes = ['bmp','png']
        backgroundImage = None
        for ext in imageTypes:
            path = os.path.join( os.path.expanduser("~"), '.{1}.{0}'.format(ext, fileName)).replace('\\','/')
            if os.path.exists( path):
                backgroundImage = path

        if backgroundImage:
            backgroundImage = 'background-image: url("%s");'%backgroundImage
            backroundColor = ['rgba(14,0,31,0)','rgba(80, 78, 78,0)'][production]
            selectBackgroundColor = ['rgba(7,0,16,0)','rgba(40, 40, 40,0)'][production]
        else:
            backroundColor = ['rgb(14,0,31)','rgb(35, 35, 36)'][production]
            selectBackgroundColor = ['rgb(7,0,16)','rgb(40, 40, 40)'][production]
            backgroundImage = ""

        sStyleSheet = ""
        sStyleSheet += """
            QWidget {
                background-color: %s;
                color: white;
                selection-background-color: %s;
                }
            """%(backroundColor,selectBackgroundColor)
        sStyleSheet += """
            QGroupBox {
                border:1px solid rgb(40, 40, 40);
                border-radius: 0px;
                margin-top: 5ex;
                font-size: 12px;
                font-weight:bold;
            }
            QGroupBox::title  {
                subcontrol-origin: margin;
                top: -2px;
                left: 3px;
                }
            """
        sStyleSheet += """
            QFrame#launcherAppFrame {
                padding-top: 7 7px;
                %s
            }
            """ %(backgroundImage)
        sStyleSheet += """
            QListWidget {
                border:1px solid rgb(40, 40, 40);
                border-radius: 0px;
                background-color: %s;
                selection-background-color: %s;
            }
            """ %(backroundColor,selectBackgroundColor)
        sStyleSheet += """
            QComboBox {
                background-color: %s;
                selection-background-color: %s;
            }
            """ %(backroundColor,selectBackgroundColor)
        sStyleSheet += """
            QComboBox QAbstractItemView {
                background-color: %s;
                selection-background-color: %s;
                background-attachment: scroll;
                %s
            }
            """ %(backroundColor,selectBackgroundColor,backgroundImage)
        sStyleSheet += """
            QPushButton {
                background-color: %s;
                selection-background-color: %s;
                border: none; /* no border for a flat push button */
            }
            QPushButton:hover {
                color:#555555;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                       stop: 0 #dadbde, stop: 1 #f6f7fa);
            }
            QPushButton:pressed  {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                       stop: 0 #000000, stop: 1 #111111);
            }
            """ %(backroundColor,selectBackgroundColor)
        sStyleSheet += """
            QGridLayout {
                background-color: #101010;
            }
            """

        return sStyleSheet
