from praw import Reddit
import praw
import sys, os
import pandas as pd
import numpy as np

def extract_posts(file_name: str):
    df = pd.read_csv(file_name)
    # df_list = df.values.tolist()
    return df

def transform_posts(post_df: pd.DataFrame):
    post_df = post_df.drop('created', axis=1)
    post_df['timestamp'] = pd.to_datetime(post_df['timestamp'])
    post_df['comms_num'] = post_df['comms_num'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)
    post_df['url'] = post_df['url'].astype(str)
    post_df['id'] = post_df['id'].astype(str)
    post_df['body'] = post_df['body'].astype(str)
    post_df = post_df[~post_df['body'].isnull() | (post_df['body'] != '')]

    return post_df


def load_data_to_csv(transformed_df: pd.DataFrame, output_file_path: str):
    transformed_df.to_csv(output_file_path+"reddit_cleaned.csv", index=False)
    print('DONE')
    return output_file_path+"reddit_cleaned.csv"