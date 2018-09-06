word = ["S","P","A","C","E","M","A","N"]
word_reveal = ["","","","","","","",""]
spaceman = 0
count = 0
spacePicture = ["\
.........................=MMMMM?............................\
...................MOM MMMMMMMMMMMMMM7.  .   . .\
............ ..7MMMMMMMMMMMMMMMMMMMMMMMMMMM=.\
.......... ....DMMMMMMMMMMMMMMMMMMMMMMMMMMMMM      .\
...... . .=M=MMMMMMMMMMMMMMMMMMMMMM .M8. MMMMM..      ..\
..........MMMMMMMMMMMMM+MM: MMMZ. ......MMMMMMMM   .  ......\
........ MMMMMMMMM,.....M...M..........+ MMMMMMMM ... .. .","\
.......NMMMMMMM, . ...7MM...........I ..M.:.MMMMMMM.. . ....\
.......ZMMMMMM ..$M MMMM............M...  : .MMMMMM.  ..\
......MMMMMMM .. MMMMM7..  ...... .,M .M.. ..M.MMMMMM. . . .\
.....MMMMMMM...ZMMMMMM....  .D ... ?MMO...   ..8MMMMMM.. .\
...DOMMMMMM...DMMMMMM+..... .,=..M MMM$,..M.....MMMMMM.. . .\
...,MMMMMM....MMMMMM..........MM.,MMMM  .~. ... IMMMMMMM..\
...DMMMMM......MMMMMM.........MMM MMMMO..M=   . .OMMMMM. ..","\
...MMMMMMN.....MMMMMM.....M..ZMMMMMMMMM ,M ..... .MMMMM.  ..\
...NMMMMMM ....NM MMM ..N ~MMM MMMMMMMMIM=M, .   ,MMMMM.  ..\
....MMMMMMMM....... .M..D~.MMMMMMMMMMMMMMMMMM$ ..MMMMMM.   .\
.....ZMMMMMN,.......... ...MMMMMMMMMMMNMMMMMM+..MMMMMM.....\
.....NMMMMMMM......M~ N7. MI...$MMMM,.. M.M=. .DMMMMMM.   ..\
......MMMMMM=....... MMMMMMN  :+   ~MMMM.. ....MMMMMM..  ...\
......MMMM ......................MMMMMM  . .  .MMMMMM  .   .","\
......MMM,....... ...~MM  ... . .MMMM$ . .      MMMMM..\
......MMM...........87M ... ....MMMM......      DMMMM. .\
...... MM .... ....M$MIZ ...  ..MM ..... . ..   MMMMM,. ...\
. ....=MM....... .M+MMMMM......:M. ..........M  :MMMM ..  ..\
......IMM........M~MMMMM7.....+ ... ...... ..M.. MMMM...  .\
......MMM .. ...M~MMMMMMZ... M..... .........M . MMMMM......\
...... MM...M .. M..MMMMMM.M:... MM .... = ..MM. MMM........","\
...... MMM..M.. OMMM= .ZMMM ..MM7.........7MMMM. MMMM ......\
......M.MM..M.?.$ ...:MM.M MMMI.MM......... M? . MMM+M......\
.......OM8.. .M ........IMMMM .M ...........M ...MMMM  .....\
........,I.. .~DMMMMMM  MMMM...... MMMMMM........MMMM ......\
.........~M.MN .DM~  . MMMM ....... . .I............8.......\
..........~:M.. ,M  ..MMMM .................................\
...........M=M.... MMMMMM.....................M.............","\
............ .....MMMMMM ....................,...M .........\
............M....8MMMMM .....................DMMMM .........\
............M...MMMMM8... .... ..............$MMMM .........\
............D...7MMM ....OM..NM..............8MMMM..........\
............:=..8MM..........................MMMMM8.........\
....... ....?M :MM...........................MMMMMM.........\
............MM .M.......................... MMMMMMM ........","\
............MMM.M......$MMMMMMMMM: ....... M$MMMMMM ........\
.......... MMMM8?....MMMMM8IMMMMMMM ......M.8MMMMMM.........\
..........MMMMMMM......MMMN.MMMMMD.......N..MMMMMMM ........\
.........MMMMMMN.N........=~...........:=...MMMMMMM ........\
........,NMMMM ... ?..................8 ....MMMM$...........\
....................M................M......MMM.............\
.....................N..............M....... ~..............\
.......................M~.........M ..........8.............\
"]
blankPicture = ["","","","","","","",""]
while (count < len(word_reveal)) and (spaceman < 8):
    word1 = raw_input("Enter a letter: ").upper()
    counter = 0
    for i in range(0, len(word)):
        if word1 == word[i]:
            word_reveal[i] = word[i]
            count += 1
        else:
            counter += 1
    if counter == len(word):
        spaceman += 1
        blankPicture[spaceman-1] = spacePicture[spaceman-1]
    print(blankPicture)
    print(word_reveal)
