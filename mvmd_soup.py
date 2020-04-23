
# MY SUGGESTED LIST
# mvmt=["#vegan", "#restaurant", "#queenwest", "#westqueenwest", "#toreats", "#bonapetite", "#decor", "#veganbreakfast", "#veganlove", "#animallover", "#veganshare", "#animallove", "#glutenfree", "#organic", "#veganbeauty",

# BELOW ARE HASHTAGS TO PICK FROM. THE LONGER THE LIST THE MORE WE GET TO PICK FROM
mvmt = ["#sustainability", "#sustainable", "#blogto", "#torontoeats", 
"#parkdale" ,"#queenwest" ,"#libertyvillage", "#vegan" ,"#foodie" ,
"#torontofoodie", "#health", "#blogger", "#travel", "#takeout"]
# OUR UNIQUE TAGS THAT WILL SHOW FIRST
base=["#relaxedfoods", "#restaurant", "#toronto", ]

from random import shuffle

shuffle(mvmt)
mvmt = mvmt[:27] # LIST OF TOTAL OUTPUT FROM FIRST LIST + THE "BASE"
totalsoup=(base+mvmt)
def listToString(totalsoup):  
    str1 = " " 
    return (str1.join(totalsoup)) 
print(listToString(totalsoup))

