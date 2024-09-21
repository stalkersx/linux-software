#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="Radio Button")
				Gtk.Window.set_default_size(self, 200, 30)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create box
				hbox = Gtk.Box(spacing=3)
				
				# create button radio
				btn1 = Gtk.RadioButton.new_with_label_from_widget(None, "tombol 1")
				btn2 = Gtk.RadioButton.new_from_widget(btn1)
				btn2.set_label("tombol 2")
				btn2.set_active("is active")
				btn3 = Gtk.RadioButton.new_with_mnemonic_from_widget(btn1, "tombol 3")
				
				# action click button radio
				btn1.connect("toggled", self.click_toggled, "1")
				btn2.connect("toggled", self.click_toggled, "2")
				btn3.connect("toggled", self.click_toggled, "3")
				
				# put button radio to box
				hbox.pack_start(btn1, False, False, 0)
				hbox.pack_start(btn2, False, False, 0)
				hbox.pack_start(btn3, False, False, 0)
				
				# add box
				self.add(hbox)
				
		def click_toggled(self, button, name):
				if button.get_active():
						state = "on"
				else:
						state = "off"
				print("button", name, "was turn", state)
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
