import csv
import configparser

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

config = configparser.ConfigParser()
config.read("config.ini")

settings = Gtk.Settings.get_default()
settings.set_property("gtk-application-prefer-dark-theme", config['DEFAULT']['Darkmode'] == 'True')

class PeriodicTable(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Periodic Table")
        
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
                
                number = Gtk.Label()
                number.set_markup("<span font_desc='11'>%s</span>" % element['AtomicNumber'])
                
                name = Gtk.Label()
                name.set_markup("<span font_desc='13'>%s</span>" % element['Element'])
                
                symbol = Gtk.Label()
                symbol.set_markup("<span font_desc='15'><b>%s</b></span>" % element['Symbol'])

                mass = Gtk.Label()
                mass.set_markup("<span font_desc='8'>%s</span>" % element['AtomicMass'])
                
                box.add(number)
                box.add(symbol)
                # box.add(name)
                box.add(mass)
                
                button = Gtk.ToggleButton()
                button.set_relief(Gtk.ReliefStyle.NONE)
                button.add(box)
                button.connect("toggled", self.on_element_toggled, int(element['AtomicNumber']))
                
                grid.attach(button, int(element['Group']), int(element['Period']), 1, 1)

        
        grid.set_row_homogeneous(True)
        grid.set_column_homogeneous(True)
        grid.set_row_spacing(3)
        grid.set_column_spacing(3)
    
    def on_element_toggled(self, widget, number):
        number -=1
        if widget.get_active():
            #populate page
            window = Gtk.ScrolledWindow()
            
            window.set_margin_top(10)
            window.set_margin_bottom(10)
            window.set_margin_start(10)
            window.set_margin_end(10)
            
            rows = Gtk.Grid()
            
            box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)
            
            header = Gtk.Label()
            header.set_markup("<b><span font_desc='36'>%(Element)s</span> </b> \n \n" % self.elements[number])
            header.set_justify(Gtk.Justification.FILL)
            
            gheader = Gtk.Label()
            gheader.set_markup("<b><span font_desc='20'>General Information: </span> </b>" % self.elements[number])
            gheader.set_halign(Gtk.Align.START)
            
            if(self.elements[number]["Radioactive"] == ""):
                self.elements[number]["Radioactive"] = "no"
            
            if(self.elements[number]["Natural"] == ""):
                self.elements[number]["Natural"] = "no"
            
            gcontent = Gtk.Label()
            gcontent.set_markup("<span font_desc='15'>Neutrons: %(NumberofNeutrons)s</span> \n"
                                "<span font_desc='15'>Electrons: %(NumberofShells)s</span> \n"
                                "<span font_desc='15'>Phase: %(Phase)s</span> \n"
                                "<span font_desc='15'>Radioactive: %(Radioactive)s</span> \n"
                                "<span font_desc='15'>Isotopes: %(NumberOfIsotopes)s</span> \n"
                                "<span font_desc='15'>Natural: %(Natural)s</span> \n"
                                "<span font_desc='15'>Type: %(Type)s</span> \n"
                                "<span font_desc='15'><a href='https://en.wikipedia.org/wiki/%(Element)s'> Wikipedia Page</a></span>"
                                 % self.elements[number])
            gcontent.set_halign(Gtk.Align.START)
            
            eheader = Gtk.Label()
            eheader.set_markup("<b><span font_desc='20'>Electron Information: </span> </b>" % self.elements[number])
            eheader.set_halign(Gtk.Align.START)
            
            if(self.elements[number]["NumberofValence"] == ""):
                self.elements[number]["NumberofValence"] = "n/a"
            
            econtent = Gtk.Label()
            econtent.set_markup("<span font_desc='15'>Valence Electrons: %(NumberofValence)s</span> \n"
                                "<span font_desc='15'>Electron Shells: %(NumberofShells)s</span> \n"
                                "<span font_desc='15'>Number of Electrons: %(NumberofElectrons)s</span> \n"
                                "<span font_desc='15'>Electronegativity: %(Electronegativity)s</span> \n"
                                "<span font_desc='15'>Ionization Energy: %(FirstIonization)s</span>"
                                 % self.elements[number])
            econtent.set_halign(Gtk.Align.START)
            
            theader = Gtk.Label()
            theader.set_markup("<b><span font_desc='20'>Thermal Information: </span> </b>" % self.elements[number])
            theader.set_halign(Gtk.Align.START)
            
            tcontent = Gtk.Label()
            tcontent.set_markup("<span font_desc='15'>Boiling Point: %(BoilingPoint)s</span> \n"
                                "<span font_desc='15'>Melting Point: %(MeltingPoint)s</span> \n"
                                "<span font_desc='15'>Specific Heat: %(SpecificHeat)s</span>"
                                 % self.elements[number])
            tcontent.set_halign(Gtk.Align.START)
            
            
            box.add(header)
            
            box.add(gheader)
            box.add(gcontent)
            
            box.add(eheader)
            box.add(econtent)
            
            box.add(theader)
            box.add(tcontent)
            
            rows.attach(box, 0, 0, 1, 1)
            
            
            rows.attach
            
            window.add(rows)
            
            #add page
            page_number = self.notebook.append_page(window, Gtk.Label(label=self.elements[number]['Symbol']))
            self.pagenumbers[number] = page_number
        else:
            self.notebook.remove_page(self.pagenumbers[number])
            #decrement page because page removal shifts page numbers backwards
            for i in self.pagenumbers:
                if(self.pagenumbers[number] < self.pagenumbers[i]):
                    self.pagenumbers[i] -= 1
            
        self.show_all()
    
win = PeriodicTable()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()