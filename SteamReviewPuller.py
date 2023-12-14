from hashlib import new
import steamreviews
import pandas as pd
import json
from datetime import datetime
import os

now = datetime.now()
current_time = now.strftime("%H-%M-%S") 
outputFile = 'filtered_data' + str(current_time) + '.xlsx' #This is going to set the title of the document. I used time to avoid duplicates and overwriting/errors on accident


with pd.ExcelWriter(outputFile, engine='xlsxwriter', mode='w') as writer:
    app_ids = [521890] 
    details = ['recommendationid', 'steamid', 'num_games_owned', 'num_reviews', 'playtime_forever', 'playtime_last_two_weeks', 'playtime_at_review', 'last_played', 'language', 'review', 'timestamp_created', 'timestamp_updated', 'voted_up', 'votes_up', 'votes_funny', 'weighted_vote_score', 'comment_count', 'steam_purchase', 'received_for_free', 'written_during_early_access', 'hidden_in_steam_china', 'steam_china_location']
#Edit the app_ids with what games you want to get data on. You can find the appid in this part of the link. https://store.steampowered.com/app/1144200/Ready_or_Not/?snr=1_4_4__118 -> in this case it would be 1144200
#Edit details with what data you want. The more you request the longer it takes.
    for app in app_ids: 
        file_exists = os.path.isfile('filtered_data' + str(current_time) + 'csv') 
        review_dict,query_count = steamreviews.download_reviews_for_app_id(app)
        inputfile = open(r"C:\Users\jorge\Downloads\data\review_" + str(app) + ".json", 'r')
 #Edit the path with whatever directory you're running the script on. This is where the data that the script checks is put. + ""review_ + str(app) + .json will remain consistent across systems".
        data = json.load(inputfile)
        reviews = data.get('reviews', {})

        # Initialize an empty dictionary for each app
        filtered_data = {topic: [] for topic in details}

        # Iterate through reviews and filter for specific topics
        for review_dict, review_info in reviews.items():
            authordata = review_info.get('author', {})
            for topic in details:
                value = review_info.get(topic, '')
                value2 = authordata.get(topic, '')
                filtered_data[topic].append(str(value) + str(value2))

        # Create DataFrame for the current app
        df = pd.DataFrame(filtered_data)

        # Write DataFrame to Excel file as a new sheet
        df.to_excel(writer, sheet_name=str(app), index=False)
