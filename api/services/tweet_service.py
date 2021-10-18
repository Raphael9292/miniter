"""
Business Layer: 실제 시스템이 구현해야 하는 로직
사용자 관련 로직, tweet 관련 로직
"""


class TweetService:
    def __init__(self, tweet_dao):
        self.tweet_dao = tweet_dao

    def tweet(self, user_id, tweet):
        if len(tweet) > 300:
            return None

        return self.tweet_dao.insert_tweet(user_id, tweet)

    def get_timeline(self, user_id):
        return self.tweet_dao.get_timeline(user_id)
