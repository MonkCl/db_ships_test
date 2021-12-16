import pytest
import shutil
import sqlite3
import random


# @pytest.fixture(scope='session')
# def copy_table():
#     shutil.copyfile('mydatabase.db', 'mydatabase1.db')

class CopyChange:
    def __init__(self):
        self.engines, self.hulls, self.weapons, self.ships = {}, {}, {}, {}
        shutil.copyfile('mydatabase.db', 'copy.db')
        self.db = sqlite3.connect("copy.db")
        self.sql = self.db.cursor()
        for engine in self.sql.execute("SELECT * FROM Engines"):
            self.engines[engine[0]] = {'power': engine[1],
                                       'type': engine[2]}
        for hull in self.sql.execute("SELECT * FROM Hulls"):
            self.hulls[hull[0]] = {'armor': hull[1],
                                   'type': hull[2],
                                   'capacity': hull[3]}
        for weapon in self.sql.execute("SELECT * FROM Weapons"):
            self.weapons[weapon[0]] = {'reload_speed': weapon[1],
                                       'rotation_speed': weapon[2],
                                       'diameter': weapon[3],
                                       'power_volley': weapon[4],
                                       'count': weapon[5]}
        for ship in self.sql.execute("SELECT * FROM Ships"):
            self.ships[ship[0]] = {'weapon': ship[1],
                                   'hull': ship[2],
                                   'engine': ship[3]}

        self.change_engine()
        self.change_hull()
        self.change_weapon()
        self.change_ship()

    def change_engine(self):
        """
        change values in TABLE engines
        :return:
        """
        # sql_request = "SELECT Engine FROM Engines"
        # for engine in self.sql.execute(sql_request):
        #     self.engines.append(engine[0])

        for engine in self.engines:
            columns = ['power', 'type']
            change_column = random.choice(columns)
            value = random.randint(1, 20)
            sql_request = f'UPDATE Engines SET {change_column} = {value} WHERE Engine = "{engine}"'
            self.sql.execute(sql_request)
            self.db.commit()
            self.engines[engine][change_column] = value

    def change_hull(self):
        """
        change values in TABLE hulls
        :return:
        """
        # sql_request = "SELECT Hull FROM Hulls"
        # for hull in self.sql.execute(sql_request):
        #     self.hulls.append(hull[0])

        for hull in self.hulls:
            columns = ['armor', 'type', 'capacity']
            change_column = random.choice(columns)
            value = random.randint(1, 20)
            sql_request = f'UPDATE Hulls SET {change_column} = {value} WHERE Hull = "{hull}"'
            self.sql.execute(sql_request)
            self.db.commit()
            self.hulls[hull][change_column] = value

    def change_weapon(self):
        """
        change values in TABLE weapon
        :return:
        """
        # sql_request = "SELECT Weapon FROM Weapons"
        # for weapon in self.sql.execute(sql_request):
        #     self.weapons.append(weapon[0])

        for weapon in self.weapons:
            columns = ['reload_speed', 'rotation_speed', 'diameter', 'power_volley', 'count']
            change_column = random.choice(columns)
            value = random.randint(1, 20)
            sql_request = f'UPDATE Weapons SET {change_column} = {value} WHERE Weapon = "{weapon}"'
            self.sql.execute(sql_request)
            self.db.commit()
            self.weapons[weapon][change_column] = value

    def change_ship(self):
        """
        change values in TABLE ships
        :return:
        """
        for ship in self.ships:
            columns = ['weapon', 'hull', 'engine']
            change_column = random.choice(columns)
            value = ''
            if change_column == 'weapon':
                value = random.choice(list(self.weapons))
            elif change_column == 'hull':
                value = random.choice(list(self.hulls))
            elif change_column == 'engine':
                value = random.choice(list(self.engines))
            sql_request = f'UPDATE Ships SET {change_column} = "{value}" WHERE Ship = "{ship}"'
            self.sql.execute(sql_request)
            self.db.commit()
            self.ships[ship][change_column] = value

# change = CopyChange()
# change.change_ship()
# change.change_weapon()
# change.change_engine()
# change.change_hull()
