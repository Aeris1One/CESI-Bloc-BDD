import sqlite3
import logging
import dataset.dataset as dataset
from tqdm import tqdm

# Use PyCharm log format
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logs = logging.getLogger(__name__)


def connect_db():
    logs.debug("Connexion à la base de données")
    return sqlite3.connect("database/database.db")


def init_db(db):
    logs.debug("Éxécution de schema.sql")
    with open("database/schema.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    logs.debug("Éxécution de schema.sql terminée")

# We have a dictionnary of all expeditions and their data
# We need to store it in the database using the following schema:
# - expedition
#   - id (unique)
#   - Nom_bateau (foreign key, boat)
#   - Nom_heros (foreign key, leader)
#   - Nom_divinite (foreign key, divinity)
# - Bateau
#   - Nom_bateau (unique)
# - Heros
#   - Nom_heros (unique)
# - Divinites
#   - Nom_divinite (unique)
# - Lieu
#   - Nom_lieu (unique)
# - escales
#   - Nom_lieu (foreign key, stops)
#   - Numero (foreign key, expedition)
# - equipage
#   - Nom_heros (foreign key, crew)
#   - Numero (foreign key, expedition)

def insert_divinities(db, expeditions):
    for expedition in tqdm(expeditions, desc="Insertion des divinités dans la base de données", total=len(expeditions)):
        divinity = expeditions[expedition]["divinity"]
        # insert if not exists
        db.execute("INSERT OR IGNORE INTO Divinites (Nom_divinite) VALUES (?)", (divinity,))
        db.commit()

def insert_boats(db, expeditions):
    for expedition in tqdm(expeditions, desc="Insertion des bateaux dans la base de données", total=len(expeditions)):
        boat = expeditions[expedition]["boat"]
        # insert if not exists
        db.execute("INSERT OR IGNORE INTO Bateau (Nom_bateau) VALUES (?)", (boat,))
        db.commit()

def insert_heros(db, expeditions):
    for expedition in tqdm(expeditions, desc="Insertion des héros dans la base de données", total=len(expeditions)):
        crew = expeditions[expedition]["crew"]
        for member in crew:
            # insert if not exists
            db.execute("INSERT OR IGNORE INTO Heros (Nom_heros) VALUES (?)", (member,))
            db.commit()

def insert_locations(db, expeditions):
    for expedition in tqdm(expeditions, desc="Insertion des escales dans la base de données", total=len(expeditions)):
        stops = expeditions[expedition]["stops"]
        for stop in stops:
            # insert if not exists
            db.execute("INSERT OR IGNORE INTO Lieu (Nom_lieu) VALUES (?)", (stop,))
            db.commit()

def insert_crews(db, expeditions):
    for expedition in tqdm(expeditions, desc="Insertion des équipages dans la base de données", total=len(expeditions)):
        crew = expeditions[expedition]["crew"]
        for member in crew:
            # insert if not exists
            db.execute("INSERT OR IGNORE INTO equipage (Nom_heros, Numero) VALUES (?, ?)", (member, expedition))
            db.commit()

def insert_stops(db, expeditions):
    for expedition in tqdm(expeditions, desc="Insertion des escales dans la base de données", total=len(expeditions)):
        stops = expeditions[expedition]["stops"]
        n = 0
        for stop in stops:
            # insert if not exists
            db.execute("INSERT OR IGNORE INTO escales (Nom_lieu, Numero, Ordre) VALUES (?, ?, ?)", (stop, expedition, n))
            db.commit()
            n+=1

def insert_expeditions(db, expeditions):
    for expedition in tqdm(expeditions, desc="Insertion des expéditions dans la base de données", total=len(expeditions)):
        boat = expeditions[expedition]["boat"]
        leader = expeditions[expedition]["leader"]
        divinity = expeditions[expedition]["divinity"]
        # insert if not exists
        db.execute("INSERT OR IGNORE INTO Expedition (Numero, Nom_bateau, Nom_heros, Nom_divinite) VALUES (?, ?, ?, ?)",
                   (expedition, boat, leader, divinity))
        db.commit()

if __name__ == '__main__':
    db = connect_db()
    init_db(db)
    dataset.prepare_dataset()
    expeditions = dataset.get_expeditions()
    insert_divinities(db, expeditions)
    insert_boats(db, expeditions)
    insert_heros(db, expeditions)
    insert_locations(db, expeditions)
    insert_crews(db, expeditions)
    insert_stops(db, expeditions)
    insert_expeditions(db, expeditions)

