from pydantic import ValidationError
from schema import UserSchema


def validate_rows(data):

    valid = []

    for row in data:
        if not isinstance(row, dict):
            continue

        try:
            validated = UserSchema(**row)
            valid.append(validated.model_dump())

        except ValidationError as e:
            print("\nVALIDATION FAILED:")
            print(row)
            print(e)

        except TypeError as e:
            print("\nTYPE ERROR (bad row structure):")
            print(row)
            print(e)

    return valid
