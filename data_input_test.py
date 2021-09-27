import os
import glob
import pandas as pd

def process_log_file(filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    print(df.head())

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms') 

    #print(t.head())
    
    # insert time data records
    time_data = []
    for ts in t:
        time_data.append([ts, ts.hour, ts.day, ts.week, ts.month, ts.year, ts.day_name()])
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    time_df = pd.DataFrame.from_records(time_data, columns=column_labels)

    #print(time_df.head())

    #for i, row in time_df.iterrows():
    #    cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    print(user_df.head())
    # insert user records
    #for i, row in user_df.iterrows():
    #    cur.execute(user_table_insert, row)

    # insert songplay records
    #for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
    #    cur.execute(song_select, (row.song, row.artist, row.length))
    #    results = cur.fetchone()
        
    #    if results:
    #        songid, artistid = results
    #    else:
    #        songid, artistid = None, None

        # insert songplay record
    #    songplay_data = (
    #        index, 
    #        pd.to_datetime(row["ts"], unit='ms'),
    #        row["userId"],
    #        row["level"],
    #        songid,
    #        artistid,
    #        row["sessionId"],
    #        row["location"],
    #        row["userAgent"]
    #    )
    #    cur.execute(songplay_table_insert, songplay_data)

def process_data(filepath, func):

    all_files = []

    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print(f"{num_files} files found in {filepath}")

    for i, datafile in enumerate(all_files, 1):
        func(datafile)
        print(f"{i}/{num_files} files processed.")


def main():

 process_data(filepath='data/log_data', func=process_log_file)

if __name__ == "__main__":
    main()