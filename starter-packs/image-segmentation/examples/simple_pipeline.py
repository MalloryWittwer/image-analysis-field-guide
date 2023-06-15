# Setup: `pip install scikit-image pandas`

import skimage.filters
import skimage.morphology
import skimage.measure
import skimage.io
import pandas as pd

# Load your image (or use the blobs from Fiji as an example)
image = skimage.io.imread('blobs.tif')

# Apply a median filter for denoising
denoised_image = skimage.filters.median(image)

# Threshold the image
threshold = skimage.filters.threshold_otsu(denoised_image)
binary_mask = denoised_image >= threshold

# Remove small objects
final_mask = skimage.morphology.remove_small_objects(binary_mask, min_size=60)

# Connected components labeling
instance_mask = skimage.morphology.label(final_mask)

# Measure object properties
properties = skimage.measure.regionprops_table(
	instance_mask, 
	properties=['label', 'area', 'centroid']
)

# Load the properties in a Pandas DataFrame for downstream analysis
df = pd.DataFrame.from_dict(properties)

print(df.head())  # Show the resulting table