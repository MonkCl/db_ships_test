from fill_table import *
from copy_change import *
import pytest


# class TestCopyChange:
#     def __init__(self):
#         self.mainDB = FillTable()
#         self.copyDB = CopyChange()
#
#         self.engines = self.mainDB.engines
#         self.weapons = self.mainDB.weapons
#         self.hulls = self.mainDB.hulls
#         self.ships = self.mainDB.ships
#
#         self._engines = self.copyDB.engines
#         self._weapons = self.copyDB.weapons
#         self._hulls = self.copyDB.hulls
#         self._ships = self.copyDB.ships
#         # print(self.engines)
#         # print(self._engines)
#         # print(self.weapons)
#         # print(self._weapons)
#         # print(self.hulls)
#         # print(self._hulls)
#         print(self.ships)
#         print(self._ships)
#
#     def test_change_in_ship(self):
#         for ship in self.ships:
#             weapon1 = self.ships[ship]["weapon"]
#             weapon2 = self._ships[ship]["weapon"]
#             if weapon1 != weapon2:
#                 assert f'{ship}, {weapon2}\n\tExpected weapon {weapon1}, was {weapon2}'
#
#     def test_change_engine(self):
#         pass
#
#     def test_change_hull(self):
#         pass
#
#     def test_change_weapon(self):
#         pass


def get_tables():
    global engines
    global hulls
    global weapons
    global ships
    global _engines
    global _hulls
    global _weapons
    global _ships
    db = sqlite3.connect("mydatabase.db")
    sql = db.cursor()

    for engine in sql.execute("SELECT * FROM Engines"):
        engines[engine[0]] = {'power': engine[1],
                              'type': engine[2]}
    for hull in sql.execute("SELECT * FROM Hulls"):
        hulls[hull[0]] = {'armor': hull[1],
                          'type': hull[2],
                          'capacity': hull[3]}
    for weapon in sql.execute("SELECT * FROM Weapons"):
        weapons[weapon[0]] = {'reload_speed': weapon[1],
                              'rotation_speed': weapon[2],
                              'diameter': weapon[3],
                              'power_volley': weapon[4],
                              'count': weapon[5]}
    for ship in sql.execute("SELECT * FROM Ships"):
        ships[ship[0]] = {'weapon': ship[1],
                          'hull': ship[2],
                          'engine': ship[3]}

    db = sqlite3.connect("copy.db")
    sql = db.cursor()

    for engine in sql.execute("SELECT * FROM Engines"):
        _engines[engine[0]] = {'power': engine[1],
                               'type': engine[2]}
    for hull in sql.execute("SELECT * FROM Hulls"):
        _hulls[hull[0]] = {'armor': hull[1],
                           'type': hull[2],
                           'capacity': hull[3]}
    for weapon in sql.execute("SELECT * FROM Weapons"):
        _weapons[weapon[0]] = {'reload_speed': weapon[1],
                               'rotation_speed': weapon[2],
                               'diameter': weapon[3],
                               'power_volley': weapon[4],
                               'count': weapon[5]}
    for ship in sql.execute("SELECT * FROM Ships"):
        _ships[ship[0]] = {'weapon': ship[1],
                           'hull': ship[2],
                           'engine': ship[3]}

    print(engines, _engines, hulls, _hulls, weapons, _weapons, ships, _ships, sep='\n')
    return engines, hulls, weapons, ships, _engines, _hulls, _weapons, _ships


engines, hulls, weapons, ships = {}, {}, {}, {}
_engines, _hulls, _weapons, _ships = {}, {}, {}, {}
get_tables()


# print("------", engines, _engines, hulls, _hulls, weapons, _weapons, ships, _ships, "------", sep='\n')

# def check_ship_weapon(weapon1, weapon2):
#     yield weapon1 == weapon2
#     # assert weapon1 != weapon2
#
#
# def test_ship_weapon():
#     for ship in ships:
#         weapon1 = ships[ship]["weapon"]
#         weapon2 = _ships[ship]["weapon"]
#         # yield weapon1 == weapon2
#         check_ship_weapon(weapon1, weapon2)


@pytest.mark.parametrize('ship', ships)
def test_ship_weapon(ship):
    weapon = ships[ship]["weapon"]
    _weapon = _ships[ship]["weapon"]
    message = f"\n{ship},{weapon}"
    assert weapon == _weapon, message + f'\n\texpected {weapon}, was {_weapon}'
    assert weapons[weapon]["reload_speed"] == _weapons[_weapon][
        "reload_speed"], message + f'\n\treload_speed: expected {weapons[weapon]["reload_speed"]}' \
                                   f'was: {_weapons[_weapon]["reload_speed"]}'
    assert weapons[weapon]["rotation_speed"] == _weapons[_weapon][
        "rotation_speed"], message + f'\n\trotation_speed: expected {weapons[weapon]["rotation_speed"]}, was  {_weapons[_weapon]["rotation_speed"]}'
    assert weapons[weapon]["diameter"] == _weapons[_weapon][
        "diameter"], message + f'\n\tdiameter: expected {weapons[weapon]["diameter"]}, was  {_weapons[_weapon]["diameter"]}'
    assert weapons[weapon]["power_volley"] == _weapons[_weapon][
        "power_volley"], message + f'\n\tpower_volley: expected {weapons[weapon]["power_volley"]}, was  {_weapons[_weapon]["power_volley"]}'
    assert weapons[weapon]["count"] == _weapons[_weapon][
        "count"], message + f'\n\tcount: expected {weapons[weapon]["count"]}, was  {_weapons[_weapon]["count"]}'


@pytest.mark.parametrize('ship', ships)
def test_ship_engine(ship):
    engine = ships[ship]["engine"]
    _engine = _ships[ship]["engine"]
    message = f"\n\n\n{ship},{engine}"
    assert engine == _engine, message + f'\n\texpected {engine}, was {_engine}'
    assert engines[engine]["power"] == _engines[_engine][
        "power"], message + f'\n\tpower: expected {engines[engine]["power"]}, was {_engines[_engine]["power"]}'
    assert engines[engine]["type"] == _engines[_engine][
        "type"], message + f'\n\ttype: expected {engines[engine]["type"]}, was {_engines[_engine]["type"]}'


@pytest.mark.parametrize('ship', ships)
def test_ship_hull(ship):
    hull = ships[ship]["hull"]
    _hull = _ships[ship]["hull"]
    message = f"\n\n\n{ship},{hull}"
    assert hull == _hull, message + f'\n\texpected {hull}, was {_hull}'
    assert hulls[hull]["armor"] == _hulls[_hull][
        "armor"], message + f'\n\tarmor: expected {hulls[hull]["armor"]}, was {_hulls[_hull]["armor"]}'
    assert hulls[hull]["type"] == _hulls[_hull][
        "type"], message + f'\n\ttype: expected {hulls[hull]["type"]}, was {_hulls[_hull]["type"]}'
    assert hulls[hull]["capacity"] == _hulls[_hull][
        "capacity"], message + f'\n\tcapacity: expected {hulls[hull]["capacity"]}, was {_hulls[_hull]["capacity"]}'
