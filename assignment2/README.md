# Spartan Senior Data Engineer Test

## Overview

We have a system that tracking IOT device record each calendar date when a user did an event in device. Such as login into a device gonna be counted as 1 activity.
A sample input can be found in the `data/activity_tracking.csv` file. Your task is to build a simple ETL
pipeline that aggregates the data by user_id and stores the results to another database.

## Task 1. ETL Pipeline Implementations
### Requirements

* Dockerize your application into a Docker file and add a `docker-compose` service for it.

* Add a docker container for PostgreSQL 15 to the compose file. The ETL pipeline should write its
  output to this database.

* Use `main.py` as an entry point to your application. The ETL tool needs to be a python command
  line tool that accepts the following arguments:

  | Argument | Description                      |
  | -------- | -------------------------------- |
  | source   | Path to the source file          |
  | database | Database name for inserting data |
  | table    | Table name for inserting data    |

  The application should be executed using the following:
  ```shell
  python main.py \
    --source /opt/data/activity_tracking.csv \
    --database warehouse \
    --table user_activity
  ```

* Aggregated user data needs to be stored in the PostgreSQL database. The target table should be
  named `user_activity` and the schema should be:

  | Column           | Description   |
  | ---------------- | ------------- |
  | user_id          | Column `user_id` from source data |
  | device_id    | Column `device_id` from source data which has the greatest total activity from the `total_activity` column |
  | longest_active_streak   | The longest period of consecutive days this user has been active. For example, if the user had activity record on 2011-08-10, 2011-08-11, 2011-08-14, 2011-08-15 and 2011-08-16, the value of `longest_active_streak` would be 3. |

* Add an integration test to your project that runs the ETL pipeline using the given sample input
  file `data/activity_tracking.csv` and writes it to PostgreSQL. Assert values of `longest_streak` and
  `device_id` for `user_id=5bfd0e8d472bcf0009a1014d`. 
  It is up to your design if you want to run the tests inside or outside docker.

### Instructions

* Feel free to structure your project as you find fit, and add modules and packages if necessary.
* Remember to ask Google. Requried tools Python, Docker and PostgreSQL are all popular tools with
  tons of information online.
* If you get suck, feel free to take shortcuts by changing requirements and let us know what you
  changed. For example, if you want to skip using PostgreSQL, you can just use local filesystem as
  a target

### Submission
* Implement the requirements in this Git repository and create a [patch file](https://git-scm.com/docs/git-format-patch)
  for the changes. Include the patch file in your submitted documents.

### Testing Guidance
* Candidates can optionally choose the database as the destination, which can be SQLite, PostgreSQL, MySQL, etc.
* For junior-level candidates, the scope can include writing the result to a local file without importing to database.
* Consider removing the unit test/integration test in case of time limitations.