from osgeo import gdal


filename = 'modis.tif' # input filename
dst_filename = 'output.tif' # output filename

# config of output file
x_size = 2400
y_size = 2400
e_type = gdal.GDT_Int16

file_format = 'GTiff' # file format


def get_array_from_file(filename):
	''' return array of band number 1
	'''
	src_ds = gdal.Open(filename)
	array = src_ds.GetRasterBand(1).ReadAsArray()
	return array


def create_tif_file(file_format, dst_filename, x_size, y_size, e_type):
	''' return a empty file
	'''
	driver = gdal.GetDriverByName(file_format) # create driver
	dst_ds = driver.Create(dst_filename, xsize=x_size, ysize=y_size, bands=1, eType=e_type) # create empty file
	return dst_ds


def write_array_to_file(dst_ds, array):
	''' write array into band number 1 of dataset
	'''
	return dst_ds.GetRasterBand(1).WriteArray(array)


def close_dataset():
	src_ds = None


def run_process():
	array = get_array_from_file(filename)
	dst_ds = create_tif_file(file_format, dst_filename, x_size, y_size, e_type)
	output_ds = write_array_to_file(dst_ds, array)
	close_dataset()


if __name__ == '__main__':
	run_process()