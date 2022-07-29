import re
import os
import sys
import math

##*****************************##
##        Conversion Start     ##
##*****************************##
pdk_list= ["sc_hd","sc_hs", "sc_ls", "sc_ms"]

#typ = input("\n")#same as in script initial delay in SAs

for i in pdk_list:
    lib="sky130_fd_"+i
    os.system("sh conversion_run.sh"+" "+str(lib))


##***************************##
##        Conversion End     ##
##***************************##
