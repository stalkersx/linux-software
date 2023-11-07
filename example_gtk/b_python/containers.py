#!/bin/python

# import module gtk
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="Containers")
				Gtk.Window.set_default_size(self, 300, 150)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create button
				btn1 = Gtk.Button("Tombol 1")
				btn2 = Gtk.Button("Tombol 2")
				btn3 = Gtk.Button("Tomboo 3")
				btn4 = Gtk.Button("Tombol 4")
				
				# create containers
				con = Gtk.Layout()
				con.put(btn1, 0, 0)
				con.put(btn2, 10, 30)
				con.put(btn3, 20, 60)
				con.put(btn4, 30, 90)
				
				# add containers
				self.add(con)
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
