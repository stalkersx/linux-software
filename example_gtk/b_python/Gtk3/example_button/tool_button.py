#!/bin/python

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create class window
class window(Gtk.Window):
		def __init__(self):
				Gtk.Window.__init__(self, title="Tool Button")
				Gtk.Window.set_default_size(self, 300, 300)
				Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
				
				# toolbutton
				self.btn1 = Gtk.ToolButton(Gtk.STOCK_ADD)
				self.btn1.connect('clicked', self.click)
				btn2 = Gtk.ToolButton(Gtk.STOCK_CLOSE)
				btn4 = Gtk.ToolButton(Gtk.STOCK_HOME)
				btn5 = Gtk.ToolButton(Gtk.STOCK_FIND)
				btn6 = Gtk.ToolButton(Gtk.STOCK_GO_DOWN)
				btn7 = Gtk.ToolButton(Gtk.STOCK_GO_UP)
				btn8 = Gtk.ToolButton(Gtk.STOCK_GO_BACK)
				btn9 = Gtk.ToolButton(Gtk.STOCK_GO_FORWARD)
				btn10 = Gtk.ToolButton(Gtk.STOCK_REFRESH)
				
				# vbox
				vbox = Gtk.VBox()
				vbox.pack_start(self.btn1, False, False, 0)
				vbox.pack_start(btn2, False, False, 0)
				vbox.pack_start(btn4, False, False, 0)
				vbox.pack_start(btn5, False, False, 0)
				vbox.pack_start(btn6, False, False, 0)
				vbox.pack_start(btn7, False, False, 0)
				vbox.pack_start(btn8, False, False, 0)
				vbox.pack_start(btn9, False, False, 0)
				vbox.pack_start(btn10, False, False, 0)
				
				# add button
				self.add(vbox)
				
		def click(self, widget):
			print('good')
	
win = window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
