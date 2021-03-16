import kivy
from random import randint
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from items import basic_armour, dangerous_armour, basic_weapon, basic_ranged, dangerous_weapon, basic_gear, dangerous_gear


class OddRow(GridLayout):
    """layout initialisation for kivy"""
    pass


class EvenRow(GridLayout):
    """layout initialisation for kivy"""
    pass


class LandingScreen(Screen):
    """initialise the landing screen in kivy and give a name"""
    Screen(name='LandingScreen')


class StatsAndSkills(Screen):
    """Screen initialisation, as well as setting properties for use in the GUI and
    recovering them as they are generated.
    Also does some checking and popups to inform the user what errors may have been made and how to fix them"""

    Screen(name='StatsAndSkills')

    bully_check = ObjectProperty(None)
    lift_check = ObjectProperty(None)
    duel_check = ObjectProperty(None)
    sport_check = ObjectProperty(None)
    heft_check = ObjectProperty(None)
    swim_check = ObjectProperty(None)
    wrassle_check = ObjectProperty(None)
    fear_check = ObjectProperty(None)
    shoot_check = ObjectProperty(None)
    lackey_check = ObjectProperty(None)
    human_check = ObjectProperty(None)
    sage_check = ObjectProperty(None)
    trap_check = ObjectProperty(None)
    tinker_check = ObjectProperty(None)
    bard_check = ObjectProperty(None)
    perform_check = ObjectProperty(None)
    cook_check = ObjectProperty(None)
    critter_check = ObjectProperty(None)
    dungeon_check = ObjectProperty(None)
    track_check = ObjectProperty(None)
    nature_check = ObjectProperty(None)
    trade_check = ObjectProperty(None)
    fast_check = ObjectProperty(None)
    ride_check = ObjectProperty(None)
    hide_check = ObjectProperty(None)
    sneak_check = ObjectProperty(None)
    nurture_check = ObjectProperty(None)
    steal_check = ObjectProperty(None)
    wiggle_check = ObjectProperty(None)

    def get_stats(self):
        app = App.get_running_app()
        self.ids.brawn1.text = str(app.brawn1)
        self.ids.brawn2.text = str(app.brawn2)
        self.ids.brawn.text = str(app.brawn)
        self.ids.meat.text = str(app.meat)

        self.ids.ego1.text = str(app.ego1)
        self.ids.ego2.text = str(app.ego2)
        self.ids.ego.text = str(app.ego)
        self.ids.cunning.text = str(app.cunning)

        self.ids.extraneous1.text = str(app.extraneous1)
        self.ids.extraneous2.text = str(app.extraneous2)
        self.ids.extraneous.text = str(app.extraneous)
        self.ids.luck.text = str(app.luck)

        self.ids.reflexes1.text = str(app.reflexes1)
        self.ids.reflexes2.text = str(app.reflexes2)
        self.ids.reflexes.text = str(app.reflexes)
        self.ids.agility.text = str(app.agility)

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

    def check_skills_and_move_on(self):
        brawn_checked = NumericProperty(0)
        ego_checked = NumericProperty(0)
        extraneous_checked = NumericProperty(0)
        reflexes_checked = NumericProperty(0)
        brawn_checked = 0
        ego_checked = 0
        extraneous_checked = 0
        reflexes_checked = 0

        app = App.get_running_app()
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
        max_per_stat = 0
        if app.max_skills <= 4:
            max_per_stat = 1
        else:
            max_per_stat = 2
        if num_checked == 7 and app.max_skills == 7:
            app.death_check()

        if not num_checked:
            no_skills_popup.open()

        elif num_checked > app.max_skills:
            too_many_skills_popup.open()

        elif brawn_checked > max_per_stat or ego_checked > max_per_stat or extraneous_checked > max_per_stat or reflexes_checked > max_per_stat:
            too_many_skills_in_one_stat_popup.open()

        elif brawn_checked > 1 or ego_checked > 1 or extraneous_checked > 1 or reflexes_checked > 1:
            if brawn_checked == 0 or ego_checked == 0 or extraneous_checked == 0 or reflexes_checked == 0:
                too_many_skills_in_one_stat_popup.open()
            elif num_checked == 7 and app.max_skills == 7:
                app.setting()
                if "Cook" not in app.extraneous_skills:
                    app.death_check()
                app.sm.current = 'EdgesBogiesAndEquipment'

            else:
                if "Cook" not in app.extraneous_skills:
                    app.death_check()
                app.sm.current = 'EdgesBogiesAndEquipment'
                app.setting()
        else:
            if "Cook" not in app.extraneous_skills:
                app.death_check()
            app.sm.current = 'EdgesBogiesAndEquipment'
            app.setting()


class EdgesBogiesAndEquipment(Screen):
    """
    Edges and Bogies and equipment screen initialisation,
    popups for informing users of errors, and look ups for information stored in items.py
    """
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
            if 'Sport' in app.brawn_skills:
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
            if 'Lift' in app.brawn_skills:
                app.armour = dangerous_armour[(roll - 1)]
            else:
                app.armour = basic_armour[roll]
            app.armour_name = str(app.armour['Type'])
            app.armour_hits = app.armour['Armour Hits']
            app.armour_rolled += 1
            app.death_check()

    def basic_weapon(self):
        app = App.get_running_app()
        if app.weapon_rolled == 0:
            roll = app.d6(1)[0]
            if 'Shoot' in app.ego_skills:
                app.weapon = basic_ranged[roll]
            elif 'Heft' in app.brawn_skills:
                app.weapon = basic_weapon[(roll - 1)]
            else:
                app.weapon = basic_weapon[roll]
            app.weapon_name = str(app.weapon['Type'])
            app.weapon_rolled += 1

    def dangerous_weapon(self):
        app = App.get_running_app()
        if app.weapon_rolled == 0:
            roll = app.d6(1)[0]
            if 'Duel' in app.brawn_skills:
                app.weapon = dangerous_weapon[(roll - 1)]
            else:
                app.weapon = dangerous_weapon[roll]
            app.weapon_name = str(app.weapon['Type'])
            app.weapon_rolled += 1
            app.death_check()

    def basic_gear(self):
        app = App.get_running_app()
        if app.gear_rolled == 0:
            roll = app.d6(1)[0]
            if 'Nature' in app.extraneous_skills:
                app.gear = basic_gear[(roll - 1)]
            else:
                app.gear = basic_gear[roll]
            app.gear_name = str(app.gear['Type'])
            app.gear_rolled += 1

    def dangerous_gear(self):
        app = App.get_running_app()
        if app.gear_rolled == 0:
            roll = app.d6(1)[0]
            if 'Dungeon' in app.extraneous_skills:
                app.gear = dangerous_gear[(roll - 1)]
            else:
                app.gear = dangerous_gear[roll]
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
    """
    Character sheet generated with information generated from character creation, also some buttons to add
    deathchecks, take hits, and text boxes for the equipment in use
    """
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




class KAMBApp(App):
    """
    App initilisation as well as main data to be carried over between screens held in this class.
    as well as methods used to generate said character
    """
    name = StringProperty("Name Your Kobold")
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

        self.edges_rolled = 0
        self.armour_rolled = 0
        self.weapon_rolled = 0
        self.gear_rolled = 0
        death_popup.open()
        self.sm.current = 'LandingScreen'

    def death_check(self):
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

    def build(self):
        KAMBApp.sm.add_widget(LandingScreen(name='LandingScreen'))
        KAMBApp.sm.add_widget(StatsAndSkills(name='StatsAndSkills'))
        KAMBApp.sm.add_widget(EdgesBogiesAndEquipment(name='EdgesBogiesAndEquipment'))
        KAMBApp.sm.add_widget(KoboldSheet(name='KoboldSheet'))
        return KAMBApp.sm
        # TODO: Reactivate pages

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
        """
        test for popup tool tips, to be expanded to all edges, bogies, skills, stats, and potentially equipment
        """
        self.kobold_senses.open()


if __name__ == "__main__":
    KAMBApp().run()
