### window local용 mysql 설치 
https://dev.mysql.com/downloads/windows/installer/8.0.html
root / test1234

### pk, fk에 관한 설명
https://docs.microsoft.com/ko-kr/sql/relational-databases/tables/primary-and-foreign-key-constraints?view=sql-server-ver15

```sql
create table users(
    id int not null auto_increment,
    name varchar(255) not null,
    email varchar(255) not null,
    hashed_passwd varchar(255) not null,
    profile varchar(2000) not null,
    created_at timestamp not null default current_timestamp,
    updated_at timestamp null default null on update current_timestamp,
    primary key (id),
    unique key email (email)
);

create table users_follow_list(
    user_id int not null,
    follow_user_id int not null,
    created_at timestamp not null default current_timestamp,
    primary key (user_id, follow_user_id),
    constraint users_follow_list_user_id_fkey foreign key (user_id) references users(id),
    constraint users_follow_list_follow_user_id_fkey foreign key (follow_user_id) references users(id)
);

create table tweets(
    id int not null auto_increment,
    user_id int not null,
    tweet varchar(300) not null,
    created_at timestamp not null default current_timestamp,
    primary key (id),
    constraint tweets_user_id_fkey foreign key (user_id) references users(id)
);
```

show tables;

explain users;  
explain users_follow_list;  
explain tweets;  


### profile_picture_add_column.sql
```sql
ALTER TABLE users ADD COLUMN profile_picture VARCHAR(255);
```
