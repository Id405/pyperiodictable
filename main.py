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
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Element('He', 'Helium', '2', '4.0026')], 
            [Element('Li', 'Lithium', '3', '6.94'), Element('Be', 'Beryllium', '4', '9.0122'), None, None, None, None, None, None, None, None, None, None, Element('B', 'Boron', '5', '10.81'), Element('C', 'Carbon', '6', '12.011'), Element('N', 'Nitrogen', '7', '14.007'), Element('O', 'Oxygen', '8', '15.99'), Element('F', 'Flourine', '9', '18.998'), Element('Ne', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, Element('Al', 'Aluminium', '13', '26.982'), Element('Si', 'Silicone', '14', '28.085'), Element('P', 'Phosphorus', '15', '30.974'), Element('O', 'Oxygen', '8', '15.99'), Element('F', 'Flourine', '9', '18.998'), Element('Ne', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Element('He', 'Helium', '2', '4.0026')],
            [Element('H', 'Hydrogen', '1', '1.008'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Element('He', 'Helium', '2', '4.0026')],
           ]

class PeriodicTable(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")

		grid = Gtk.Grid()
		self.add(grid)
        
		for y, row in enumerate(elements):
			for x, element in enumerate(row):
				if element != None:
					button = Gtk.Button(label=element.symbol)
					grid.attach(button, x, y, 1, 1)
				else:
					label = Gtk.Label("")
					grid.attach(label, x, y, 1, 1)
		
		grid.set_row_homogeneous(True)
		grid.set_column_homogeneous(True)
		
	def on_button_clicked(self, widget):
		print("Hello World")

win = PeriodicTable()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()