import csv
import pandas as pd
import pickle
import re


# this function will grab a list of links to grab dataframes from
def open_links_from_CVS(file_name):
    with open(file_name, newline='', encoding='utf-8') as f:
        file = csv.reader(f, delimiter=',')
        # file = csv.reader(f)
        list_of_string = []
        for current in file:
            for more_current in current:
                list_of_string.append(more_current)
    return list_of_string


# this function will concatinate all dataframes pulled from web from a list of strings containing the links
def concat_data_frames_from_web(list_of_links):
    dframes_to_concat = []
    for link in list_of_links:
        dframes_to_concat.append(pd.read_csv(link))
    concated_df = pd.concat(dframes_to_concat)
    return concated_df


# this function will save a dataframe as a pickle
def save_dataframe_as_pickle(frame_to_save, save_name):
    with open(save_name, 'wb') as f:
        pickle.dump(frame_to_save, f)


# this function will open a dataframe as a pickle
def open_dataframe_pickle(name_of_pickle):
    with open(name_of_pickle, 'rb') as f:
        df_from_pickle = pickle.load(f)
    return df_from_pickle


# this function is for cleaning the station name data from typos in the dataset
def clean_station_names(dataframe_to_clean):
    dataframe_to_clean['STATION'] = [re.sub(r'AV', 'AVE', spot) for spot in dataframe_to_clean['STATION']]
    dataframe_to_clean['STATION'] = [re.sub(r'AVE{2}', 'AVE', spot) for spot in dataframe_to_clean['STATION']]
    dataframe_to_clean['STATION'] = [re.sub(r'RD', 'ROAD', spot) for spot in dataframe_to_clean['STATION']]
    dataframe_to_clean['STATION'] = [re.sub(r'PK', 'PARK', spot) for spot in dataframe_to_clean['STATION']]
    dataframe_to_clean['STATION'] = [re.sub(r'PARKWAY', 'PKWY', spot) for spot in dataframe_to_clean['STATION']]
    dataframe_to_clean['STATION'] = [re.sub(r'STS', 'ST', spot) for spot in dataframe_to_clean['STATION']]
    dataframe_to_clean['STATION'] = [re.sub(r'RACETR', 'TRACETRACK', spot) for spot in dataframe_to_clean['STATION']]
    dataframe_to_clean['STATION'] = [re.sub(r'PARKWY', 'PARKWAY', spot) for spot in dataframe_to_clean['STATION']]
    dataframe_to_clean['STATION'] = [re.sub(r'HWY', 'HIGHWAY', spot) for spot in dataframe_to_clean['STATION']]
    dataframe_to_clean['STATION'] = [re.sub(r'BLVD', 'BL', spot) for spot in dataframe_to_clean['STATION']]
    return dataframe_to_clean


# this function scrapes the MTA website and grabs all relevent links
def get_links(website_string):
    flag = 0
    instance_loc = 0
    links = []
    while flag != -1:
        instance_loc = website_string.find('<a href="data', instance_loc+1)
        if instance_loc == -1:
            flag = instance_loc
        else:
            ref_start = instance_loc+14
            ref_end = website_string.find('"', ref_start+1)
            links.append('http://web.mta.info/developers/data/' + website_string[ref_start:ref_end])
            flag = instance_loc
    return links


# this function saves scraped websites into a csv file
def save_links_to_CVS(links, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(links)
    return


# this function will sort a list of strings and only keep those from a sepecified period of time
def sort_links_by_time_period(links):
    # m = re.search('\d\d[0][3-6]\d\d', current)
    focused_links = []
    for current in links:
        if re.search('[1][5-6][0][3-6]\d\d', current):
            focused_links.append(current)
    return focused_links