# -\*- coding: utf-8 -\*-
# ...\addons\source-python\plugins\zombiemod\zombiemod.py



# =============================================================================
# >> IMPORTS
# =============================================================================



# PYTHON IMPORT
import random

# SOURCE PYTHON IMPORTS
from events  import Event
from players.helpers import index_from_userid
from players.entity import PlayerEntity
from filters.players import PlayerIter
from engines.server import engine_server
from players.helpers import playerinfo_from_userid
from entities import TakeDamageInfo
from filters.entities import EntityIter
from entities.entity import BaseEntity




# TRANSLATOR IMPORT
from translations.strings import LangStrings
from zombiemod.core.translator import sendMessage

# GENERAL ZOMBIEMOD IMPORTS
from zombiemod.core.makeZombie import _players, switchTeam, Player_Death, _displayScreen, zombie_end_round_event
from zombiemod.core.restriction import dropWeapon, get_player_restriction
from zombiemod.paths.path import Z_INI_PATH, Z_MATERIALS
from zombiemod.core.signature import OnTakeDamage


#DOWNLOADS
from stringtables.downloads import Downloadables


# PLUGIN STUFF IMPORTS
from cvars import ConVar
from cvars.flags import ConVarFlags
from plugins.info import PluginInfo


# DELAY IMPORT
from listeners.tick.delays import tick_delays


# PRE HOOK IMPORTS

from memory.hooks import PreHook
from memory import make_object



# =============================================================================
# >> PLUGIN INFORMATION
# =============================================================================

info = PluginInfo()
info.author = 'RoOF'
info.basename = 'zombiemod'
info.name = 'ZombieMod'
info.description = 'Orginal Zombiemod'
info.version = '1.1'
info.url = 'http://roof3.de'

ConVar('zombiemod_version', info.version, ConVarFlags.NOTIFY, info.description)
'''

    userid = GameEvent.GetInt('userid')
    player = Player.EdictOfUserid(userid)
    index = Engine.IndexOfEdict(player)
	#for userid in PlayerIter(return_types='userid'):
'''

# =============================================================================
# >> GLOBALS
# =============================================================================

__messages = sendMessage(LangStrings('zombiemod'))

# =============================================================================
# >> SETTINGS
# =============================================================================

# Minimum amount of seconds after round_freeze_end for first random Zombification.
zombie_timer_min = 2

#  Maximum amount of seconds after round_freeze_end for first random Zombification.
zombie_timer_max = 5

_firstZombie = list()

dl = Downloadables()


# =============================================================================
# >> LOAD AND UNLOAD FUNCTIONS
# =============================================================================

def load():

    engine_server.server_command('mp_restartgame 1\n')
    
    __messages['Plugin Loaded'].send()
        
        
        
def unload():
    _players.clear()

	
	
# =============================================================================
# >> GAME EVENTS
# =============================================================================


@Event
def round_start(event):
    #print (round(random.uniform(zombie_timer_min, zombie_timer_max), 2))
    #say_delay = Timer(round(random.uniform(zombie_timer_min, zombie_timer_max), 2), zombiefyme,())
    #round(random.uniform(zombie_timer_min, zombie_timer_max), 2)
    #tick_delays.delay(round(random.uniform(zombie_timer_min, zombie_timer_max), 2), zombiefyme)
    #tick_delays.cancel_delay(zDelay)
    #print (round(random.uniform(zombie_timer_min, zombie_timer_max), 2))
    #say_delay.start()
    #tick_delays.delay(round(random.uniform(zombie_timer_min, zombie_timer_max), 2), zombiefyme())
	#tick_delays.delay(12, zombiefyme)
    zombiefyme()
	
'''@Event
def player_say(event):
    tick_delays.delay(round(random.uniform(zombie_timer_min, zombie_timer_max), 2), zombiefyme)
	
	
@Event
def player_say(game_event):
    global _firstZombie
    #for key in Z_INI_PATH:
        #_players[index_from_userid(game_event.get_int('userid'))].Zombie = (key, index_from_userid(game_event.get_int('userid')))
    print (PlayerEntity(index_from_userid(game_event.get_int('userid'))).steamid)
    if PlayerEntity(index_from_userid(game_event.get_int('userid'))).steamid == 'STEAM_0:1:11481373':
        #print (_players[index_from_userid(game_event.get_int('userid'))].Zombie)
        print(_players)
        

        _firstZombie = index_from_userid(game_event.get_int('userid'))
        
        zombiefyme(index_from_userid(game_event.get_int('userid')))

'''
        


# =============================================================================
# >> CALLBACK
# =============================================================================
@PreHook(OnTakeDamage)
def pre_on_take_damage(args):
    attack = make_object(TakeDamageInfo, args[1])
    attacker = PlayerEntity(attack.attacker)
    victim = make_object(PlayerEntity, args[0])
    if attacker.get_team() == victim.get_team() or attacker == victim:
        return

    if _players[attack.attacker].getStatus():
        
        attacker.kills += 1
        
        event = Player_Death()
        event.userid = victim.userid
        event.attacker = attacker.userid
        event.weapon = 'weapon_knife'
        event.headshot = False
        event.dominated = 0
        event.revenge = 0
        event.fire()
        #zombie_round_end()
        #tick_delays.delay(0.1, zombie_round_end)
        for key in Z_INI_PATH:
            _players[victim.index].Zombie = (key, victim.index)
        _players[victim.index].playerZombie()
        #tick_delays.delay(0.1, _players[victim.index].playerZombie())
        
@Event
def player_death(game_event):
     tick_delays.delay(0.1, zombie_round_end)
    
def zombie_round_end():
    if get_ALv_Player('ct') == 0:
        zombie_end_round_event(8)
    #elif get_ALv_Player('t') == 0:
        #zombie_end_round_event(1)
        
def get_ALv_Player(t):
    x = list(PlayerIter([t, 'alive']))
    return len(x)
        
@Event
def round_end(game_event):
    if game_event.get_int('reason') == 7:
        _displayScreen('zombiemod/hud/1024_humans.vmt')
        #set_team_score(3, 1)
        print ('ct won')
    elif game_event.get_int('reason') == 8:
        _displayScreen('zombiemod/hud/1024_zombies.vmt')
        #set_team_score(2, 1)
        print ('t won')
    for x in _players:
        _players[x].PlayerHuman()
        
        
@Event
def round_start(game_event):
    _displayScreen('0')
        

  

# =============================================================================
# >> FUNCTIONS
# =============================================================================

		
def zombiefyme():
    switchTeam(getPlayer(), 2)
    _players[getPlayer()].playerZombie()
    print (list(PlayerIter('all')))
    print('exe')
    for Players in getRestPlayer():
        switchTeam(Players, 3)
	
def getPlayer():
    global _firstZombie

    if not len(PlayerIter('all')):
        return
        
    _firstZombie = random.choice(list(PlayerIter('all', return_types='index')))
    return _firstZombie
	
def getRestPlayer():
    RestPlayers = list(PlayerIter('all', return_types='index'))
    RestPlayers.remove(_firstZombie)
    return RestPlayers
    
    
def prepare_materials():
    '''
    Adds all found paintball materials to the download table and returns the
    added material names as a tuple.
    '''

    materials = set()

    # Loop through all paintball material files
    for f in Z_MATERIALS.files():
        materials.add('hud/%s.vmt'% f.namebase)

        # Add the file to the download table
        dl.add(str('materials/zombiemod/hud/' + f.basename()))

    return tuple(materials)

materials = prepare_materials()

# Check if any material was found
if not materials:
    raise ValueError('No materials were found.')
	
    
def set_team_score(team, score):

    for entity in EntityIter('cs_team_manager', return_types='entity'):
        
        if entity.team != team:

            continue

        print(dir(entity))

        entity.set_prop_int('m_scoreTotal', score)
	
	  
'''class ZombieClass():
    zClass = None
 
    def __init__(self, index):
        self.index = index
        print('You are in !!')
		
class PlayerDict(dict):
    def __getitem__(self, index):
        if index in self:
            return super(PlayerDict, self).__getitem__(index)
        x = self[index] = ZombieClass(index)
        return x
 
    def __delitem__(self, index):
        if index in self:
            super(PlayerDict, self).__delitem__(index)
 
zombies = PlayerDict()


@Event
def player_death(game_event):
    print(get_ALv_Player('ct'))
    print(type(get_ALv_Player('ct')))
    print(PlayerEntity(index_from_userid(game_event.get_int('userid'))).get_name())
    if get_ALv_Player('ct') == 0 or get_ALv_Player('t') == 0:
       __messages['Plugin Loaded'].send()

        
        
def get_ALv_Player(t):
    x = list(PlayerIter([t, 'alive']))
    return len(x)
'''



'''
	
@Event
def player_hurt(game_event):
    victim = game_event.get_int('userid')
    attacker = game_event.get_int('attacker')
    index = index_from_userid(victim)
    aindex = index_from_userid(attacker)
    #print ('Player '+ str(PlayerEntity(aindex).name)+ ' knifed '+ str(PlayerEntity(index).name))
    #print ('index '+ str(index))
    print ('ROOF is not a fucking zombie')
    print (_players[aindex].getStatus())
    if _players[aindex].getStatus():
        print ('ROOF is a fucking zombie')
        #print ('Player '+ str(PlayerEntity(aindex).name)+ ' knifed '+ str(PlayerEntity(index).name)+' and is a zombie')
        #print('status forced')
        _players[index].playerHit(index, game_event.get_string('weapon'), playerinfo_from_userid(attacker).get_team_index(),  playerinfo_from_userid(victim).get_team_index())
        
for userid in PlayerIter(return_types='userid'):
        index = index_from_userid(use
        SayText2(message='The Random userid is'+ str(random.choice(list(PlayerIter(return_types='userid'))))).send(index)'''
		
		
		






