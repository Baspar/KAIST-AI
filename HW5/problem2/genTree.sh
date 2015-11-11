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

    best=0
    bestEntropy=0

    local listZero=""
    local listOne=""

    #Init
    for i in $nb
    do
        nbZeroInZero[$i]=0
        nbOneInZero[$i]=0
        nbOneInOne[$i]=0
        nbZeroInOne[$i]=0

        listZeroTmp[$i]=""
        listOneTmp[$i]=""
        results[$i]=""
    done

    #Compute original entropy (Of the parent)
    nbOriginalZero=$(echo "$list"| sed "s/.*://g" | grep 0 | wc -l)
    nbOriginalOne=$(echo "$list"| sed "s/.*://g" | grep 1 | wc -l)
    originalEntropy=$(computeEntropy $nbOriginalZero $nbOriginalOne)


    #Read input list to fill information about 0 and 1
    for line in $(echo "$list" | tr '\n' ' ')
    do
        result=$(echo $line | sed "s/.*://g")
        data=$(echo $line | sed "s/:.*//g")
        for i in $nb
        do
            criteria=$(echo $data | cut -d ',' -f $i)

            results[$i]=$(echo -e "${results[$i]}\n$result")
            if [ $criteria -eq 0 ]
            then
                listZeroTmp[$i]=$(echo -e "${listZeroTmp[$i]}\n$line")
                if [ $result -eq 0 ]
                then
                    let nbZeroInZero[$i]+=1
                else
                    let nbOneInZero[$i]+=1
                fi
            else
                listOneTmp[$i]=$(echo -e "${listOneTmp[$i]}\n$line")
                if [ $result -eq 0 ]
                then
                    let nbZeroInOne[$i]+=1
                else
                    let nbOneInOne[$i]+=1
                fi
            fi
        done
    done

    #Take the best children entropy
    for i in $nb
    do
        averageEntropy=$(computeAverageEntropy ${nbZeroInZero[$i]} ${nbOneInZero[$i]} ${nbZeroInOne[$i]} ${nbOneInOne[$i]})
        informationGain=$(echo "$originalEntropy-$averageEntropy" | bc -l)
        if [ $(echo "$informationGain<$bestEntropy" | bc -l) -eq 0 ]
        then
            bestEntropy=$informationGain
            best=$i
            listZero="${listZeroTmp[$i]}"
            listOne="${listOneTmp[$i]}"
        fi
    done

    #Print this step information for the graph
    echo -e "class \"Split on I_$best\" as $myClassId{\n$list\n}\n" >> graph.uml
    if [ $parentId -ne 0 ];then echo "$parentId --> $myClassId : $parentSplit" >> graph.uml; fi

    #See if we need to go reccursively, and go reccusrive
    if [ $(echo "${results[$best]}" | sort | uniq | wc -l) -eq 3 ]
    then
        local newNb=$(echo $nb | sed "s/$best//g; s/ +/ /g; s/^ //g; s/ $//g")
        local newLevel=$((level+1))


        echo "Split I_$best"

        indent $level
        echo -n "0:  "
        if [ "$listZero" ]; then recc "$myClassId" "0" "$newLevel" "$newNb" "$listZero"; else echo ""; fi

        indent $level
        echo -n "1:  "
        if [ "$listOne" ]; then recc "$myClassId" "1" "$newLevel" "$newNb" "$listOne"; else echo ""; fi
    else
        echo " Leaf"
    fi
}

list=$(cat d | sed "s/ //g")
nb=$(seq $(echo "$list"| head -n 1 | sed "s/[^,]//g" | wc -c))

echo "@startuml" > graph.uml
recc "0" "0" "0" "$nb" "$list"
echo "hide empty methods" >> graph.uml
echo "@enduml" >> graph.uml
