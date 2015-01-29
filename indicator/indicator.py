#!/usr/bin/env python

"""
Python indicator applet to show the status of batch git

Currently displays a 'tick' if no repositories are ahead of master and an 
upload symbol otherwise.

Icons provided by 

<div>Icons made by <a href="http://www.icons8.com" title="Icons8">Icons8</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a>         is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0">CC BY 3.0</a></div>

"""

# Python 2.7.x standard library imports
import subprocess
import os
import sys
import inspect

sys.tracebacklimit=0

try:
    import pygtk
    pygtk.require('2.0')
    import gobject
    import gtk
except ImportError:
    raise ImportError(
    "The python package gobject required for the batchgit indicator\n"
    "is not installed. To install you may use\n\n"
    "    apt-get install python-gobject\n")
except AssertionError:
    raise ImportError(
    "The python package gtk2 required for the batchgit indicator\n"
    "is not installed. To install you may use\n\n"
    "    apt-get install python-gtk2\n")

try:
    import appindicator
except ImportError:
    raise ImportError(
    "The python package appindicator required for the batchgit indicator\n"
    "is not installed. To install you may use\n\n"
    "    apt-get install python-appindicator\n")


RCFILENAME = ".batchgitrc"
CONFIGFILENAME = "/.config"
this_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def ReadConfigFile():
    _file = this_dir + CONFIGFILENAME
    config = {}
    with open(_file, "r") as f:
        for line in f:
            [key, value] = line.split(":")
            key = key.replace(" ", "")
            value = value.replace(" ", "").rstrip("\n")
            config[key] = value
    return config

def WriteDefaultConfig():
    _file = this_dir + CONFIGFILENAME
    with open(_file, "w+") as f:
        f.write(
"""theme : light
update_period : 100
""")

def GetIconsNames(config):
    theme = config['theme']
    config['ahead_icon'] = this_dir + "/Icons/" + "upload62_{}.svg".format(theme)
    config['synced_icon'] = this_dir + "/Icons/" + "checkmark6_{}.svg".format(theme)
    return config


class AppIndicator:
    def __init__(self, config):

        self.dirs = config['dirs']
        self.ahead_icon = config['ahead_icon']
        self.synced_icon = config['synced_icon']

        self.ind = appindicator.Indicator("GitCheck", 
                                     "",
                                     appindicator.CATEGORY_APPLICATION_STATUS)

        self.ind.set_status (appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon ("indicator-messages-new")


        # create a menu
        menu = gtk.Menu()
        Check = gtk.MenuItem("Check if any directories are ahead")
        Check.connect("activate", lambda s: self.SetIcon())
        Check.show()
        menu.append(Check)

        dirs_items = []
        for dir in self.dirs:
            item = gtk.CheckMenuItem(dir)
            item.set_active(True)
            item.show()
            menu.append(item)
            dirs_items.append(item)

        self.dirs_items = dirs_items

        quit = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        quit.connect("activate", self.quit)
        quit.show()
        menu.append(quit)

        self.ind.set_menu(menu)

        self.SetIcon() # Initialise the icon
        
        gobject.timeout_add_seconds(10, self.SetIcon)
        gtk.threads_init()     

    def IsAhead(self, path):
        path = path.rstrip("/") + "/"
        cmd_line = "git --git-dir={}.git --work-tree={} status".format(path, path)
        status = subprocess.check_output(cmd_line, shell=True)
        if "ahead" in status:
            return True
        else:
            return False

    def CheckStatus(self):
        s = []
        for (dir, list_item) in zip(self.dirs, self.dirs_items):
            if list_item.active:
                s.append(self.IsAhead(dir))
        return any(s)
            
    def SetIcon(self):
        Status = self.CheckStatus()
        if Status:
            self.ind.set_icon(self.ahead_icon)
        else:
            self.ind.set_icon(self.synced_icon)
        return True

    def quit(self, widget, data=None):
        gtk.main_quit()

if __name__ == "__main__":

    if not os.path.isfile(this_dir + CONFIGFILENAME):
        WriteDefaultConfig()
    config = ReadConfigFile()

    config = GetIconsNames(config)

    rcfile = os.path.expanduser("~") + "/" + RCFILENAME
    if os.path.isfile(rcfile):
        dirs = []
        with open(rcfile, "r") as f:
            for line in f:
                dirs.append(line.rstrip("\n"))

        config['dirs'] = dirs

        indicator = AppIndicator(config)

        gtk.main()
    


