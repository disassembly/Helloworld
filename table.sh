#!/bin/bash
##定义9项积分榜参数
clubname=( 莱斯特城 阿森纳 热刺 曼城 曼联 南安普敦 西汉姆联 利物浦 斯托克城 切尔西 埃弗顿 斯旺西 沃特福德 西布朗 水晶宫 伯恩茅斯 桑德兰 赫尔城 米堡 伯恩利 )
score=( 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 )
gs=( 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 )
gc=( 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 )
gd=( 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 )
victory=( 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 )
lose=( 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 )
draw=( 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 )
round=( 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 )
##定义9项积分榜参数

##计算每队的积分，进球，场次等情况
for (( i=1; i<21; i++)); do
    for (( j=1; j<21; j++)); do 
        file=/home/pl/pl/`echo $i`_`echo $j`
        if [ -s $file ]; then
            a=$(sed -n "1p" $file)
            b=$(sed -n "2p" $file)
            let " c = $i - 1"
            let " d = $j - 1"
            gs[$c]=`expr ${gs[$c]} + $a`
            gc[$c]=`expr ${gc[$c]} + $b`
            gd[$c]=`expr ${gs[$c]} - ${gc[$c]}`
            gs[$d]=`expr ${gs[$d]} + $b`
            gc[$d]=`expr ${gc[$d]} + $a`
            gd[$d]=`expr ${gs[$d]} - ${gc[$d]}`
            if [ $a -gt $b ]; then
                let "score[$c] = ${score[$c]} + 3"
                let "score[$d] = ${score[$d]} + 0"
                victory[$c]=`expr ${victory[$c]} + 1`
                lose[$d]=`expr ${lose[$d]} + 1`
            fi
            if [ $a -eq $b ]; then
                let "score[$c] = ${score[$c]} + 1"
                let "score[$d] = ${score[$d]} + 1"
                draw[$c]=`expr ${draw[$c]} + 1`
                draw[$d]=`expr ${draw[$d]} + 1`
            fi
            if [ $a -lt $b ]; then
                let "score[$c] = ${score[$c]} + 0"
                let "score[$d] = ${score[$d]} + 3"
                lose[$c]=`expr ${lose[$c]} + 1`
                victory[$d]=`expr ${victory[$d]} + 1`
            fi
            round[$c]=`expr ${victory[$c]} + ${draw[$c]} + ${lose[$c]}`
            round[$d]=`expr ${victory[$d]} + ${draw[$d]} + ${lose[$d]}`
        fi
    done
done 
##计算每队的积分，进球，场次等情况

##根据积分，净胜球，进球数的次序进行积分榜的排序
for (( u=0; u<20; u++)); do
    for (( v=`expr $u + 1`;v<20;v++)); do
        if [ ${score[$v]} -gt ${score[$u]} ]; then
            scoretmp=${score[$v]};score[$v]=${score[$u]};score[$u]=$scoretmp
            clubnametmp=${clubname[$v]};clubname[$v]=${clubname[$u]};clubname[$u]=$clubnametmp
            gstmp=${gs[$v]};gs[$v]=${gs[$u]};gs[$u]=$gstmp
            gctmp=${gc[$v]};gc[$v]=${gc[$u]};gc[$u]=$gctmp
            gdtmp=${gd[$v]};gd[$v]=${gd[$u]};gd[$u]=$gdtmp
            victorytmp=${victory[$v]};victory[$v]=${victory[$u]};victory[$u]=$victorytmp
            losetmp=${lose[$v]};lose[$v]=${lose[$u]};lose[$u]=$losetmp
            drawtmp=${draw[$v]};draw[$v]=${draw[$u]};draw[$u]=$drawtmp
            roundtmp=${round[$v]};round[$v]=${round[$u]};round[$u]=$roundtmp
        fi
        if [ ${score[$v]} -eq ${score[$u]} ]; then
            if [ ${gd[$v]} -gt ${gd[$u]} ]; then
                scoretmp=${score[$v]};score[$v]=${score[$u]};score[$u]=$scoretmp
                gstmp=${gs[$v]};gs[$v]=${gs[$u]};gs[$u]=$gstmp
                gctmp=${gc[$v]};gc[$v]=${gc[$u]};gc[$u]=$gctmp
                gdtmp=${gd[$v]};gd[$v]=${gd[$u]};gd[$u]=$gdtmp
                victorytmp=${victory[$v]};victory[$v]=${victory[$u]};victory[$u]=$victorytmp
                losetmp=${lose[$v]};lose[$v]=${lose[$u]};lose[$u]=$losetmp
                drawtmp=${draw[$v]};draw[$v]=${draw[$u]};draw[$u]=$drawtmp
                roundtmp=${round[$v]};round[$v]=${round[$u]};round[$u]=$roundtmp
                clubnametmp=${clubname[$v]};clubname[$v]=${clubname[$u]};clubname[$u]=$clubnametmp
            fi
            if [ ${gd[$v]} -eq ${gd[$u]} ]; then
                if [ ${gs[$v]} -gt ${gs[$u]} ]; then
                    scoretmp=${score[$v]};score[$v]=${score[$u]};score[$u]=$scoretmp
                    gstmp=${gs[$v]};gs[$v]=${gs[$u]};gs[$u]=$gstmp
                    gctmp=${gc[$v]};gc[$v]=${gc[$u]};gc[$u]=$gctmp
                    gdtmp=${gd[$v]};gd[$v]=${gd[$u]};gd[$u]=$gdtmp
                    victorytmp=${victory[$v]};victory[$v]=${victory[$u]};victory[$u]=$victorytmp
                    losetmp=${lose[$v]};lose[$v]=${lose[$u]};lose[$u]=$losetmp
                    drawtmp=${draw[$v]};draw[$v]=${draw[$u]};draw[$u]=$drawtmp
                    roundtmp=${round[$v]};round[$v]=${round[$u]};round[$u]=$roundtmp
                    clubnametmp=${clubname[$v]};clubname[$v]=${clubname[$u]};clubname[$u]=$clubnametmp
                fi
            fi
        fi
    done
done
##根据积分，净胜球，进球数的次序进行积分榜的排序

##输出积分榜
printf "排名\t球队\t\t积分\t场次\t胜\t平\t负\t进球\t失球\t净胜球\n"
for (( i=0; i<20; i++)); do
    let "j = $i + 1"
    printf "$j\t${clubname[$i]}\t\t${score[$i]}\t${round[$i]}\t${victory[$i]}\t${draw[$i]}\t${lose[$i]}\t${gs[$i]}\t${gc[$i]}\t${gd[$i]}\n"      
#    z=`echo ${clubname[i]} |wc -L`
#    if [ $z -lt 7 ]; then
#      printf "$j\t${clubname[$i]}\t${score[$i]}\t${round[$i]}\t${victory[$i]}\t${draw[$i]}\t${lose[$i]}\t${gs[$i]}\t${gc[$i]}\t${gd[$i]}\n"      
#    else
#      printf "$j\t${clubname[$i]}\t${score[$i]}\t${round[$i]}\t${victory[$i]}\t${draw[$i]}\t${lose[$i]}\t${gs[$i]}\t${gc[$i]}\t${gd[$i]}\n"      
#    fi
done
##输出积分榜,球队名称超过4个汉字时会占用两个制表位
