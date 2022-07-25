import re
import os
import sys
import math

##*****************************##
##        Conversion Start     ##
##*****************************##

print("write one of these [sc_hd, sc_hdll, sc_hs, sc_ls or sc_ms] to compile other SC variants")

typ = input("\n")#same as in script initial delay in SAs

lib="sky130_fd_"+typ

os.system("sh conversion_run.sh"+" "+str(lib))


##***************************##
##        Conversion End     ##
##***************************##
