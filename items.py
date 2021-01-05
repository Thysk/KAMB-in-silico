"""
The file listing all of the equipment in the game,
and where needed in dictionaries for access from random number generation
"""


basic_armour = {
    0: {'Type': 'Spare Tire',
        'Armour Hits': 3,
        'Special': ['+Bouncy']},
    1: {'Type': 'Small Shield',
        'Armour Hits': 4,
        'Special': ['-Item']},
    2: {'Type': 'Leather Vest',
        'Armour Hits': 3,
        'Special': ['']},
    3: {'Type': 'Hoodie',
        'Armour Hits': 2,
        'Special': ['']},
    4: {'Type': 'Kid Clothes',
        'Armour Hits': 2,
        'Special': ['']},
    5: {'Type': 'Socks',
        'Armour Hits': 1,
        'Special': ['']},
    6: {'Type': 'NEKKID!',
        'Armour Hits': 0,
        'Special': ['']},
    'Skill': 'Sport'
}

dangerous_armour = {
    0: {'Type': 'Bone Mail',
        'Armour Hits': 8,
        'Special': ['']},
    1: {'Type': 'Beer Barrel',
        'Armour Hits': 10,
        'Special': ['-Bulky']},
    2: {'Type': 'Colander Helm',
        'Armour Hits': 8,
        'Special': ['-Item']},
    3: {'Type': 'Chain Vest',
        'Armour Hits': 8,
        'Special': ['-Jangley']},
    4: {'Type': 'Leather Jacket',
        'Armour Hits': 6,
        'Special': ['+Fonzie']},
    5: {'Type': 'Leather Apron',
        'Armour Hits': 6,
        'Special': ['+Backpack']},
    6: {'Type': 'Kite Shield',
        'Armour Hits': 12,
        'Special': ['-Big', '-Bulky']},
    'Skill': 'Lift'
}

basic_weapon = {
    0: {'Type': 'Ham Hock, Rotting',
        'Dam': 2,
        'Special': ['-Foul Smelling']},
    1: {'Type': 'Spork-Tipped Spear',
        'Dam': 2,
        'Special': ['']},
    2: {'Type': 'Kitchen Knife',
        'Dam': 2,
        'Special': ['-Razor']},
    3: {'Type': 'Hammer',
        'Dam': 1,
        'Special': ['+Useful']},
    4: {'Type': 'Cooking Utensil',
        'Dam': 1,
        'Special': ['+Cook']},
    5: {'Type': 'Dead Rat',
        'Dam': 0,
        'Special': ['-Foul Smelling']},
    6: {'Type': 'Diddly Squat',
        'Dam': None,
        'Special': ['']},
    'Skill': 'Heft'
}

basic_ranged = {
    1: {'Type': 'A Rock',
        'Dam': 1,
        'Special': ['']},
    2: {'Type': 'Sling Shot',
        'Dam': 0,
        'Special': ['+Stones']},
    3: {'Type': 'Sling Shot',
        'Dam': 0,
        'Special': ['+Stones']},
    4: {'Type': 'Sling Shot',
        'Dam': 0,
        'Special': ['+Stones']},
    5: {'Type': 'Sling',
        'Dam': 0,
        'Special': ['+Stones', '-Flail']},
    6: {'Type': 'Sling',
        'Dam': 0,
        'Special': ['+Stones', '-Flail']},
}

dangerous_weapon = {
    0: {'Type': 'Axe, Big',
        'Dam': 4,
        'Special': ['-Big', '-Bulky']},
    1: {'Type': 'Iron Skillet',
        'Dam': 3,
        'Special': ['+Cook']},
    2: {'Type': 'Bone, Large',
        'Dam': 3,
        'Special': ['-Big']},
    3: {'Type': 'Chain',
        'Dam': 2,
        'Special': ['+Climb']},
    4: {'Type': 'Club, Heavy',
        'Dam': 2,
        'Special': ['+Bash']},
    5: {'Type': 'Cleaver, Butcher',
        'Dam': 2,
        'Special': ['+ Cook']},
    6: {'Type': 'Flail',
        'Dam': 2,
        'Special': ['-Flail']},
    'Skill': 'Duel'
}

# TODO: Add gear descriptions
basic_gear = {
    0: {'Type': 'Dowsing Rod'},

    1: {'Type': 'Adventurers Cast-offs'},

    2: {'Type': 'Backpack'},

    3: {'Type': 'Sack of Spices'},

    4: {'Type': 'Rope, 25 feet, hemp'},

    5: {'Type': '9 foot pole'},

    6: {'Type': 'Lint, Belly Button'},

    'Skill': 'Nature',
}

dangerous_gear = {
    0: {'Type': 'Booze'},

    1: {'Type': 'Spell Pages'},

    2: {'Type': 'Circle of Sign Talking'},

    3: {'Type': 'Bag of Holding: Chickens'},

    4: {'Type': 'Bracers of Offence'},

    5: {'Type': 'Thieves Tool'},

    6: {'Type': 'Cup of Elemental Summoning: Milk'},

    'Skill': 'Dungeon',
}

adventurers_cast_offs = {
    0: {'Type': 'Rogue\'s Choice', 'Description': 'Who says crime doesn\'t pay, select any item.'},
    1: {'Type': 'Nearly Empty Vial of Holy Water', 'Description': 'Can be used on -UNDEAD creatures\ncausing 1D6 DAM.\nMakes a nice salad dressing.'},
    2: {'Type': 'Leaking Flask of Oil', 'Description': 'Can be tossed into a fire to cause a 1D6 DAM\nexplosion to everything in the map square.\nGain -FLAMMABLE for the rest of the adventure.\nIf you already have that -BOGIE you ignite.'},
    3: {'Type': 'Whetstone', 'Description': 'Can be used to sharpen your teeth and claws.\nThe process is painful, causing 3 DAM, but for the next 1D6\nturns your teeth and claws do 2 DAM.'},
    4: {'Type': 'Iron Ration', 'Description': 'A small metal box that contains a small dried up snack.\nEating the snack restores 3 lost HITS,\nand you succeed at -HUNGRY or -TASTES LIKE rolls\nfor the next 3 turns.'},
    5: {'Type': 'Flaming Club', 'Description': 'A stick with some oily, pitch-covered rags at one end.\n Once lit, the rags will burn steadily for 2d6 turns\n before crumbling to ash. While burning is provides\n plenty of unnecessary light, can be used to light fires,\nand causes 2 DAM if used as a weapon.'},
    6: {'Type': 'Empty Wineskin', 'Description': 'Let\'s fill it up and have a party'}
}