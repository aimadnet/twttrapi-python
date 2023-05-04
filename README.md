# TwttrAPI - Unofficial Twitter API

A Python API wrapper for TwttrAPI, an unofficial Twitter API available on RapidAPI, which is built using Twitter's mobile API.

https://rapidapi.com/contact-cmWXEDTql/api/twttrapi

## Installation

Copy the `twttrapi.py` file into your project directory.

## Usage

Import the `TwttrAPIClient` class and instantiate it with your RapidAPI key:

```python
from twttrapi import TwttrAPIClient

api_key = "your_rapidapi_key_here"
client = TwttrAPIClient(api_key)
```

## Methods

Here is a list of methods available in the `TwttrAPIClient` class:

* `get_tweet(tweet_id)`
* `get_tweet_conversation(tweet_id)`
* `user_tweets(username=None, user_id=None, cursor=None)`
* `user_media(username=None, user_id=None, cursor=None)`
* `user_likes(username=None, user_id=None, cursor=None)`
* `for_you_timeline(cursor=None)`
* `following_timeline(cursor=None)`
* `create_tweet(tweet_text, attachment_url=None, in_reply_to_tweet_id=None, media_id=None)`
* `delete_tweet(tweet_id)`
* `get_user(username=None)`
* `user_followers(username=None, user_id=None, cursor=None)`
* `user_following(username=None, user_id=None, cursor=None)`
* `search_suggestions(query, cursor=None)`
* `search_top(query, cursor=None)`
* `search_latest(query, cursor=None)`
* `search_users(query, cursor=None)`
* `search_images(query, cursor=None)`
* `search_videos(query, cursor=None)`
* `login_email_username(username_or_email, password)`
* `login_2fa(login_data, response)`
* `logout()`
* `follow_user(username=None, user_id=None)`
* `unfollow_user(username=None, user_id=None)`
* `favorite_tweet(tweet_id)`
* `unfavorite_tweet(tweet_id)`
* `retweet_tweet(tweet_id)`
* `unretweet_tweet(tweet_id)`
* `get_dm_conversations(cursor=None)`
* `get_dm_conversation(username=None, user_id=None, cursor=None)`
* `send_dm(message, to_user_name=None, to_user_id=None, media_id=None)`
* `upload_image(image_url)`

For more information on each method and its parameters, please refer to the `twttrapi.py` file.

## Example

Here's an example on how to use the API wrapper:

```python
from twttrapi import TwttrAPIClient

api_key = "your_rapidapi_key_here"
client = TwttrAPIClient(api_key)

# Get a tweet by its ID
tweet_id = "1652849795336159233"
tweet = client.get_tweet(tweet_id)
print(tweet)
```
