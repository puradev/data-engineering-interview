from utils import extract_data, transform_data, write_to_csv
import logging

# set up logging
logging.basicConfig(filename='randomuser_extract.log', level=logging.DEBUG)

# here is the data wrangler
try:
    # data extract
    extracted_data = extract_data(10)
    logging.info(f'Extracted {len(extracted_data)} users from API.')

    # transformations
    transformed_data = transform_data(extracted_data)
    logging.info('Transformed user info from API.')

    # saving to csv
    csv_df = write_to_csv(transformed_data)
    logging.info('Wrote data to CSV.')

except Exception as e:
    logging.error(f'Error while running the ETL process for the randomuser api. See {e}.')
    raise e
