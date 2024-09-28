#!/bin/python

# import module gtk
import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

# pixbuf
pb1 = Pixbuf.new_from_file_at_scale(filename='logo.png', width=30, height=30, preserve_aspect_ratio=True)

# image
img1 = Gtk.Image()
img1.set_from_pixbuf(pb1)

# button
btn = Gtk.Button('tombol 1')
btn.set_image(img1)

# window
win = Gtk.Window()
win.set_default_size(300, 300)
win.set_title('button image')
win.connect('delete-event', Gtk.main_quit)
win.add(btn)
win.show_all()
Gtk.main()
