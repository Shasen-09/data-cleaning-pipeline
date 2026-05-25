import re
from datetime import datetime


def clean_email(email):

    if not email:
        return None

    email = str(email).strip().lower()

    if "@" not in email:
        return None

    domain = email.split("@")[-1]

    if "." not in domain:
        return None

    return email


def clean_age(age):

    age = str(age)
    age = re.sub(r"\D", "", age)

    if not age:
        return None

    try:
        age = int(age)
    except:
        return None

    if age < 0 or age > 120:
        return None

    return age


def clean_salary(salary):

    if not salary:
        return None

    salary = str(salary)
    salary = re.sub(r"[^\d.]", "", salary)

    if not salary:
        return None

    try:
        return float(salary)
    except:
        return None


def clean_date(value):

    if not value:
        return None

    value = str(value).strip()

    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%Y/%m/%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).date()
        except:
            continue

    return None


def clean_data(data):

    cleaned = []

    for row in data:

        if not isinstance(row, dict):
            continue

        try:
            cleaned_row = {
                "name": str(row.get("name", "")).strip().lower() or None,
                "email": clean_email(row.get("email")),
                "age": clean_age(row.get("age")),
                "salary": clean_salary(row.get("salary")),
                "created_at": clean_date(row.get("created_at")),
            }

            if (
                not cleaned_row["name"]
                or not cleaned_row["email"]
                or cleaned_row["age"] is None
            ):
                continue

            cleaned.append(cleaned_row)

        except Exception:
            continue

    return cleaned
