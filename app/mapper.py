from app.models import User, Post


def map_users(user_dicts):
    return [
        User(
            user_id=u["id"],
            name=u["name"],
            email=u["email"]
        )
        for u in user_dicts
    ]


def map_posts(post_dicts):
    return [
        Post(
            post_id=p["id"],
            user_id=p["userId"],
            title=p["title"]
        )
        for p in post_dicts
    ]
