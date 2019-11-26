import csv

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PeriodicTable(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        
        grid = Gtk.Grid()
        self.add(grid)
        
        elements = []
        
        with open('PTable.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                elements.append(row)
        
        
        for element in elements:
            if(element['Group'].isdigit()):
                # button = Gtk.Button(label='')
                # grid.attach(button, int(element['Group']), int(element['Period']), 1, 1)
                
                box = Gtk.VBox()
                
                number = Gtk.Label(element['AtomicNumber'])
                name = Gtk.Label(element['Element'])
                symbol = Gtk.Label(element['Symbol'])
                mass = Gtk.Label(element['AtomicMass'])
                
                box.add(number)
                box.add(symbol)
                box.add(name)
                box.add(mass)
                
                button = Gtk.Button(label = None)
                button.add(box)
                button.connect("clicked", self.on_Element_Clicked)
                
                grid.attach(button, int(element['Group']), int(element['Period']), 1, 1)

        
        grid.set_row_homogeneous(True)
        grid.set_column_homogeneous(True)
        grid.set_row_spacing(3)
        grid.set_column_spacing(3)
    
    def on_Element_Clicked(self, widget):
        print(widget)

win = PeriodicTable()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()