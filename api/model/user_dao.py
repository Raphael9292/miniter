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


class UserDao:
    def __init__(self, database):
        self.db = database

    def insert_user(self, user):
        return self.db.execute(text("""
            INSERT INTO users (
                name,
                email,
                profile,
                hashed_password
            ) VALUES (
                :name,
                :email,
                :profile,
                :password
            )
        """), user).lastrowid

    def get_user_id_and_password(self, email):
        row = self.db.execute(text("""    
            SELECT
                id,
                hashed_password
            FROM users
            WHERE email = :email
        """), {'email': email}).fetchone()

        return {
            'id': row['id'],
            'hashed_password': row['hashed_password']
        } if row else None

    def insert_follow(self, user_id, follow_id):
        return self.db.execute(text("""
            INSERT INTO users_follow_list (
                user_id,
                follow_user_id
            ) VALUES (
                :id,
                :follow
            )
        """), {
            'id': user_id,
            'follow': follow_id
        }).rowcount

    def insert_unfollow(self, user_id, unfollow_id):
        return self.db.execute(text("""
            DELETE FROM users_follow_list
            WHERE user_id      = :id
            AND follow_user_id = :unfollow
        """), {
            'id': user_id,
            'unfollow': unfollow_id
        }).rowcount
