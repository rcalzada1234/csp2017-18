#Madlibs Projects
#By Robyn Calzada
# From Mad Libs book Teachers rule by Laura Marcheani Published by Price Stern Sloan A Imprint of Penguin Random House

#waiter is a pause in the reading for the reader not to be overwhelmed by text.
def waiter():
  raw_input("press any key to continue")
  print ""
  return


def introduction():
    #This is introducing what a Mad lib is.
    print " Instructions to play MAD LIBS. Answer the word please input the"
    print "correct type of word or the story won't make scence.  Then, using"
    print "the words you have selected, fill in the blank spaces in the story."
    print "Now lets play a hilarious MAD LIBS game!"
    waiter()
    #This is where I got the specific Mad Lib I used.
    print "From the Teachers Rule!Mad Libs book:"
    print "book writen by: Laura Marchesani"
    print "book published by: Price Stern Sloan"
    waiter()
    print ""
    print ""
    print ""
    # The title
    print "A Teachers Summer Vacation"
    print ""
    print ""
    print ""
    return
    
def word_selection():
    #the following is the word selection for the madlib
    word1=raw_input("Choose a Adjective:    ")
    word2=raw_input("Choose A Place:    ")
    word3=raw_input("Choose an Animal (Plural):    ")
    word4=raw_input("Choose a Noun:    ")
    word5=raw_input("Choose an Adverb:    ")
    word6=raw_input("Choose an Ajective:    ")
    word7=raw_input("Choose an Type of Food:    ")
    word8=raw_input("Choose a Plural Noun:    ")
    word9=raw_input("Choose a Person in the room (Female):    ")
    word10=raw_input("Choose a Plural Noun:    ")
    word11=raw_input("Choose a Adjective:    ")
    word12=raw_input("Choose an Type of Food:    ")
    word13=raw_input("Choose a Plural Noun:    ")
    word14=raw_input("Choose a Adjective:    ")
    word15=raw_input("Choose a Silly Word:    ")
    word16=raw_input("Choose a Person in the Room:    ")
    word17=raw_input("Choose a Plural Noun:    ")
        
    waiter()
    #The Story
    print "Think kids have the most fun and "+word1+" summer vacations?"
    print "Think again! Teachers also like to enjoy every minute of their time"
    print "away from (the) "+word2+" Here's what one teacher's typical"
    print "summer day looks like:"
    waiter()
    print "9:00 a.m.: Wake up to the sound of "+word3+" chirping outside"
    print "   and not the sound of my "+word4+" beeping " +word5+"!"
    print "10:00 a.m.: Eat a/an "+word6+" breakfast of "+word7+" .Sure"
    print "   beats a Tupperware of "+word8+" in the teachers' lounge!"
    waiter()
    print "12:00 p.m.: Hit the beach with my friend "+word9+". No"
    print "   pencils, notebooks, or "+word10+" anywhere in sight!"
    print "5:00 p.m.: Have an early dinner in a/an "+word11+" restaurant. The"
    print "   delicious lobster and "+word12+" has noting on the cafeteria's"
    print "   steamed "+word13+" and broccoli!"
    waiter()
    print "10:00 p.m.: Watch a marathon of the "+word14+" TV show"
    print "   "+word15+" while eating a pint of "+word16+" and Jerry's"
    print "   straight from the carton. It's east to pay attention when you don't"
    print "   have to grade "+word17+" at the same time!"
    return
    print "                             The End"
introduction()
word_selection()

    
   