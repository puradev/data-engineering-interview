# %% 1.
import polars as pl
import requests
import schemas
import random_user_config as conf

# %% 2.
try:
    request = requests.get(
        conf.paths["read_path"] + str(conf.values["num_users"])
        ).json()
except requests.exceptions.RequestException as e: raise SystemExit(e)

# %% 3.
try:
    data = (pl.
            DataFrame(request["results"]).
            unnest("name", "dob").
            with_columns(
                pl.struct([pl.col("phone"), pl.col("cell")]).alias("phone_numbers"),
                pl.col("date").alias("dob")).
            select(schemas.pii))
except: 
    print("Unable to create Polars DataFrame, follow trace stack")
    raise SystemExit()

# %% 4.
try:
    data.write_parquet(f'{conf.paths["write_path"]}/batch_{request["info"]["seed"]}.parquet')
except: 
    print("Unable to write parquet, follow trace stack")

# %% 5. 
import pandas as pd
validate_data = pd.read_parquet(conf.paths["write_path"])