import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Element():
    def __init__(self, s, n, nu, m):
        self.symbol = s
        self.name = n
        self.number = nu
        self.mass = m

elements = [
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [Element('He', 'Helium', '2', '4.0026')], 
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [Element('He', 'Helium', '2', '4.0026')],
           ]

class PeriodicTable(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        grid = Gtk.Grid()
        self.add(grid)
        
        for y in range(0, 9):
            for x in range(0, 18):
                

    def on_button_clicked(self, widget):
        print("Hello World")

win = PeriodicTable()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()