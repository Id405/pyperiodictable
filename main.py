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
		if widget.get_active():
			box = Gtk.VBox()
			box.add(Gtk.Label(label="test"))
			page_number = self.notebook.append_page(box, Gtk.Label(label=self.elements[number-1]['Symbol']))
			self.pagenumbers[number] = page_number
		else:
			self.notebook.remove_page(self.pagenumbers[number])
			for i in self.pagenumbers:
				if(self.pagenumbers[number] < self.pagenumbers[i]):
					self.pagenumbers[i] -= 1
			
		self.show_all()

win = PeriodicTable()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()