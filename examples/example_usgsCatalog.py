# example_usgsCatalog.py
import logging
from mapper import USGSCatalog

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Create an instance of USGSCatalog
catalog = USGSCatalog()

# Get earthquake events from the oldest available data to today
events = catalog.get_events(event_type='earthquake')

# Save the DataFrame externally
if events is not None and not events.empty:
    events.to_csv('data/usgs.csv', index=False)
    logger.info("Catalog data saved to 'data/usgs.csv'.")
else:
    logger.warning("No events retrieved or data is empty.")
