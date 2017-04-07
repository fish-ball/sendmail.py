#!/bin/bash

echo > command.log
echo "#0: $0" >> command.log
echo "#1: $1" >> command.log
echo "#2: $2" >> command.log
echo "#3: $3" >> command.log
echo "#4: $4" >> command.log
echo ">>>>>>" >> command.log
read fin; echo $fin >> command.log
echo ">>>>>>" >> command.log
read fin; echo $fin >> command.log
echo ">>>>>>" >> command.log
read fin; echo $fin >> command.log
echo ">>>>>>" >> command.log
read fin; echo $fin >> command.log
echo ">>>>>>" >> command.log
read fin; echo $fin >> command.log
echo ">>>>>>" >> command.log
read fin; echo $fin >> command.log
echo "<<<<<<" >> command.log
