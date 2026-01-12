import asyncio
from app.api.async_ import fetch_all
from app.core.processor import (
    filter_users_by_email_domain,
    map_user_names,
    active_user_generator
)
from app.storage.sync import save_json
from app.concurrency.threads import fetch_data_with_threads
from app.concurrency.processes import process_data_with_multiprocessing 
from app.utils.exceptions import APIError, DataProcessingError, StorageError
from app.core.mapper import map_users, map_posts
from app.storage.async_ import save_json_async
from app.utils.logger import logger


def main():
    try:
        print("Application started")

        # -------- THREADING FUNCTIONALITY --------
        result = fetch_data_with_threads()
        raw_users = result["users"]
        raw_posts = result["posts"]

        users = map_users(raw_users)
        posts = map_posts(raw_posts)

        # -------- PROCESSING --------
        filtered_users = filter_users_by_email_domain(users)    
        user_names = map_user_names(users)

        # -------- MULTIPROCESSING FUNCTIONALITY --------  
        users_count, posts_count = process_data_with_multiprocessing(users, posts)

        print(f"Users count: {users_count}")
        print(f"Posts count: {posts_count}")

        # -------- STORAGE --------
        save_json("users.json", [u.to_dict() for u in users])
        save_json("posts.json", [p.to_dict() for p in posts])
        save_json("filtered_users.json", [user.to_dict() for user in filtered_users])
        save_json("user_names.json", user_names)        

        # -------- ASYNC --------
        async def async_reference_demo():

            raw_users, raw_posts = await fetch_all()

            users = map_users(raw_users)
            posts = map_posts(raw_posts)

            filtered_users = list(active_user_generator(users))
            user_names = map_user_names(users)

            await save_json_async("users_async.json", [u.to_dict() for u in users])
            await save_json_async("posts_async.json", [p.to_dict() for p in posts])
            await save_json_async("filtered_users_async.json",[u.to_dict() for u in filtered_users])
            await save_json_async("user_names_async.json", user_names)

        asyncio.run(async_reference_demo())

        print("Application finished successfully")

    except (APIError, DataProcessingError, StorageError) as e:
        logger.error(f"Application error: {e}")

    except Exception as e:
        logger.exception("Unexpected error occurred")


if __name__ == "__main__":
    main()
