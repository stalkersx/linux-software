#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="button checklis")
				Gtk.Window.set_default_size(self, 200, 30)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create hbox
				hbox = Gtk.Box(spacing=4)
				
				# create button checklis
				bc1 = Gtk.CheckButton(label="checklis 1")
				bc2 = Gtk.CheckButton(label="checklis 2")
				bc3 = Gtk.CheckButton(label="checklis 3")
				bc4 = Gtk.CheckButton(label="checklis 4")
				
				# action checklis
				bc1.connect("toggled", self.click_toggled)
				
				# put button checklis to box
				hbox.pack_start(bc1, True, True, 0)
				hbox.pack_start(bc2, True, True, 0)
				hbox.pack_start(bc3, True, True, 0)
				hbox.pack_start(bc4, True, True, 0)
				
				# add box
				self.add(hbox)
				
		def click_toggled(self, button):
				if button.get_active():
						print("active")
				else:
						print("nonactive")
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
