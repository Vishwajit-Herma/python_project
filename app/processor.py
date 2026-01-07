from functools import reduce

def filter_users_with_email(users):
    return list(filter(lambda u: "@" in u["email"], users))


def map_user_names(users):
    return list(map(lambda u: u["name"], users))


def count_posts(posts):
    return reduce(lambda acc, _: acc + 1, posts, 0)


def user_generator(users):
    for user in users:
        yield user["name"]
