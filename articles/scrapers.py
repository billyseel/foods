import requests


class Pixnet:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
    # this part is to get the restaurants review

    def get_articles(self):

        result = []  # return an empty list so that it can be filled with the search result

        if self.restaurant_name:  # if not empty it should be crawled.

            # we get the information to be displayed
            response = requests.get(
                f"https://www.pixnet.net/mainpage/api/tags/{self.restaurant_name}/feeds?filter=articles&sort=latest&per_page=15")
            # print(response.json()) ... we could print this info on a json form to choose what to display
            # obtaining the info and passing to a variable feeds
            feeds = response.json()["data"]["feeds"]

            for feed in feeds:

                avatar = feed["avatar"]
                author = feed["display_name"]
                title = feed["title"]
                hit = feed["hit"]
                link = feed["link"]
                source = "痞客邦"

                result.append(
                    dict(avatar=avatar, author=author, title=title, hit=hit, link=link, source=source))

        return result
