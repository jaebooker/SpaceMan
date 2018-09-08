import subprocess
import random
def play_mp3(path):
    subprocess.Popen(['mpg321', '-q', path]).wait()
word_list = [["S","T","A","R","D","U","S","T"], ["R","U","B","Y","T","U","E","S","D","A","Y"]]
spacePicture = [["\
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
"], ["                      .MMMM.      ..MMM7.","\
                    MOOOOOOOZ. ..NOOOOOOO8.","\
                 .MOOO......OO.MOOOO.....OO,","\
                .OOOO.     .OOOOOO.     .$OO.","\
               NOOOOO.8OO, 8OOOOOOO8OOO.+OOOM","\
              .OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.","\
              OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.","\
             OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON.","\
           .OOOOOO.   ...OOOOOO,......OOOOOOOOOM","\
          .OOOO8.         ....         .OOOOOOOOON.","\
        .MOOOOMMM.                      .=OOOOOOOODI","\
     .8OOOOOMMMMMMMMM.              . .  ..DOOOOOOOOOM","\
    .OOOOOOMMMMMMMMOOOOO+MMMMMM.  ..OOO..8OOOONOOOOOOO.","\
     .OOOOOOMMMMMOOOOOOOOOMMMMDOOOOOOOOOOOOOOOZOOOOOMI.","\
      .MOOOOOMMOOOOOOOOOMMOOOOOOOOOOOOOOOOOOMOOOOOO.","\
       .MOOOOOOOOOO..O8MOOOOOOOOOOOO..OOOOODOOOOON.","\
         MOOOOOOO:..OMMOOOOOOOOOOO?..OOOOOOOOOOOM","\
         .OOOOO8...OOMOOOOOOOOOOO. .OOOOOOOOOOOM","\
        .8OOOOO. .OOMOOOOOOOOOOO. .OOOOZOOOOOOM.","\
       .MOOOO.  .OOMOOOOOOOOOOO. .OOOOOOOOOOOM.","\
       MOOOO,. .OOMZOOOOOOOOOO=. 8OOOOMOOOOOO.","\
       OOOOO. .OOOMOOOOOOOOOOO. .OOOOMOOOOOOM","\
     .NOOOO.  .OOOOOOOOOOOOOO. .OOOOOMOOOOON.","\
      OOOO?.  OOOMOOOOOOOOOOO. .OOOOMOOOOOOM.","\
     MOOOO.  .OOOOOOOOOOOOOO.  OOOOOMOOOOOM","\
    .MOOOO   OOOOOOOOOOOOOO8   OOOOMOOOOOO.","\
    .OOOOO.  OOOOOOOOOOOOOO.  .OOOOMOOOOOM","\
    .OOOOO. .OOOOOOOOOOOOOI  ..OOOMOOOOOM.","\
    .OOOOOOOOOOOOOOOOOOOOO.  .OOODDOOOOM","\
     MOOOOOOOOOOOOOOOOOOO.   .OOOMOOOOM.","\
     ,OOOOOOOOOOOOOOOOOO.   .OOON8OON.","\
     .DOOOOOOOOOOOOOOOOOO..,OOOOMM.","\
      .OOOOOOOOOOOOOOOOOOOOOOOOD","\
        MOOOOOOOOOOOOOOOOOOOOO?","\
         .NOOOOOOOOOOOOOOOOOM.","\
           .MOOOOOOOOOOOOOM.","\
               ..MMMNMM:.\
"]]
def game(n):
    word = word_list[n]
    word_reveal = []
    for i in range(0,len(word)):
        word_reveal.append("")
    spaceman = 0
    count = 0
    realPicture = spacePicture[n]
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
                    blankPicture.append(realPicture[i])
            elif spaceman == 2:
                for i in range(8,15):
                    blankPicture.append(realPicture[i])
            elif spaceman == 3:
                for i in range(15,22):
                    blankPicture.append(realPicture[i])
            elif spaceman == 4:
                for i in range(22,29):
                    blankPicture.append(realPicture[i])
            elif spaceman == 5:
                for i in range(29,36):
                    blankPicture.append(realPicture[i])
            elif spaceman == 6:
                for i in range(36,43):
                    blankPicture.append(realPicture[i])
            else:
                for i in range(43,49):
                    blankPicture.append(realPicture[i])
        for i in blankPicture:
            print(i)
        print(word_reveal)
        if n == 0:
            if spaceman == 7:
                print("Sorry, you lost. Thanks for playing")
                play_mp3("./ziggy.mp3")
            if count == len(word):
                print("You won! Stay here for Level 2")
                play_mp3("./starman2.mp3")
                game(n+1)
        elif n == 1:
            if spaceman == 5:
                print("Sorry, you lost. Thanks for trying!")
                play_mp3("./itry.mp3")
                spaceman = 7
            if count == len(word):
                print("You won! Level 3 coming up...")
                play_mp3("./goodbyeruby.mp3")
                game(n+1)
        elif n == 0:
            if spaceman == 3:
                print("Sorry, you lost. Thanks for playing")
                play_mp3("./ziggy.mp3")
                spaceman == 7
            if count == len(word):
                print("You won! Your prize is... nothing!")
                play_mp3("./starman2.mp3")
game(0)
