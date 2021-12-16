import sqlite3


class CreateDB:
    def __init__(self):
        self.db = sqlite3.connect("mydatabase.db")
        self.sql = self.db.cursor()

        try:
            self.sql.execute("""DROP TABLE Weapons""")
            self.sql.execute("""DROP TABLE Hulls""")
            self.sql.execute("""DROP TABLE Engines""")
            self.sql.execute("""DROP TABLE Ships""")
        except:
            pass

        self.sql.execute("""CREATE TABLE Weapons(
                        weapon VARCHAR(255) PRIMARY KEY,
                        reload_speed INT,
                        rotation_speed INT,
                        diameter INT,
                        power_volley INT,
                        count INT
                        )""")

        self.sql.execute("""CREATE TABLE Hulls(
                        hull VARCHAR(255) PRIMARY KEY,
                        armor INT,
                        type INT,
                        capacity INT
                        )""")

        self.sql.execute("""CREATE TABLE Engines(
                        engine VARCHAR(255) PRIMARY KEY,
                        power INT,
                        type INT
                        )""")

        self.sql.execute("""CREATE TABLE Ships(
                            ship VARCHAR(255) PRIMARY KEY,
                            weapon VARCHAR(255),
                            hull VARCHAR(255),
                            engine VARCHAR(255),
                            FOREIGN KEY (weapon) REFERENCES weapons(weapon),
                            FOREIGN KEY (hull) REFERENCES hulls(hull),
                            FOREIGN KEY (engine) REFERENCES engines(engine)
                        )""")



