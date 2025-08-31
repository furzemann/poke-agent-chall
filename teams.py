import numpy as np

from poke_env.teambuilder import Teambuilder

class RandomTeamFromPool(Teambuilder):
    def __init__(self, teams):
        self.teams = [self.join_team(self.parse_showdown_team(team)) for team in teams]

    def yield_team(self):
        return np.random.choice(self.teams)

team1 = """
Torkoal @ Heat Rock  
Ability: Drought  
Tera Type: Ground  
EVs: 104 HP / 252 SpA / 152 SpD  
Quiet Nature  
- Eruption  
- Overheat  
- Earthquake  
- Stealth Rock  

Hatterene @ Air Balloon  
Ability: Magic Bounce  
Tera Type: Ghost  
EVs: 252 HP / 252 Def / 4 SpD  
Relaxed Nature  
IVs: 0 Atk / 0 Spe  
- Trick Room  
- Psychic Noise  
- Dazzling Gleam  
- Healing Wish  

Raging Bolt @ Life Orb  
Ability: Protosynthesis  
Tera Type: Ghost  
EVs: 36 Def / 252 SpA / 220 Spe  
Modest Nature  
IVs: 20 Atk  
- Thunderclap  
- Weather Ball  
- Dragon Pulse  
- Solar Beam  

Slither Wing @ Assault Vest  
Ability: Protosynthesis  
Tera Type: Fire  
EVs: 40 HP / 252 Atk / 216 Spe  
Adamant Nature  
- U-turn  
- First Impression  
- Earthquake  
- Temper Flare  

Venusaur @ Life Orb  
Ability: Chlorophyll  
Tera Type: Fire  
EVs: 4 Atk / 252 SpA / 252 Spe  
Naive Nature  
- Growth  
- Giga Drain  
- Weather Ball  
- Earthquake  

Walking Wake @ Wise Glasses  
Ability: Protosynthesis  
Tera Type: Fairy  
EVs: 12 HP / 244 SpA / 252 Spe  
Timid Nature  
- Hydro Steam  
- Weather Ball  
- Draco Meteor  
- Flip Turn 
"""

team2 = """
Meruem (Kingambit) @ Leftovers  
Ability: Supreme Overlord  
Tera Type: Ghost  
EVs: 164 HP / 252 Atk / 92 Spe  
Adamant Nature  
- Sucker Punch  
- Iron Head  
- Kowtow Cleave  
- Swords Dance  

Moebius (Deoxys-Speed) @ Life Orb  
Ability: Pressure  
Tera Type: Psychic  
EVs: 28 HP / 252 SpA / 228 Spe  
Modest Nature  
IVs: 0 Atk  
- Nasty Plot  
- Focus Blast  
- Psycho Boost  
- Shadow Ball  

Anomaly (Great Tusk) @ Booster Energy  
Ability: Protosynthesis  
Tera Type: Steel  
EVs: 252 Atk / 4 Def / 252 Spe  
Jolly Nature  
- Headlong Rush  
- Ice Spinner  
- Rapid Spin  
- Close Combat  

Yoshi (Dragonite) @ Choice Band  
Ability: Multiscale  
Shiny: Yes  
Tera Type: Normal  
EVs: 16 HP / 252 Atk / 240 Spe  
Adamant Nature  
- Outrage  
- Extreme Speed  
- Ice Spinner  
- Fire Punch  

Anomаly (Iron Moth) @ Booster Energy  
Ability: Quark Drive  
Tera Type: Ground  
EVs: 124 Def / 132 SpA / 252 Spe  
Timid Nature  
- Fiery Dance  
- Sludge Wave  
- Tera Blast  
- Toxic Spikes  

Siren (Primarina) @ Assault Vest  
Ability: Torrent  
Tera Type: Poison  
EVs: 76 HP / 252 SpA / 180 Spe  
Modest Nature  
IVs: 0 Atk  
- Surf  
- Moonblast  
- Whirlpool  
- Psychic Noise 
"""

team3 = """ 
Ogerpon-Wellspring (F) @ Wellspring Mask  
Ability: Water Absorb  
Tera Type: Water  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Ivy Cudgel  
- Horn Leech  
- Play Rough  
- Taunt  

Kingambit @ Leftovers  
Ability: Supreme Overlord  
Tera Type: Ghost  
EVs: 240 HP / 252 Atk / 16 Spe  
Adamant Nature  
- Swords Dance  
- Kowtow Cleave  
- Iron Head  
- Sucker Punch  

Landorus-Therian @ Rocky Helmet  
Ability: Intimidate  
Tera Type: Fairy  
EVs: 248 HP / 8 Def / 252 Spe  
Jolly Nature  
- Earthquake  
- U-turn  
- Stealth Rock  
- Taunt  

Glimmora @ Power Herb  
Ability: Toxic Debris  
Tera Type: Ghost  
EVs: 4 HP / 8 Def / 248 SpA / 248 Spe  
Modest Nature  
- Meteor Beam  
- Earth Power  
- Mortal Spin  
- Spikes  

Dragapult @ Choice Specs  
Ability: Clear Body  
Tera Type: Ghost  
EVs: 4 Def / 252 SpA / 252 Spe  
Timid Nature  
- Shadow Ball  
- Draco Meteor  
- Flamethrower  
- U-turn  

Iron Valiant @ Booster Energy  
Ability: Quark Drive  
Tera Type: Steel  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Swords Dance  
- Spirit Break  
- Knock Off  
- Encore
"""

custom_builder = RandomTeamFromPool([team1, team2, team3])
