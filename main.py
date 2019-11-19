import pokebase
import functools

# atk . def
type_attacks = {
	'fire': {
		'fire': .5,
		'water': .5,
		'electric': 1,
		'ice': 2,
		'ground': 1,
		'rock': .5,
		'grass': 2,
		'bug': 2,
		'poison': 1,
		'psychic': 1,
		'dark': 1,
		'flying': 1,
		'normal': 1,
		'fighting': 1,
		'fairy': 1,
		'dragon': .5,
		'steel': 2,
		'ghost': 1,
	},
	'water': {
		'fire': 2,
		'water': .5,
		'electric': 1,
		'ice': 1,
		'ground': 2,
		'rock': 2,
		'grass': .5,
		'bug': 1,
		'poison': 1,
		'psychic': 1,
		'dark': 1,
		'flying': 1,
		'normal': 1,
		'fighting': 1,
		'fairy': 1,
		'dragon': .5,
		'steel': 1,
		'ghost': 1,
	},
	'electric': {
		'fire': 1,
		'water': 2,
		'electric': .5,
		'ice': 1,
		'ground': 0,
		'rock': 1,
		'grass': .5,
		'bug': 1,
		'poison': 1,
		'psychic': 1,
		'dark': 1,
		'flying': 2,
		'normal': 1,
		'fighting': 1,
		'fairy': 1,
		'dragon': .5,
		'steel': 1,
		'ghost': 1,
	},
	'ice': {
		'fire': .5,
		'water': .5,
		'electric': 1,
		'ice': .5,
		'ground': 2,
		'rock': 1,
		'grass': 2,
		'bug': 1,
		'poison': 1,
		'psychic': 1,
		'dark': 1,
		'flying': 2,
		'normal': 1,
		'fighting': 1,
		'fairy': 1,
		'dragon': 2,
		'steel': .5,
		'ghost': 1,
	},
	'ground': {
		'fire': 2,
		'water': 1,
		'electric': 2,
		'ice': 1,
		'ground': 1,
		'rock': 2,
		'grass': .5,
		'bug': .5,
		'poison': 2,
		'psychic': 1,
		'dark': 1,
		'flying': 0,
		'normal': 1,
		'fighting': 1,
		'fairy': 1,
		'dragon': 1,
		'steel': 2,
		'ghost': 1,
	},
	'rock': {
		'fire': 2,
		'water': 1,
		'electric': 1,
		'ice': 2,
		'ground': .5,
		'rock': 1,
		'grass': 1,
		'bug': 2,
		'poison': 1,
		'psychic': 1,
		'dark': 1,
		'flying': 2,
		'normal': 1,
		'fighting': .5,
		'fairy': 1,
		'dragon': 1,
		'steel': .5,
		'ghost': 1,
	},
	'grass': {
		'fire': .5,
		'water': 2,
		'electric': 1,
		'ice': 1,
		'ground': 2,
		'rock': 2,
		'grass': .5,
		'bug': .5,
		'poison': .5,
		'psychic': 1,
		'dark': 1,
		'flying': .5,
		'normal': 1,
		'fighting': 1,
		'fairy': 1,
		'dragon': .5,
		'steel': .5,
		'ghost': 1,
	},
	'bug': {
		'fire': .5,
		'water': 1,
		'electric': 1,
		'ice': 1,
		'ground': 1,
		'rock': 1,
		'grass': 2,
		'bug': 1,
		'poison': .5,
		'psychic': 2,
		'dark': 2,
		'flying': .5,
		'normal': 1,
		'fighting': .5,
		'fairy': .5,
		'dragon': 1,
		'steel': .5,
		'ghost': .5,
	},
	'poison': {
		'fire': 1,
		'water': 1,
		'electric': 1,
		'ice': 1,
		'ground': .5,
		'rock': .5,
		'grass': 2,
		'bug': 1,
		'poison': .5,
		'psychic': 1,
		'dark': 1,
		'flying': 1,
		'normal': 1,
		'fighting': 1,
		'fairy': 2,
		'dragon': 1,
		'steel': 1,
		'ghost': .5,
	},
	'psychic': {
		'fire': 1,
		'water': 1,
		'electric': 1,
		'ice': 1,
		'ground': 1,
		'rock': 1,
		'grass': 1,
		'bug': 1,
		'poison': 2,
		'psychic': .5,
		'dark': 0,
		'flying': 1,
		'normal': 1,
		'fighting': 2,
		'fairy': 1,
		'dragon': 1,
		'steel': .5,
		'ghost': 1,
	},
	'dark': {
		'fire': 1,
		'water': 1,
		'electric': 1,
		'ice': 1,
		'ground': 1,
		'rock': 1,
		'grass': 1,
		'bug': 1,
		'poison': 1,
		'psychic': 2,
		'dark': .5,
		'flying': 1,
		'normal': 1,
		'fighting': .5,
		'fairy': .5,
		'dragon': 1,
		'steel': 1,
		'ghost': 2,
	},
	'flying': {
		'fire': 1,
		'water': 1,
		'electric': .5,
		'ice': 1,
		'ground': 1,
		'rock': .5,
		'grass': 2,
		'bug': 2,
		'poison': 1,
		'psychic': 1,
		'dark': 1,
		'flying': 1,
		'normal': 1,
		'fighting': 2,
		'fairy': 1,
		'dragon': 1,
		'steel': .5,
		'ghost': 1,
	},
	'normal': {
		'fire': 1,
		'water': 1,
		'electric': 1,
		'ice': 1,
		'ground': 1,
		'rock': .5,
		'grass': 1,
		'bug': 1,
		'poison': 1,
		'psychic': 1,
		'dark': 1,
		'flying': 1,
		'normal': 1,
		'fighting': 1,
		'fairy': 1,
		'dragon': 1,
		'steel': .5,
		'ghost': 0,
	},
	'fighting': {
		'fire': 1,
		'water': 1,
		'electric': 1,
		'ice': 2,
		'ground': 1,
		'rock': 2,
		'grass': 1,
		'bug': .5,
		'poison': .5,
		'psychic': .5,
		'dark': 2,
		'flying': .5,
		'normal': 2,
		'fighting': 1,
		'fairy': .5,
		'dragon': 1,
		'steel': 2,
		'ghost': 0,
	},
	'fairy': {
		'fire': .5,
		'water': 1,
		'electric': 1,
		'ice': 1,
		'ground': 1,
		'rock': 1,
		'grass': 1,
		'bug': 1,
		'poison': .5,
		'psychic': 1,
		'dark': 2,
		'flying': 1,
		'normal': 1,
		'fighting': 2,
		'fairy': 1,
		'dragon': 2,
		'steel': .5,
		'ghost': 1,
	},
	'dragon': {
		'fire': 1,
		'water': 1,
		'electric': 1,
		'ice': 1,
		'ground': 1,
		'rock': 1,
		'grass': 1,
		'bug': 1,
		'poison': 1,
		'psychic': 1,
		'dark': 1,
		'flying': 1,
		'normal': 1,
		'fighting': 1,
		'fairy': 0,
		'dragon': 2,
		'steel': .5,
		'ghost': 1,
	},
	'steel': {
		'fire': .5,
		'water': .5,
		'electric': .5,
		'ice': 2,
		'ground': 1,
		'rock': 2,
		'grass': 1,
		'bug': 1,
		'poison': 1,
		'psychic': 1,
		'dark': 1,
		'flying': 1,
		'normal': 1,
		'fighting': 1,
		'fairy': 2,
		'dragon': 1,
		'steel': .5,
		'ghost': 1,
	},
	'ghost': {
		'fire': 1,
		'water': 1,
		'electric': 1,
		'ice': 1,
		'ground': 1,
		'rock': 1,
		'grass': 1,
		'bug': 1,
		'poison': 1,
		'psychic': 2,
		'dark': .5,
		'flying': 1,
		'normal': 0,
		'fighting': 1,
		'fairy': 1,
		'dragon': 1,
		'steel': 1,
		'ghost': 2,
	},
}


def get_damage_multiplier(attacker_type_primary, defender_type_primary, attacker_type_secondary=None,
                          defender_type_secondary=None):
	attacker_primary_type_modifier = type_attacks[attacker_type_primary][defender_type_primary]
	if defender_type_secondary:
		attacker_primary_type_modifier = attacker_primary_type_modifier * type_attacks[attacker_type_primary][
			defender_type_secondary]

	attacker_secondary_type_modifier = type_attacks[attacker_type_secondary][defender_type_primary]
	if defender_type_secondary:
		attacker_secondary_type_modifier = attacker_primary_type_modifier * type_attacks[attacker_type_secondary][
			defender_type_secondary]

	return attacker_primary_type_modifier, attacker_secondary_type_modifier


# print(get_damage_multiplier('grass', 'bug', 'poison', 'fairy'))


def get_mon(id):
	response = pokebase.pokemon(id)
	return Pokemon(response)


class Pokemon:
	def __init__(self, pokebase_mon):
		self.pokebase_mon = pokebase_mon
		self.id = pokebase_mon.id
		self.name = pokebase_mon.name
		self.types = [type.type.name for type in pokebase_mon.types]


def type_advantage(atk_type, def_type):
	return type_attacks[atk_type][def_type]


def atk_advantage(atk_type, def_mon):
	multipliers = [type_advantage(atk_type, def_type) for def_type in def_mon.types]
	ret = functools.reduce(lambda x, y: x * y, multipliers)
	# print(atk_type + ' against ' + def_mon.name + ' ' + str(multipliers))
	return ret


def mon_advantage(atk_mon, def_mon):
	advantages = [atk_advantage(atk_type, def_mon) for atk_type in atk_mon.types]
	advantages.sort()
	return advantages[-1]


def mon_matchup(mon_a, mon_b):
	return Matchup(mon_a, mon_b, mon_advantage(mon_a, mon_b), mon_advantage(mon_b, mon_a))


def get_team(team_names):
	return [get_mon(name) for name in team_names]


class Matchup:
	def __init__(self, a, b, ab, ba):
		self.a = a
		self.b = b
		self.ab = ab
		self.ba = ba

	def __str__(self):
		return str(str(self.ab) + ', ' + str(self.ba))


team_names = [
	'tyranitar',
	'rayquaza',
	'slowbro',
	'ferrothorn',
	'flygon',
	'heatran',
	# 'crawdaunt',
	# 'umbreon'
]
enemy_team_names = ['houndoom', 'marshadow', 'dragonite', '647', 'raikou', 'starmie', 'toxapex']
# team_names = ['ferrothorn']
# enemy_team_names = ['heatran']

team = get_team(team_names)
enemy_team = get_team(enemy_team_names)

# team_types = [[type.pokebase_type.type.name for type in mon.types] for mon in team]
#
# types = type_attacks.keys()

for enemy_mon in enemy_team:
	print(enemy_mon.name)
	type_advantages = [mon_matchup(mon, enemy_mon) for mon in team]
	type_advantages.sort(key=lambda x: x.ab / x.ba if x.ba else x.ab + .1, reverse=True)
	for adv in type_advantages:
		print('    vs ' + adv.a.name + ' ' + str(adv))
