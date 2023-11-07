#!/bin/python

# import module gtk
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="judul")
				Gtk.Window.set_default_size(self, 300, 150)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
