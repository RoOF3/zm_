# ../zombiemod/paths/path.py

# =============================================================================
# >> IMPORTS
# =============================================================================


# PYTHON IMPORT

from configobj import ConfigObj


# SOURCE PYTHON IMPORT PATH

from paths import BASE_PATH
from paths import GAME_PATH



# =============================================================================
# >> GENERAL VARIABLE
# =============================================================================

Z_INI_PATH = ConfigObj(BASE_PATH.joinpath('plugins', 'zombiemod' + '\classes.ini'), encoding= 'utf_8')

Z_MATERIALS = GAME_PATH / 'materials' / 'zombiemod' / 'hud'

