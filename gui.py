from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

blackjack = Tk()
blackjack.title("blackjack")
blackjack.geometry("800x800")
canv = Canvas(width=1440,height=1920)
canv.place(x=0, y=0)

img = ImageTk.PhotoImage(Image.open("blackjackimage.jpg"))
canv.create_image(0, 0, image=img)

backcardcanv = Canvas(width=74, height=107)
imagebackcard = ImageTk.PhotoImage(Image.open("backcard.png"))
backcardcanv.create_image(0, 0, image=imagebackcard, anchor='nw')

club1cardcanv = Canvas(width=74, height=107)
image1clubcard = ImageTk.PhotoImage(Image.open("1_club.png"))
club1cardcanv.create_image(0, 0, image=image1clubcard, anchor='nw')

diamond1cardcanv = Canvas(width=74, height=107)
image1diamondcard = ImageTk.PhotoImage(Image.open("1_diamond.png"))
diamond1cardcanv.create_image(0, 0, image=image1diamondcard, anchor='nw')

heart1cardcanv = Canvas(width=74, height=107)
image1heartcard = ImageTk.PhotoImage(Image.open("1_heart.png"))
heart1cardcanv.create_image(0, 0, image=image1heartcard, anchor='nw')

spade1cardcanv = Canvas(width=74, height=107)
image1spadecard = ImageTk.PhotoImage(Image.open("1_spade.png"))
spade1cardcanv.create_image(0, 0, image=image1spadecard, anchor='nw')
all1card = [club1cardcanv,diamond1cardcanv,heart1cardcanv,spade1cardcanv]

club2cardcanv = Canvas(width=74, height=107)
image2clubcard = ImageTk.PhotoImage(Image.open("2_club.png"))
club2cardcanv.create_image(0, 0, image=image2clubcard, anchor='nw')

diamond2cardcanv = Canvas(width=74, height=107)
image2diamondcard = ImageTk.PhotoImage(Image.open("2_diamond.png"))
diamond2cardcanv.create_image(0, 0, image=image2diamondcard, anchor='nw')

heart2cardcanv = Canvas(width=74, height=107)
image2heartcard = ImageTk.PhotoImage(Image.open("2_heart.png"))
heart2cardcanv.create_image(0, 0, image=image2heartcard, anchor='nw')

spade2cardcanv = Canvas(width=74, height=107)
image2spadecard = ImageTk.PhotoImage(Image.open("2_spade.png"))
spade2cardcanv.create_image(0, 0, image=image2spadecard, anchor='nw')
all2card = [club2cardcanv,diamond2cardcanv,heart2cardcanv,spade2cardcanv]

club3cardcanv = Canvas(width=74, height=107)
image3clubcard = ImageTk.PhotoImage(Image.open("3_club.png"))
club3cardcanv.create_image(0, 0, image=image3clubcard, anchor='nw')

diamond3cardcanv = Canvas(width=74, height=107)
image3diamondcard = ImageTk.PhotoImage(Image.open("3_diamond.png"))
diamond3cardcanv.create_image(0, 0, image=image3diamondcard, anchor='nw')

heart3cardcanv = Canvas(width=74, height=107)
image3heartcard = ImageTk.PhotoImage(Image.open("3_heart.png"))
heart3cardcanv.create_image(0, 0, image=image3heartcard, anchor='nw')

spade3cardcanv = Canvas(width=74, height=107)
image3spadecard = ImageTk.PhotoImage(Image.open("3_spade.png"))
spade3cardcanv.create_image(0, 0, image=image3spadecard, anchor='nw')
all3card = [club3cardcanv,diamond3cardcanv,heart3cardcanv,spade3cardcanv]


club4cardcanv = Canvas(width=74, height=107)
image4clubcard = ImageTk.PhotoImage(Image.open("4_club.png"))
club4cardcanv.create_image(0, 0, image=image4clubcard, anchor='nw')

diamond4cardcanv = Canvas(width=74, height=107)
image4diamondcard = ImageTk.PhotoImage(Image.open("4_diamond.png"))
diamond4cardcanv.create_image(0, 0, image=image4diamondcard, anchor='nw')

heart4cardcanv = Canvas(width=74, height=107)
image4heartcard = ImageTk.PhotoImage(Image.open("4_heart.png"))
heart4cardcanv.create_image(0, 0, image=image4heartcard, anchor='nw')

spade4cardcanv = Canvas(width=74, height=107)
image4spadecard = ImageTk.PhotoImage(Image.open("4_spade.png"))
spade4cardcanv.create_image(0, 0, image=image4spadecard, anchor='nw')
all4card = [club4cardcanv,diamond4cardcanv,heart4cardcanv,spade4cardcanv]



club5cardcanv = Canvas(width=74, height=107)
image5clubcard = ImageTk.PhotoImage(Image.open("5_club.png"))
club5cardcanv.create_image(0, 0, image=image5clubcard, anchor='nw')

diamond5cardcanv = Canvas(width=74, height=107)
image5diamondcard = ImageTk.PhotoImage(Image.open("5_diamond.png"))
diamond5cardcanv.create_image(0, 0, image=image5diamondcard, anchor='nw')

heart5cardcanv = Canvas(width=74, height=107)
image5heartcard = ImageTk.PhotoImage(Image.open("5_heart.png"))
heart5cardcanv.create_image(0, 0, image=image5heartcard, anchor='nw')

spade5cardcanv = Canvas(width=74, height=107)
image5spadecard = ImageTk.PhotoImage(Image.open("5_spade.png"))
spade5cardcanv.create_image(0, 0, image=image5spadecard, anchor='nw')
all5card = [club5cardcanv,diamond5cardcanv,heart5cardcanv,spade5cardcanv]


club6cardcanv = Canvas(width=74, height=107)
image6clubcard = ImageTk.PhotoImage(Image.open("6_club.png"))
club6cardcanv.create_image(0, 0, image=image6clubcard, anchor='nw')

diamond6cardcanv = Canvas(width=74, height=107)
image6diamondcard = ImageTk.PhotoImage(Image.open("6_diamond.png"))
diamond6cardcanv.create_image(0, 0, image=image6diamondcard, anchor='nw')

heart6cardcanv = Canvas(width=74, height=107)
image6heartcard = ImageTk.PhotoImage(Image.open("6_heart.png"))
heart6cardcanv.create_image(0, 0, image=image6heartcard, anchor='nw')

spade6cardcanv = Canvas(width=74, height=107)
image6spadecard = ImageTk.PhotoImage(Image.open("6_spade.png"))
spade6cardcanv.create_image(0, 0, image=image6spadecard, anchor='nw')
all6card = [club6cardcanv,diamond6cardcanv,heart6cardcanv,spade6cardcanv]

club7cardcanv = Canvas(width=74, height=107)
image7clubcard = ImageTk.PhotoImage(Image.open("7_club.png"))
club7cardcanv.create_image(0, 0, image=image7clubcard, anchor='nw')

diamond7cardcanv = Canvas(width=74, height=107)
image7diamondcard = ImageTk.PhotoImage(Image.open("7_diamond.png"))
diamond7cardcanv.create_image(0, 0, image=image7diamondcard, anchor='nw')

heart7cardcanv = Canvas(width=74, height=107)
image7heartcard = ImageTk.PhotoImage(Image.open("7_heart.png"))
heart7cardcanv.create_image(0, 0, image=image7heartcard, anchor='nw')

spade7cardcanv = Canvas(width=74, height=107)
image7spadecard = ImageTk.PhotoImage(Image.open("7_spade.png"))
spade7cardcanv.create_image(0, 0, image=image7spadecard, anchor='nw')
all7card = [club7cardcanv,diamond7cardcanv,heart7cardcanv,spade7cardcanv]


club8cardcanv = Canvas(width=74, height=107)
image8clubcard = ImageTk.PhotoImage(Image.open("8_club.png"))
club8cardcanv.create_image(0, 0, image=image8clubcard, anchor='nw')

diamond8cardcanv = Canvas(width=74, height=107)
image8diamondcard = ImageTk.PhotoImage(Image.open("8_diamond.png"))
diamond8cardcanv.create_image(0, 0, image=image8diamondcard, anchor='nw')

heart8cardcanv = Canvas(width=74, height=107)
image8heartcard = ImageTk.PhotoImage(Image.open("8_heart.png"))
heart8cardcanv.create_image(0, 0, image=image8heartcard, anchor='nw')

spade8cardcanv = Canvas(width=74, height=107)
image8spadecard = ImageTk.PhotoImage(Image.open("8_spade.png"))
spade8cardcanv.create_image(0, 0, image=image8spadecard, anchor='nw')
all8card = [club8cardcanv,diamond8cardcanv,heart8cardcanv,spade8cardcanv]

club9cardcanv = Canvas(width=74, height=107)
image9clubcard = ImageTk.PhotoImage(Image.open("9_club.png"))
club9cardcanv.create_image(0, 0, image=image9clubcard, anchor='nw')

diamond9cardcanv = Canvas(width=74, height=107)
image9diamondcard = ImageTk.PhotoImage(Image.open("9_diamond.png"))
diamond9cardcanv.create_image(0, 0, image=image9diamondcard, anchor='nw')

heart9cardcanv = Canvas(width=74, height=107)
image9heartcard = ImageTk.PhotoImage(Image.open("9_heart.png"))
heart9cardcanv.create_image(0, 0, image=image9heartcard, anchor='nw')

spade9cardcanv = Canvas(width=74, height=107)
image9spadecard = ImageTk.PhotoImage(Image.open("9_spade.png"))
spade9cardcanv.create_image(0, 0, image=image9spadecard, anchor='nw')
all9card = [club9cardcanv,diamond9cardcanv,heart9cardcanv,spade9cardcanv]

club10cardcanv = Canvas(width=74, height=107)
image10clubcard = ImageTk.PhotoImage(Image.open("10_club.png"))
club10cardcanv.create_image(0, 0, image=image10clubcard, anchor='nw')

diamond10cardcanv = Canvas(width=74, height=107)
image10diamondcard = ImageTk.PhotoImage(Image.open("10_diamond.png"))
diamond10cardcanv.create_image(0, 0, image=image10diamondcard, anchor='nw')

heart10cardcanv = Canvas(width=74, height=107)
image10heartcard = ImageTk.PhotoImage(Image.open("10_heart.png"))
heart10cardcanv.create_image(0, 0, image=image10heartcard, anchor='nw')

spade10cardcanv = Canvas(width=74, height=107)
image10spadecard = ImageTk.PhotoImage(Image.open("10_spade.png"))
spade10cardcanv.create_image(0, 0, image=image10spadecard, anchor='nw')

clubjackcardcanv = Canvas(width=74, height=107)
imagejackclubcard = ImageTk.PhotoImage(Image.open("jack_club.png"))
clubjackcardcanv.create_image(0, 0, image=imagejackclubcard, anchor='nw')

diamondjackcardcanv = Canvas(width=74, height=107)
imagejackdiamondcard = ImageTk.PhotoImage(Image.open("jack_diamond.png"))
diamondjackcardcanv.create_image(0, 0, image=imagejackdiamondcard, anchor='nw')

heartjackcardcanv = Canvas(width=74, height=107)
imagejackheartcard = ImageTk.PhotoImage(Image.open("jack_heart.png"))
heartjackcardcanv.create_image(0, 0, image=imagejackheartcard, anchor='nw')

spadejackcardcanv = Canvas(width=74, height=107)
imagejackspadecard = ImageTk.PhotoImage(Image.open("jack_spade.png"))
spadejackcardcanv.create_image(0, 0, image=imagejackspadecard, anchor='nw')

clubkingcardcanv = Canvas(width=74, height=107)
imagekingclubcard = ImageTk.PhotoImage(Image.open("king_club.png"))
clubkingcardcanv.create_image(0, 0, image=imagekingclubcard, anchor='nw')

diamondkingcardcanv = Canvas(width=74, height=107)
imagekingdiamondcard = ImageTk.PhotoImage(Image.open("king_diamond.png"))
diamondkingcardcanv.create_image(0, 0, image=imagekingdiamondcard, anchor='nw')

heartkingcardcanv = Canvas(width=74, height=107)
imagekingheartcard = ImageTk.PhotoImage(Image.open("king_heart.png"))
heartkingcardcanv.create_image(0, 0, image=imagekingheartcard, anchor='nw')

spadekingcardcanv = Canvas(width=74, height=107)
imagekingspadecard = ImageTk.PhotoImage(Image.open("king_spade.png"))
spadekingcardcanv.create_image(0, 0, image=imagekingspadecard, anchor='nw')

clubqueencardcanv = Canvas(width=74, height=107)
imagequeenclubcard = ImageTk.PhotoImage(Image.open("queen_club.png"))
clubqueencardcanv.create_image(0, 0, image=imagequeenclubcard, anchor='nw')

diamondqueencardcanv = Canvas(width=74, height=107)
imagequeendiamondcard = ImageTk.PhotoImage(Image.open("queen_diamond.png"))
diamondqueencardcanv.create_image(0, 0, image=imagequeendiamondcard, anchor='nw')

heartqueencardcanv = Canvas(width=74, height=107)
imagequeenheartcard = ImageTk.PhotoImage(Image.open("queen_heart.png"))
heartqueencardcanv.create_image(0, 0, image=imagequeenheartcard, anchor='nw')

spadequeencardcanv = Canvas(width=74, height=107)
imagequeenspadecard = ImageTk.PhotoImage(Image.open("queen_spade.png"))
spadequeencardcanv.create_image(0, 0, image=imagequeenspadecard, anchor='nw')

all10card = [club10cardcanv,diamond10cardcanv,heart10cardcanv,spade10cardcanv,
clubjackcardcanv,diamondjackcardcanv,heartjackcardcanv,spadejackcardcanv,
clubkingcardcanv,diamondkingcardcanv,heartkingcardcanv,spadekingcardcanv,
clubqueencardcanv,diamondqueencardcanv,heartqueencardcanv,spadequeencardcanv]


allcards = [all1card,all2card,all3card,all4card,all5card,all6card,all7card,
all8card,all9card,all10card]
listx = 150
listy = 50

sum_computer_cards = 0

randomlist2 = random.choice(allcards)
randomlist1 = random.choice(allcards)
randomlistrandom = random.choice(randomlist1)
randomlist3 = random.choice(allcards)
randomlist4 = random.choice(allcards)

sum_cards = []

xcard = 70
xcard2 = 150
ycard = 50
ycard2 = 50

randomlistrandom3 = random.choice(randomlist3)
randomlistrandom4 = random.choice(randomlist4)
randomlistrandom3.place(x=xcard,y=ycard)
randomlistrandom4.place(x=xcard2,y=ycard2)
if randomlist3 == allcards[0] or randomlist4 == allcards[0]:
    sum_cards.append(11)
if randomlist3 == allcards[1] or randomlist4 == allcards[1]:
    sum_cards.append(2)
if randomlist3 == allcards[2] or randomlist4 == allcards[2]:
    sum_cards.append(3)
if randomlist3 == allcards[3] or randomlist4 == allcards[3]:
    sum_cards.append(4)
if randomlist3 == allcards[4] or randomlist4 == allcards[4]:
    sum_cards.append(5)
if randomlist3 == allcards[5] or randomlist4 == allcards[5]:
    sum_cards.append(6)
if randomlist3 == allcards[6] or randomlist4 == allcards[6]:
    sum_cards.append(7)
if randomlist3 == allcards[7] or randomlist4 == allcards[7]:
    sum_cards.append(8)
if randomlist3 == allcards[8] or randomlist4 == allcards[8]:
    sum_cards.append(9)
if randomlist3 == allcards[9] or randomlist4 == allcards[9]:
    sum_cards.append(10)

def more_cards_Function():
    global listy
    global listx
    listx += 80
    randomlist5 = random.choice(allcards)
    randomlistrandom5 = random.choice(randomlist5)
    randomlistrandom5.place(x=listx, y=listy)
    if randomlist5 == allcards[0]:
        sum_cards.append(11)
    if randomlist5 == allcards[1]:
        sum_cards.append(2)
    if randomlist5 == allcards[2]:
        sum_cards.append(3)
    if randomlist5 == allcards[3]:
        sum_cards.append(4)
    if randomlist5 == allcards[4]:
        sum_cards.append(5)
    if randomlist5 == allcards[5]:
        sum_cards.append(6)
    if randomlist5 == allcards[6]:
        sum_cards.append(7)
    if randomlist5 == allcards[7]:
        sum_cards.append(8)
    if randomlist5 == allcards[8]:
        sum_cards.append(9)
    if randomlist5 == allcards[9]:
        sum_cards.append(10)


button_submit = Button(blackjack, text="Hit", width=6, command=more_cards_Function)
button_submit.place(x=400, y=400)


def calculate_score():
    global sum_cards
    if sum(sum_cards) == 21 and len(sum_cards) == 2:
        return 0
    if 11 in sum_cards and sum(sum_cards) > 21:
        sum_cards.remove(11)
        sum_cards.append(1)
    return sum(sum_cards)


calculate_score()
lbl = Label(width=14,text=f"your sum cards: {calculate_score()}")
lbl.place(x=50)
usercardslbl = Label(blackjack,height=7,width=7, text="you")
usercardslbl.place(y=50)
computercardslbl = Label(blackjack,height=7,width=7, text="computer")
computercardslbl.place(y=170)

xcard = 70
xcard2 = 150
ycard = 170
ycard2 = 170


backcardcanv.place(x=xcard,y=ycard)
randomlistrandom.place(x=xcard2, y=ycard2)
if randomlist1 == allcards[0] or randomlist2 == allcards[0]:
    sum_computer_cards += 11
if randomlist1 == allcards[1] or randomlist2 == allcards[1]:
    sum_computer_cards += 2
if randomlist1 == allcards[2] or randomlist2 == allcards[2]:
    sum_computer_cards += 3
if randomlist1 == allcards[3] or randomlist2 == allcards[3]:
    sum_computer_cards += 4
if randomlist1 == allcards[4] or randomlist2 == allcards[4]:
    sum_computer_cards += 5
if randomlist1 == allcards[5] or randomlist2 == allcards[5]:
    sum_computer_cards += 6
if randomlist1 == allcards[6] or randomlist2 == allcards[6]:
    sum_computer_cards += 7
if randomlist1 == allcards[7] or randomlist2 == allcards[7]:
    sum_computer_cards += 8
if randomlist1 == allcards[8] or randomlist2 == allcards[8]:
    sum_computer_cards += 9
if randomlist1 == allcards[9] or randomlist2 == allcards[9]:
    sum_computer_cards += 10
print(sum_computer_cards)


try_again = 0
if sum(sum_cards) > 21:
    lost = messagebox.showinfo('information', 'you went over 21, you lost.')
    try_again = messagebox.askquestion('Ask Question', 'Do try again?')
if try_again == 'no':
    messagebox.showinfo('bye', 'ok, bye bye.')
    blackjack.destroy()
if try_again == 'yes':
    randomlist2 = random.choice(allcards)
    randomlist1 = random.choice(allcards)
    randomlist3 = random.choice(allcards)
    randomlist4 = random.choice(allcards)
lblcardsbit = Label(blackjack, width=14, text=f"your sum cards: {calculate_score()}")
lblcardsbit.place(x=50)



def calculate_computer_score():
    global sum_computer_cards
    if sum_computer_cards == 21 and sum_computer_cards == 2:
        return 0
    if sum_computer_cards > 21:
        sum_computer_cards -= 11
        sum_computer_cards += 1
    return sum_computer_cards


randomlistrandom2 = random.choice(randomlist2)
def stand():
    global sum_computer_cards
    global xcard2
    global ycard2
    randomlistrandom2.place(x=70, y=170)
    randomlist = random.choice(allcards)
    randomlistrandom = random.choice(randomlist)
    randomlistrandom.place(x=listx, y=listy)
    while sum_computer_cards != 0 and sum_computer_cards < 17:
        xcard2 += 80
        randomlist3 = random.choice(allcards)
        randomlistrandom3 = random.choice(randomlist3)
        randomlistrandom3.place(x=xcard2, y=ycard2)
        if randomlist3 == allcards[0]:
            sum_computer_cards += 1
        if randomlist3 == allcards[1]:
            sum_computer_cards += 2
        if randomlist3 == allcards[2]:
            sum_computer_cards += 3
        if randomlist3 == allcards[3]:
            sum_computer_cards += 4
        if randomlist3 == allcards[4]:
            sum_computer_cards += 5
        if randomlist3 == allcards[5]:
            sum_computer_cards += 6
        if randomlist3 == allcards[6]:
            sum_computer_cards += 7
        if randomlist3 == allcards[7]:
            sum_computer_cards += 8
        if randomlist3 == allcards[8]:
            sum_computer_cards += 9
        if randomlist3 == allcards[9]:
            sum_computer_cards += 10
    print(sum_computer_cards)
button_submit = Button(blackjack,text="Stand",width=6, command=stand)
button_submit.place(x=300, y=400)

blackjack.mainloop()