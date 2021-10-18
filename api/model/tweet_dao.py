from sqlalchemy import text

"""
Persistence layer: DB와 관련된 로직 구현체
DAO(Data Access Object): 데이터 접속을 담당하는 object
DAO 객체들을 통해 데이터베이스 처리를 한다.

그래서 service class들은 DAO에 의존한다.

클래스 안에서 직접 DB를 연겨하는게 아니라 외부에서 dependency를 받아서 사용하는 이유는
unit test가 간편해서이다.
외부에서 설정이 가능해야 UserDao class를 unit test하기 쉽다.
"""


class TweetDao:
    def __init__(self, database):
        self.db = database

    def insert_tweet(self, user_id, tweet):
        return self.db.execute(text("""
            INSERT INTO tweets (
                user_id,
                tweet
            ) VALUES (
                :id,
                :tweet
            )
        """), {
            'id': user_id,
            'tweet': tweet
        }).rowcount

    def get_timeline(self, user_id):
        timeline = self.db.execute(text("""
            SELECT 
                t.user_id,
                t.tweet
            FROM tweets t
            LEFT JOIN users_follow_list ufl ON ufl.user_id = :user_id
            WHERE t.user_id = :user_id 
            OR t.user_id = ufl.follow_user_id
        """), {
            'user_id': user_id
        }).fetchall()

        return [{
            'user_id': tweet['user_id'],
            'tweet': tweet['tweet']
        } for tweet in timeline]
