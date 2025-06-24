from pydantic import BaseModel, EmailStr, conint, ValidationError

class UserProfile(BaseModel):
    name: str
    email: EmailStr
    age: conint(ge=18, le=100)  # constrained int: 18 ≤ age ≤ 100

# Example usage
try:
    user = UserProfile(
        name = "harika",
        email = "harika@example.com",
        age = 28
    )
    print("✅ User profile created successfully:")
    print(user.model_dump_json(indent=4))
except ValidationError as e:
    print("❌ Validation error:")
    print(e)

