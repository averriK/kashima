# example_usgs_map.py
import logging
import os
from mapper import MapConfig, EventConfig, FaultConfig, StationConfig, EventMap

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

faults_gem_file_path = 'data/gem_active_faults_harmonized.geojson'
event_file_path = 'data/usgs.csv'
station_file_path = 'data/stations.csv'
legend_file_path = 'data/usgs_legend.csv'

map_config = MapConfig(
    project_name='Plutonic Gold Mine',
    client='Joe',
    latitude=-25.312525,
    longitude=119.448047,
    radius_km=2500,
    epicentral_circles_title="Epicentral Distance"
)

event_config = EventConfig(
    vmin=4.5,
    vmax=8.5,
    color_palette='magma',
    color_reversed=True,
    scaling_factor=4,
    legend_position='bottomright',
    legend_title='Magnitude',
    heatmap_radius=20,
    heatmap_blur=15,
    heatmap_min_opacity=0.5,
    event_radius_multiplier=1.5  # e.g. no multiplier, or 1.5, etc.
)

fault_config = FaultConfig(
    include_faults=True,
    faults_gem_file_path=faults_gem_file_path,
    regional_faults_color='darkblue',
    regional_faults_weight=3,
    coordinate_system='EPSG:4326'
)

station_config = StationConfig(
    station_file_path=station_file_path,
    coordinate_system='EPSG:32722',
    layer_title='Seismic Stations'
)

em = EventMap(
    map_config=map_config,
    event_config=event_config,
    events_csv=event_file_path,
    legend_csv=legend_file_path,
    fault_config=fault_config,
    station_config=station_config,
    x_col=None, 
    y_col=None,
    location_crs='EPSG:4326',
    mandatory_mag_col='mag',
    calculate_distance=True
)

em.load_data()
map_object = em.get_map()

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)
map_path = os.path.join(output_dir, 'usgs_map_v2.html')

if map_object:
    map_object.save(map_path)
    logger.info(f"Map saved to '{map_path}'.")
else:
    logger.error("Failed to generate the map.")

# If you want the final events dataset, for example:
if not em.events_df.empty:
    out_csv = os.path.join(output_dir, 'catalog.csv')
    em.events_df.to_csv(out_csv, index=False)
    logger.info(f"Events data saved to '{out_csv}'.")