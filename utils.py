import requests
import csv
import json
import logging
import pandas as pd
import datetime

# set up logging
logging.basicConfig(filename='randomuser_extract.log', level=logging.DEBUG)

def extract_data(total_users):
    try:
        with requests.Session() as session:
            response = session.get(f'https://randomuser.me/api/?results={total_users}')
            data = response.json()
        logging.info(f'Extracted {total_users} users from API.')
        return data['results']
        
    except Exception as e:
        logging.error(f'Error while extracting data from API. See {e}.')
        raise e

def transform_data(data):
    try:
        # create an empty list to store the data
        extracted_data = []
        
        # loop through the data and extract the desired fields.
        for user in data:
            user_info = {
                'First Name': user['name']['first'],
                'Last Name': user['name']['last'],
                'Gender': user['gender'],
                'Email': user['email'],
                'Date of Birth': user['dob']['date'],
                'Phone Number': user['phone'],
                'Nationality': user['nat']
            }
            extracted_data.append(user_info)
        logging.info('Extracted user info from API.')
        return extracted_data
    except Exception as e:
        logging.error(f'Error while extracting user info. See {e}.')
        raise e
    
def write_to_csv(data):
    try:
        # turn the data into a pandas dataframe
        df = pd.DataFrame(data)
        # create variable for today's date
        today = datetime.date.today()
        # write to csv
        df.to_csv(f'users_{today}.csv', index=False)
        # return df
        return df
    except Exception as e:
        logging.error(f'Error while writing to CSV. See {e}.')
        raise e

def save_to_parquet(df):
    try:
        df.to_parquet(f'users_{today}.parquet')
    except Exception as e:
        logging.error(f'Error while saving to parquet. See {e}.')
        raise e
