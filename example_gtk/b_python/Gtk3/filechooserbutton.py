#!/bin/python3

# import module gtk
import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# fungsi button click
def on_file_selected1(widget) :
    print(widget.get_filename())
def on_folder_selected2(widget) :
    print(widget.get_filename())
def on_folder_selected3(widget) :
    print(widget.get_filename())

# filter hanya menampilkan folder
filter_directory = Gtk.FileFilter()
filter_directory.set_name("folder")
filter_directory.add_mime_type("inode/directory")

# pilih file
chooserfile1 = Gtk.FileChooserButton("Open File")
chooserfile1.set_action(Gtk.FileChooserAction.OPEN)
chooserfile1.connect("selection-changed", on_file_selected1)

# pilih folder
chooserfile2 = Gtk.FileChooserButton("Open Folder")
chooserfile2.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
chooserfile2.add_filter(filter_directory)
chooserfile2.connect("selection-changed", on_folder_selected2)

# hbox
hbox1 = Gtk.HBox()
hbox1.pack_start(chooserfile1, False, False, 0)
hbox1.pack_start(chooserfile2, False, False, 0)

# open window
win = Gtk.Window()
win.set_title("FileChooserButton")
#win.set_icon_from_file("/usr/share/icons/hicolor/scalable/apps/tsa_logo.svg")
win.set_position(Gtk.WindowPosition.CENTER)
win.set_default_size(200, 20)
win.add(hbox1)

# close window
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
