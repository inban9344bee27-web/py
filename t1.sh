#!/bin/blash
#for arg in "$@"
#do
  # index=$(echo $arg | cut -f1 -d = )
   #val=$(echo $arg | cut -f2 -d = )
   #case $index in
      x=$1
      y=$2


#   esac
#done
((result=x+y))
echo "X + Y =$result "
