#!/bin/python3

# import module gtk
import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import time
8
# progressbar
pb = Gtk.ProgressBar()
#pb.pulse()
pb.set_fraction(0.0)

# label
label = Gtk.Label()

#vbox
vbox = Gtk.VBox()
vbox.pack_start(pb, True, True, 0)
vbox.pack_start(label, True, True, 0)

#  open window
win = Gtk.Window()
win.set_title("Progress Bar")
#win.set_icon_from_file("/usr/share/icons/hicolor/scalable/apps/tf_logo.svg")
win.set_position(Gtk.WindowPosition.CENTER)
win.set_default_size(200, 30)
win.add(vbox)

# close window
win.connect("delete-event", Gtk.main_quit)
win.show_all()
for i in range(101) :
    pb.set_fraction(i/100)
    time.sleep(0.2)
    label.set_text(f"Loading... {i}%")
    while Gtk.events_pending():
        Gtk.main_iteration()
Gtk.main()