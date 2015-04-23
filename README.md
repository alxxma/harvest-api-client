Harvest API client
===================================

A Python library for Harvest's API (getharvest.com) which supports OAuth2 authentication. It's inspired by https://github.com/lann/Harvest and has some distinctions:

  * Supports Python 3x
  * Supports Oauth2
  * Has tests coverage

It doesn't support the basic authentication.

How to install
-----

    $ pip install harvest_api_client

Using
_____

1. Get the access and refresh token and put them in a file. The file has to look like this:

{"access_token": {"last_refresh_time": "2015-04-20T00:18:52.494946", "value": "[your access token]"}, "refresh_token": {"last_refresh_time": "2015-04-20T16:02:30.831858", "value": "[your refresh token]"}}


Source
-----

The source is available here
- https://github.com/GildedHonour/harvest-api-client


License
-----

The MIT License (MIT)