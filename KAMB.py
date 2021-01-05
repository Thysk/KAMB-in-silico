import kivy
from kivy_deps import sdl2, glew
from random import randint
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from items import basic_armour, dangerous_armour, basic_weapon, basic_ranged, dangerous_weapon, basic_gear, dangerous_gear, adventurers_cast_offs
from magic import random_magick_table, magick_table


class OddRow(GridLayout):
    pass


class EvenRow(GridLayout):
    pass


class LandingScreen(Screen):
    Screen(name='LandingScreen')


class StatsAndSkills(Screen):
    Screen(name='StatsAndSkills')

    def get_stats(self):
        app = App.get_running_app()

        if app.ego in range(0, 5):
            app.max_skills = app.ego
            self.ids.max_skills.text = str(app.ego)
        elif app.ego == 5:
            app.max_skills = 7
            self.ids.max_skills.text = str(7)
        else:
            app.max_skills = 6
            self.ids.max_skills.text = str(6)

        self.ids.death_checks.text = str(app.death_checks)
        self.ids.vps.text = str(app.vps)

    def magic(self):
        app = App.get_running_app()
        roll = sum(app.d6(2))
        app.magick = random_magick_table[roll]

    def check_skills_and_move_on(self):
        app = App.get_running_app()

        brawn_checked = 0
        ego_checked = 0
        extraneous_checked = 0
        reflexes_checked = 0

        app.brawn_skills = []
        app.ego_skills = []
        app.extraneous_skills = []
        app.reflexes_skills = []

        too_many_skills_popup = Popup(title='Too Many Skills Selected',
                                      content=Label(text='Seems you have checked too many boxes!'),
                                      size_hint=(0.6, 0.6))

        no_skills_popup = Popup(title='No Skills Selected',
                                content=Label(text='You don\'t seem to have selected any skills, you really should!'),
                                size_hint=(0.6, 0.6))

        too_many_skills_in_one_stat_popup = Popup(title='Too many checks in one STAT',
                                                  content=Label(text="""You have to put at least 1 skill in each STAT,
before you can get a second one.
OR
at least 2 in each STAT before you
get a third etc.""",
                                                                halign='center'),
                                                  size_hint=(0.6, 0.6))

        get_some_stats_popup = Popup(title="You don't seem to exist yet",
                                     content=Label(text="You haven\'t clicked that button at the top yet.\nYou should do that to pop into existance,\nthen think about your upbringing (skills)"),
                                     size_hint=(0.6, 0.6))
        app.brawn_skills.clear()
        app.ego_skills.clear()
        app.extraneous_skills.clear()
        app.reflexes_skills.clear()

        if self.bully_check.active:
            brawn_checked += 1
            app.brawn_skills.append('Bully')
        if self.lift_check.active:
            brawn_checked += 1
            app.brawn_skills.append('Lift')
        if self.duel_check.active:
            brawn_checked += 1
            app.brawn_skills.append('Duel')
        if self.sport_check.active:
            brawn_checked += 1
            app.brawn_skills.append('Sport')
        if self.heft_check.active:
            brawn_checked += 1
            app.brawn_skills.append('Heft')
        if self.swim_check.active:
            brawn_checked += 1
            app.brawn_skills.append('Swim')
        if self.wrassle_check.active:
            brawn_checked += 1
            app.brawn_skills.append('Wrassle')
        if self.fear_check.active:
            ego_checked += 1
            app.ego_skills.append('Fear')
        if self.shoot_check.active:
            ego_checked += 1
            app.ego_skills.append('Shoot')
        if self.lackey_check.active:
            ego_checked += 1
            app.ego_skills.append('Lackey')
        if self.human_check.active:
            ego_checked += 1
            app.ego_skills.append('S. Human')
        if self.sage_check.active:
            ego_checked += 1
            app.ego_skills.append('Sage')
        if self.trap_check.active:
            ego_checked += 1
            app.ego_skills.append('Trap')
        if self.tinker_check.active:
            ego_checked += 1
            app.ego_skills.append('Tinker')
        if self.bard_check.active:
            extraneous_checked += 1
            app.extraneous_skills.append('Bard')
        if self.perform_check.active:
            extraneous_checked += 1
            app.extraneous_skills.append('Perform')
        if self.cook_check.active:
            extraneous_checked += 1
            app.extraneous_skills.append('Cook')
        if self.critter_check.active:
            extraneous_checked += 1
            app.extraneous_skills.append('S. Critter')
        if self.dungeon_check.active:
            extraneous_checked += 1
            app.extraneous_skills.append('Dungeon')
        if self.track_check.active:
            extraneous_checked += 1
            app.extraneous_skills.append('Track')
        if self.nature_check.active:
            extraneous_checked += 1
            app.extraneous_skills.append('Nature')
        if self.trade_check.active:
            extraneous_checked += 1
            app.extraneous_skills.append('Trade')
        if self.fast_check.active:
            reflexes_checked += 1
            app.reflexes_skills.append('Fast')
        if self.ride_check.active:
            reflexes_checked += 1
            app.reflexes_skills.append('Ride')
        if self.hide_check.active:
            reflexes_checked += 1
            app.reflexes_skills.append('Hide')
        if self.sneak_check.active:
            reflexes_checked += 1
            app.reflexes_skills.append('Sneak')
        if self.nurture_check.active:
            reflexes_checked += 1
            app.reflexes_skills.append('Nurture')
        if self.steal_check.active:
            reflexes_checked += 1
            app.reflexes_skills.append('Steal')
        if self.wiggle_check.active:
            reflexes_checked += 1
            app.reflexes_skills.append('Wiggle')

        num_checked = (brawn_checked + ego_checked + extraneous_checked + reflexes_checked)

        if app.max_skills <= 4:
            max_per_stat = 1
        else:
            max_per_stat = 2

        if app.created == 0:
            get_some_stats_popup.open()
        elif not num_checked:
            no_skills_popup.open()
        elif num_checked > app.max_skills:
            too_many_skills_popup.open()
        elif brawn_checked > max_per_stat or ego_checked > max_per_stat or extraneous_checked > max_per_stat or reflexes_checked > max_per_stat:
            too_many_skills_in_one_stat_popup.open()
        elif brawn_checked > 1 or ego_checked > 1 or extraneous_checked > 1 or reflexes_checked > 1:
            if brawn_checked == 0 or ego_checked == 0 or extraneous_checked == 0 or reflexes_checked == 0:
                too_many_skills_in_one_stat_popup.open()
            elif num_checked == 7 and app.max_skills == 7:
                app.death_check()
                app.setting()
                if "Cook" not in app.extraneous_skills:
                    app.death_check()
                if 'Lackey' in app.ego_skills:
                    self.magic()
                app.sm.current = 'EdgesBogiesAndEquipment'

            else:
                if "Cook" not in app.extraneous_skills:
                    app.death_check()
                if 'Lackey' in app.ego_skills:
                    self.magic()
                app.sm.current = 'EdgesBogiesAndEquipment'
                app.setting()
        else:
            if "Cook" not in app.extraneous_skills:
                app.death_check()
            if 'Lackey' in app.ego_skills:
                self.magic()
            app.sm.current = 'EdgesBogiesAndEquipment'
            app.setting()


class EdgesBogiesAndEquipment(Screen):
    Screen(name='EdgesBogiesAndEquipment')
    edges_and_bogies_needed_popup = Popup(title='You need to roll some +Edges and -Bogies',
                                          content=Label(text="""You haven't rolled your +Edges or -Bogies."
All Kobolds have these in their nature."""),
                                          size_hint=(0.6, 0.6))
    all_piles_not_visited_popup = Popup(title="No Gear, No Adventures!",
                                        size_hint=(0.6, 0.6),
                                        content=Label(text="""You aren't equipped to venture out of The Caves.
Visit all three of the Three Great Piles!"""))

    def roll_edges_and_bogies(self):
        app = App.get_running_app()
        edge_table = {
            1: "+Animal Chum",
            2: "+Bouncy",
            3: "+Extra Padding",
            4: "+Red Thumb",
            5: "+Troll Blood",
            6: "+Winning Smile"
        }
        bogie_table = {
            1: "-Animal Foe",
            2: "-Flammable",
            3: "-Foul Smelling",
            4: "-Hungry",
            5: "-In Heat",
            6: "-Tastes Like Baby"
        }

        if app.edges_rolled == 0:
            app.edges = edge_table[app.d6(1)[0]]

            app.bogies = bogie_table[app.d6(1)[0]]

            app.edges_rolled += 1

        self.ids.edges.text = str(app.edges)
        self.ids.bogies.text = str(app.bogies)
        if "Extra Padding" in app.edges:
            app.hits += app.d6(1)[0]
        app.max_hits = app.hits

    def basic_armour(self):
        app = App.get_running_app()
        if app.armour_rolled == 0:
            roll = app.d6(1)[0]
            if 'Sport' in app.brawn_skills or 'Perform' in app.extraneous_skills:
                app.armour = basic_armour[roll - 1]
            else:
                app.armour = basic_armour[roll]
            app.armour_name = str(app.armour['Type'])
            app.armour_hits = app.armour['Armour Hits']
            app.armour_rolled += 1

    def dangerous_armour(self):
        app = App.get_running_app()
        if app.armour_rolled == 0:
            roll = app.d6(1)[0]
            if 'Lift' in app.brawn_skills or 'Perform' in app.extraneous_skills:
                app.armour = dangerous_armour[(roll - 1)]
            else:
                app.armour = basic_armour[roll]
            app.armour_name = str(app.armour['Type'])
            app.armour_hits = app.armour['Armour Hits']
            app.armour_rolled += 1
            app.death_check()

    def use_that_perform(self, roll):
        app = App.get_running_app()
        app.weapon = basic_ranged[roll]
        app.weapon_name = app.weapon['Type']

    def what_a_passe_role(self, roll):
        app = App.get_running_app()
        if 'Heft' in app.brawn_skills or 'Perform' in app.extraneous_skills:
            app.weapon = basic_weapon[(roll - 1)]

        else:
            app.weapon = basic_weapon[roll]

        app.weapon_name = str(app.weapon['Type'])
        app.weapon_rolled += 1

    def to_shoot_or_not_to_shoot(self, roll:int):
        grid = GridLayout(cols=1)
        popup = Popup(title="To Shoot, or Not to Shoot",
                      content=grid,
                      size_hint=(0.6, 0.6),
                      auto_dismiss=False)
        grid.add_widget(Label(text="So Keanu, do you want to pretend to be good with\nRanged weapons to dive into the\nThe Basic Ranged Weapon Pile?"))
        innergrid = GridLayout(cols=2)
        innergrid.add_widget(Button(text='Yes', on_press=lambda x: self.use_that_perform(roll), on_release=popup.dismiss))
        innergrid.add_widget(Button(text='No', on_press=lambda x: self.what_a_passe_role(roll), on_release=popup.dismiss))
        grid.add_widget(innergrid)
        popup.open()

    def basic_weapon(self):
        app = App.get_running_app()
        if app.weapon_rolled == 0:
            roll = app.d6(1)[0]
            if 'Perform' in app.extraneous_skills:
                self.to_shoot_or_not_to_shoot(roll)
            elif 'Shoot' in app.ego_skills:
                app.weapon = basic_ranged[roll]
                app.weapon_name = str(app.weapon['Type'])
            elif 'Heft' in app.brawn_skills or 'Perform' in app.extraneous_skills:
                app.weapon = basic_weapon[(roll - 1)]
                app.weapon_name = str(app.weapon['Type'])
            else:
                app.weapon = basic_weapon[roll]
                app.weapon_name = str(app.weapon['Type'])
            app.weapon_rolled += 1

    def dangerous_weapon(self):
        app = App.get_running_app()
        if app.weapon_rolled == 0:
            roll = app.d6(1)[0]
            if 'Duel' in app.brawn_skills or 'Perform' in app.extraneous_skills:
                app.weapon = dangerous_weapon[(roll - 1)]
            else:
                app.weapon = dangerous_weapon[roll]
            app.weapon_name = str(app.weapon['Type'])
            app.weapon_rolled += 1
            app.death_check()

    def gear_select(self, select: int):
        app = App.get_running_app()
        app.gear = adventurers_cast_offs[select]
        app.gear_name = app.gear['Type']

    def gear_choice(self, select: int, *args):
        grid = GridLayout(cols=1)
        popup = Popup(title=adventurers_cast_offs[select]['Type'],
                      content=grid,
                      size_hint=(0.6, 0.6),
                      auto_dismiss=False)
        inner_grid = GridLayout(cols=2)
        grid.add_widget(Label(text=adventurers_cast_offs[select]['Description']))
        inner_grid.add_widget(Button(text='Yes', on_press=lambda x: self.gear_select(select), on_release=popup.dismiss))
        inner_grid.add_widget(Button(text='No', on_press=self.rogues_choice_popup, on_release=popup.dismiss))
        grid.add_widget(inner_grid)

        popup.open()

    def rogues_choice_popup(self, *args):
        grid = GridLayout(cols=1)
        popup = Popup(title="Rogue's Choice",
                      content=grid,
                      size_hint=(0.6, 0.6),
                      auto_dismiss=False)
        grid.add_widget(Label(text="""Seems luck is on your side!
Choose what you want from the Adventurer's Cast-Offs"""))

        grid.add_widget(Button(text=adventurers_cast_offs[1]['Type'], on_press=lambda x: self.gear_choice(select=1), on_release=popup.dismiss))
        grid.add_widget(Button(text=adventurers_cast_offs[2]['Type'], on_press=lambda x: self.gear_choice(select=2), on_release=popup.dismiss))
        grid.add_widget(Button(text=adventurers_cast_offs[3]['Type'], on_press=lambda x: self.gear_choice(select=3), on_release=popup.dismiss))
        grid.add_widget(Button(text=adventurers_cast_offs[4]['Type'], on_press=lambda x: self.gear_choice(select=4), on_release=popup.dismiss))
        grid.add_widget(Button(text=adventurers_cast_offs[5]['Type'], on_press=lambda x: self.gear_choice(select=5), on_release=popup.dismiss))
        grid.add_widget(Button(text=adventurers_cast_offs[6]['Type'], on_press=lambda x: self.gear_choice(select=6), on_release=popup.dismiss))

        popup.open()

    def basic_gear(self):
        app = App.get_running_app()
        if app.gear_rolled == 0:
            roll = app.d6(1)[0]
            if 'Nature' in app.extraneous_skills or 'Perform' in app.extraneous_skills:
                app.gear = basic_gear[(roll - 1)]
            else:
                app.gear = basic_gear[roll]

            if app.gear['Type'] == 'Adventurers Cast-offs':
                roll_adventure_gear = app.d6(1)[0]

                if 'Steal' in app.reflexes_skills or 'Perform' in app.extraneous_skills:
                    app.gear = adventurers_cast_offs[roll_adventure_gear - 1]
                    if app.gear['Type'] == 'Rogue\'s Choice':
                        self.rogues_choice_popup()
                else:
                    app.gear = adventurers_cast_offs[roll_adventure_gear]
            app.gear_name = str(app.gear['Type'])
            app.gear_rolled += 1

    def dangerous_gear(self):
        app = App.get_running_app()
        if app.gear_rolled == 0:
            roll = app.d6(1)[0]
            if 'Dungeon' in app.extraneous_skills or 'Perform' in app.extraneous_skills:
                app.gear = dangerous_gear[(roll - 1)]
            else:
                app.gear = dangerous_gear[roll]

            if app.gear['Type'] == 'Spell Pages':
                app.spell_pages = sum(app.d6(1))

            app.gear_name = str(app.gear['Type'])
            app.gear_rolled += 1
            app.death_check()

    def move_on_to_character_sheet(self):
        app = App.get_running_app()
        if app.edges_rolled == 0:
            self.edges_and_bogies_needed_popup.open()
        elif app.armour_rolled == 0:
            self.all_piles_not_visited_popup.open()
        elif app.weapon_rolled == 0:
            self.all_piles_not_visited_popup.open()
        elif app.gear_rolled == 0:
            self.all_piles_not_visited_popup.open()
        else:
            app.sm.current = 'KoboldSheet'


class KoboldSheet(Screen):
    Screen(name='KoboldSheet')

    def minus_hit(self):
        app = App.get_running_app()
        if self.ids.a_hits != app.armour_hits:
            app.armour_hits = int(self.ids.a_hits.text)
        if self.ids.k_hits != app.hits:
            if int(self.ids.k_hits.text) > app.max_hits:
                app.hits = app.max_hits
            else:
                app.hits = int(self.ids.k_hits.text)
        if app.armour_hits > 0:
            app.armour_hits -= 1
        else:
            app.hits -= 1
        if app.hits <= 0:
            app.death()

    def use_luck(self):
        app = App.get_running_app()
        if app.luck:
            app.luck -= 1

    def use_spell_page(self, *args):
        app = App.get_running_app()
        app.spell_pages = app.spell_pages - 1
        roll = sum(app.d6(2))
        spell = random_magick_table[roll]
        description = magick_table[spell]
        popup = Popup(title=spell,
                      size_hint=(0.6, 0.6),
                      content=Label(text=description),
                      on_dismiss=self.spell_pages_popup)
        popup.open()

    def lackey_popup(self, *args):
        app = App.get_running_app()
        grid = GridLayout(cols=1)
        popup = Popup(title='You know a spell: {}'.format(app.magick),
                      size_hint=(0.6, 0.6),
                      content=grid)
        grid.add_widget(Label(text=magick_table[app.magick]))
        grid.add_widget((Button(text="Use spell", on_press=app.death_check, on_release=popup.dismiss)))

        popup.open()

    def spell_pages_popup(self, *args):
        app = App.get_running_app()
        grid = GridLayout(cols=1)
        popup = Popup(title='You have pages of spells',
                      size_hint=(0.6, 0.6),
                      content=grid)
        grid.add_widget(Label(halign='center', text="""Kobolds karnt reed gud,
SO! instead of reciting the spell,
just launch the page at whatever it is,
and see what happens"""))
        grid.add_widget(Label(halign='center', text="You have {} spell page/s left".format(app.spell_pages)))
        grid.add_widget(Button(text="Use spell page", on_press=self.use_spell_page, on_release=popup.dismiss))


        popup.open()

    no_magic_popup = Popup(title='We got a Muggle over here!',
                           size_hint=(0.6, 0.6),
                           content=Label(text="You don't know any magick!"))

    def magick_and_pages_popup(self):
        app = App.get_running_app()
        grid = GridLayout(cols=1)
        grid.add_widget(Label(halign='center', text="""Whoa!
What a spell caster you are!
Not one but TWO ways to cast a spell!
Which one do you want to use?"""))
        inner_grid = (GridLayout(cols=2))
        lackey_button = Button(text=app.magick, on_press=self.lackey_popup)
        pages_button = Button(text='Spell Pages', on_press=self.spell_pages_popup)
        inner_grid.add_widget(lackey_button)
        inner_grid.add_widget(pages_button)
        grid.add_widget(inner_grid)

        popup = Popup(title='You have more than one way to cast a spell',
                      size_hint=(0.6, 0.6),
                      content=grid,
                                   )
        popup.open()

    def use_magick(self):
        app = App.get_running_app()
        if app.magick and app.gear_name == 'Spell Pages':
            self.magick_and_pages_popup()
        elif app.magick:
            self.lackey_popup()
        elif app.gear_name == 'Spell Pages':
            self.spell_pages_popup()
        else:
            self.no_magic_popup.open()


class KAMBApp(App):
    name = StringProperty("Name Your Kobold")
    created = NumericProperty(0)
    brawn1 = NumericProperty(0)
    brawn2 = NumericProperty(0)
    brawn = NumericProperty(0)
    meat = NumericProperty(0)
    ego1 = NumericProperty(0)
    ego2 = NumericProperty(0)
    ego = NumericProperty(0)
    cunning = NumericProperty(0)
    extraneous1 = NumericProperty(0)
    extraneous2 = NumericProperty(0)
    extraneous = NumericProperty(0)
    luck = NumericProperty(0)
    reflexes1 = NumericProperty(0)
    reflexes2 = NumericProperty(0)
    reflexes = NumericProperty(0)
    agility = NumericProperty(0)
    max_skills = NumericProperty(0)
    death_checks = NumericProperty(0)
    vps = NumericProperty(0)
    brawn_skills = []
    ego_skills = []
    extraneous_skills = []
    reflexes_skills = []
    edges = ObjectProperty(None)
    bogies = ObjectProperty(None)
    armour = ObjectProperty(None)
    weapon = ObjectProperty(None)
    gear = ObjectProperty(None)
    brawn_skill1 = StringProperty('')
    brawn_skill2 = StringProperty('')
    ego_skill1 = StringProperty('')
    ego_skill2 = StringProperty('')
    extraneous_skill1 = StringProperty('')
    extraneous_skill2 = StringProperty('')
    reflexes_skill1 = StringProperty('')
    reflexes_skill2 = StringProperty('')
    weapon_name = StringProperty("Dig for weapons")
    armour_name = StringProperty("Dig for armour")
    gear_name = StringProperty("Dig for gear")
    edges_rolled = NumericProperty(0)
    armour_rolled = NumericProperty(0)
    weapon_rolled = NumericProperty(0)
    gear_rolled = NumericProperty(0)
    armour_hits = NumericProperty(0)
    hits = NumericProperty(0)
    max_hits = NumericProperty(0)
    string_of_skills = StringProperty("")
    magick = StringProperty("")
    spell_pages = NumericProperty(0)

    sm = ScreenManager()

    def kobold_create(self):

        if self.brawn1 == 0:

            self.brawn1 = self.d6(1)[0]
            self.brawn2 = self.d6(1)[0]
            self.brawn = self.brawn1 + self.brawn2
            self.meat = self.handy_look_up(self.brawn)
            self.hits = self.brawn

            self.ego1 = self.d6(1)[0]
            self.ego2 = self.d6(1)[0]
            self.ego = self.ego1 + self.ego2
            self.cunning = self.handy_look_up(self.ego)

            self.extraneous1 = self.d6(1)[0]
            self.extraneous2 = self.d6(1)[0]
            self.extraneous = self.extraneous1 + self.extraneous2
            self.luck = self.handy_look_up(self.extraneous)

            self.reflexes1 = self.d6(1)[0]
            self.reflexes2 = self.d6(1)[0]
            self.reflexes = self.reflexes1 + self.reflexes2
            self.agility = self.handy_look_up(self.reflexes)
            if self.ego == 10:
                self.death_check()
            if self.extraneous == 10:
                self.victory_point()
            self.created = 1

    @classmethod
    def d6(cls, n):
        rolls = []
        for roll in range(n):
            rolls.append(randint(1, 6))
        return rolls

    @classmethod
    def handy_look_up(cls, n):
        if n in range(1, 5):
            return 1
        elif n in range(5, 9):
            return 2
        elif n in range(9, 13):
            return 3
        elif n in range(13, 17):
            return 4
        elif n in range(17, 21):
            return 5
        elif n in range(21, 25):
            return 6

    def death(self):
        death_popup = Popup(
            title_align='center',
            title_size='32',
            title='You Died!!!!',
            content=Label(text="""It seems your kobold has died a horrible death.
But feel free to now create a new kobold.""",
                          halign='center'),
            size_hint=(0.6, 0.6)
        )
        self.name = ""
        self.created = 0
        self.brawn1 = 0
        self.brawn2 = 0
        self.brawn = 0
        self.meat = 0
        self.ego1 = 0
        self.ego2 = 0
        self.ego = 0
        self.cunning = 0
        self.extraneous1 = 0
        self.extraneous2 = 0
        self.extraneous = 0
        self.luck = 0
        self.reflexes1 = 0
        self.reflexes2 = 0
        self.reflexes = 0
        self.agility = 0
        self.max_skills = 0
        self.death_checks = 0
        self.vps = 0
        self.brawn_skills = []
        self.ego_skills = []
        self.extraneous_skills = []
        self.reflexes_skills = []
        self.edges = "None"
        self.bogies = "None"
        self.armour = {}
        self.weapon = {}
        self.gear = {}
        self.brawn_skill1 = ""
        self.brawn_skill2 = ""
        self.ego_skill1 = ""
        self.ego_skill2 = ""
        self.extraneous_skill1 = ""
        self.extraneous_skill2 = ""
        self.reflexes_skill1 = ""
        self.reflexes_skill2 = ""
        self.weapon_name = "Dig for weapons"
        self.armour_name = "Dig for armour"
        self.gear_name = "Dig for gear"
        self.armour_hits = 0
        self.hits = 0
        self.max_hits = 0
        self.string_of_skills = ""
        self.edges_rolled = 0
        self.armour_rolled = 0
        self.weapon_rolled = 0
        self.gear_rolled = 0
        self.magick = ""
        self.spell_pages = 0
        death_popup.open()
        self.sm.current = 'LandingScreen'

    def death_check(self, *args):
        roll = sum(self.d6(2))
        current = self.death_checks

        if current + roll > 13:
            self.death()
        else:
            self.death_checks += 1

    def victory_point(self):
        self.vps += 1

    def setting(self):
        if len(self.brawn_skills) < 1:
            self.brawn_skills.append('')
        if len(self.brawn_skills) < 2:
            self.brawn_skills.append('')

        if len(self.ego_skills) < 1:
            self.ego_skills.append('')
        if len(self.ego_skills) < 2:
            self.ego_skills.append('')

        if len(self.extraneous_skills) < 1:
            self.extraneous_skills.append('')
        if len(self.extraneous_skills) < 2:
            self.extraneous_skills.append('')

        if len(self.reflexes_skills) < 1:
            self.reflexes_skills.append('')
        if len(self.reflexes_skills) < 2:
            self.reflexes_skills.append('')

        self.brawn_skill1 = self.brawn_skills[0]
        self.brawn_skill2 = self.brawn_skills[1]

        self.ego_skill1 = self.ego_skills[0]
        self.ego_skill2 = self.ego_skills[1]

        self.extraneous_skill1 = self.extraneous_skills[0]
        self.extraneous_skill2 = self.extraneous_skills[1]

        self.reflexes_skill1 = self.reflexes_skills[0]
        self.reflexes_skill2 = self.reflexes_skills[1]

        list_of_skills = [self.brawn_skill1, self.brawn_skill2, self.ego_skill1, self.ego_skill2, self.extraneous_skill1, self.extraneous_skill2, self.reflexes_skill1, self.reflexes_skill2]

        for skill in list_of_skills:
            if skill:
                self.string_of_skills = self.string_of_skills + skill + " "

    def build(self):
        KAMBApp.sm.add_widget(LandingScreen(name='LandingScreen'))
        KAMBApp.sm.add_widget(StatsAndSkills(name='StatsAndSkills'))
        KAMBApp.sm.add_widget(EdgesBogiesAndEquipment(name='EdgesBogiesAndEquipment'))
        KAMBApp.sm.add_widget(KoboldSheet(name='KoboldSheet'))
        return KAMBApp.sm

    kobold_senses = Popup(title="+Kobold Senses",
                          content=Label(text="""For humans the sense of smell strongly informs the sense of taste.
    But Kobolds don't have noses (merely nostrils), so for you the inverse is true.
    Your sense of taste is so refined that you can actually taste the smell of things.
    In addition, your eyes are so accustomed to living and hunting in deep, 
    dark caves that you can see as well in near total blackness
    as you can in the light (mostly through echo-taste-location).""",
                                        halign="center"),
                          size_hint=(0.7, 0.7))

    def kobold_senses_popup(self):
        self.kobold_senses.open()


if __name__ == "__main__":
    KAMBApp().run()
