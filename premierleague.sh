#!/bin/bash
##创建比分存储文件
cd /home/pl/
if [ ! -d "pl" ]; then
   mkdir pl
fi
cd pl
for ((i=1;i<21;i++)); do
   for ((j=1;j<21;j++)); do
   if [ $i -ne $j ]; then  
       file=`echo $i`_`echo $j`
       if [ -f /home/pl/pl/$file ]; then
          echo "$file文件已存在"
       else
          touch /home/pl/pl/$file
       fi
   fi
   done
done
##结束创建比分存储文件
