HOW TO USE:

This script runs utilizes the steamreviews module to pull Steam reviews for multiple games via the steam api, parse the JSON data, then move them to excel. For each game a new sheet is created in the excel sheet. 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
There's a few things with this script that need to be adjusted to a particular usecase:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
app_ids -> edit the app_ids with what games you want to get data on. You can find the appid in this part of the link: https://store.steampowered.com/app/1144200/Ready_or_Not/?snr=1_4_4__118 -> in this case it would be 1144200

details ->Edit details with what data you want. The more you request the longer it takes.

input file details ->  inputfile = open(r"C:\Users\jorge\Downloads\data\review_" + str(app) + ".json", 'r') -> Edit the path with whatever directory you're running the script on. This is where the data that the script checks is put. + ""review_ + str(app) + .json will remain consistent across systems".

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Adjustments could be made if you wanted to have some of this pull from text files or if you wanted to pull large amounts of data. However there's a few limitations:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Given the limits on the steam API and the absurd amount of reviews some games have, it could take a while to pull all the review data you want. Steam does place a cool down of 5 minutes. Let the script continue to run and it will power through. This usually only occurs if you're pulling more than a few games. 
2. Most of the work is in parsing the JSON data we get from Steam and adding it to excel. the more details you want, the more it has to iterate. There are more efficent ways to code this but there shouldn't be a issue
unless you have a excessively large dataset. Even with 400k reviews across 12 games It took 10 minutes to get everything together.
3. If you want absurd datasets (1M+ reviews, or 100+ games) it would probably make more sense to work with something aside from Excel. Especially with popular games, the reviews are long and numerous. Even if everything loads in, you will certainly end up with issues creating formulas and manipulating that data. I recommend R in this case for manipulation on this scale.
4. You can also move the excel writer into the inital loop to get a new document made for each game, rather than a new sheet. This could be better if you only want data for the games individually, rather than having them all in one super chunky excel doc. Especially if you are pulling data from tons of games.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 If anyone has issues or would like assistance getting this to cater to different/larger datasets please don't hesitate to reachout to jdelgado1256@gmail.com
 
