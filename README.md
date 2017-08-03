# populartimes
Exploring google maps popular times data. Forked from https://github.com/m-wrzr/populartimes.
## Requirements
+ Google Chrome WebDriver for Selenium: https://sites.google.com/a/chromium.org/chromedriver/getting-started
+ Google Maps API key: https://developers.google.com/places/web-service/
+ Add params.json file to root directory, e.g.
```
{
  "API_key" : "your-key-here",
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
+ Data returned is output to results.json and should be formatted like the following example:
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
+ Popularity is in terms of percentage of the max, since Google doesn't expose precise data
