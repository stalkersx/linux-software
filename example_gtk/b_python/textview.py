#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="TextView")
				Gtk.Window.set_default_size(self, 100, 50)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create textview 1
				textview1 = Gtk.TextView() # contruktor
				textview1.set_editable(False) # edit text
				textview1.set_cursor_visible(False) # garis tulis
				textview1.get_buffer().set_text("hello world !") # write text.
				
				# add
				self.add(textview1)
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
