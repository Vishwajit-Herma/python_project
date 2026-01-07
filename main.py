import asyncio
from app.api_sync import fetch_users, fetch_posts
from app.api_async import fetch_all
from app.processor import filter_users_with_email, map_user_names
from app.storage import save_json
from app.concurrency import run_threading, run_multiprocessing

def main():
    users = fetch_users()
    posts= fetch_posts()

    filtered_users = filter_users_with_email(users)
    user_names = map_user_names(users)

    save_json("data/users.json", users)
    save_json("data/posts.json", posts)
    save_json("data/processed_data.json", user_names)

    asyncio.run(fetch_all())

    run_threading()
    run_multiprocessing()

    if __name__ == "__main__":
        main()

