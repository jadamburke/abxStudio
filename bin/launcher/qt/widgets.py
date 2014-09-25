__author__ = 'adamb'

from settings import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PQTitleBar(QFrame):

    def __init__(self, parent, title=""):

        super(PQTitleBar, self).__init__(parent)

        self.title = title
        self.setMouseTracking(True)
        self.offset = False
        self.stop = True
        self.closeOn = False
        self.doClose = False
        self.doMinimize = False
        self.pinOn = False
        self.doPin = False

    def mousePressEvent(self, event):
        self.stop = False
        self.doMinimize = False
        if event.button() == Qt.LeftButton:
            if self.closeRect.contains( event.pos() ):
                self.stop = True
                self.doClose = True
            elif self.pinRect.contains(event.pos()):
                self.stop = True
                self.doPin = not self.doPin
            elif self.minimizeRect.contains(event.pos()):
                self.stop = True
                self.doMinimize = True
            else:
                self.offset = event.globalPos() - self.parent().pos()

    def mouseReleaseEvent(self, event):
        super(PQTitleBar, self).mouseReleaseEvent(event)
        self.stop = True
        if self.doClose and self.closeOn:
            self.parent().close()
        elif self.pinOn:
            if self.doPin:
                print "pin"
                self.parent().setWindowFlags( self.parent().windowFlags() | Qt.WindowStaysOnTopHint )
                self.parent().show()
            else:
                print "unpin"
                self.parent().setWindowFlags(self.parent().windowFlags() & ~Qt.WindowStaysOnTopHint )
                self.parent().show()
        elif self.doMinimize:
            self.parent().showMinimized()

    def mouseMoveEvent(self, event):
        super(PQTitleBar, self).mouseMoveEvent(event)

        self.closeOn = False
        self.pinOn = False

        if self.closeRect.contains(event.pos()):
            self.closeOn = True
            self.update()
        elif self.pinRect.contains(event.pos()):
            self.pinOn = True
            self.update()
        else:
            self.closeOn = False
            self.pinOn = False
            self.update()

        if not self.stop:

            x=event.globalX()
            y=event.globalY()

            if self.offset:
                x_w = self.offset.x()
                y_w = self.offset.y()

                resultX = x - x_w
                resultY = y - y_w

                self.parent().move( resultX, resultY )


    def paintEvent(self, event):
        super(PQTitleBar, self).paintEvent(event)

        painter = QPainter(self)
        painter.setBrush(QColor(35,35,36))
        painter.setPen(QColor(35,35,36))

        rect = QRect(0,0,self.width(), 25)
        painter.drawRect(rect)
        self.topBarRect = rect

        painter.setBrush(QColor(160,160,165))
        painter.setPen(QColor(160,160,165))

        font = painter.font()
        #font.setWeight(QFont.Bold)
        font.setPixelSize(14)
        painter.setFont(font)

        painter.drawText(QPoint(6,17),self.title)

        self.closeImage = QImage(os.path.join(RES,"closeIcon.png"))
        self.pinImage = QImage(os.path.join(RES,"pinOff.png"))
        self.minimizeImage = QImage(os.path.join(RES,"minimiseIcon.png"))

        if self.underMouse():
            if self.closeOn:
                self.closeImage.invertPixels()

        if self.pinOn or self.doPin:
            self.pinImage = QImage(os.path.join(RES,"pin.png"))
            self.pinImage.invertPixels()

        self.closeImage = self.closeImage.scaled(40,20, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pinImage = self.pinImage.scaled(20,20, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.minimizeImage = self.minimizeImage.scaled(20,20, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        rect = self.rect().topRight() - QPoint(self.closeImage.width()+5, 0)
        pinRect = self.rect().topRight() - QPoint(self.closeImage.width() + self.pinImage.width() + 10, 0)
        minimizeRect = self.rect().topRight() - QPoint(self.closeImage.width() + self.pinImage.width() + self.minimizeImage.width() + 15, 0)

        painter.drawImage(rect, self.closeImage)
        painter.drawImage(pinRect, self.pinImage)
        painter.drawImage(minimizeRect, self.minimizeImage)
        self.closeRect = QRect(rect,QSize(self.closeImage.width(), self.closeImage.height()))
        self.pinRect = QRect(pinRect,QSize(self.pinImage.width(), self.pinImage.height()))
        self.minimizeRect = QRect(minimizeRect, QSize(self.minimizeImage.width(), self.minimizeImage.height()))


class GridLayout(QGridLayout):

    def __init__(self, cols=0, rows=0):

        if cols:
            self.cols = True
            self.n = cols
        elif rows:
            self.cols = False
            self.n = rows

        self.i = 0
        self.j = 0

        super(GridLayout,self).__init__()

    def inc( self):

        self.i = self.i+1
        if self.i==self.n:
            self.i=0
            self.j=self.j+1

    def addWidgetAuto( self, widget):

        if not self.cols:
            super(GridLayout,self).addWidget( widget, self.i, self.j)
        else:
            super(GridLayout,self).addWidget( widget, self.j, self.i)

        self.inc()

    def removeWidgetAuto(self, widget):

        super(GridLayout,self).removeWidget( widget)

        self.i = self.i-1
        if self.i==-1:
            self.i=self.n-1
            self.j=self.j-1

    def removeLayoutAuto(self, widget):

        super(GridLayout,self).removeItem( widget)

        self.i = self.i-1
        if self.i==-1:
            self.i=self.n-1
            self.j=self.j-1

    def addLayoutAuto( self, widget):

        if not self.cols:
            super(GridLayout,self).addLayout( widget, self.i, self.j)
        else:
            super(GridLayout,self).addLayout( widget, self.j, self.i)

        self.inc()


class AppLayout(QVBoxLayout):

    def __init__(self, name, parent):

        self.name = name
        self.parent = parent

        super(AppLayout,self).__init__()

        self.setup()

    def setup( self):

        iconpath = os.path.join( RES, "{0}.png".format(self.name))
        pixmap = QPixmap( iconpath)

        self.button = PicButton(pixmap, pixmapHover=True, textRight="", textLeft="")
        self.button.clicked.connect( lambda clicked, name=self.name: self.parent.selectApp(name))
        self.addWidget( self.button)

    def select( self, selected):
        self.button.select( selected)

    def update(self, version, status):

        self.button.textLeft = version
        self.button.textRight = status
        self.button.colorRight = [QColor(255,0,0), QColor(6,244,47)][status=='OK']



class PicButton(QToolButton):

    def __init__(self, pixmap, pixmapHover=None, parent=None, textRight="", textLeft="", colorRight=None, colorLeft=None):

        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap
        self.pixmapHover = pixmapHover
        self.hover = False
        self.textRight = textRight
        self.textLeft = textLeft
        self.colorRight = colorRight
        self.colorLeft = colorLeft

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.hover and self.pixmapHover:
            if isinstance(self.pixmapHover, QPixmap):
                painter.drawPixmap(self.pixmap.rect(), self.pixmapHover)
            else:
                #### paint selection rectangle
                painter.setBrush(QColor(53,53,53,196))
                painter.setPen(QColor(53,53,53,196))
                painter.drawRect(event.rect())
                #### paint Image on top
                painter.drawPixmap(self.pixmap.rect(), self.pixmap)
        else:
            painter.drawPixmap(self.pixmap.rect(), self.pixmap)

        rect = event.rect().adjusted(4,4,-4,-4)
        if self.colorRight:
            painter.setPen(self.colorRight)

        if self.colorLeft:
            painter.setPen(self.colorLeft)

        painter.drawText(rect, Qt.AlignRight | Qt.AlignBottom, self.textRight)
        painter.setPen(QColor(255,255,255))
        painter.drawText(rect, Qt.AlignLeft | Qt.AlignBottom, self.textLeft)


    def sizeHint(self):
        if isinstance(self.pixmapHover, QPixmap):
            size = self.pixmap.size()
        else:
            size = self.pixmap.size() + QSize(0,17)
        return size

    def select(self,hover):
        self.hover = hover
        self.update()


class HoverButton(PicButton):

    def __init__(self, pixmap, pixmapHover=None, parent=None):
        super(HoverButton, self).__init__(pixmap, pixmapHover, parent)
        self.setMouseTracking(True)

    def enterEvent(self,event):
        self.hover = True
        super(HoverButton,self).enterEvent(event)

    def leaveEvent(self,event):
        self.hover = False
        super(HoverButton,self).leaveEvent(event)