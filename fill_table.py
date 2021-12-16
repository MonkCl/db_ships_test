import sqlite3
import random
from create_table import CreateDB


class FillTable:
    def __init__(self):
        CreateDB()
        self.db = sqlite3.connect("mydatabase.db")
        self.sql = self.db.cursor()
        self.engines, self.hulls, self.weapons, self.ships = {}, {}, {}, {}
        self.fill_all()

    def random_engine(self):
        """
        fill TABLE engines by 6 random values
        :return:
        """
        for i in range(6):
            self.engines[f'Engine-{i}'] = {'power': random.randint(1, 20),
                                           'type': random.randint(1, 20)}

        for engine in self.engines:
            sql_request = "INSERT INTO engines (`engine`,`power`,`type`)" \
                          "VALUES ('{0}', {1}, {2})".format(engine,
                                                            self.engines[engine]['power'],
                                                            self.engines[engine]['type'])
            self.sql.execute(sql_request)
            self.db.commit()

    def random_hulls(self):
        """
        fill TABLE Hulls by 5 random values
        :return:
        """
        for i in range(5):
            self.hulls[f'Hull-{i}'] = {'armor': random.randint(1, 20),
                                       'type': random.randint(1, 20),
                                       'capacity': random.randint(1, 20)}

        for hull in self.hulls:
            sql_request = "INSERT INTO Hulls (`hull`,`armor`,`type`,`capacity`)" \
                          "VALUES ('{0}', {1}, {2}, {3})".format(hull,
                                                                 self.hulls[hull]['armor'],
                                                                 self.hulls[hull]['type'],
                                                                 self.hulls[hull]['capacity'])
            self.sql.execute(sql_request)
            self.db.commit()

    def random_weapons(self):
        """
        fill TABLE Weapons by 20 random values
        :return:
        """
        for i in range(20):
            self.weapons[f'Weapon-{i}'] = {'reload_speed': random.randint(1, 20),
                                           'rotation_speed': random.randint(1, 20),
                                           'diameter': random.randint(1, 20),
                                           'power_volley': random.randint(1, 20),
                                           'count': random.randint(1, 20)}

        for weapon in self.weapons:
            sql_request = "INSERT INTO Weapons (`weapon`,`reload_speed`,`rotation_speed`,`diameter`,`power_volley`,`count`)" \
                          "VALUES ('{0}', {1}, {2}, {3}, {4}, {5})".format(weapon,
                                                                           self.weapons[weapon]['reload_speed'],
                                                                           self.weapons[weapon]['rotation_speed'],
                                                                           self.weapons[weapon]['diameter'],
                                                                           self.weapons[weapon]['power_volley'],
                                                                           self.weapons[weapon]['count'])
            self.sql.execute(sql_request)
            self.db.commit()

    def random_ships(self):
        """
        fill TABLE Ships by 200 random values
        :return:
        """
        for i in range(200):
            self.ships[f'Ship-{i}'] = {'weapon': random.choice(list(self.weapons)),
                                       'hull': random.choice(list(self.hulls)),
                                       'engine': random.choice(list(self.engines))}

        for ship in self.ships:
            sql_request = "INSERT INTO Ships (`ship`,`weapon`,`hull`, `engine`)" \
                          "VALUES ('{0}', '{1}', '{2}', '{3}')".format(ship,
                                                                       self.ships[ship]['weapon'],
                                                                       self.ships[ship]['hull'],
                                                                       self.ships[ship]['engine'])
            self.sql.execute(sql_request)
            self.db.commit()

    def fill_all(self):
        """
        Fill all tables in database
        :return:
        """
        self.random_engine()
        self.random_hulls()
        self.random_weapons()
        self.random_ships()
