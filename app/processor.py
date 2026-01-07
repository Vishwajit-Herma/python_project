from functools import reduce
from app.logger import logger
from app.exceptions import DataProcessingError


def filter_users_with_email(users):
    try:
        return list(filter(lambda u: "@" in u.get("email", ""), users))
    except Exception as e:
        logger.error(f"Filtering users failed: {e}")
        raise DataProcessingError("User filtering failed")


def map_user_names(users):
    try:
        return list(map(lambda u: u["name"], users))
    except Exception as e:
        logger.error(f"Mapping user names failed: {e}")
        raise DataProcessingError("User name mapping failed")


def count_total_posts(posts):
    try:
        return reduce(lambda acc, _: acc + 1, posts, 0)
    except Exception as e:
        logger.error(f"Counting posts failed: {e}")
        raise DataProcessingError("Post counting failed")
    
    
def user_name_generator(users):
    try:
        for user in users:
            yield user["name"]
    except Exception as e:
        logger.error(f"User name generator failed: {e}")
        raise DataProcessingError("User name generation failed")