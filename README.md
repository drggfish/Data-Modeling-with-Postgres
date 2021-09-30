# Data-Modeling-with-Postgres

Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

# Song Dataset
The first dataset is a subset of real data from the Million Song Dataset.
Each file is in JSON format and contains metadata about a song and the artist of that song.
The files are organized by the first three letters of each song's track ID.
```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```

And below is an example of what a single song file, TRABBAM128F429D223.json, looks like.
```
{
    "num_songs": 1, 
    "artist_id": "ARBGXIG122988F409D",
    "artist_latitude": 37.77916,
    "artist_longitude": -122.42005,
    "artist_location": "California - SF",
    "artist_name": "Steel Rain", 
    "song_id": "SOOJPRH12A8C141995",
    "title": "Loaded Like A Gun",
    "duration": 173.19138,
    "year": 0
}
```

# Log dataset

The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset you'll be working with are partitioned by year and month. For example:

```
log_data/2018/11/2018-11-01-events.json
log_data/2018/11/2018-11-02-events.json
```

# Schema for Song Play Analysis
Using these two datasets, the data engineer will need to create a star schema to hold the data and allow for subsequent queries across the multiple tables in the **sparkifydb** database. The star schema will include the following tables.

### Fact tables

#### Songplays

Records in log data associated with song plays i.e. records with `page` set to
`NextSong`.

|   Column    |            Type             |
| ----------- | --------------------------- |
| songplay_id | serial                      |
| start_time  | timestamp                   |
| user_id     | integer                     |
| level       | character varying           |
| song_id     | character varying           |
| artist_id   | character varying           |
| session_id  | integer                     |
| location    | character varying           |
| user_agent  | character varying           |

Primary key: songplay_id

### Dimension tables

#### Users

Users in the app.

|   Column   |       Type        |
| ---------- | ----------------- |
| user_id    | integer           |
| first_name | character varying |
| last_name  | character varying |
| gender     | character varying |
| level      | character varying |

Primary key: user_id

#### Songs

Songs in music database.

|  Column   |         Type          |
| --------- | --------------------- |
| song_id   | character varying     |
| title     | character varying     |
| artist_id | character varying     |
| year      | integer               |
| duration  | double precision      |

Primary key: song_id

#### Artists

Artists in music database.

|  Column   |         Type          |
| --------- | --------------------- |
| artist_id | character varying     |
| name      | character varying     |
| location  | character varying     |
| latitude  | double precision      |
| longitude | double precision      |

Primary key: artist_id

#### Time

Timestamps of records in songplays broken down into specific units.

|   Column   |            Type             |
| ---------- | --------------------------- |
| start_time | timestamp                   |
| hour       | integer                     |
| day        | integer                     |
| week       | integer                     |
| month      | integer                     |
| year       | integer                     |
| weekday    | character varying           |

## Database

The database can be installed locally or ran using Docker, which is the
preferred method. I have included a **docker-compose.yml** file that when ran using "docker-compose up -d"
will start a docker container running a PostgreSQL database and a container running pgAdmin4 that can
be used to interact with the databases running in PostgreSQL.

## Project structure

Files used on the project:
1. **data** data folder with separate song files and log files in JSON format that will be processed by the subsequent scripts.
2. **sql_queries.py** contains all sql queries. Imported by the `create_tables.py` script.
3. **create_tables.py** drops and creates various tables for the **sparkifydb**. It is used to reset all tables prior to running the ETL script.
4. **test.ipynb** IPython notebook used to display the first few rows of each table.
5. **etl.ipynb** IPython notebook used to build the actual code segments that would eventually make their way into the final **etl.py** file.
6. **etl.py** actual ETL script that reads and processes files from song_data and log_data and loads them into their corresponding tables in the **sparkifydb**.

## Running the project

1. Run the **create_tables.py** script.  This script drops and creates tables. This resets all tables before each time ETL scripts are being run.
2. Run the **etl.py** script. This script that reads and processes files from song_data and log_data and loads them into corresponding tables.