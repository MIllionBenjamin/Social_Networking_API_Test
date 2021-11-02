import googleapiclient.discovery
import pprint

pp = pprint.PrettyPrinter(indent=4)

API_KEY = "AIzaSyDr20RNT9fDyJEqu5DvW9458jJZiz11QMo"

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)

request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        forUsername="GoogleDevelopers"
    )
response = request.execute()

print(response)
'''
with open("GoogleDevelopers_channel_info.json", "w+") as channel_info_file:
    channel_info_file.write(pp.pformat(response))
'''