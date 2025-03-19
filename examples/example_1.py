# example_blasting_map.py

import logging
import os
from mapper import EventMap, MapConfig, EventConfig, TILE_LAYERS

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# ----------------------------------------------------------------
# Path to the processed blast catalog
# ----------------------------------------------------------------
# Typically, you produce "blast.csv" from blast_catalog.py
event_file_path = 'data/blast.csv'
legend_file_path = 'data/blast_legend.csv'

# Example blast_legend.csv might be:
#   Field,Legend
#   mag,"Explosive Magnitude"
#   latitude,"Latitude"
#   longitude,"Longitude"
#   time,"Date"
#   place,"Blast Location"
#   Repi,"Distance (km)"
#   ...
# Anything not listed is hidden from the tooltip.

# ----------------------------------------------------------------
# Create the MapConfig
# ----------------------------------------------------------------
map_config = MapConfig(
    project_name='Lagoa Do Violao, Sector S11D',
    client='VALE',
    latitude=-6.402210,
    longitude=-50.351785,
    radius_km=10,
    epicentral_circles_title='Epicentral Distance',
    default_tile_layer=TILE_LAYERS['ESRI_SATELLITE']
)

# ----------------------------------------------------------------
# Create EventConfig
# ----------------------------------------------------------------
event_config = EventConfig(
    color_palette='magma',
    color_reversed=True,
    scaling_factor=4,
    legend_position='bottomright',
    legend_title='Magnitude',
    heatmap_radius=20,
    heatmap_blur=15,
    heatmap_min_opacity=0.5
)

# ----------------------------------------------------------------
# Instantiate GenericEventMap
# ----------------------------------------------------------------
generic_map = EventMap(
    map_config=map_config,
    event_config=event_config,
    events_csv=event_file_path,
    legend_csv=legend_file_path,
    x_col=None,        # If your CSV already has lat/lon
    y_col=None,
    # If your CSV only has X, Y columns, you'd do something like:
    #   x_col='x', y_col='y', location_crs='EPSG:32722'
    mandatory_mag_col='mag',  # the "magnitude" column
    calculate_distance=True
)

# ----------------------------------------------------------------
# Load data and generate map
# ----------------------------------------------------------------
generic_map.load_data()
map_object = generic_map.get_map()

# ----------------------------------------------------------------
# Save the map
# ----------------------------------------------------------------
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)
map_path = os.path.join(output_dir, 'blast_map_v2.html')

if map_object:
    map_object.save(map_path)
    logger.info(f"Map saved to '{map_path}'.")
else:
    logger.error("Failed to generate the map.")

# ----------------------------------------------------------------
# Save the final events DataFrame (optional)
# ----------------------------------------------------------------
if not generic_map.events_df.empty:
    out_csv = os.path.join(output_dir, 'blast_catalog.csv')
    generic_map.events_df.to_csv(out_csv, index=False)
    logger.info(f"Blasting events data saved to '{out_csv}'.")
else:
    logger.warning("No events to save.")