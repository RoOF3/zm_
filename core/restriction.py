# ...\addons\source-python\plugins\zombiemod\core\restriction.py


# =============================================================================
# >> IMPORTS
# =============================================================================

# PYTHON IMPORT
import collections


# SOURCE PYTHON IMPORTS
from entities.helpers import index_from_pointer
from entities.entity import BaseEntity
from players.entity import PlayerEntity
from entities.helpers import remove_entity
from filters.weapons import WeaponClassIter
from weapons.entity import WeaponEntity

# SP HOOK IMPORT

from memory.hooks import PreHook
from memory import make_object
from zombiemod.core.signature import BUMP_WEAPON
 
 
# =============================================================================
# >> CLASSES
# =============================================================================
class PlayerRestriction(set):
    def is_restricted(self, weapon):
        return weapon in self
 
    def add_restriction(self, weapon):
        self.add(weapon)
 
    def add_restriction_by_filter(self, is_filters=None, not_filters=None):
        self.update(WeaponClassIter(
            is_filters, not_filters, return_types='classname'))
 
    def remove_restriction(self, weapon):
        self.discard(weapon)
 
    def remove_restriction_by_filter(self, is_filters=None, not_filters=None):
        self.difference_update(WeaponClassIter(
            is_filters, not_filters, return_types='classname'))
 
player_restrictions = collections.defaultdict(PlayerRestriction)
 
 
# =============================================================================
# >> FUNCTIONS
# =============================================================================
def get_player_restriction(player_index):
    return player_restrictions[player_index]
 
 
# =============================================================================
# >> HOOKS
# =============================================================================
@PreHook(BUMP_WEAPON)
def pre_bump_weapon(args):
    player_index = index_from_pointer(args[0])
    weapon = make_object(WeaponEntity, args[1])
    player_restriction = get_player_restriction(player_index)
    if player_restriction.is_restricted(weapon.classname):
        return False

'''

# =============================================================================
# >> GLOBALS
# =============================================================================

restrictions = {}

__all__ = ['Restrict']



# =============================================================================
# >> GLOBAL VARIABLES | HOOK EVENT
# =============================================================================

server = memory.find_binary('cstrike/bin/server')

if PLATFORM == 'windows':
    identifier = b'\x55\x8B\xEC\x83\xEC\x38\x89\x4D\xF4'
else:
    identifier = '_ZN9CCSPlayer10BumpWeaponEP17CBaseCombatWeapon'

BUMP_WEAPON = server[identifier].make_function(
    Convention.THISCALL,
    (DataType.POINTER, DataType.POINTER),
    DataType.BOOL
)

@PreHook(BUMP_WEAPON)
def pre_bump_weapon(args):
    player_index = index_from_pointer(args[0])
    weapon_index = index_from_pointer(args[1])
    weapon = WeaponEntity(weapon_index)
    if player_index in restrictions:
        if weapon.classname in restrictions[player_index]:
            return False


# =============================================================================
# >> CLASSES
# =============================================================================
		
		
		
class weaponSet(set):
    def __init__(self, index):
        self.index = index
    
    def add(self, items):
	
        
        @ index = int: index of Palyer
        @.add  = list:(['weapon_awp']) Add all Weapons which will be restricted
		
        Restrict(<index>).add(['__all']) will Restrict all Weapons from Game Except Knife
        Restrict(self.index).add(['weapon_usp','weapon_c4'])
		
        
	
        for item in items:
            if item not in self:
			
                if not item == '__all': 
                    set.add(self, item)
                else:
				
                    for weapon in WeaponClassIter(not_filters='knife'):
                        set.add(self, weapon.name)

    def discard(self, items):
        for item in items:
			
            if item in self:
			
                if not item == '__all':
                    set.discard(self, item)
                else:
				
                    for weapon in WeaponClassIter(not_filters='knife'):
                        set.discard(self, weapon.name)
				
'''
				
# =============================================================================
# >> FUNCTIONS
# =============================================================================

def dropWeapon(index):

    '''
    @ index = int: index of Palyer
	
    DROPS ALL WEAPONS IN PLAYERS HANDLE EXCEPT 
    '''
	
    player = PlayerEntity(index)
    for weapon_index in player.weapon_indexes(not_filters='knife'):
        weapon = BaseEntity(weapon_index)
        player.drop_weapon(weapon.pointer, None, None)
        # if allowed to :
        #remove_entity(weapon.index)
			

'''	
def Restrict(index):

    if not index in restrictions:
        restrictions[index] = weaponSet(index)


    return restrictions[index]
'''
	
	
	

		
		


