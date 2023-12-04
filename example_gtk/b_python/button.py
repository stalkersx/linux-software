#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="Button")
				Gtk.Window.set_default_size(self, 50, 50)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create button
				btn1 = Gtk.Button()
				btn1.set_label("tombol")
				btn1.connect("clicked", self.clickbtn2)
				
				# add to window
				self.add(btn1)
				
		# methods click button outside super methods
		def clickbtn2(self, button):
				print("wellcome")
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
