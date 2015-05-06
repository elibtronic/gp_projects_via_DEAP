#
#
# Filter Functions for the GP
#
import numpy as np

#Will find the AVG grey centered on x,y with mag/2 in either direction
#Required by assingment spec
def f_avg(mag, x,y,texture):
	
	l_x = mag / 2
	h_x = (mag / 2) + 1
	l_y = mag / 2
	h_y = (mag / 2) + 1

	x_start = x - l_x
	x_end = x + h_x
	y_start = y - l_y
	y_end = y + h_y
	
	#boundary conditions
	if x_start < 0:
		x_start = 0
	if y_start < 0:
		y_start = 0
	if x_end > 255:
		x_end = 255
	if y_end > 255:
		x_end = 255
	if x_start == x_end or y_start == y_end:
		return texture[min(x,255),min(y,255)]
	
	avg_grey = np.array(texture[x_start:x_end,y_start:y_end])
	return int(round(avg_grey.mean()))
	
	
#Will find the standard deviation centered on x,y with mag/2 in either direction
#Required by assignment spec
def f_std(mag, x,y,texture):
	
	l_x = mag / 2
	h_x = (mag / 2) + 1
	l_y = mag / 2
	h_y = (mag / 2) + 1

	x_start = x - l_x
	x_end = x + h_x
	y_start = y - l_y
	y_end = y + h_y
	
	#boundary conditions
	if x_start < 0:
		x_start = 0
	if y_start < 0:
		y_start = 0
	if x_end > 255:
		x_end = 255
	if y_end > 255:
		x_end = 255
	if x_start == x_end or y_start == y_end:
		return texture[min(x,255),min(y,255)]
	
	avg_grey = np.array(texture[x_start:x_end,y_start:y_end])
	return int(round(avg_grey.std()))

#Finds min value in area mag/2 in each direction centered on x,y
#first additional function, as mentioned in assignment description
def f_min(mag, x,y,texture):
	
	l_x = mag / 2
	h_x = (mag / 2) + 1
	l_y = mag / 2
	h_y = (mag / 2) + 1
	
	x_start = x - l_x
	x_end = x + h_x
	y_start = y - l_y
	y_end = y + h_y
	
	#boundary conditions
	if x_start < 0:
		x_start = 0
	if y_start < 0:
		y_start = 0
	if x_end > 255:
		x_end = 255
	if y_end > 255:
		x_end = 255
	if x_start == x_end or y_start == y_end:
		return texture[min(x,255),min(y,255)]
	
	avg_grey = np.array(texture[x_start:x_end,y_start:y_end])
	return int(round(avg_grey.min()))

#Finds max value in area mag/2 in each direction centered on x,y
#Second additional function, as mentioned in assignment description
def f_max(mag, x,y,texture):
	
	l_x = mag / 2
	h_x = (mag / 2) + 1
	l_y = mag / 2
	h_y = (mag / 2) + 1
	
	x_start = x - l_x
	x_end = x + h_x
	y_start = y - l_y
	y_end = y + h_y
	
	#boundary conditions
	if x_start < 0:
		x_start = 0
	if y_start < 0:
		y_start = 0
	if x_end > 255:
		x_end = 255
	if y_end > 255:
		x_end = 255
	if x_start == x_end or y_start == y_end:
		return texture[min(x,255),min(y,255)]
	
	avg_grey = np.array(texture[x_start:x_end,y_start:y_end])
	return int(round(avg_grey.max()))
