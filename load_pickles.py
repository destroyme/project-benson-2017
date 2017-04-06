import pickle
import pandas as pd
from collections import Counter


def open_dataframe_pickle(name_of_pickle):
    with open(name_of_pickle, 'rb') as f:
        df_from_pickle = pickle.load(f)
    return df_from_pickle


def concat_data_frames(list_of_dfs):
    concated_df = pd.concat(list_of_dfs)
    return concated_df


pickle_1 = 'MTA_DATA_SPRING_2014_to_2016_1.pickle'
pickle_2 = 'MTA_DATA_SPRING_2014_to_2016_2.pickle'
pickle_3 = 'MTA_DATA_SPRING_2014_to_2016_3.pickle'


df_1 = open_dataframe_pickle(pickle_1)
df_2 = open_dataframe_pickle(pickle_2)
df_3 = open_dataframe_pickle(pickle_3)
del(pickle_1, pickle_2, pickle_3)

list_of_df = [df_1, df_2, df_3]

df = concat_data_frames(list_of_df)
del(df_1, df_2, df_3)


