from app.fetch import fetch_users
from app.transform import transform_users
from app.writer import write_to_parquet


def run_pipeline():
    print("Fetching users...")
    users = fetch_users()

    print("Transforming users...")
    transformed = transform_users(users)

    print("Writing to parquet...")
    write_to_parquet(transformed)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()