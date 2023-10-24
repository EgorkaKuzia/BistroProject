#!/bin/bash

strList=('Manera' 'Krytit' 'Mir')

function perebor{
    for t in ${strList[@]}; do
    echo $t
    done
    for i in ${!strList[@]}; do
        echo $i ${strList[$i]}
    done
