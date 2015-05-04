# ======================================================================
# >> IMPORTS
# ======================================================================


# SOURCE PYTHON IMPORT

from messages import SayText2



# ======================================================================
# >> FUNCTIONS
# ======================================================================



def sendMessage(lang_strings):

    return {key: SayText2(message=lang_strings[key]) for key in lang_strings}

