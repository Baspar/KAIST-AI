#!/bin/bash
indent(){
    for i in $(seq $1);do echo -n "    "; done
}
log(){
    echo "l($1)/l(2)" | bc -l
}
computeEntropy(){
    zero=$1
    one=$2
    total=$((zero+one))
    out=0

    if [ $zero -ne 0 ]
    then
        out=$(echo "$out-($zero/$total*$(log $zero/$total))"| bc -l)
    fi
    if [ $one -ne 0 ]
    then
        out=$(echo "$out-($one/$total*$(log $one/$total))"| bc -l)
    fi

    echo $out
}
computeAverageEntropy(){
    nbZeroInZero=$1
    nbOneInZero=$2
    nbZeroInOne=$3
    nbOneInOne=$4

    totalInZero=$((nbZeroInZero+nbOneInZero))
    totalInOne=$((nbZeroInOne+nbOneInOne))
    total=$((nbZeroInZero+nbOneInZero+nbZeroInOne+nbOneInOne))

    out=0
    if [ $total -ne 0 ]
    then
        out=$(echo "$totalInZero/$total*$(computeEntropy $nbZeroInZero $nbOneInZero) + $totalInOne/$total*$(computeEntropy $nbZeroInOne $nbOneInOne)" | bc -l)
    fi

    echo $out
}
recc(){
    local level="$1"
    nb="$2"
    list="$3"

    total=$(echo "$list" | wc -l)

    nbOriginalZero=$(echo "$list"| sed "s/.*://g" | grep 0 | wc -l)
    nbOriginalOne=$(echo "$list"| sed "s/.*://g" | grep 1 | wc -l)
    originalEntropy=$(computeEntropy $nbOriginalZero $nbOriginalOne)

    best=0
    bestEntropy=0

    local listZero=""
    local listOne=""
    for i in $nb
    do
        nbZeroInZero=0
        nbOneInZero=0
        nbOneInOne=0
        nbZeroInOne=0

        listZeroTmp=""
        listOneTmp=""
        for line in $(echo "$list" | tr '\n' ' ')
        do
            result=$(echo $line | sed "s/.*://g")
            data=$(echo $line | sed "s/:.*//g")
            criteria=$(echo $data | cut -d ',' -f $i)
            if [ $criteria -eq 0 ]
            then
                listZeroTmp=$(echo -e "$listZeroTmp\n$line")
                if [ $result -eq 0 ]
                then
                    let nbZeroInZero+=1
                else
                    let nbOneInZero+=1
                fi
            else
                listOneTmp=$(echo -e "$listOneTmp\n$line")
                if [ $result -eq 0 ]
                then
                    let nbZeroInOne+=1
                else
                    let nbOneInOne+=1
                fi
            fi
        done
        averageEntropy=$(computeAverageEntropy $nbZeroInZero $nbOneInZero $nbZeroInOne $nbOneInOne)
        informationGain=$(echo "$originalEntropy-$averageEntropy" | bc -l)
        if [ $(echo "$informationGain<$bestEntropy" | bc -l) -eq 0 ]
        then
            bestEntropy=$informationGain
            best=$i
            listZero="$listZeroTmp"
            listOne="$listOneTmp"
        fi
    done

    local newNb=$(echo $nb | sed "s/$best//g; s/ +/ /g; s/^ //g; s/ $//g")
    local newLevel=$((level+1))

    #indent $level
    echo "Split I_$best"

    indent $level
    echo -n "0:  "
    if [ "$newNb" ]; then recc "$newLevel" "$newNb" "$listZero"; else echo ""; fi

    indent $level
    echo -n "1:  "
    if [ "$newNb" ]; then recc "$newLevel" "$newNb" "$listOne"; else echo ""; fi
}

list=$(cat d | sed "s/ //g")
nb=$(seq $(echo "$list"| head -n 1 | sed "s/[^,]//g" | wc -c))

recc "0" "$nb" "$list"
