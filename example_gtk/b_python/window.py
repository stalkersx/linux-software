#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="judul")
				Gtk.Window.set_default_size(self, 300, 150)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				#Gtk.Window.set_position(self, Gtk.WindowPosition.MOUSE)
				
win = window()
#win.set_icon_from_file(loci + image)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
