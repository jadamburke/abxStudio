__author__ = 'adamb'

import sys,os
from settings import *
import yaml
import re

class StudioEnvironment():



    def __init__ (self):
        self.vars = {}
        return


    def load_app_config_file(self, filepath, app, version):
        dataMap = self.get_config_file(filepath)
        self.load_app_config(dataMap, app, version)

    def load_module_config_file(self, filepath, module, version):
        dataMap = self.get_config_file(filepath)
        self.load_module_config(dataMap, module, version)

    def load_workgroup_config_file(self, filepath, workgroup=None, app=None):
        dataMap = self.get_config_file(filepath)
        self.load_workgroup_config(dataMap, workgroup, app)

    def get_config_file(self,filepath):
        f = open(filepath)
        # use safe_load instead load
        dataMap = yaml.safe_load(f)
        f.close()
        return dataMap

    def load_app_config(self, dataMap, app='studiotools', version='1.0'):
        if app in dataMap:
            for key, value in dataMap.iteritems():
                if key == app:
                    if 'env' in dataMap[key]:
                        for var, val in dataMap[key]['env'].iteritems():
                            self.add(var, val)
                    if 'versions' in dataMap[key]:
                        if version in dataMap[key]['versions']:
                            if 'env' in dataMap[key]['versions'][version]:
                                for var, val in dataMap[key]['versions'][version]['env'].iteritems():
                                    self.add(var, val)

        #if dataMap[]
        self.parse_subst()
        return

    def load_module_config(self, dataMap, module, version):
        print ("loading module: "+module+","+version)
        if module in dataMap:
            for key, value in dataMap.iteritems():
                if key == module:
                    # add module env vars
                    if 'env' in dataMap[key]:
                        for var, val in dataMap[key]['env'].iteritems():
                            self.add(var, val)
                    # add module/package env vars
                    if 'packages' in dataMap[key]:
                        for app, data in dataMap[key]['packages'].iteritems():
                            if 'env' in dataMap[key]['packages'][app]:
                                for var, val in dataMap[key]['packages'][app]['env'].iteritems():
                                    self.add(var, val)
                            if 'versions' in dataMap[key]['packages'][app]:
                                if version in dataMap[key]['packages'][app]['versions']:
                                    if 'env' in dataMap[key]['packages'][app]['versions'][version]:
                                        for var, val in dataMap[key]['packages'][app]['versions'][version]['env'].iteritems():
                                            self.add(var, val)

        #if dataMap[]
        self.parse_subst()
        self.parse_subst()
        self.parse_subst()
        return

    def load_workgroup_config(self, dataMap, workgroup=None, app=None):
        if workgroup in dataMap:
            for key, value in dataMap.iteritems():
                if key == workgroup:
                    # add module env vars
                    if 'env' in dataMap[key]:
                        for var, val in dataMap[key]['env'].iteritems():
                            self.add(var, val)
                    # add module/package env vars
                    if 'packages' in dataMap[key]:
                        for package, data in dataMap[key]['packages'].iteritems():
                            if app == None or package == app:
                                if 'env' in dataMap[key]['packages'][package]:
                                    for var, val in dataMap[key]['packages'][package]['env'].iteritems():
                                        self.add(var, val)
                                if 'version' in dataMap[key]['packages'][package]:
                                    self.load_app_config(dataMap=APPS, app=package, version=dataMap[key]['packages'][package]['version'])
                                if 'modules' in dataMap[key]['packages'][package]:
                                    for m, mv in dataMap[key]['packages'][package]['modules'].iteritems():
                                        self.load_module_config(dataMap=MODULES, module=m, version=mv)
                                        if 'env' in dataMap[key]['packages'][app]['modules']:
                                            for var, val in dataMap[key]['packages'][package]['modules']['env'].iteritems():
                                                self.add(var, val)

        #if dataMap[]
        self.parse_subst()
        self.parse_subst()
        self.parse_subst()

    def write_to_bat(self, output_path):
        return

    def write_to_shellscript(self, output_path):
        return

    def add(self, var, val):

        #if adding to an existing var then add the val to the original value, else just add it
        if var in self.vars:
            self.vars[var] += (';'+val)
        else:
            self.vars[var] = val
        #os.environ[var] = self.vars[var]

    def setEnv(self):

        for var, value in self.vars.iteritems():
            os.environ[var] = value

    def parse_subst(self):
        trashvars = []
        for var, val in self.vars.iteritems():
            var_subst = re.search('%(.+?)%', var)
            if var_subst:
                if var_subst.group(1) in self.vars:
                    trashvars.append(var)
                    var = var.replace(('%'+var_subst.group(1)+'%'), self.vars[var_subst.group(1)])
                if var_subst.group(1) in os.environ:
                    trashvars.append(var)
                    var = var.replace(('%'+var_subst.group(1)+'%'), os.environ[var_subst.group(1)])

            # check if any string substitution is needed in the value
            val_subst = re.search('%(.+?)%', val)
            if val_subst:
                if val_subst.group(1) in self.vars:
                    val = val.replace(('%'+val_subst.group(1)+'%'), self.vars[val_subst.group(1)])
                if val_subst.group(1) in os.environ:
                    val = val.replace(('%'+val_subst.group(1)+'%'), os.environ[val_subst.group(1)])
            self.vars[var] = val
            #os.environ[var] = val

            #remove old junk var names that were substituted therefore changed to a new var name
            for key in trashvars:
                del self.vars[key]
                #del os.environ[key]

    def expandvars(self,path):

        # expand any local var as well as previosly declared system environtment vars
        var_subst = re.search('%(.+?)%', path)
        if var_subst:
            if var_subst.group(1) in self.vars:
                path = path.replace(('%'+var_subst.group(1)+'%'), self.vars[var_subst.group(1)])
            if var_subst.group(1) in os.environ:
                path = path.replace(('%'+var_subst.group(1)+'%'), os.environ[var_subst.group(1)])
        path = os.path.expandvars(path)
        return path

    def remove(self, var):
        del self.vars[var]
        #del os.environ[var]

    def printout(self):
        for key, value in self.vars.iteritems():
            print (key+'='+value)

