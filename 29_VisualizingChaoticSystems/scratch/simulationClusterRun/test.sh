#!/bin/bash

# for dir in *_System
# do
#     val=`echo $dir | cut -d '_' -f 2- | sed 's/_/ /g' | awk '{print $0}'`
#     sysName=`echo $val| rev | cut -d ' ' -f 2- | rev`
#
#     cp README.md $dir/cppCode/
#
#     sed -i "s/CHAOTIC/$sysName/g" $dir/cppCode/README.md
#     echo $sysName
# done


for dir in ../../*_System
do
    dirName=`echo $dir | cut -d'/' -f 3`
    cp -r $dirName/cppCode $dir/
    echo $dirName
done
