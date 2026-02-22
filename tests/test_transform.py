from app.mask import mask_email
from app.transform import transform_users


def test_mask_email():
    email = "john.doe@gmail.com"
    masked = mask_email(email)
    assert masked == "j***@gmail.com"


def test_transform_users():
    sample_input = [
        {
            "name": {"first": "John", "last": "Doe"},
            "email": "john.doe@gmail.com",
            "dob": {"age": 30},
            "location": {"country": "UK"}
        }
    ]

    result = transform_users(sample_input)

    assert len(result) == 1
    assert result[0]["full_name"] == "John Doe"
    assert result[0]["email"] == "j***@gmail.com"
    assert result[0]["age"] == 30
    assert result[0]["country"] == "UK"