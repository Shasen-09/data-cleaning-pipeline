import json
import csv
import os
from logger import setup_logger

logger = setup_logger()


def loadfile(filepath):
    if not os.path.exists(filepath):
        logger.error("There is no such file or directory")
        raise FileNotFoundError("No such file")

    if filepath.endswith('.csv'):
        return loadcsv(filepath)

    elif filepath.endswith('.json'):
        return loadjson(filepath)

    else:
        raise ValueError("File format not supported")


def loadcsv(filepath):
    data = []
    with open(filepath, "r", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
        logger.info(f"{len(data)} rows loaded from csv")
        return data


def loadjson(filepath):
    with open(filepath, "r", encoding='utf-8') as f:
        data = json.load(f)
    logger.info(f"{len(data)} loaded from json")
    return data
