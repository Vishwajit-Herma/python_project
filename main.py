import asyncio

from app.api_async import fetch_all
from app.processor import (
    filter_users_with_email,
    map_user_names
)
from app.storage import save_json
from app.concurrency import (
    fetch_data_with_threads,
    process_data_with_multiprocessing
)
from app.exceptions import APIError, DataProcessingError, StorageError


def main():
    try:
        print("Application started")

        # -------- THREADING FUNCTIONALITY --------
        result = fetch_data_with_threads()

        users = result["users"]
        posts = result["posts"]

        # -------- PROCESSING --------
        filtered_users = filter_users_with_email(users)
        user_names = map_user_names(users)

        # -------- MULTIPROCESSING FUNCTIONALITY --------
        
        users_count, posts_count = process_data_with_multiprocessing(users, posts)

        print(f"Users count: {users_count}")
        print(f"Posts count: {posts_count}")

        # -------- STORAGE --------
        save_json("users.json", users)
        save_json("filtered_users.json", filtered_users)
        save_json("user_names.json", user_names)
        save_json("posts.json", posts)

        # -------- ASYNC --------
        asyncio.run(fetch_all())

        print("Application finished successfully")

    except (APIError, DataProcessingError, StorageError) as e:
        print(f"Application error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
