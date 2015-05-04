# ...\addons\source-python\plugins\zombiemod\core\signature.py



# =============================================================================
# >> IMPORTS
# =============================================================================

# SOURCE PYTHON IMPORTS

import memory

from memory import find_binary
from memory import Convention
from memory import DataType
from core import PLATFORM






# =============================================================================
# >> CONSTANTS
# =============================================================================
if PLATFORM == 'windows':

    # PLAYER HURT

    ON_TAKE_DAMAGE_IDENTIFIER = b'\x55\x8B\xEC\x81\xEC\x44\x01\x2A\x2A\x56' \
        b'\x89\x4D\xFC'
    # RESTRICT

    identifier = b'\x55\x8B\xEC\x83\xEC\x38\x89\x4D\xF4'
    
else:

    # PLAYER HURT

    ON_TAKE_DAMAGE_IDENTIFIER = '_ZN20CBaseCombatCharacter12OnTakeDamageERK15CTakeDamageInfo' 

    # RESTRICT

    identifier = '_ZN9CCSPlayer10BumpWeaponEP17CBaseCombatWeapon'



# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================

server = find_binary('cstrike/bin/server')

OnTakeDamage = server[ON_TAKE_DAMAGE_IDENTIFIER].make_function(Convention.THISCALL, (DataType.POINTER, DataType.POINTER), DataType.VOID)

BUMP_WEAPON = server[identifier].make_function(Convention.THISCALL, (DataType.POINTER, DataType.POINTER), DataType.BOOL)