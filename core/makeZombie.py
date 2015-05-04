# ...\addons\source-python\plugins\zombiemod\core\makeZombie.py


# =============================================================================
# >> IMPORTS
# =============================================================================


# SOURCE PYTHON IMPORTS
from players.entity import PlayerEntity
from entities.entity import BaseEntity
from players.helpers import index_from_userid
from players.entity import PlayerEntity
from entities.helpers import spawn_entity
from filters.players import PlayerIter
from filters.entities import EntityIter
from engines.server import engine_server
from entities.helpers import create_entity

from events  import Event

# TRANSLATOR IMPORTS
from translations.strings import LangStrings
from zombiemod.core.translator import sendMessage


#ZOMBIE_EVENT
from events.custom import CustomEvent
from events.variable import StringVariable
from events.variable import ShortVariable
from events.variable import BoolVariable


# RESTRICTIONS IMPORT
from zombiemod.core.restriction import dropWeapon, get_player_restriction


# GAME PATH IMPORTS
from zombiemod.paths.path import Z_INI_PATH

# DELAY IMPORT
from listeners.tick.delays import tick_delays


# =============================================================================
# >> GLOBALS
# =============================================================================

__messages = sendMessage(LangStrings('zombiemod'))



# =============================================================================
# >> CLASSES
# =============================================================================


class PlayerDict(dict):
    def __getitem__(self, index):
        if index in self:
            return super(PlayerDict, self).__getitem__(index)
        x = self[index] = Zombie('FirstZombie', index)
        return x
 
    def __delitem__(self, index):
        if index in self:
            super(PlayerDict, self).__delitem__(index)
			
 


class Zombie(object):

    def __init__(self, zombie_type, index):
	
        self.zombie_type = zombie_type

            
            
        self.index = index
		
        self.validated = 0
      
        self.model_path = Z_INI_PATH[zombie_type]['model']
        self.health = int(Z_INI_PATH[zombie_type]['health'])
        self.speed = int(Z_INI_PATH[zombie_type]['speed'])
        self.crouch_speed = int(Z_INI_PATH[zombie_type]['crouch_speed'])
        self.run_speed = int(Z_INI_PATH[zombie_type]['run_speed'])
        self.jump_height = int(Z_INI_PATH[zombie_type]['jump_height'])
        self.knockback = int(Z_INI_PATH[zombie_type]['knockback'])
        self.headshots = int(Z_INI_PATH[zombie_type]['headshots'])
        self.hs_only = int(Z_INI_PATH[zombie_type]['hs_only'])
        self.regen_time = float(Z_INI_PATH[zombie_type]['regen_time'])
        self.gren_multiplier = float(Z_INI_PATH[zombie_type]['gren_multiplier'])
        self.gren_knockback = float(Z_INI_PATH[zombie_type]['gren_knockback'])
        self.health_bonus = int(Z_INI_PATH[zombie_type]['health_bonus'])

 
    def playerZombie(self):
    
        if not self.index in _players:
            for key in Z_INI_PATH:
                _players[self.index].Zombie = (key, self.index)

                
        player = PlayerEntity(self.index)
        switchTeam(self.index, 2)
        dropWeapon(self.index)
        player_restriction = get_player_restriction(self.index)
        player_restriction.add_restriction_by_filter(not_filters='knife')
        self.validated = 1
        #tick_delays.delay(0.1, self.zombie_round_end)
        self.playerAttr()
            
    def playerAttr(self):
        print ('atrrr')
        PlayerEntity(self.index).health = self.health
        #PlayerEntity(self.index).speed = self.speed
        
        
    def playerAttr_reset(self):
        PlayerEntity(self.index).health = 100
        #PlayerEntity(self.index).speed = 1.0
        
        
    def PlayerHuman(self):
        print('human fores')
        player_restriction = get_player_restriction(self.index)
        player_restriction.remove_restriction_by_filter(not_filters='knife')
        self.playerAttr_reset()
        self.validated = 0
        
        
    def getStatus(self):
        return self.validated
        
'''@Event
def player_team(game_event):
    zombie_round_end()
    
def zombie_round_end():
    if get_ALv_Player('ct') == 0:
        zombie_end_round_event(3)
    elif get_ALv_Player('t') == 0:
        zombie_end_round_event(1)
        
def get_ALv_Player(t):
    x = list(PlayerIter([t, 'alive']))
    return len(x)
		'''
		

        
        
class Player_Death(CustomEvent):
    userid = ShortVariable("PLAYER'S USERID")  
    attacker = ShortVariable("PLAYER'S ATTACKERID") 
    weapon = StringVariable("WEAPON")  
    headshot = BoolVariable("HEADSHOT")   
    dominated = ShortVariable("DOMINATION")  
    revenge = ShortVariable("REVENGE") 
    
    
def zombie_end_round_event(condition):  
    for info_map_parameters in EntityIter('info_map_parameters', return_types='entity'):
    
        break
        
    else:
    
        info_map_parameters = BaseEntity(create_entity('info_map_parameters'))
        
    info_map_parameters.get_input('FireWinCondition')(condition)
    #info_map_parameters.fire_win_condition(condition)
    
'''def zombie_end_round_event(condition):
 
    for info_map_parameters in EntityIter('info_map_parameters', return_types='entity'):
    
        break
    else:
        info_map_parameters = BaseEntity.create('info_map_parameters')

    info_map_parameters.call_input('FireWinCondition', condition)
   '''
   
   

def _displayScreen(screen):   
    for edict in list(PlayerIter('all', return_types='edict')):
        engine_server.client_command(edict, 'r_screenoverlay ' + screen)

    
'''class Round_End(CustomEvent):
    winner = ShortVariable("WINNER TEAM") 
    reason = ShortVariable("REASON")
    message = StringVariable("MESSAGE")'''
        

_players = PlayerDict()




# =============================================================================
# >> FUNCTIONS
# =============================================================================


def switchTeam(index, team):
    if not index:
        return
        
    Player = PlayerEntity(index)
    if not Player.get_team() == team:
        Player.switch_team(team, False, False)
		
		



'''

ini File. Da sollten sich die Daten von den Classen geholt werden.

z.B FirstZombie.ini



[FirstZombie]
modelpath = 'test/test.mdl'
health = 100

# usw.

[ScaryZombie]
modelpath = 'test/test2.mdl'
health = 200

if player.is_dead():
            print ('player was death')
            player.set_property_int('m_iPlayerState', 0)
            player.godmode = False
            spawn_entity(player.index)
            
            
ЯoOF |- 21 -

'''

# END


'''
class FirstZombie(PlayerClass):

    classname = 'First Zombie' # Ich möchte den namen mit samt den Settings von einem ini file laden
    
    model = my_ini_file[FirstZombie.classname]['path']
    health = int(my_ini_file[FirstZombie.classname]['health'])
 
    def playerZombie(self):
        userid = self.userid
        pass
 
    def playerDamage(self, weapon, victim, damage):
        pass

 #hooks
 
from entities.entity import BaseEntity

from memory.hooks import PreHook

@PreHook(BaseEntity(0).take_damage)
def pre_on_take_damage(args):
    print(tuple(args))



'''


#zombie = Zombie('FirstZombie', <player_index>)








