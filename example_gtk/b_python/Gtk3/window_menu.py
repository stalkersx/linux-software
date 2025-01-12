#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()
win.set_title("menu")
win.set_default_size(600, 400)
win.set_position(Gtk.WindowPosition.CENTER)

def method(widget) :
	print("oke")
	
# item icon
img = Gtk.Image()
img.set_from_stock(Gtk.STOCK_NEW, 1)
itm1 = Gtk.ImageMenuItem("facebook")
itm1.set_image(img)
itm1.connect("activate", method)

# menu bar
ms = Gtk.MenuItem("Apps")
mn = Gtk.Menu()
mn.append(itm1)
ms.set_submenu(mn)
mb = Gtk.MenuBar()
mb.append(ms)
ms1 = Gtk.MenuItem("settings")
ms1.connect("activate", method)
mb.append(ms1)

vbox = Gtk.VBox()
vbox.pack_start(mb, False, False, 0)

win.add(vbox)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
