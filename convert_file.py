from osgeo import gdal


BAND_NUMBER = 2 # index of band (index start 1)

# options pass into WarpOptopns()
WARP_OPTIONS_ARGV = {
	'dstSRS': 'EPSG:4326',
	'x_res': 0.005,
	'y_res': 0.005
}

# options pass into TranslateOptions()
TRANSLATE_OPTIONS_ARGV = {
	'format': 'GTiff',
}

filename = 'modis.hdf' # input filename (ex. modis.hdf)
des_name = '{}.tif'.format(filename.split('.')[0]) # filename of tif file
des_name_warp = '{}-{}.tif'.format(des_name.split('.')[0], 'wgs84') # filename of tif filename with warp
src_ds = gdal.Open(filename, gdal.GA_ReadOnly) # dataset from input filename


def get_band_from_number(BAND_NUMBER=1):
	''' return name of band
	'''
	sub_dataset = src_ds.GetSubDatasets()
	band = sub_dataset[BAND_NUMBER - 1][0]
	return band


def convert_file(band, des_name):
	''' convert file by band
	'''
	translate_options = gdal.TranslateOptions(
							format=TRANSLATE_OPTIONS_ARGV['format'],
						)

	return gdal.Translate(destName=des_name, srcDS=band, options=translate_options)


def ref_spatial(des_name, src_ds):
	''' warp file
	'''
	warp_options = gdal.WarpOptions(
						dstSRS=WARP_OPTIONS_ARGV['dstSRS'], 
						xRes=WARP_OPTIONS_ARGV['x_res'], 
						yRes=WARP_OPTIONS_ARGV['y_res'],
					)

	return gdal.Warp(destNameOrDestDS=des_name, srcDSOrSrcDSTab=src_ds, options=warp_options)


def close_dataset():
	src_ds = None


def run_process():
	band = get_band_from_number(BAND_NUMBER)
	geo_tiff = convert_file(band, des_name)
	ref_spatial(des_name_warp, geo_tiff)
	close_dataset()

if __name__ == '__main__':
	run_process()
