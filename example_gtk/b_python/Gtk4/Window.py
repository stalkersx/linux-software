#!/bin/python3

# import module
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def on_activate(app):
  win = Gtk.ApplicationWindow(application=app)
  win.set_title("myapp")
  win.set_default_size(600, 400)
  #win.set_child(web)
  win.present()

app = Gtk.Application()
app.connect('activate', on_activate)
app.run(None)

