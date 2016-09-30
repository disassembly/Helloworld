#!/bin/bash
clubname=( 莱斯特城 阿森纳 热刺 曼城 曼联 南安普敦 西汉姆联 利物浦 斯托克城 切尔西 埃弗顿 斯旺西 沃特福德 西布朗 水晶宫 伯恩茅斯 桑德兰 赫尔城 米堡 伯恩利 )
echo "回车开始，ctrl+D结束"
while read line
do
    for ((i=0;i<20;i++)); do
        mod=$(($i%5))
        j=`expr $i + 1`
        printf "$j.${clubname[$i]}  "
        if [ $mod -eq 4 ]; then
            printf "\n"
        fi
    done
    echo "请选择主队(用数字表示)："
    read clubhome
    echo "请选择客队(用数字表示)："
    read clubaway
    echo "主队进球数："
    read a
    echo "客队进球数："
    read b
    if [[ ! -n $clubhome ]] || [[ ! -n $clubaway ]] || [[ ! -n $a ]] || [[ ! -n $b ]];then
        echo "输入错误！"
    else
        file=/home/pl/pl/`echo $clubhome`_`echo $clubaway`
        if [ ! -f $file ]; then
            echo "文件不存在，请先执行premierleague.sh"
        else
            echo $a > $file
            echo $b >> $file
            clubhome=`expr $clubhome - 1`
            clubaway=`expr $clubaway - 1`
            printf "${clubname[$clubhome]}:${clubname[$clubaway]}"
            printf "="
            printf "$a:$b\n"
	    echo "${clubname[$clubhome]} $a,${clubname[$clubaway]} $b" >> /home/pl/plresult.txt
        fi
    fi
    echo "回车继续输入，ctrl+D结束"
done
printf "\t\t\t\t\t最新积分榜\n"
bash /home/pl/table.sh
