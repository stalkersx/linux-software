#!/bin/python

# import module gtk
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="judul")
				Gtk.Window.set_default_size(self, 300, 150)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create button link
				btn1 = Gtk.LinkButton.new_with_label(uri="https://www.mylink.org", label="Visit My First Apps")
				
				# add button
				self.add(btn1)
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
