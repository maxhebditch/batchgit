#!/usr/bin/env python

"""
Python indicator applet to show the status of batch git

Currently displays a 'tick' if no repositories are ahead of master and an 
upload symbol otherwise.

Icons provided by 

<div>Icons made by <a href="http://www.icons8.com" title="Icons8">Icons8</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a>         is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0">CC BY 3.0</a></div>

"""

import pygtk
pygtk.require('2.0')
import gtk
import appindicator
import subprocess
import os, inspect

RCFILENAME = ".batchgitrc"

this_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
AHEAD_ICON = this_dir + "/Icons/" + "upload62_white.svg"
SYNC_ICON = this_dir + "/Icons/" + "checkmark6_white.svg"

class AppIndicator:
    def __init__(self, dirs):
        self.dirs = dirs
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

        gtk.main()

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
            self.ind.set_icon(AHEAD_ICON)
        else:
            self.ind.set_icon(SYNC_ICON)

    def quit(self, widget, data=None):
        gtk.main_quit()

if __name__ == "__main__":

    rcfile = os.path.expanduser("~") + "/" + RCFILENAME
    if os.path.isfile(rcfile):
        dirs = []
        with open(rcfile, "r") as f:
            for line in f:
                dirs.append(line.rstrip("\n"))

        indicator = AppIndicator(dirs)
    


