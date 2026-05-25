from logger import setup_logger
from loader import loadfile
from cleaner import clean_data
from validator import validate_rows


def main():

    logger = setup_logger()

    logger.info("Application started")

    filepath = input("Enter:")
    logger.info(f"Loading file: {filepath}")

    raw_data = loadfile(filepath)
    logger.info(f"Loaded {len(raw_data)} rows from file")

    cleaned = clean_data(raw_data)
    logger.info(f"Cleaned data: {len(cleaned)} valid rows")

    validated = validate_rows(cleaned)
    logger.info(f"Validated data: {len(validated)} final records")

    print(f"\nTOTAL CLEANED: {len(cleaned)}")
    print(f"VALIDATED: {len(validated)}")
    print(f"{validated}")


if __name__ == "__main__":
    main()
