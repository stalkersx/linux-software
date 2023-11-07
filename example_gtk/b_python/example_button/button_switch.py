#!/bin/python

# import module gtk
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="switch button")
				Gtk.Window.set_default_size(self, 200, 50)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create box
				hbox = Gtk.Box(spacing=2)
				
				# create button switch
				bs1 = Gtk.Switch()
				bs1.set_active(True) # start first on
				bs2 = Gtk.Switch()
				bs2.set_active(False) # start first off
				
				# create action click button switch
				bs1.connect("notify::active", self.clickswitchleft)
				bs2.connect("notify::active", self.clickswitchright)
				
				# put button switch to box
				hbox.pack_start(bs1, True, True, 0)
				hbox.pack_start(bs2, True, True, 0)
				
				# add box
				self.add(hbox)
				
		def clickswitchleft(self, switch, gparam):
				# percabangan on of
				if switch.get_active():
						print("left switch is turn on ")
				else:
						print("left switch is turn off")
						
		def clickswitchright(self, pilih, onoff):
				if pilih.get_active():
						print("right switch is turn on")
				else:
						print("right switch is turn off")
						
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
