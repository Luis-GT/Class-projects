from random import randrange
from graphics import *
from time import sleep



def user(win):
    #dispaly user name box
    Text(Point(0.7,5.5), "Enter Name").draw(win)
    message = Entry(Point(2.2,5.5),20)
    message.draw(win)
    button = Text(Point(2,4.5), "Start")
    button.draw(win)
    Rectangle(Point(1.7,4.7), Point(2.3,4.3)).draw(win)
    name = ""
    while name =="":
        start_click = win.getMouse()
        if start_click.getX() >=1.7 and start_click.getX() <= 2.3 and start_click.getY() >=4.3 and start_click.getY()<=4.7:
            name = message.getText()
        else:
            start_click = win.getMouse()
    return name
def current_score():
    #create score file
    scorefile = open("score.txt",'a+')
    scorefile.seek(0)
    data = scorefile.read(1000)
    if len(data) == 0:
        print("No scores available")
    else:
        print(data)
    
    
def save_score(n,s):
    #append score file
    scorefile = open("score.txt",'a+')
    scorefile.seek(0)
    data = scorefile.read(1000)
    lines = data.split("\n")
    if len(data) > 0:
        scorefile.write("\n")
    scorefile.write("%s) %s score is: %d"  %(len(lines),n,s))
    scorefile.close()
    scorefile = open("score.txt",'r')
    scorefile.seek(0)
    data = scorefile.read(1000)
    print(data)
    scorefile.close()

def simon_game(win):
    #set point coordinates
    p1= Point(4,4)
    p2 = Point(2,2)
    p3 = Point(4,2)
    p4 = Point(2,0)
    p5 = Point(2,4)
    p6 = Point(0,2)
    p7 = Point(2,2)
    p8 = Point(0,0)
    #create game table
    Top_right = Rectangle(p1,p2)
    Bottom_right = Rectangle(p3,p4)
    Top_left = Rectangle(p5,p6)
    Bottom_left = Rectangle(p7,p8)
    Top_left.setFill("dark green")
    Top_left.draw(win)
    Top_right.setFill("dark red")
    Top_right.draw(win)
    Bottom_left.setFill("orange3")
    Bottom_left.draw(win)
    Bottom_right.setFill("dark blue")
    Bottom_right.draw(win)
    #game start sequence
    start="yes"
    score = 0
    #simon game
    while start!="n":
        count=0
        count2=0
        pattern=[]
        while count2<=count:
            new= randrange(4)
            pattern.append(str(new))
            count+=1
            sleep(1)
            while count2<count:
                if count<6:
                    if pattern[count2]=="0":
                        #flash green
                        sleep(1/count)
                        Top_left.setFill("green")
                        sleep(1/count)
                        Top_left.setFill("dark green")
                    elif pattern[count2]=="1":
                        #flash red
                        sleep(1/count)
                        Top_right.setFill("red")
                        sleep(1/count)
                        Top_right.setFill("dark red")
                    elif pattern[count2]=="2":
                        #flash blue
                        sleep(1/count)
                        Bottom_right.setFill("blue")
                        sleep(1/count)
                        Bottom_right.setFill("dark blue")
                    else:
                        #flash orange
                        sleep(1/count)
                        Bottom_left.setFill("orange")
                        sleep(1/count)
                        Bottom_left.setFill("orange3")
                else:
                    if pattern[count2]=="0":
                        #flash green
                        sleep(.2)
                        Top_left.setFill("green")
                        sleep(.2)
                        Top_left.setFill("dark green")
                    elif pattern[count2]=="1":
                        #flash red
                        sleep(.2)
                        Top_right.setFill("red")
                        sleep(.2)
                        Top_right.setFill("dark red")
                    elif pattern[count2]=="2":
                        #flash blue
                        sleep(.2)
                        Bottom_right.setFill("blue")
                        sleep(.2)
                        Bottom_right.setFill("dark blue")
                    else:
                        #flash orange
                        sleep(.2)
                        Bottom_left.setFill("orange")
                        sleep(.2)
                        Bottom_left.setFill("orange3")
                count2+=1
            #user game interaction
            count2=0
            user=[]
            while count2<count:
                select=win.getMouse()
                
                if select.getX() <=2 and select.getX() >= 0 and select.getY() <=4 and select.getY()>=2:
                    neww = 0
                    #flash green
                    Top_left.setFill("green")
                    sleep(.2)
                    Top_left.setFill("dark green")
                    user.append(str(neww))
                elif select.getX() <=4 and select.getX() >= 2 and select.getY() <=4 and select.getY()>=2:
                    neww = 1
                    #flash red
                    Top_right.setFill("red")
                    sleep(.2)
                    Top_right.setFill("dark red")
                    user.append(str(neww))
                elif select.getX() <=4 and select.getX() >= 2 and select.getY() <=2 and select.getY()>=0:
                    neww = 2
                    #flash blue
                    Bottom_right.setFill("blue")
                    sleep(.2)
                    Bottom_right.setFill("dark blue")
                    user.append(str(neww))
                else:
                    neww = 3
                    #flash orange
                    Bottom_left.setFill("orange")
                    sleep(.2)
                    Bottom_left.setFill("orange3")
                    user.append(str(neww))
                count2+=1
                
            if pattern==user:
                count2=0
                score = count
                    
            else:
                score = score
                count2=count+1
                start=input("Play Again?(Y/N): ").lower()
                if start == "n":
                    win.close()
                    return score
                    
                else:
                    print("new game")
                    return score
           

def main():
    win = GraphWin ("Simon Says", 400,600)
    win.setCoords(0,0,4,6)
    current_score()
    un = user(win)
    s = simon_game(win)
    save_score(un,s)
    
    
    

main()

