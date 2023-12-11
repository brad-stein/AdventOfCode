
pathtofile="./puzzel_4/scratchcards.txt"






game_list=open(pathtofile)
data=game_list.read().split('\n')




total_wins=0
for i in data:
    gameset=i.replace('|',':').split(':')
    game_key=list(filter(None, gameset[1].lstrip().rstrip().split(' ')))
    game_results=list(filter(None, gameset[2].lstrip().rstrip().split(' ')))


    set_winner_count=0

    for x in game_key:
        #print(x)
        key_num=x

        for y in game_results:
            game_num=y
            if key_num==game_num:
                set_winner_count+=1
    if set_winner_count>0:
        set_total=pow(2, set_winner_count-1)
    total_wins+=set_total
    set_total=0
print('the total wins are: ', total_wins)
