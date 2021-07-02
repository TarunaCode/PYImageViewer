#/usr/bin/env python3


#: main script for bootable-maker program
#: Copyright TarunaCode(C) 2020-2021
#:
#: This Program is free software: you can redistribute it and/or modify
#: it under terms of the GNU General Public License as published by
#: Free Software Foundation , either version 3 of the License, or
#: (at your option) any later version
#:
#:
#: This program is distributed in the hope that it will be useful,
#: but WITHOUT ANY WARRANTY; without even the implied warranty of
#: MERCHANTIBILTY or FITNESS FOR A PARTICULAR PURPOSE.   See the
#: GNU General Public License for more details
#:
#: You should have received a copy of the GNU General Public License
#: along with this program. If not, see <https://www.gnu.org/licenses/>
#:
#:
#:          <Maintained Under>
#:   Maulana B. <https://github.com/floppvs
import gi
gi.require_version('Gtk','3.0')

from gi.repository import Gtk as g


class xwindow(g.Window):
    def __init__(self,name,brdr):
        self.name = name
        self.brdr = brdr
        super(xwindow,self).__init__()
        self.init_ui()

    def init_ui(self):
        self.set_border_width(self.brdr)
        image = g.Image()
        image.set_from_file(self.name)
        self.add(image)
        self.set_title("ImageViewer")
        self.connect("destroy",g.main_quit)

class XFChooser(g.Window):
    def __init__(self,maintitle,brdr):
        self.maintitle = maintitle
        g.Window.__init__(self,title=maintitle)

        box = g.Box(spacing=8)
        self.add(box)

        tmbl = g.Button(label="Select File")
        tmbl.connect("clicked",self.file)

        box.add(tmbl)
        tmbl2 = g.Button(label="Select Folder")
        tmbl2.connect("clicked",self.folder)

        box.add(tmbl2)

        tmbl_keluar = g.Button(label="Exit")
        tmbl_keluar.connect("clicked",g.main_quit)

        box.add(tmbl_keluar)
    def file(self,wg):
        x = g.FileChooserDialog(
            title="Please Choose A file",
            parent=self,
            action=g.FileChooserAction.OPEN
        )
        x.add_buttons(
            g.STOCK_CANCEL,
            g.ResponseType.CANCEL,
            g.STOCK_OPEN,
            g.ResponseType.OK,
        )
        self.file_filter(x)

        respon = x.run();

        if respon == g.ResponseType.OK:
            print("File: "+x.get_filename())
            win = xwindow(x.get_filename(),5)
            win.show_all()
            g.main()
        elif respon == g.ResponseType.CANCEL:
            print("Ga jadi")
        x.destroy()

    def ViewImage(self,flnm):
        self.set_border_width(5)
        foto = g.Image()

        foto.set_from_file(flnm)

        self.add(foto)
        self.set_title(self.maintitle)
        self.connect("destroy",g.main_quit)

    def folder(self,wg):
        x = g.FileChooserDialog(
            title="Please Choose A folder",
            parent=self,
            action=g.FileChooserAction.SELECT_FOLDER

        )
        x.add_buttons(
            g.STOCK_CANCEL,
            g.ResponseType.CANCEL,
            "Select"
        )
        x.set_default_size(800,400)

        respon = x.run();
        if respon == g.ResponseType.OK:
            print("File: "+x.get_filename())
        elif respon == g.ResponseType.CANCEL:
            print("Ga Jadi")
        x.destroy()
    def file_filter(self,x):
        ftext = g.FileFilter()
        ftext.set_name("All Files")
        ftext.add_pattern("*.png")
        x.add_filter(ftext)



xwin = XFChooser("ImageViewer V1",5)
xwin.connect("destroy",g.main_quit)
xwin.show_all()
g.main()

# [2021/07/02->19:45] : beres v1 xixiixixixixix
