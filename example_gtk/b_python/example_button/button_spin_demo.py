#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="judul")
				Gtk.Window.set_default_size(self, 200, 30)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# create box
				hbox = Gtk.Box(spacing=6)
				
				# create spin button
				adjustment = Gtk.Adjustment(upper=100, step_increment=1, page_increment=10)
				self.sb = Gtk.SpinButton()
				self.cn = Gtk.CheckButton(label="Numeric")
				self.ci = Gtk.CheckButton(label="if valid")
				self.sb.set_adjustment(adjustment)
				
				# action spin button
				self.sb.connect("value-changed", self.click_value_change)
				self.cn.connect("toggled", self.click_numeric_toggled)
				self.ci.connect("toggled", self.click_ifvalid_toggled)
				
				# put spin button to box
				hbox.pack_start(self.sb, False, False, 0)
				hbox.pack_start(self.cn, False, False, 0)
				hbox.pack_start(self.ci, False, False, 0)
				
				# add
				self.add(hbox)
				
		def click_value_change(self, scroll):
				print(self.sb.get_value_as_int())
				
		def click_numeric_toggled(self, button):
				self.sb.set_numeric(button.get_active())
				
		def click_ifvalid_toggled(self, button):
				if button.get_active():
						policy = Gtk.SpinButtonUpdatePolicy.IF_VALID
				else:
						policy = Gtk.SpinButtonUpdatePolicy.ALWAYS
				self.sb.set_update_policy(policy)
				
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
