#!/bin/bash
classId=0

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
    local parentId="$1"
    local parentSplit="$2"
    local level="$3"
    nb="$4"
    list="$5"

    local myClassId=$((classId+1))
    let classId+=1
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
        results=""
        for line in $(echo "$list" | tr '\n' ' ')
        do
            result=$(echo $line | sed "s/.*://g")
            data=$(echo $line | sed "s/:.*//g")
            criteria=$(echo $data | cut -d ',' -f $i)

            results=$(echo -e "$results\n$result")
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

    if [ $(echo "$results" | sort | uniq | wc -l) -eq 3 ]
    then
        local newNb=$(echo $nb | sed "s/$best//g; s/ +/ /g; s/^ //g; s/ $//g")
        local newLevel=$((level+1))

        echo -e "class \"Split on I_$best\" as $myClassId{\n$list\n}\n" >> graph.uml
        if [ $parentId -ne 0 ];then echo "$parentId -- $myClassId : $parentSplit" >> graph.uml; fi


        echo "Split I_$best"

        indent $level
        echo -n "0:  "
        if [ "$listZero" ]; then recc "$myClassId" "0" "$newLevel" "$newNb" "$listZero"; else echo ""; fi

        indent $level
        echo -n "1:  "
        if [ "$listOne" ]; then recc "$myClassId" "1" "$newLevel" "$newNb" "$listOne"; else echo ""; fi
    else
        echo ""
        echo -e "class \"No Split needed\" as $myClassId{\n$list\n}\n" >> graph.uml
        if [ $parentId -ne 0 ];then echo "$parentId -- $myClassId : $parentSplit" >> graph.uml; fi
    fi
}

list=$(cat d | sed "s/ //g")
nb=$(seq $(echo "$list"| head -n 1 | sed "s/[^,]//g" | wc -c))

echo "@startuml" > graph.uml
recc "0" "0" "0" "$nb" "$list"
echo "hide empty methods" >> graph.uml
echo "@enduml" >> graph.uml
