import json
import timeit
import requests

from utils.scraper import BrowserScrape

def load_data():
  n_available = 0
  n_unavailable = 0

  with open("results.json", mode="w+", encoding="utf-8") as output_file:
    output_file.write("[\n")

    for place_string in params["places"]:

      print("\n-> [{}]".format(place_string))

      # places api - text-based search
      places_results = place_search_url.format(place_string, params["API_key"])

      try:
        response = requests.get(places_results, auth=('user', 'pass')).text
        results = json.loads(response)["results"]

        detail = results[0]
        searchterm = "{} {}".format(detail["name"], detail["formatted_address"])

        try:
          # get populartimes from crawler
          popular_times = {
                            "name": detail["name"],
                            "place_id": detail["place_id"],
                            "popular_times": json.loads(crawler.get_popular_times(searchterm))
                          }
          output_file.write("{}\n".format(json.dumps(popular_times)))
          n_available += 1

        except BrowserScrape.NoPopularTimesAvailable:
          n_unavailable += 1

        except KeyError:
          pass

      except requests.exceptions.RequestException as e:
        print(e)

    print("executionTime={}; nAvailable={}; nUnavailable={}"
          .format(timeit.default_timer() - start_time, n_available, n_unavailable))
    output_file.write("]\n")


if __name__ == "__main__":
  start_time = timeit.default_timer()

  place_search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}"
  place_request_url = "https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}"

  params = json.loads(open("params.json", "r").read())
  crawler = BrowserScrape()

  load_data()
