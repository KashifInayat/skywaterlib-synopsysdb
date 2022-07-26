
#!/bin/bash
#KASHIIF_INAYAT_SOCLAB-INU

Log_File=./make.log


function CommandLog(){
author='KashifInayat Script-INU'
startdate=$(date)
scriptName='make.log'

echo "${author}"
echo "[$startdate]:[Conversion]: This is ${scriptName}, which shows the loging of skywater-pdk conversion from .lib to .db:"

set -ex

echo "=============================================="
echo "---- Clone the Library---"
echo "=============================================="
echo
git clone https://github.com/KashifInayat/skywater-pdk.git
cd skywater-pdk
git checkout main
cd ../

pip install sphinx_materialdesign_theme

pip install --upgrade symbolator
}

CommandLog |& tee "${Log_File}"