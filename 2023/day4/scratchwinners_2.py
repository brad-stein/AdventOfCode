
pathtofile="./puzzel_4/scratchcards.txt"






game_list=open(pathtofile)
data=game_list.read().split('\n')
intial_numberofcards=len(data)
wins_mulitpler_list=[1]*intial_numberofcards



def winmultiplier(card_number: int, wins: int, multiplier_list: list):
    i=int(card_number)
    dup_these_cards=int(i)+wins-1
    card_repeats=multiplier_list[int(card_number)-1]
    while i <= dup_these_cards:
        multiplier_list[i] +=card_repeats
        i+=1
    return multiplier_list

total_wins=0
for i in data:
    gameset=i.replace('|',':').split(':')
    game_key=list(filter(None, gameset[1].lstrip().rstrip().split(' ')))
    game_results=list(filter(None, gameset[2].lstrip().rstrip().split(' ')))
    game_card=list(filter(None, gameset[0].lstrip().rstrip().split(' ')))

    card_number=game_card[1]


    set_winner_count=0

    for x in game_key:
        key_num=x

        for y in game_results:
            game_num=y
            if key_num==game_num:
                set_winner_count+=1
    wins_mulitpler_list=winmultiplier(card_number,set_winner_count,wins_mulitpler_list)
    #if set_winner_count>0:
    #    set_total=pow(2, set_winner_count-1)
    #total_wins+=set_total
    set_total=0
total=sum(wins_mulitpler_list)
print('the total cards are: ', total)
