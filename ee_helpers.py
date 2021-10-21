import ee 
from datetime import datetime
import os
import geemap

def cloud_score(image):
        cloud = ee.Algorithms.Landsat.simpleCloudScore(image).select('cloud')
        cloudiness = cloud.reduceRegion(ee.Reducer.mean(),
                                            geometry=region,
                                            scale=30)
        image = image.set(cloudiness)
        return image


def export_landsat_eight_images(bounding_box, start_date,end_date, out_dir, cloudy_pixel_percentage):
    
    global region
    region = ee.Geometry.Polygon(bounding_box)
    
    
    
    image_collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA') \
        .filterBounds(region) \
        .filterDate(start_date, end_date) \
        .map(algorithm = cloud_score) \
        .filter(ee.Filter.lt('cloud', cloudy_pixel_percentage))
   
    geemap.ee_export_image_collection(image_collection, 
                               out_dir,
                               scale= 30,
                               region = region,
                               file_per_band = False)

def export_landsat_seven_images(bounding_box, start_date,end_date, out_dir, cloudy_pixel_percentage):
    
    global region
    region = ee.Geometry.Polygon(bounding_box)
    
    
    
    image_collection = ee.ImageCollection('LANDSAT/LE07/C01/T1_TOA') \
        .filterBounds(region) \
        .filterDate(start_date, end_date) \
        .map(algorithm = cloud_score) \
        .filter(ee.Filter.lt('cloud', cloudy_pixel_percentage))
   
    geemap.ee_export_image_collection(image_collection, 
                               out_dir,
                               scale= 30,
                               region = region,
                               file_per_band = False)

def export_landsat_five_images(bounding_box, start_date,end_date, out_dir, cloudy_pixel_percentage):
    
    global region
    region = ee.Geometry.Polygon(bounding_box)
    
    
    
    image_collection = ee.ImageCollection('LANDSAT/LT05/C01/T1_TOA') \
        .filterBounds(region) \
        .filterDate(start_date, end_date) \
        .map(algorithm = cloud_score) \
        .filter(ee.Filter.lt('cloud', cloudy_pixel_percentage))
   
    geemap.ee_export_image_collection(image_collection, 
                               out_dir,
                               scale= 30,
                               region = region,
                               file_per_band = False)