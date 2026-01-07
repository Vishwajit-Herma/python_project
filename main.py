import asyncio
from app.api_sync import fetch_users, fetch_posts
from app.api_async import fetch_all
from app.storage import save_json
from app.concurrency import run_threading, run_multiprocessing
from app.processor import (
    filter_users_with_email,
    map_user_names,
    count_total_posts,
    user_name_generator
)
from app.exceptions import APIError, DataProcessingError, StorageError


def main():
    try:
        print("Application started")

        users = fetch_users()
        posts = fetch_posts()

        filtered_users = filter_users_with_email(users)
        user_names = map_user_names(users)
        total_posts = count_total_posts(posts)

        save_json("users.json", users)
        save_json("filtered_users.json", filtered_users)
        save_json("user_names.json", user_names)
        save_json("posts.json", posts)

        asyncio.run(fetch_all())
        run_threading()
        run_multiprocessing()

        print("Application finished successfully")

    except APIError as e:
        print(f"API Error: {e}")

    except DataProcessingError as e:
        print(f"Processing Error: {e}")

    except StorageError as e:
        print(f"Storage Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
