import csv

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PeriodicTable(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        
        grid = Gtk.Grid()
        self.notebook.append_page(grid, Gtk.Label(label='Periodic Table'))
        
        self.elements = []
        self.pagenumbers = {}
        
        with open('PTable.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.elements.append(row)
        
        
        for element in self.elements:
            if(element['Group'].isdigit()):
                # button = Gtk.Button(label='')
                # grid.attach(button, int(element['Group']), int(element['Period']), 1, 1)
                
                box = Gtk.VBox()
                
                number = Gtk.Label(label=element['AtomicNumber'])
                name = Gtk.Label(label=element['Element'])
                symbol = Gtk.Label(label=element['Symbol'])
                mass = Gtk.Label(label=element['AtomicMass'])
                
                box.add(number)
                box.add(symbol)
                box.add(name)
                box.add(mass)
                
                button = Gtk.ToggleButton()
                button.add(box)
                button.connect("toggled", self.on_element_toggled, int(element['AtomicNumber']))
                
                grid.attach(button, int(element['Group']), int(element['Period']), 1, 1)

        
        grid.set_row_homogeneous(True)
        grid.set_column_homogeneous(True)
        grid.set_row_spacing(3)
        grid.set_column_spacing(3)
    
    def on_element_toggled(self, widget, number):
        if widget.get_active():
            box = Gtk.VBox()
            box.add(Gtk.Label(label="test"))
            self.notebook.append_page(box, Gtk.Label(label=self.elements[number]['Symbol']))
        else:
            self.notebook.remove(pagenumbers[number]
        self.show_all()

win = PeriodicTable()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()