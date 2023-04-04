import roman
from tqdm import tqdm


def prepare_dataset():
    for filename in ["dataset.csv", "dataset-escales.csv"]:
        # remove first line of dataset.csv and dataset-escales.csv
        # if it contains the column names
        with open("dataset/" + filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("dataset/" + filename, "w", encoding="utf-8") as f:
            for line in lines:
                if line.startswith("\ufeffExpédition;"):
                    continue
                f.write(line)

    # remove all non-breaking spaces if they exist
        with open("dataset/" + filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("dataset/" + filename, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line.replace("\xa0", ""))

    # remove all spaces after semicolons
        with open("dataset/" + filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("dataset/" + filename, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line.replace("; ", ";"))

    # remove all spaces after commas
        with open("dataset/" + filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("dataset/" + filename, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line.replace(", ", ","))


# retrieve a dictionnary of all expeditions and their data
def get_expeditions():
    with open("dataset/dataset.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        expeditions = {}
        for line in tqdm(lines, desc="Lecture de dataset.csv", total=len(lines)):
            expedition, boat, crew_member, crew_leader = line.strip().split(";")
            expedition = roman.fromRoman(expedition)
            if expedition not in expeditions:
                expeditions[expedition] = {"boat": boat, "crew": [], "leader": None}
            expeditions[expedition]["crew"].append(crew_member)
            if crew_leader != "":
                expeditions[expedition]["leader"] = crew_leader
    with open("dataset/dataset-escales.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in tqdm(lines, desc="Lecture de dataset-escales.csv", total=len(lines)):
            expedition, divinity, stops = line.strip().split(";")
            expedition = roman.fromRoman(expedition)
            if expedition not in expeditions:
                expeditions[expedition] = {"boat": None, "crew": [], "leader": None}
            expeditions[expedition]["divinity"] = divinity
            stops = stops.split(",")
            expeditions[expedition]["stops"] = stops
    return expeditions
