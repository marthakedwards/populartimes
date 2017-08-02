# populartimes
exploring google maps popular times data
forked from https://github.com/m-wrzr/populartimes
## Requirements for RequestPlaces
+ Google Chrome WebDriver for Selenium: https://sites.google.com/a/chromium.org/chromedriver/getting-started
+ Google Maps API key: https://developers.google.com/places/web-service/?hl=de
+ Add params.json file to root directory, e.g.
```
{
  "API_key" : "AIzaSyByUdGDFevSlzYoJfoy0rHpTCMeLMbyll8",
  "places" : [
      "State Bird Provisions",
      "Tartine Manufactory",
      "Bi-Rite Creamery"
   ]
}
```
where the strings in `places` array can be any searchable term in Google Maps (name, address, etc.), but with the forewarning that if the search term returns several results, the script will just select the first one it finds and ignore the rest.
+ execute scraping: `python scrape/main.py`

## Notes
+ Data is just loaded into memory and then spat out in the terminal (but if this causes out of memory exception I can dynamically export to csv as the data gets pulled in, or similar)
+ Data returned should be JSON formatted like the following example:
```
[
  {
    "place_id": "ChIJQ7kGpLmAhYARKeCe2pDobWk",
    "name": "State Bird Provisions",
    "popular_times": [
      {
        "weekday": "Monday",
        "weekday_num": 0,
        "data": [
          {
            "popularity": 0,
            "time": 6
          },
          ...
        ],
      },
      ...
    ]
  },
  ...
]
```
+ Popularity is in terms of percentage of the max, if I understand correctly, since Google doesn't expose precise data around this
