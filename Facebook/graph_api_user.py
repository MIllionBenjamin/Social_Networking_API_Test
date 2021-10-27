import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

ACCESS_TOKEN = "EAAjHjT4W5VMBAFtJufqV0CZCD5Jgk6ZBhZCI5V0M2BZCTQUo9L2G0RVGDHi7H4DXgFsO8pFLbT5Tkr87EUreZAtzm3wzcqhJorLeNa9rQgOsmqWLJSC0eaasPveXmcvuJPmGNAUa4zRUxiJZBgZBWmQzbTerIaW1ZCHKFWkr2dZCajrYP7yeDec6TJC5e3EafORsMdVIfaakuMQZDZD"
BASIC_URL = "https://graph.facebook.com/v12.0/"

who = "me"

need_fields = ["id",
               "name",
               "picture",
               "posts",
               "birthday",
               "favorite_athletes",
               "favorite_teams",
               "hometown"]

def get_user_info(who: str, need_fields: list):
    get_params = {"fields": ",".join(need_fields), 
                      "access_token": ACCESS_TOKEN}
    response = requests.get(url=BASIC_URL + who, params=get_params)
    return response.json()
    

my_info_json = get_user_info(who, need_fields)
pp.pprint(my_info_json)
with open("my_info.json", 'w+') as my_info_file:
    my_info_file.write(pp.pformat(my_info_json))
