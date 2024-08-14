from pprint import pprint
import feedparser
from flask import request, url_for, render_template, abort, redirect
from .urls import bp


feeds = {
    "https://blog.teclado.com/rss/": {
        "title": "Teclado",
        "href": "https://blog.teclado.com/rss/",
        "show_images": True,
        "entries": {},
    },
    "https://www.joshwcomeau.com/rss.xml": {
        "title": "Josh Comeau",
        "href": "https://www.joshwcomeau.com/rss.xml",
        "show_images": False,
        "entries": {},
    },
    # "https://snarky.ca/rss/": {
    #     "title": "Snarky",
    #     "href": "https://snarky.ca/rss/",
    #     "show_images": False,
    #     "entries": {},
    # },
}


# Create your views here.
@bp.route("", endpoint="homepage", methods=["GET"])
@bp.route("/feed/<path:feed_url>", methods=["GET"])
def render_feed(feed_url: str = None):

    for url, feed_ in feeds.items():
        if feed_["entries"]:
            pass
        else:
            parsed_feed = feedparser.parse(url)
            for entry in parsed_feed.entries:
                if entry.link not in feed_["entries"]:
                    feed_["entries"][entry.link] = {**entry, "read": False}

    if feed_url is None:
        feed = list(feeds.values())[0]
    elif feed_url in feeds:
        if feed_url == list(feeds.keys())[0]:
            return redirect(url_for("sample.homepage"))
        else:
            feed = feeds[feed_url]
    else:
        return redirect(url_for("sample.homepage"))
    return render_template("feed.html", feeds=feeds, feed=feed)


@bp.route("/entries/<path:feed_url>", methods=["GET"])
def render_feed_entries(feed_url: str):
    try:
        feed = feeds[feed_url]
    except KeyError:
        abort(400)
    page = int(request.args.get("page", 0))
    entries = list(feed["entries"].values())[page * 5 : (page + 1) * 5]
    href = feed["href"]
    max_page = len(feed["entries"]) // 5

    return render_template(
        "partials/entry_page.html",
        entries=entries,
        href=href,
        page=page,
        max_page=max_page,
    )


@bp.route("/add_feed", methods=["POST"])
def add_feed():
    post_data = request.json if request.is_json else request.form
    feeds[post_data.get("href")] = {
        **post_data,
        "entries": {},
    }
    return redirect(url_for("sample.render_feed", feed_url=post_data.get("href")))


# @bp.route("/render_add_feed", methods=["GET"])
# def render_add_feed():
#     return render_template("partials/add_feed.html")


@bp.route("feed/<path:feed_url>/entry/<path:entry_url>", methods=["GET"])
def read_entry(feed_url: str, entry_url: str):
    try:
        feed = feeds[feed_url]
        entry = feed["entries"][entry_url]
        entry["read"] = True
    except KeyError:
        abort(400)
    return redirect(entry_url)
