import sqlite3
import os

DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "rpg_db.sqlite3")
conn = sqlite3.connect(DATABASE_FILEPATH)
curs = conn.cursor()
#- How many total Characters are there?
query1 = 'SELECT count(distinct character_id) FROM charactercreator_character'
result1 = curs.execute(query1).fetchall()[0]
print("There are", result1[0], "total characters.")

#- How many of each specific subclass?
query2 = 'SELECT count() FROM charactercreator_cleric'
result2 = curs.execute(query2).fetchall()[0]
print("There are", result2[0], "clerics.")

query2 = 'SELECT count() FROM charactercreator_fighter'
result2 = curs.execute(query2).fetchall()[0]
print("There are", result2[0], "fighters.")

query2 = 'SELECT count() FROM charactercreator_mage'
result2 = curs.execute(query2).fetchall()[0]
print("There are", result2[0], "mages.")

query2 = 'SELECT count() FROM charactercreator_necromancer'
result2 = curs.execute(query2).fetchall()[0]
print("There are", result2[0], "necromancers.")

query2 = 'SELECT count() FROM charactercreator_thief'
result2 = curs.execute(query2).fetchall()[0]
print("There are", result2[0], "thieves.")

#- How many total Items?
query1 = 'SELECT count(distinct item_id) FROM armory_item'
items = curs.execute(query1).fetchall()[0]
print("There are", items[0], "total items.")

#- How many of the Items are weapons? How many are not?
query1 = 'SELECT count(distinct item_ptr_id) FROM armory_weapon'
weapons = curs.execute(query1).fetchall()[0]
print("There are", weapons[0], "items that are weapons.")

nonweapons = items[0] - weapons[0]
print("There are", nonweapons, "items that are not weapons.")
#- How many Items does each character have? (Return first 20 rows)
query1 = '''SELECT 
  charactercreator_character_inventory.character_id
  ,count(distinct charactercreator_character_inventory.item_id) as itemcount
  ,count(distinct armory_weapon.item_ptr_id) as weaponcount
FROM charactercreator_character_inventory
LEFT JOIN armory_item ON charactercreator_character_inventory.item_id = armory_item.item_id
LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id 
ORDER BY charactercreator_character_inventory.character_id 
LIMIT 20'''
table1 = curs.execute(query1).fetchall()

for row in table1:
    if row[1] > 1:
        print ("Character", row[0], "has", row[1], "items.")
    else:
        print ("Character", row[0], "has", row[1], "item.")
    
#- How many Weapons does each character have? (Return first 20 rows)
for row in table1:
    if row[1] > 1:
        print ("Character", row[0], "has", row[2], "weapons.")
    else:
        print ("Character", row[0], "has", row[2], "weapon.")
#- On average, how many Items does each Character have?
query = '''SELECT 
  AVG(itemcount)
  ,avg(weaponcount)
FROM (
	SELECT 
  		charactercreator_character_inventory.character_id
 		,count(distinct charactercreator_character_inventory.item_id) as itemcount
  		,count(distinct armory_weapon.item_ptr_id) as weaponcount
		FROM charactercreator_character_inventory
		LEFT JOIN armory_item ON charactercreator_character_inventory.item_id = armory_item.item_id
		LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
		GROUP BY charactercreator_character_inventory.character_id 
		ORDER BY charactercreator_character_inventory.character_id 
) subq'''
table = curs.execute(query).fetchall()
print("On avereage each character has", table[0][0], "items.")
#- On average, how many Weapons does each character have?
print("On avereage each character has", table[0][1], "weapons.")
