import sys
import os
import pandas as pd

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

# from utils.constants import CLIENT_ID, SECRET
from etls.reddit_etl import extract_posts, transform_posts, load_data_to_csv
from utils.constants import OUTPUT_PATH

output_file_path = "data/output/"

def reddit_pipeline(file_name: str):

    # We will read the data from the CSV file, then apply the transformations

    # Extraction

    reddit_posts_df = extract_posts(file_name)
    # posts_df = pd.DataFrame(reddit_posts_list[0:10])
    print(f'Number of posts = {len(reddit_posts_df)}')
    print(reddit_posts_df.dtypes)

    # Transformation

    transformed_data = transform_posts(reddit_posts_df)

    transformed_data = transformed_data.iloc[:10]

    print(transformed_data.dtypes)

    print(transformed_data)

    print(len(transformed_data))

    # Loading to a CSV

    OP = load_data_to_csv(transformed_data, OUTPUT_PATH)

    return OP