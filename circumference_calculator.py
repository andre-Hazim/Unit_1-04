'''
Created By: Roman Beya, Raymond Octavius, Andre Hazim
Created For: ICS3U
Created On: 25-Sep-2017
Calculates the circumference of a circle given the radius inputted by a user
'''
import ui

def calculate_on_touch_up_inside(sender):
	# input
	radius = int(view['radius_textfield'].text)
	# process
	circumference = 3.14159265 * radius ** 2
	# output
	view['circumference_label'].text = str('Circumference : ') + str( circumference)
view = ui.load_view()
view.present('sheet')
