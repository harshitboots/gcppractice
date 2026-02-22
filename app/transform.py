from app.msk import mask_email


def transform_users(users):
    """
    Transform raw API users into structured dataset.
    Extract:
        - full_name
        - masked_email
        - age
        - country
    """

    transformed = []

    for user in users:
        transformed.append({
            "full_name": user["name"]["first"] + " " + user["name"]["last"],
            "email": mask_email(user["email"]),
            "age": user["dob"]["age"],
            "country": user["location"]["country"]
        })

    return transformed