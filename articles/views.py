from django.shortcuts import render

from django.shortcuts import render
from .scrapers import Pixnet


def index(request):

    pixnet = Pixnet(None)

    if request.method == "POST":
        # get the query conditions
        pixnet = Pixnet(request.POST.get("restaurant_name"))

    context = {
        "articles": pixnet.get_articles()
    }
    # print(context)
    return render(request, "articles/index.html", context)
