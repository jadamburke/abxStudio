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
import core.project

class Launcher(QMainWindow):

    studioenv = StudioEnvironment()
    os.environ['QT_AUTO_SCREEN_SCALE_FACTOR '] = 'TRUE'

    def __init__(self, parent=None):

        super(Launcher, self).__init__(parent)
        self.updategui = False
        self.resize(900, 800)

        # create a studio environment
        self.studioenv.load_app_config_file(CONFIG+'/app.yml', app='studiotools', version='1.0')
        self.studioenv.setEnv()
        self.studioenv.printout()
        QPixmapCache.setCacheLimit(20480)

        self.updateUi()

    def updateUi(self):

        sStyleSheet = StyleSheet().styleSheet(1)
        self.setStyleSheet(sStyleSheet)

        self.setWindowFlags( Qt.FramelessWindowHint )
        pixmapIcon = QPixmap(os.path.join( RES, "pink.ico"))
        self.setWindowIcon(QIcon(pixmapIcon))

        iconsize = QSize(48,48)


        vertical = QVBoxLayout()
        vertical.addSpacing(15)
        title = "Studio Launcher"
        if MODE == 'dev':
            title += MODE
        frame = PQTitleBar(self, title)
        frame.setObjectName('launcherAppFrame')
        frame.setLayout(vertical)
        frame.setFrameStyle(QFrame.NoFrame)
        self.setCentralWidget(frame)

        splitter = QSplitter()
        vertical.addWidget(splitter)

        vertical = QVBoxLayout()

        # setup sidebar
        self.sidebar_list = QListWidget()
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar)

        #WORKGROUP######
        workgroup_label = QLabel("MAIN")
        self.sidebar_layout.addWidget(workgroup_label)
        self.sidebar_layout.addWidget(self.sidebar_list)
        splitter.addWidget(self.sidebar)

        self.stack_widget = QStackedWidget()

        splitter.addWidget(self.stack_widget)

        sidebarItems = ['Apps','Projects','Workgroups']
        self.stack_layouts = {}
        i = 0
        for package in sidebarItems:
            package = package.title()
            item = QListWidgetItem(package)
            item.setIcon(QIcon(os.path.join(RES, ("list_"+package+".png"))))
            self.sidebar_list.addItem(item)
            self.stack_layouts[package] = QWidget()
            self.stack_widget.addWidget(self.stack_layouts[package])
            self.stack_layouts[package].page_index = i
            i+=1

        #self.connect(self.sidebar_list, SIGNAL("itemClicked()"), self.stackChange)
        self.sidebar_list.itemClicked.connect(self.stackChange)



        tab1_layout = QVBoxLayout(self.stack_layouts['Apps'])
        tab2_layout = QVBoxLayout(self.stack_layouts['Projects'])
        tab3_layout = QVBoxLayout(self.stack_layouts['Workgroups'])
        # launchers
        buttonsGroup = QGroupBox('Software')
        tab1_layout.addWidget( buttonsGroup)

        buttonsGrid = GridLayout(rows=3, cols=3)
        buttonsGroup.setLayout( buttonsGrid)

        iconsize = QSize(96, 96)
        self.appLayouts = {}

        for package in WORKGRP['default']['order']:
            if package in APPS and APPS[package]['show']:
                #self.appLayouts[package] = QPushButton((package+' '+WORKGRP['default']['packages'][package]['version']))
                self.appLayouts[package] = QPushButton('')

                #pixmap caching
                value = os.path.join(RES, (package+".png"))
                key = "image:%s"% value
                pixmap = QPixmap()
                if not QPixmapCache.find(key, pixmap): # loads pixmap from cache if its not already loaded
                    pixmap = QPixmap(value)
                    QPixmapCache.insert(key, pixmap)

                icon = QIcon(pixmap)
                self.appLayouts[package].setIcon(icon)
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
                self.utilLayouts[package] = PicButton(label=package, pixmap=QPixmap(os.path.join(RES, (package+".png"))))
                #self.utilLayouts[package].setIcon(QPixmap(os.path.join(RES, (package+".png"))))
                #self.utilLayouts[package].setIconSize(iconsize)
                self.connect(self.utilLayouts[package], SIGNAL("clicked()"), self.launchUtil)
                utilsGrid.addWidgetAuto(self.utilLayouts[package])

        jobsListBox = QListWidget()
        jobsList = core.project.list_jobs('jobs')
        for j in jobsList:
            jobsListBox.addItem(j)
        tab2_layout.addWidget(jobsListBox)




    def stackChange (self):
        sender = self.sender()
        page = str(sender.currentItem().text())
        self.stack_widget.setCurrentIndex(self.stack_layouts[page].page_index)



    def launchApp (self, app=None, version=None):

        sender = self.sender()
        if not version:
            version = 0
        for name, button in self.appLayouts.iteritems():
            if sender == button:
                app = name
                version = WORKGRP['default']['packages'][app]['version']

        print ("Launching "+app+" version: "+version)

        # launch the process
        if APPS[app]:
            if version in APPS[app]['versions']:

                # load the process env from the config files
                process_env = StudioEnvironment()
                # load the 'default' workgroup, this is hardcoded for now but will be adjustable in future UI
                process_env.load_workgroup_config_file(filepath=(CONFIG+'/workgroups.yml'), workgroup='default', app=app)
                process_env.printout()
                executable = os.path.join(APPS[app]['versions'][version]['path'][sys.platform], APPS[app]['versions'][version]['modes']['ui'][sys.platform])
                # expand any env variables in pathnames before running the process
                executable = process_env.expandvars(executable)

                # create any necessary user variable folders if they don't exist
                process_env.make_user_folders()

                print executable
                env = dict(os.environ.items() + self.studioenv.vars.items() + process_env.vars.items())
                try:
                    Popen(executable, env=env)
                except:
                    print (executable + " failed to open. Does it Exist?")

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
    wind.setWindowTitle(('Studio Tools -'+MODE))
    wind.show()
    app.exec_()