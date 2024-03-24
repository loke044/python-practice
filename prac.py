def gif():
    print("name=giftson\nage=20\nqualification=B.E")

def ved():
    print("name:Vedamanickam\nage=50\nqualification:MBA")

while True:
    print("to get detials of 1.giftson /2.vedamanickam /3.quit")
    a=int(input(":"))
    if a==1:
        gif()
    elif a==2:
        ved()
    elif a==3:
        break
    else:
        print("choose correct option!")
