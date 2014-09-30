__author__ = 'adamb'

from settings import *

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib2
from subprocess import Popen, PIPE, STDOUT

from environment import *
from qt.widgets import *
from qt.stylesheets import *

import yaml

class Launcher(QMainWindow):

    studioenv = StudioEnvironment()

    def __init__(self, parent=None):

        super(Launcher, self).__init__(parent)
        self.updategui = False
        self.resize(800, 500)

        # create a studio environment
        self.studioenv.load_app_config_file(CONFIG+'/app.yml', app='studiotools', version='1.0')
        self.studioenv.setEnv()
        self.studioenv.printout()

        self.updateUi()

    def updateUi(self):

        sStyleSheet = StyleSheet().styleSheet(1)
        self.setStyleSheet(sStyleSheet)

        self.setWindowFlags( Qt.FramelessWindowHint )
        pixmapPasion = QPixmap(os.path.join( RES, "passion-pink.ico"))
        self.setWindowIcon(QIcon(pixmapPasion))


        #tabWidget = QTabWidget()
        #tab1 = QWidget()
        #tab2 = QWidget()
        vertical = QVBoxLayout()
        vertical.addSpacing(15)
        title = "Passion Studio Tools "
        if MODE == 'dev':
            title += MODE
        frame = PQTitleBar(self, title)
        frame.setObjectName('launcherAppFrame')
        frame.setLayout(vertical)
        frame.setFrameStyle(QFrame.NoFrame)
        self.setCentralWidget(frame)


        # launchers
        buttonsGroup = QGroupBox('Software')
        vertical.addWidget( buttonsGroup)

        buttonsGrid = GridLayout(rows=2, cols=4)
        buttonsGroup.setLayout( buttonsGrid)

        iconsize = QSize(96, 96)
        self.appLayouts = {}

        for package in WORKGRP['default']['order']:
            if package in APPS and APPS[package]['show']:
                self.appLayouts[package] = QPushButton((package+' '+WORKGRP['default']['packages'][package]['version']))
                self.appLayouts[package].setIcon(QIcon(os.path.join(RES, (package+".png"))))
                self.appLayouts[package].setIconSize(iconsize)
                self.connect(self.appLayouts[package], SIGNAL("clicked()"), self.launchApp)
                buttonsGrid.addWidgetAuto(self.appLayouts[package])

                # launchers
        utilsGroup = QGroupBox('Utilities')
        vertical.addWidget( utilsGroup)
        utilsGrid = GridLayout(rows=1, cols=8)
        utilsGroup.setLayout( utilsGrid)

        self.utilLayouts = {}

        for package in UTILITIES:
            if UTILITIES[package]['show']:
                self.utilLayouts[package] = QPushButton(package)
                self.utilLayouts[package].setIcon(QIcon(os.path.join(RES, (package+".png"))))
                self.utilLayouts[package].setIconSize(iconsize)
                self.connect(self.utilLayouts[package], SIGNAL("clicked()"), self.launchUtil)
                utilsGrid.addWidgetAuto(self.utilLayouts[package])



    def launchApp (self, app=None, version=None):

        sender = self.sender()
        if not version:
            version = 0
        for name, button in self.appLayouts.iteritems():
            if sender == button:
                app = name
                version = WORKGRP['default']['packages'][app]['version']

        print ("Launching "+app+" version: "+version)

        if APPS[app]:
            if version in APPS[app]['versions']:
                process_env = None
                process_env = StudioEnvironment()
                process_env.load_workgroup_config_file(filepath=(CONFIG+'/workgroups.yml'), workgroup='default', app=app)
                process_env.printout()
                executable = os.path.join(APPS[app]['versions'][version]['path'][sys.platform], APPS[app]['versions'][version]['modes']['ui'][sys.platform])
                executable = process_env.expandvars(executable)
                print executable
                env = dict(os.environ.items() + self.studioenv.vars.items() + process_env.vars.items())
                Popen(executable, env=env)

        return

    def launchUtil (self, util=None, version=None):
        sender = self.sender()

        for name, button in self.utilLayouts.iteritems():
            if sender == button:
                util = name
                version = UTILITIES[util]['versions'].keys()[0]

        executable = os.path.join(UTILITIES[util]['versions'][version]['path'][sys.platform], UTILITIES[util]['versions'][version]['modes']['ui'][sys.platform])
        print executable
        env = dict(os.environ.items() + self.studioenv.vars.items())
        Popen(executable, env=env)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = Launcher()
    wind.setWindowTitle(('Passion Studio Tools -'+MODE))
    wind.show()
    app.exec_()