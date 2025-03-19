from mapper import BlastCatalog, BlastConfig
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# User-provided file paths
blast_file_path = 'data/mic.csv'         # Path to your blast data file
output_catalog_path = 'data/blast.csv'   # Path to save the processed catalog

# Create a BlastConfig instance with parameters
blast_config = BlastConfig(
    blast_file_path=blast_file_path,     # Blast data file path
    coordinate_system='EPSG:32722',      # Coordinate system of x, y data
    f_TNT=0.90,                          # TNT equivalence factor
    a_ML=0.75,                           # Coefficient for log10 scaling
    b_ML=-1.0                            # Constant offset
)

# Create an instance of blastCatalog with the configuration object
blast_catalog = BlastCatalog(blast_config)

# Process the blast data
blast_catalog.read_blast_data()          # Reads the data
catalog_df = blast_catalog.build_catalog()  # Builds the catalog

# Save the catalog DataFrame externally
if catalog_df is not None and not catalog_df.empty:
    catalog_df.to_csv(output_catalog_path, index=False)
    logger.info(f"Blast catalog data saved to '{output_catalog_path}'.")
else:
    logger.warning("No blast events to save.")