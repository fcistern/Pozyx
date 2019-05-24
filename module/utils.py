"""   """

import math

import pandas as pd

##
##

def load_posyx_file(f_name):
    """Helper function to load data."""

    # Update this list to specify which columns you want to keep
    keep_cols = ['tagId', 'timestamp', 'x', 'y', 'z', 'latency']

    # Load the data
    df = pd.read_json(f_name, lines=True, orient='records')

    # Grab the data column, unpack and add all the embedded jsons
    data_df = pd.read_json(df.pop('data').to_json(), orient='index')
    for col in ['coordinates', 'metrics', 'orientation']:
        temp = pd.read_json(data_df[col].to_json(), orient='index')
        df = pd.concat([df, temp], axis=1, join_axes=[df.index])

    # Select columns to return
    df = df[keep_cols]

    return df


def distance(x1, y1, x2, y2):
    """   """

    dist_x = x1 - x2
    dist_y = y1 - y2

    distance = math.sqrt(dist_x**2 + dist_y**2)

    return distance
