###########################################################################
# following method, you will need to repeat the module name again and again.
###########################################################################

import module_with_logo_and_art

print(module_with_logo_and_art.logo)
print(module_with_logo_and_art.art)

###########################################################################
# following method, you only need to mention the variable name. Same
###########################################################################

from module_with_logo_and_art import logo
from module_with_logo_and_art import art

print(logo)
print(art)
