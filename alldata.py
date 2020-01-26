import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import numpy.polynomial.polynomial as poly





#fitting functions for curve_fit
def func(x, a, b, c):
	return a*(x**b) + c

def func2(x, a, b, c, d):
	return a/((x-b)**c) + d

def func3(x, a, b):
	return np.log(x)*a +b


def sum_of_clicks(data):
	data.pop(0)
	return sum(map(int, data))

def get_logarithmic(data):
	return list(map(np.log, data))

#just cleaning of data: returns array with all views for pages (sorted eather decreasing or increasing)
def get_view_data(csv_file, decreasing = False, logarithmic = False):
	with open(csv_file) as csvfile:
		csvreader = csv.reader(csvfile)
		data = []
		next(csvreader) #skipping first row that is description
		for row in csvreader:
			total_views = sum_of_clicks(row)
			if not logarithmic: #wenn logarithmish nullwerte rauslöschen
				data.append(total_views)
			else:
				if total_views != 0:
					data.append(total_views)
		data.sort(reverse=decreasing)
		return data


#plots the data and all views based on a csv-file
def plot(csv_file, decreasing = False, logarithmic = False):
	data = get_view_data(csv_file, decreasing, logarithmic)
	if logarithmic:
		plt.yscale('log')
		plt.plot(data)
		plt.show()
	else:
		plt.plot(data)
		plt.show()

#looks for the best fitting function in an increasing list of views
def best_fit_increasing(csv_file, function):
	data = get_view_data(csv_file)
	popt, pcov = curve_fit(function, list(range(0,len(data))), data, maxfev=100000)
	print(popt)
	plt.plot(func(list(range(0,len(data))), *popt))
	plt.plot(data)
	plt.show()

	
#looks for the best fitting function in an decreasing list of views
def best_fit_decreasing(csv_file, function):
	data = get_view_data(csv_file, True)
	popt, pcov = curve_fit(function, list(range(1,len(data)+1)), data, maxfev=100000)
	plt.plot(data)
	plt.show()



#testing instance: get logarithmically scaled y axis of click-data
data = get_logarithmic(get_view_data('viewsnov19.csv', False, True))
plt.plot(data)
plt.show()

"""
data = data[120:]
x = list(range(0,len(data)))


#print(popt)
#plt.plot(func3(list(range(0,len(data))), *popt))
coefs = poly.polyfit(x, data, 2)
print(coefs)
ffit = poly.polyval(x, coefs)
plt.plot(x, ffit)
plt.plot(data)
plt.show()
"""





