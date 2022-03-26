from tkinter import *
from PIL import ImageTk,Image
import random

blackjack = Tk()
blackjack.title("blackjack")
blackjack.geometry("500x500")
canv = Canvas(width=1440,height=1920)
canv.place(x=0, y=0)

img = ImageTk.PhotoImage(Image.open("blackjackimage.jpg"))
canv.create_image(0,0,image=img)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card = random.choice(cards)
card2 = random.choice(cards)
sum_cards = card + card2
def calculate_score():
    global sum_cards
    if sum_cards == 21 and sum_cards == 2:
        return 0
    if sum_cards > 21:
        sum_cards -= 11
        sum_cards += 1
    return sum_cards
lbl = Label(blackjack,width=10,height=7,text=(calculate_score()))
lbl.place(x=300,y=50)
lbl = Label(blackjack,width=12,height=7,text="your sum cards: ")
lbl.place(x=240,y=50)
buttonClicked = False
#def changeValue():
#    if buttonClicked:
#        buttonClicked=False
#    if not buttonClicked:
#        buttonClicked=True
#tk = Tk()
#btn = Button(tk, text="Put whatever text you want here, to tell the person what pressing the button will do", command=changeValue())
#btn.pack()
def comuter_cards(back_card,random_card3,num_of_the_card):
    xcard = 50
    xcard2 = 150
    ycard = 170
    ycard2 = 170
    if card == num_of_the_card:
        back_card.place(x=xcard,y=ycard)
    if card2 == num_of_the_card:
        random_card3.place(x=xcard2,y=ycard2)


def user_cards(random_card,random_card2,random_card3,num_of_the_card,club_cards_canv,diamond_cards_canv,heart_cards_canv,spade_cards_canv):
    xcard = 50
    xcard2 = 150
    ycard = 50
    ycard2 = 50
    if card == num_of_the_card:
        random_card.place(x=xcard,y=ycard)
    if card2 == num_of_the_card:
        random_card2.place(x=xcard2,y=ycard2)
    while random_card == random_card3 or random_card3 == random_card2 or random_card == random_card2  and card == num_of_the_card and card2 == num_of_the_card:
        if random_card2 == club_cards_canv:
            random_card2 = diamond_cards_canv
            random_card2.place(x=xcard2,y=ycard2)
        if random_card2 == diamond_cards_canv:
            random_card2 = club_cards_canv
            random_card2.place(x=xcard2,y=ycard2)
        if random_card2 == heart_cards_canv:
            random_card2 = club_cards_canv
            random_card2.place(x=xcard2,y=ycard2)
        if random_card2 == spade_cards_canv:
            random_card2 = club_cards_canv
            random_card2.place(x=xcard2,y=ycard2)
        if random_card == club_cards_canv:
            random_card = diamond_cards_canv
            random_card.place(x=xcard2,y=ycard2)
        if random_card == diamond_cards_canv:
            random_card = club_cards_canv
            random_card.place(x=xcard2,y=ycard2)
        if random_card == heart_cards_canv:
            random_card = club_cards_canv
            random_card.place(x=xcard2,y=ycard2)
        if random_card == spade_cards_canv:
            random_card = club_cards_canv
            random_card.place(x=xcard2,y=ycard2)
        if random_card3 == club_cards_canv:
            random_card3 = diamond_cards_canv
            random_card3.place(x=xcard2,y=ycard2)
        if random_card3 == diamond_cards_canv:
            random_card3 = club_cards_canv
            random_card3.place(x=xcard2,y=ycard2)
        if random_card3 == heart_cards_canv:
            random_card3 = club_cards_canv
            random_card3.place(x=xcard2,y=ycard2)
        if random_card3 == spade_cards_canv:
            random_card3 = club_cards_canv
            random_card3.place(x=xcard2,y=ycard2)

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
random1card = random.choice(all1card)
random1card2 = random.choice(all1card)
random1card3 = random.choice(all1card)

user_cards(random1card,random1card2,random1card3,11,club1cardcanv,diamond1cardcanv,heart1cardcanv,spade1cardcanv)
comuter_cards(backcardcanv,random1card3,11)

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
random2card = random.choice(all2card)
random2card2 = random.choice(all2card)
random2card3 = random.choice(all2card)

user_cards(random2card,random2card2,random2card3,2,club2cardcanv,diamond2cardcanv,heart2cardcanv,spade2cardcanv)
comuter_cards(backcardcanv,random2card3,2)

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
random3card = random.choice(all3card)
random3card2 = random.choice(all3card)
random3card3 = random.choice(all3card)

user_cards(random3card,random3card2,random3card3,3,club3cardcanv,diamond3cardcanv,heart3cardcanv,spade3cardcanv)
comuter_cards(backcardcanv,random3card3,3)

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
random4card = random.choice(all4card)
random4card2 = random.choice(all4card)
random4card3 = random.choice(all4card)

user_cards(random4card,random4card2,random4card3,4,club4cardcanv,diamond4cardcanv,heart4cardcanv,spade4cardcanv)
comuter_cards(backcardcanv,random4card3,4)

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
random5card = random.choice(all5card)
random5card2 = random.choice(all5card)
random5card3 = random.choice(all5card)

user_cards(random5card,random5card2,random5card3,5,club5cardcanv,diamond5cardcanv,heart5cardcanv,spade5cardcanv)
comuter_cards(backcardcanv,random5card3,5)

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
random6card = random.choice(all6card)
random6card2 = random.choice(all6card)
random6card3 = random.choice(all6card)

user_cards(random6card,random6card2,random6card3,6,club6cardcanv,diamond6cardcanv,heart6cardcanv,spade6cardcanv)
comuter_cards(backcardcanv,random6card3,6)

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
random7card = random.choice(all7card)
random7card2 = random.choice(all7card)
random7card3 = random.choice(all7card)

user_cards(random7card,random7card2,random7card3,7,club7cardcanv,diamond7cardcanv,heart7cardcanv,spade7cardcanv)
comuter_cards(backcardcanv,random7card3,7)

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
random8card = random.choice(all8card)
random8card2 = random.choice(all8card)
random8card3 = random.choice(all8card)

user_cards(random8card,random8card2,random8card3,8,club8cardcanv,diamond8cardcanv,heart8cardcanv,spade8cardcanv)
comuter_cards(backcardcanv,random8card3,8)

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
random9card = random.choice(all9card)
random9card2 = random.choice(all9card)
random9card3 = random.choice(all9card)

user_cards(random9card,random9card2,random9card3,9,club9cardcanv,diamond9cardcanv,heart9cardcanv,spade9cardcanv)
comuter_cards(backcardcanv,random9card3,9)

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
random10card = random.choice(all10card)
random10card2 = random.choice(all10card)
random10card3 = random.choice(all9card)

user_cards(random10card,random10card2,random10card3,10,club10cardcanv,diamond10cardcanv,heart10cardcanv,spade10cardcanv)
comuter_cards(backcardcanv,random10card3,10)

blackjack.mainloop()