#!/bin/python3

# import module gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def go_clicked(widget):
    print("ok")

# entry
addr_bar = Gtk.Entry()
addr_bar.set_hexpand(True)

# button
back_button = Gtk.Button(label="Back")
forward_button = Gtk.Button(label="forward")
go_button = Gtk.Button(label="Go")
go_button.connect("clicked", go_clicked)
refresh_btn = Gtk.Button(label="Refresh")
stop_btn = Gtk.Button(label="stop")
progress = Gtk.ProgressBar()
spin = Gtk.Spinner()

# grid
grid = Gtk.Grid()
grid.attach(back_button, 0, 0, 1, 1)
grid.attach(forward_button, 1, 0, 1, 1)
grid.attach(addr_bar, 2, 0, 1, 1)
grid.attach(go_button, 3, 0, 1, 1)
grid.attach(refresh_btn, 4, 0, 1, 1)
grid.attach(stop_btn, 5, 0, 1, 1)
grid.attach(progress, 0, 2, 5, 1)
grid.attach(spin, 5, 2, 1, 1)

# open window
win = Gtk.Window()
win.set_title("judul")
#win.set_icon_from_file("/usr/share/icons/hicolor/scalable/apps/tf_logo.svg")
win.set_position(Gtk.WindowPosition.CENTER)
win.set_default_size(600, 400)
win.add(grid)

# close window
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
