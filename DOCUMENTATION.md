# Random User API - ETL
### Pura Data Engineering Interview
#### Gavin South - 11/14/2023 

In this document I'll have mapped sections that connect to portions of the repository I built. All requirements, comments, and details will be numbered an expounded upon. Follow the path after each number to see the work. This is a project that's modular, but the main script that performs the task is the `random_user_etl.py`.
****
##### 1. cell of python file `random_user_etl.py`
With the problem at hand being a case of ETL I considered all the different tools and libraries that could achieve the desired results. I decided to use the **Polars** package to do the heavy work. This tool has proven to be a fast and robust tool that's also user friendly. [link: Polars](https://pola-rs.github.io/polars/py-polars/html/index.html)

The package **requests** is also being used to request data from the RandomUsers.me API.

**schemas** is another Python file within the project is a reference file that contains the RandomUsers PII (Personal Identifiable Information) 'schema'. 

Finally **random_user_config** is another Python file in the project that houses paths, variable used in the job, and other credentials if needed. 

*Note:* Some of these separate modules may seem over-kill for this simple project, but in reality data engineering projects scale quickly and need detailed and concise organization to keep things in order. Everything I built is an example of how to scale and keep things organized. 
****
##### 2. cell in `random_user_etl.py`

Here is just a call to request the data from the API, the html path is set in the config file and is being called here to keep things organized. The API is also designed to return a n number of random user data so that value is also sitting in the conf file and in this case is set to n = 100. 
****
##### 3. cell in `random_user_etl.py`

Using the Polars API the results list of data is accessed from the request and goes through a little bit of data transformation. Unnest opens nested structs, with_columns renames and combines the required fields, and select is referencing a schema list in that file to choose which fields to keep (which is a PII set).

****
##### 4. cell in `random_user_etl.py`

Lastly, after the data has been wrangled/transformed we send it off in a parquet file format (to save disk space) with a serialized name to differentiate each batch of data that's been processed. All the files are in a directory called processed_data. Again, this is overkill but it's so valuable to consider partitioning and sorting data for later retrieval. The random seed value from the original request is used as a unique file id.  

****
##### 5. cell in `random_user_etl.py`

This is just an example and is not necessary for the project. But if an analyst or data scientist is needing to grab all this data processed they would likely use this call to gather all the data that's been saved thus far. 

****
##### 6. `random_user_config.py`

Config files are so valuable to large data engineering projects. It will contain all sorts of information and values that will be used around all different jobs. There are config parsers and other libraries that will allow us to load all sorts of configuration information into a job or script. But, for this case we'll just call variables as they sit in there to emulate that functionality.

****
##### Final Notes:
This project was a fun exercise and I appreciated the opportunity to do it. It took me about two hours to get everything done and I was able to get it documented and polished in another hour or so. 
As far as limitations and inefficiencies I'd worry about local space and power as things scale, but using Polars this can remove some of those constrains but they still exist as things scale. But, in the real world doing a project like this I'd consider doing some sort of big data pipeline and build process using PySpark and Apache software to get things completely automated and scaled of course. I'd then place that job on a K8s cluster that has enough resources to complete the task by created a pod and a cron job to run that job when it needs to be done. This small project is just an exercise of etl processes and I chose not to go that route.
Thanks again!