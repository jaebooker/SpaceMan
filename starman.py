import subprocess
import random
# import playsound
# playsound.playsound('./starman.mp3', True)
def play_mp3(path):
    subprocess.Popen(['mpg321', '-q', path]).wait()
word_list = [["S","P","A","C","E","M","A","N"], ["B","O","W","I","E"]]
word = word_list[random.randrange(0,len(word_list))]
word_reveal = []
for i in range(0,len(word)):
    word_reveal.append("")
spaceman = 0
count = 0
spacePicture = ["\
.........................=MMMMM?............................","\
...................MOM MMMMMMMMMMMMMM7.  .   . .","\
............ ..7MMMMMMMMMMMMMMMMMMMMMMMMMMM=.","\
.......... ....DMMMMMMMMMMMMMMMMMMMMMMMMMMMMM      .","\
...... . .=M=MMMMMMMMMMMMMMMMMMMMMM .M8. MMMMM..      ..","\
..........MMMMMMMMMMMMM+MM: MMMZ. ......MMMMMMMM   .  ......","\
........ MMMMMMMMM,.....M...M..........+ MMMMMMMM ... .. .","\
.......NMMMMMMM, . ...7MM...........I ..M.:.MMMMMMM.. . ....","\
.......ZMMMMMM ..$M MMMM............M...  : .MMMMMM.  ..","\
......MMMMMMM .. MMMMM7..  ...... .,M .M.. ..M.MMMMMM. . . .","\
.....MMMMMMM...ZMMMMMM....  .D ... ?MMO...   ..8MMMMMM.. .","\
...DOMMMMMM...DMMMMMM+..... .,=..M MMM$,..M.....MMMMMM.. . .","\
...,MMMMMM....MMMMMM..........MM.,MMMM  .~. ... IMMMMMMM..\
...DMMMMM......MMMMMM.........MMM MMMMO..M=   . .OMMMMM. ..","\
...MMMMMMN.....MMMMMM.....M..ZMMMMMMMMM ,M ..... .MMMMM.  ..","\
...NMMMMMM ....NM MMM ..N ~MMM MMMMMMMMIM=M, .   ,MMMMM.  ..","\
....MMMMMMMM....... .M..D~.MMMMMMMMMMMMMMMMMM$ ..MMMMMM.   .","\
.....ZMMMMMN,.......... ...MMMMMMMMMMMNMMMMMM+..MMMMMM.....","\
.....NMMMMMMM......M~ N7. MI...$MMMM,.. M.M=. .DMMMMMM.   ..","\
......MMMMMM=....... MMMMMMN  :+   ~MMMM.. ....MMMMMM..  ...","\
......MMMM ......................MMMMMM  . .  .MMMMMM  .   .","\
......MMM,....... ...~MM  ... . .MMMM$ . .      MMMMM..","\
......MMM...........87M ... ....MMMM......      DMMMM. .","\
...... MM .... ....M$MIZ ...  ..MM ..... . ..   MMMMM,. ...","\
. ....=MM....... .M+MMMMM......:M. ..........M  :MMMM ..  ..","\
......IMM........M~MMMMM7.....+ ... ...... ..M.. MMMM...  .","\
......MMM .. ...M~MMMMMMZ... M..... .........M . MMMMM......","\
...... MM...M .. M..MMMMMM.M:... MM .... = ..MM. MMM........","\
...... MMM..M.. OMMM= .ZMMM ..MM7.........7MMMM. MMMM ......","\
......M.MM..M.?.$ ...:MM.M MMMI.MM......... M? . MMM+M......","\
.......OM8.. .M ........IMMMM .M ...........M ...MMMM  .....","\
........,I.. .~DMMMMMM  MMMM...... MMMMMM........MMMM ......","\
.........~M.MN .DM~  . MMMM ....... . .I............8.......","\
..........~:M.. ,M  ..MMMM .................................","\
...........M=M.... MMMMMM.....................M.............","\
............ .....MMMMMM ....................,...M .........","\
............M....8MMMMM .....................DMMMM .........","\
............M...MMMMM8... .... ..............$MMMM .........","\
............D...7MMM ....OM..NM..............8MMMM..........","\
............:=..8MM..........................MMMMM8.........","\
....... ....?M :MM...........................MMMMMM.........","\
............MM .M.......................... MMMMMMM ........","\
............MMM.M......$MMMMMMMMM: ....... M$MMMMMM ........","\
.......... MMMM8?....MMMMM8IMMMMMMM ......M.8MMMMMM.........","\
..........MMMMMMM......MMMN.MMMMMD.......N..MMMMMMM ........","\
.........MMMMMMN.N........=~...........:=...MMMMMMM ........","\
........,NMMMM ... ?..................8 ....MMMM$...........","\
....................M................M......MMM.............","\
.....................N..............M....... ~..............","\
.......................M~.........M ..........8.............\
"]
blankPicture = []
while (count < len(word)) and (spaceman < 7):
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
        if spaceman == 1:
            for i in range(0,8):
                blankPicture.append(spacePicture[i])
        elif spaceman == 2:
            for i in range(8,15):
                blankPicture.append(spacePicture[i])
        elif spaceman == 3:
            for i in range(15,22):
                blankPicture.append(spacePicture[i])
        elif spaceman == 4:
            for i in range(22,29):
                blankPicture.append(spacePicture[i])
        elif spaceman == 5:
            for i in range(29,36):
                blankPicture.append(spacePicture[i])
        elif spaceman == 6:
            for i in range(36,43):
                blankPicture.append(spacePicture[i])
        else:
            for i in range(43,49):
                blankPicture.append(spacePicture[i])
    for i in blankPicture:
        print(i)
    if spaceman == 7:
        play_mp3("./starman.mp3")
    print(word_reveal)
