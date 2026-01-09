from functools import reduce
from app.logger import logger
from app.exceptions import DataProcessingError


def filter_users_by_email_domain(users):
    try:
        return [
            user for user in users
            if user.email.endswith((".org", ".biz"))
        ]
        # return list(
        #     filter(lambda user: user.email.endswith((".org", ".biz")), users)
        # )

    except Exception as e:
        logger.error(f"Filtering users failed: {e}")
        raise DataProcessingError("User filtering failed")


def map_user_names(users):
    try:
        return [user.name for user in users]
        # return list(map(lambda user: user.name, users))
    except Exception as e:
        logger.error(f"Mapping user names failed: {e}")
        raise DataProcessingError("User name mapping failed")


def count_total_posts(posts):
    try:
        return reduce(lambda acc, _: acc + 1, posts, 0)
    except Exception as e:
        logger.error(f"Counting posts failed: {e}")
        raise DataProcessingError("Post counting failed")

def active_user_generator(users):
    for user in users:
        if user.email.endswith((".org", ".biz")):
            yield user
