#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="Entry")
				Gtk.Window.set_default_size(self, 200, 30)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create entry
				en = Gtk.Entry() # contruktor
				#en.set_visibility(False) # hide text
				en.set_text("write text here ....") # create text default
				en.connect("activate", self.entry_text) # action text
				
				print(en.get_text()) # get text default or for button click
				
				self.add(en) # add entry
				
		def entry_text(self, text):
				print("input_entry : ", text.get_text()) # get text from entry
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
