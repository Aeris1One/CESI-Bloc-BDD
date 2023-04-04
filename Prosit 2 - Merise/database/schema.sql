--------------------------------------------------------------
--        Script MySQL.
--------------------------------------------------------------


--------------------------------------------------------------
-- Table: Bateau
--------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Bateau(
        Nom_bateau Text NOT NULL
	,CONSTRAINT Bateau_PK PRIMARY KEY (Nom_bateau)
);


--------------------------------------------------------------
-- Table: Héros
--------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Heros(
        Nom_heros Text NOT NULL
	,CONSTRAINT Heros_PK PRIMARY KEY (Nom_heros)
);


--------------------------------------------------------------
-- Table: Lieu
--------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Lieu(
        Nom_lieu Text NOT NULL
	,CONSTRAINT Lieu_PK PRIMARY KEY (Nom_lieu)
);


--------------------------------------------------------------
-- Table: Divinités
--------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Divinites(
        Nom_divinite Text NOT NULL
	,CONSTRAINT Divinites_PK PRIMARY KEY (Nom_divinite)
);


--------------------------------------------------------------
-- Table: Expédition
--------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Expedition(
        Numero       Int NOT NULL ,
        Nom_bateau   Text NOT NULL ,
        Nom_heros    Text NOT NULL ,
        Nom_divinite Text NOT NULL
	,CONSTRAINT expedition_PK PRIMARY KEY (Numero)

	,CONSTRAINT expedition_Bateau_FK FOREIGN KEY (Nom_bateau) REFERENCES Bateau(Nom_bateau)
	,CONSTRAINT expedition_Heros0_FK FOREIGN KEY (Nom_heros) REFERENCES Heros(Nom_heros)
	,CONSTRAINT expedition_Divinites1_FK FOREIGN KEY (Nom_divinite) REFERENCES Divinites(Nom_divinite)
);


--------------------------------------------------------------
-- Table: équipage
--------------------------------------------------------------

CREATE TABLE IF NOT EXISTS equipage(
        Nom_heros Text NOT NULL ,
        Numero    Int NOT NULL
	,CONSTRAINT equipage_PK PRIMARY KEY (Nom_heros,Numero)

	,CONSTRAINT equipage_Heros_FK FOREIGN KEY (Nom_heros) REFERENCES Heros(Nom_heros)
	,CONSTRAINT equipage_expedition0_FK FOREIGN KEY (Numero) REFERENCES expedition(Numero)
);


--------------------------------------------------------------
-- Table: escales
--------------------------------------------------------------

CREATE TABLE IF NOT EXISTS escales(
        Nom_lieu Text NOT NULL ,
        Numero   Int NOT NULL ,
        Ordre    Int NOT NULL
	,CONSTRAINT escales_PK PRIMARY KEY (Nom_lieu,Numero)

	,CONSTRAINT escales_Lieu_FK FOREIGN KEY (Nom_lieu) REFERENCES Lieu(Nom_lieu)
	,CONSTRAINT escales_expedition0_FK FOREIGN KEY (Numero) REFERENCES expedition(Numero)
);