#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="box")
				Gtk.Window.set_default_size(self, 300, 150)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create box
				vbox = Gtk.Box.new(Gtk.Orientation.VERTICAL, 8) # box vertical
				vbox.set_spacing(3) # jumblah isi box
				hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 8) # box horizontal
				hbox.set_spacing(2)
				
				# create button
				btn1 = Gtk.Button("tombol 1")
				btn2 = Gtk.Button("tombol 2")
				btn3 = Gtk.Button("tombol 3")
				btn4 = Gtk.Button("tombol 4")
				
				# put button to box
				vbox.pack_start(btn1, True, True, 0)
				vbox.pack_start(btn2, True, True, 0)
				hbox.pack_start(btn3, True, True, 0)
				hbox.pack_start(btn4, True, True, 0)
				vbox.pack_start(hbox, True, True, 0)
				
				# add
				self.add(vbox)
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
