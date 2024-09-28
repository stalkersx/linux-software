#!/bin/python

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# array
item = Gtk.MenuItem('jeruk')
btn = Gtk.Button('tombol')

# listbox
listbox = Gtk.ListBox()
listbox.add(item)
listbox.add(btn)

# scroll
sc = Gtk.ScrolledWindow()
sc.add(listbox)

# window
win = Gtk.Window()
win.set_default_size(400, 400)
win.set_title('list box')
win.add(sc)
win.show_all()
win.connect('delete-event', Gtk.main_quit)
Gtk.main()
