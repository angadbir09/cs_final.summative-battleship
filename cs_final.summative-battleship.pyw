import random
turn=1
import time

comppb=2
compgs=3
compsm=3
compbs=4
compac=5
playerpb=2
playergs=3
playersm=3
playerbs=4
playerac=5
player2pb=2
player2gs=3
player2sm=3
player2bs=4
player2ac=5
userpb=2
usergs=3
usersm=3
userbs=4
userac=5

num=[]
num2=[]
num3=[]
num4=[]
num5=[]
num6=[]
num7=[]
num8=[]
num9=[]
num10=[]

numa=[]
num2a=[]
num3a=[]
num4a=[]
num5a=[]
num6a=[]
num7a=[]
num8a=[]
num9a=[]
num10a=[]

numb=[]
num2b=[]
num3b=[]
num4b=[]
num5b=[]
num6b=[]
num7b=[]
num8b=[]
num9b=[]
num10b=[]

numc=[]
num2c=[]
num3c=[]
num4c=[]
num5c=[]
num6c=[]
num7c=[]
num8c=[]
num9c=[]
num10c=[]

numd=[]
num2d=[]
num3d=[]
num4d=[]
num5d=[]
num6d=[]
num7d=[]
num8d=[]
num9d=[]
num10d=[]

nume=[]
num2e=[]
num3e=[]
num4e=[]
num5e=[]
num6e=[]
num7e=[]
num8e=[]
num9e=[]
num10e=[]

for xd in range(10):
    num.append(0)
    num2.append(0)
    num3.append(0)
    num4.append(0)
    num5.append(0)
    num6.append(0)
    num7.append(0)
    num8.append(0)
    num9.append(0)
    num10.append(0)
    numa.append(0)
    num2a.append(0)
    num3a.append(0)
    num4a.append(0)
    num5a.append(0)
    num6a.append(0)
    num7a.append(0)
    num8a.append(0)
    num9a.append(0)
    num10a.append(0)
    numb.append(0)
    num2b.append(0)
    num3b.append(0)
    num4b.append(0)
    num5b.append(0)
    num6b.append(0)
    num7b.append(0)
    num8b.append(0)
    num9b.append(0)
    num10b.append(0)
    numc.append(0)
    num2c.append(0)
    num3c.append(0)
    num4c.append(0)
    num5c.append(0)
    num6c.append(0)
    num7c.append(0)
    num8c.append(0)
    num9c.append(0)
    num10c.append(0)
    numd.append(0)
    num2d.append(0)
    num3d.append(0)
    num4d.append(0)
    num5d.append(0)
    num6d.append(0)
    num7d.append(0)
    num8d.append(0)
    num9d.append(0)
    num10d.append(0)
    nume.append(0)
    num2e.append(0)
    num3e.append(0)
    num4e.append(0)
    num5e.append(0)
    num6e.append(0)
    num7e.append(0)
    num8e.append(0)
    num9e.append(0)
    num10e.append(0)
    compgrid=[num,num2,num3,num4,num5,num6,num7,num8,num9,num10]
    user2grid=[numa,num2a,num3a,num4a,num5a,num6a,num7a,num8a,num9a,num10a]
    user2aimgrid=[numb,num2b,num3b,num4b,num5b,num6b,num7b,num8b,num9b,num10b]
    usergrid=[numc,num2c,num3c,num4c,num5c,num6c,num7c,num8c,num9c,num10c]
    userpseudogrid=[numd,num2d,num3d,num4d,num5d,num6d,num7d,num8d,num9d,num10d]
    useraimgrid=[nume,num2e,num3e,num4e,num5e,num6e,num7e,num8e,num9e,num10e]

def playeraimgrid():
    print "  \t 1  2  3  4  5  6  7  8  9  10"
    print 1, "\t", useraimgrid[0]
    print 2, "\t", useraimgrid[1]
    print 3, "\t", useraimgrid[2]
    print 4, "\t", useraimgrid[3]
    print 5, "\t", useraimgrid[4]
    print 6, "\t", useraimgrid[5]
    print 7, "\t", useraimgrid[6]
    print 8, "\t", useraimgrid[7]
    print 9, "\t", useraimgrid[8]
    print 10, "\t", useraimgrid[9]

def player2aimgrid():
    print "  \t 1  2  3  4  5  6  7  8  9  10"
    print 1, "\t", user2aimgrid[0]
    print 2, "\t", user2aimgrid[1]
    print 3, "\t", user2aimgrid[2]
    print 4, "\t", user2aimgrid[3]
    print 5, "\t", user2aimgrid[4]
    print 6, "\t", user2aimgrid[5]
    print 7, "\t", user2aimgrid[6]
    print 8, "\t", user2aimgrid[7]
    print 9, "\t", user2aimgrid[8]
    print 10, "\t", user2aimgrid[9]

def playergrid():
    print "  \t 1  2  3  4  5  6  7  8  9  10"
    print 1, "\t", usergrid[0]
    print 2, "\t", usergrid[1]
    print 3, "\t", usergrid[2]
    print 4, "\t", usergrid[3]
    print 5, "\t", usergrid[4]
    print 6, "\t", usergrid[5]
    print 7, "\t", usergrid[6]
    print 8, "\t", usergrid[7]
    print 9, "\t", usergrid[8]
    print 10, "\t", usergrid[9]

def player2grid():
    print "  \t 1  2  3  4  5  6  7  8  9  10"
    print 1, "\t", user2grid[0]
    print 2, "\t", user2grid[1]
    print 3, "\t", user2grid[2]
    print 4, "\t", user2grid[3]
    print 5, "\t", user2grid[4]
    print 6, "\t", user2grid[5]
    print 7, "\t", user2grid[6]
    print 8, "\t", user2grid[7]
    print 9, "\t", user2grid[8]
    print 10, "\t", user2grid[9]

def nocheat():
    for c in range (15):
        print "NO CHEAT SPACER \n \n \n \n \n"

print "BATTLESHIP\nSelect Number of Players"
playercount=raw_input("Singleplayer or Multiplayer?: ")

while (playercount!="multiplayer") and (playercount!="singleplayer") and (playercount!="Multiplayer") and (playercount!="Singleplayer"):
    print "ERROR", playercount, "is not an option. Try again!"
    playercount=raw_input("Singleplayer or Multiplayer?: ")
    

if(playercount=="Multiplayer") or (playercount=="multiplayer"):    
    #Location of the Player's Ships
    
    print "Ship Locations of Player 1"
    print "Enter Coordinates of Starting Location of Patrol Boat"
    pbx=input("Enter y-coordinate: ")
    pby=input("Enter x-coordinate: ")
    while (pbx>10) or (pbx<1):
        print pbx, "is not on the grid. Try again!"
        pbx=input("Enter y-coordinate: ")
        pby=input("Enter x-coordinate: ")
    while (pby>10) or (pby<1):
        print pby, "is not on the grid. Try again!"
        pby=input("Enter x-coordinate: ")
    direction_pb=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
    while (direction_pb!="up") and (direction_pb!="down") and (direction_pb!="left") and (direction_pb!="right"):
        print "ERROR", direction_pb, "is not an option"
        direction_pb=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")   
    if direction_pb=="right":
        pb2y=pby+1
        pb2x=pbx
    elif direction_pb=="left":
        pb2y=pby-1
        pb2x=pbx
    elif direction_pb=="up":
        pb2x=pbx-1
        pb2y=pby
    else:
        pb2x=pbx+1
        pb2y=pby
    while (pb2x>10) or (pb2x<1) or (pb2y>10) or (pb2y<1):
        print "ERROR, the ships cannot be placed off the grid"
        direction_pb=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
        while (direction_pb!="up") and (direction_pb!="down") and (direction_pb!="left") and (direction_pb!="right"):
            print "ERROR", direction_pb, "is not an option"
            direction_pb=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")   
        if direction_pb=="right":
            pb2y=pby+1
            pb2x=pbx
        elif direction_pb=="left":
            pb2y=pby-1
            pb2x=pbx
        elif direction_pb=="up":
            pb2x=pbx-1
            pb2y=pby
        else:
            pb2x=pbx+1
            pb2y=pby

    usergrid[pbx-1][pby-1]=1
    usergrid[pb2x-1][pb2y-1]=1

    playergrid()  

    subcheck="invalid"
    while subcheck=="invalid":
            print "Enter Coordinates of Stating Location of Submarine"
            subx=input("Enter y-coordinate: ")
            while (subx>10) or (subx<1):
                print subx, "is not on the grid. Try again!"
                subx=input("Enter y-coordinate: ")
            suby=input("Enter x-coordinate: ")
            while (suby>10) or (suby<1):
                print suby, "is not on the grid. Try again!"
                suby=input("Enter x-coordinate: ")
            direction_sub=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_sub!="up") and (direction_sub!="down") and (direction_sub!="left") and (direction_sub!="right"):
                print "ERROR", direction_sub, "is not an option. Please try again"
                direction_sub=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_sub=="right":
                        sub2y=suby+1
                        sub2x=subx
                        sub3y=suby+2
                        sub3x=subx
            elif direction_sub=="left":
                sub2y=suby-1
                sub2x=subx
                sub3y=suby-2
                sub3x=subx
            elif direction_sub=="up":
                sub2x=subx-1
                sub2y=suby
                sub3x=subx-2
                sub3y=suby
            else:
                sub2x=subx+1
                sub2y=suby
                sub3x=subx+2
                sub3y=suby
            while (sub3x>10) or (sub3x<1) or (sub3y>10) or (sub3y<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_sub=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_sub!="up") and (direction_sub!="down") and (direction_sub!="left") and (direction_sub!="right"):
                print "ERROR", direction_sub, "is not an option. Please try again"
                directin_sub=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_sub=="right":
                    sub2y=suby+1
                    sub2x=subx
                    sub3y=suby+2
                    sub3x=subx
                elif direction_sub=="left":
                    sub2y=suby-1
                    sub2x=subx
                    sub3y=suby-2
                    sub3x=subx
                elif direction_sub=="up":
                    sub2x=subx-1
                    sub2y=suby
                    sub3x=subx-2
                    sub3y=suby
                else:
                    sub2x=subx+1
                    sub2y=suby
                    sub3x=subx+2
                    sub3y=suby
            if usergrid[subx-1][suby-1]!=0 or usergrid[sub2x-1][sub2y-1]!=0 or usergrid[sub3x-1][sub3y-1]!=0:
                    print "ERROR"
                    print "Select again"
                    subcheck="invalid"
            elif usergrid[subx-1][suby-1]==0 or usergrid[sub2x-1][sub2y-1]==0 or usergrid[sub3x-1][sub3y-1]==0:
                    usergrid[subx-1][suby-1]=2
                    usergrid[sub2x-1][sub2y-1]=2
                    usergrid[sub3x-1][sub3y-1]=2
                    subcheck="valid"

    playergrid()

    gscheck="invalid"
    while gscheck=="invalid":
            print "Enter Coordinates of Stating Location of Gunship"
            gsx=input("Enter y-coordinate: ")
            while (gsx>10) or (gsx<1):
                print gsx, "is not on the grid. Try again!"
                gsx=input("Enter y-coordinate: ")
            gsy=input("Enter x-coordinate: ")
            while (gsy>10) or (gsy<1):
                print gsy, "is not on the grid. Try again!"
                gsy=input("Enter x-coordinate: ")
            direction_gs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_gs!="up") and (direction_gs!="down") and (direction_gs!="left") and (direction_gs!="right"):
                print "ERROR", direction_gs, "is not an option. Please try again"
                direction_gs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_gs=="right":
                gs2y=gsy+1
                gs2x=gsx
                gs3y=gsy+2
                gs3x=gsx
            elif direction_gs=="left":
                gs2y=gsy-1
                gs2x=gsx
                gs3y=gsy-2
                gs3x=gsx
            elif direction_gs=="up":
                gs2x=gsx-1
                gs2y=gsy
                gs3x=gsx-2
                gs3y=gsy
            else:
                gs2x=gsx+1
                gs2y=gsy
                gs3x=gsx+2
                gs3y=gsy
            while (gs3x>10) or (gs3x<1) or (gs3y>10) or (gs3y<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_gs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_gs=="right":
                    gs2y=gsy+1
                    gs2x=gsx
                    gs3y=gsy+2
                    gs3x=gsx
                elif direction_gs=="left":
                    gs2y=gsy-1
                    gs2x=gsx
                    gs3y=gsy-2
                    gs3x=gsx
                elif direction_gs=="up":
                    gs2x=gsx-1
                    gs2y=gsy
                    gs3x=gsx-2
                    gs3y=gsy
                else:
                    gs2x=gsx+1
                    gs2y=gsy
                    gs3x=gsx+2
                    gs3y=gsy

            if usergrid[gsx-1][gsy-1]!=0 or usergrid[gs2x-1][gs2y-1]!=0 or usergrid[gs3x-1][gs3y-1]!=0:
                    print "ERROR"
                    print "Select again"
                    gscheck="invalid"
            elif usergrid[gsx-1][gsy-1]==0 or usergrid[gs2x-1][gs2y-1]==0 or usergrid[gs3x-1][gs3y-1]==0:
                    usergrid[gsx-1][gsy-1]=5
                    usergrid[gs2x-1][gs2y-1]=5
                    usergrid[gs3x-1][gs3y-1]=5
                    gscheck="valid"

    playergrid()


    bscheck="invalid"
    while bscheck=="invalid":
            print "Enter Coordinates of Stating Location of Battleship"
            bsx=input("Enter y-coordinate: ")
            while (bsx>10) or (bsx<1):
                print bsx, "is not on the grid. Try again!"
                bsx=input("Enter y-coordinate: ")
            bsy=input("Enter x-coordinate: ")
            while (bsy>10) or (bsy<1):
                print bsy, "is not on the grid. Try again!"
                bsy=input("Enter x-coordinate: ")
            direction_bs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_bs!="up") and (direction_bs!="down") and (direction_bs!="left") and (direction_bs!="right"):
                print "ERROR", direction_bs, "is not an option. Please try again"
                direction_bs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_bs=="right":
                bs2y=bsy+1
                bs2x=bsx
                bs3y=bsy+2
                bs3x=bsx
                bs4y=bsy+3
                bs4x=bsx
            elif direction_bs=="left":
                bs2y=bsy-1
                bs2x=bsx
                bs3y=bsy-2
                bs3x=bsx
                bs4y=bsy-3
                bs4x=bsx
            elif direction_bs=="up":
                bs2x=bsx-1
                bs2y=bsy
                bs3x=bsx-2
                bs3y=bsy
                bs4x=bsx-3
                bs4y=bsy
            else:
                bs2x=bsx+1
                bs2y=bsy
                bs3x=bsx+2
                bs3y=bsy
                bs4x=bsx+3
                bs4y=bsy
            while (bs4x>10) or (bs4x<1) or (bs4y>10) or (bs4y<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_bs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_bs=="right":
                    bs2y=bsy+1
                    bs2x=bsx
                    bs3y=bsy+2
                    bs3x=bsx
                    bs4y=bsy+3
                    bs4x=bsx
                elif direction_bs=="left":
                    bs2y=bsy-1
                    bs2x=bsx
                    bs3y=bsy-2
                    bs3x=bsx
                    bs4y=bsy-3
                    bs4x=bsx
                elif direction_bs=="up":
                    bs2x=bsx-1
                    bs2y=bsy
                    bs3x=bsx-2
                    bs3y=bsy
                    bs4x=bsx-3
                    bs4y=bsy
                else:
                    bs2x=bsx+1
                    bs2y=bsy
                    bs3x=bsx+2
                    bs3y=bsy
                    bs4x=bsx+3
                    bs4y=bsy
            if usergrid[bsx-1][bsy-1]!=0 or usergrid[bs2x-1][bs2y-1]!=0 or usergrid[bs3x-1][bs3y-1]!=0 or usergrid[bs4x-1][bs4x-1]!=0:
                    print "ERROR"
                    print "Select again"
                    bscheck="invalid"
            elif usergrid[bsx-1][bsy-1]==0 and usergrid[bs2x-1][bs2y-1]==0 and usergrid[bs3x-1][bs3y-1]==0 and usergrid[bs4x-1][bs4x-1]==0:
                    usergrid[bsx-1][bsy-1]=3
                    usergrid[bs2x-1][bs2y-1]=3
                    usergrid[bs3x-1][bs3y-1]=3
                    usergrid[bs4x-1][bs4y-1]=3
                    bscheck="valid"

    playergrid()

    accheck="invalid"
    while accheck=="invalid":
            print "Enter Coordinates of Starting Location of Aircraft Carrier"
            acx=input("Enter y-coordinate: ")
            while (acx>10) or (acx<1):
                print acx, "is not on the grid. Try again!"
                acx=input("Enter y-coordinate: ")
            acy=input("Enter x-coordinate: ")
            while (acy>10) or (acy<1):
                print acy, "is not on the grid. Try again!"
                acy=input("Enter x-coordinate: ")
            direction_ac=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_ac!="up") and (direction_ac!="down") and (direction_ac!="left") and (direction_ac!="right"):
                print "ERROR", direction_ac, "is not an option. Please try again"
                direction_ac=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_ac=="right":
                ac2y=acy+1
                ac2x=acx
                ac3y=acy+2
                ac3x=acx
                ac4y=acy+3
                ac4x=acx
                ac5y=acy+4
                ac5x=acx
            elif direction_ac=="left":
                ac2y=acy-1
                ac2x=acx
                ac3y=acy-2
                ac3x=acx
                ac4y=acy-3
                ac4x=acx
                ac5y=acy-4
                ac5x=acx
            elif direction_ac=="up":
                ac2x=acx-1
                ac2y=acy
                ac3x=acx-2
                ac3y=acy
                ac4x=acx-3
                ac4y=acy
                ac5x=acx-4
                ac5y=acy
            else:
                ac2x=acx+1
                ac2y=acy
                ac3x=acx+2
                ac3y=acy
                ac4x=acx+3
                ac4y=acy
                ac5x=acx+4
                ac5y=acy
            if (ac5x>10) or (ac5x<1) or (ac5y>10) or (ac5y<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_bs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_ac=="right":
                    ac2y=acy+1
                    ac2x=acx
                    ac3y=acy+2
                    ac3x=acx
                    ac4y=acy+3
                    ac4x=acx
                    ac5y=acy+4
                    ac5x=acx
                elif direction_ac=="left":
                    ac2y=acy-1
                    ac2x=acx
                    ac3y=acy-2
                    ac3x=acx
                    ac4y=acy-3
                    ac4x=acx
                    ac5y=acy-4
                    ac5x=acx
                elif direction_ac=="up":
                    ac2x=acx-1
                    ac2y=acy
                    ac3x=acx-2
                    ac3y=acy
                    ac4x=acx-3
                    ac4y=acy
                    ac5x=acx-4
                    ac5y=acy
                else:
                    ac2x=acx+1
                    ac2y=acy
                    ac3x=acx+2
                    ac3y=acy
                    ac4x=acx+3
                    ac4y=acy
                    ac5x=acx+4
                    ac5y=acy   
            if usergrid[acx-1][acy-1]!=0 or usergrid[ac2x-1][ac2y-1]!=0 or usergrid[ac3x-1][ac3y-1]!=0 or usergrid[ac4x-1][ac4y-1]!=0 or usergrid[ac5x-1][ac5y-1]!=0:
                    print "ERROR"
                    print "Select again"
                    accheck="invalid"
            elif usergrid[acx-1][acy-1]==0 and usergrid[ac2x-1][ac2y-1]==0 and usergrid[ac3x-1][ac3y-1]==0 and usergrid[ac4x-1][ac4y-1]==0 and usergrid[ac5x-1][ac5y-1]==0:
                    usergrid[acx-1][acy-1]=4
                    usergrid[ac2x-1][ac2y-1]=4
                    usergrid[ac3x-1][ac3y-1]=4
                    usergrid[ac4x-1][ac4y-1]=4
                    usergrid[ac5x-1][ac5y-1]=4
                    accheck="valid"

    playergrid()

    nocheat()
    #Ship locations for player 2


    print "Ship Locations for Player 2"
    print "Enter Coordinates of Starting Location of Patrol Boat"
    pbx2=input("Enter y-coordinate: ")
    while (pbx2>10) or (pbx2<1):
        print pbx2, "is not on the grid. Try again!"
        pbx2=input("Enter y-coordinate: ")
    pby2=input("Enter x-coordinate: ")
    while (pby2>10) or (pby2<1):
        print pby2, "is not on the grid. Try again!"
        pby2=input("Enter x-coordinate: ")
    direction_pb2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
    while (direction_pb2!="up") and (direction_pb2!="down") and (direction_pb2!="left") and (direction_pb2!="right"):
        print "ERROR", direction_pb2, "is not an option"
        direction_pb2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")   
    if direction_pb2=="right":
        pb2y2=pby2+1
        pb2x2=pbx2
    elif direction_pb2=="left":
        pb2y2=pby2-1
        pb2x2=pbx2
    elif direction_pb2=="up":
        pb2x2=pbx2-1
        pb2y2=pby2
    else:
        pb2x2=pbx2+1
        pb2y2=pby2
    while (pb2x2>10) or (pb2x2<1) or (pb2y2>10) or (pb2y2<1):
        print "ERROR, the ships cannot be placed off the grid"
        direction_pb2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
        while (direction_pb2!="up") and (direction_pb2!="down") and (direction_pb2!="left") and (direction_pb2!="right"):
            print "ERROR", direction_pb2, "is not an option"
            direction_pb2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")   
        if direction_pb2=="right":
            pb2y2=pby2+1
            pb2x2=pbx2
        elif direction_pb2=="left":
            pb2y2=pby2-1
            pb2x2=pbx2
        elif direction_pb2=="up":
            pb2x2=pbx2-1
            pb2y2=pby2
        else:
            pb2x2=pbx2+1
            pb2y2=pby2

    user2grid[pbx2-1][pby2-1]=1
    user2grid[pb2x2-1][pb2y2-1]=1

    player2grid()
    
    sub2check="invalid"
    while sub2check=="invalid":
            print "Enter Coordinates of Stating Location of Submarine"
            subx2=input("Enter y-coordinate: ")
            while (subx2>10) or (subx2<1):
                print subx2, "is not on the grid. Try again!"
                subx2=input("Enter y-coordinate: ")
            suby2=input("Enter x-coordinate: ")
            while (suby2>10) or (suby2<1):
                print suby2, "is not on the grid. Try again!"
                suby2=input("Enter x-coordinate: ")
            direction_sub2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_sub2!="up") and (direction_sub2!="down") and (direction_sub2!="left") and (direction_sub2!="right"):
                print "ERROR", direction_sub2, "is not an option. Please try again"
                direction_sub2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_sub2=="right":
                        sub2y2=suby2+1
                        sub2x2=subx2
                        sub3y2=suby2+2
                        sub3x2=subx2
            elif direction_sub2=="left":
                sub2y2=suby2-1
                sub2x2=subx2
                sub3y2=suby2-2
                sub3x2=subx2
            elif direction_sub2=="up":
                sub2x2=subx2-1
                sub2y2=suby2
                sub3x2=subx2-2
                sub3y2=suby2
            else:
                sub2x2=subx2+1
                sub2y2=suby2
                sub3x2=subx2+2
                sub3y2=suby2
            while (sub3x2>10) or (sub3x2<1) or (sub3y2>10) or (sub3y2<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_sub2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_sub2!="up") and (direction_sub2!="down") and (direction_sub2!="left") and (direction_sub2!="right"):
                print "ERROR", direction_sub2, "is not an option. Please try again"
                directin_sub2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_sub2=="right":
                    sub2y2=suby2+1
                    sub2x2=subx2
                    sub3y2=suby2+2
                    sub3x2=subx2
                elif direction_sub2=="left":
                    sub2y2=suby2-1
                    sub2x2=subx2
                    sub3y2=suby2-2
                    sub3x2=subx2
                elif direction_su2b=="up":
                    sub2x2=subx2-1
                    sub2y2=suby2
                    sub3x2=subx2-2
                    sub3y2=suby2
                else:
                    sub2x2=subx+1
                    sub2y2=suby2
                    sub3x2=subx2+2
                    sub3y2=suby2
            if user2grid[subx2-1][suby2-1]!=0 or user2grid[sub2x2-1][sub2y2-1]!=0 or user2grid[sub3x2-1][sub3y2-1]!=0:
                    print "ERROR"
                    print "Select again"
                    sub2check="invalid"
            elif user2grid[subx2-1][suby2-1]==0 or user2grid[sub2x2-1][sub2y2-1]==0 or user2grid[sub3x2-1][sub3y2-1]==0:
                    user2grid[subx2-1][suby2-1]=2
                    user2grid[sub2x2-1][sub2y2-1]=2
                    user2grid[sub3x2-1][sub3y2-1]=2
                    sub2check="valid"

    player2grid()

    gs2check="invalid"
    while gs2check=="invalid":
            print "Enter Coordinates of Stating Location of Gunship"
            gsx2=input("Enter y-coordinate: ")
            while (gsx2>10) or (gsx2<1):
                print gsx2, "is not on the grid. Try again!"
                gsx2=input("Enter y-coordinate: ")
            gsy2=input("Enter x-coordinate: ")
            while (gsy2>10) or (gsy2<1):
                print gsy2, "is not on the grid. Try again!"
                gsy2=input("Enter x-coordinate: ")
            direction_gs2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_gs2!="up") and (direction_gs2!="down") and (direction_gs2!="left") and (direction_gs2!="right"):
                print "ERROR", direction_gs2, "is not an option. Please try again"
                direction_gs2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_gs2=="right":
                gs2y2=gsy2+1
                gs2x2=gsx2
                gs3y2=gsy2+2
                gs3x2=gsx2
            elif direction_gs2=="left":
                gs2y2=gsy2-1
                gs2x2=gsx2
                gs3y2=gsy2-2
                gs3x2=gsx2
            elif direction_gs2=="up":
                gs2x2=gsx2-1
                gs2y2=gsy2
                gs3x2=gsx2-2
                gs3y2=gsy2
            else:
                gs2x2=gsx2+1
                gs2y2=gsy2
                gs3x2=gsx2+2
                gs3y2=gsy2
            while (gs3x2>10) or (gs3x2<1) or (gs3y2>10) or (gs3y2<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_gs2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_gs2=="right":
                    gs2y2=gsy2+1
                    gs2x2=gsx2
                    gs3y2=gsy2+2
                    gs3x2=gsx2
                elif direction_gs2=="left":
                    gs2y2=gsy2-1
                    gs2x2=gsx2
                    gs3y2=gsy2-2
                    gs3x2=gsx2
                elif direction_gs2=="up":
                    gs2x2=gsx2-1
                    gs2y2=gsy2
                    gs3x2=gsx2-2
                    gs3y2=gsy2
                else:
                    gs2x2=gsx2+1
                    gs2y2=gsy2
                    gs3x2=gsx2+2
                    gs3y2=gsy2

            if user2grid[gsx2-1][gsy2-1]!=0 or user2grid[gs2x2-1][gs2y2-1]!=0 or user2grid[gs3x2-1][gs3y2-1]!=0:
                    print "ERROR"
                    print "Select again"
                    gs2check="invalid"
            elif user2grid[gsx2-1][gsy2-1]==0 or user2grid[gs2x2-1][gs2y2-1]==0 or user2grid[gs3x2-1][gs3y2-1]==0:
                    user2grid[gsx2-1][gsy2-1]=5
                    user2grid[gs2x2-1][gs2y2-1]=5
                    user2grid[gs3x2-1][gs3y2-1]=5
                    gs2check="valid"

    player2grid()


    bs2check="invalid"
    while bs2check=="invalid":
            print "Enter Coordinates of Stating Location of Battleship"
            bsx2=input("Enter y-coordinate: ")
            while (bsx2>10) or (bsx2<1):
                print bsx2, "is not on the grid. Try again!"
                bsx2=input("Enter y-coordinate: ")
            bsy2=input("Enter x-coordinate: ")
            while (bsy2>10) or (bsy2<1):
                print bsy2, "is not on the grid. Try again!"
                bsy2=input("Enter x-coordinate: ")
            direction_bs2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_bs2!="up") and (direction_bs2!="down") and (direction_bs2!="left") and (direction_bs2!="right"):
                print "ERROR", direction_bs2, "is not an option. Please try again"
                direction_bs2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_bs2=="right":
                bs2y2=bsy2+1
                bs2x2=bsx2
                bs3y2=bsy2+2
                bs3x2=bsx2
                bs4y2=bsy2+3
                bs4x2=bsx2
            elif direction_bs2=="left":
                bs2y2=bsy2-1
                bs2x2=bsx2
                bs3y2=bsy2-2
                bs3x2=bsx2
                bs4y2=bsy2-3
                bs4x2=bsx2
            elif direction_bs2=="up":
                bs2x2=bsx2-1
                bs2y2=bsy2
                bs3x2=bsx2-2
                bs3y2=bsy2
                bs4x2=bsx2-3
                bs4y2=bsy2
            else:
                bs2x2=bsx2+1
                bs2y2=bsy2
                bs3x2=bsx2+2
                bs3y2=bsy2
                bs4x2=bsx2+3
                bs4y2=bsy2
            while (bs4x2>10) or (bs4x2<1) or (bs4y2>10) or (bs4y2<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_bs2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_bs2=="right":
                    bs2y2=bsy2+1
                    bs2x2=bsx2
                    bs3y2=bsy2+2
                    bs3x2=bsx2
                    bs4y2=bsy2+3
                    bs4x2=bsx2
                elif direction_bs2=="left":
                    bs2y2=bsy2-1
                    bs2x2=bsx2
                    bs3y2=bsy2-2
                    bs3x2=bsx2
                    bs4y2=bsy2-3
                    bs4x2=bsx2
                elif direction_bs2=="up":
                    bs2x2=bsx2-1
                    bs2y2=bsy2
                    bs3x2=bsx2-2
                    bs3y2=bsy2
                    bs4x2=bsx2-3
                    bs4y2=bsy2
                else:
                    bs2x2=bsx2+1
                    bs2y2=bsy2
                    bs3x2=bsx2+2
                    bs3y2=bsy2
                    bs4x2=bsx2+3
                    bs4y2=bsy2
            if user2grid[bsx2-1][bsy2-1]!=0 or user2grid[bs2x2-1][bs2y2-1]!=0 or user2grid[bs3x2-1][bs3y2-1]!=0 or user2grid[bs4x2-1][bs4x2-1]!=0:
                    print "ERROR"
                    print "Select again"
                    bs2check="invalid"
            elif user2grid[bsx2-1][bsy2-1]==0 and user2grid[bs2x2-1][bs2y2-1]==0 and user2grid[bs3x2-1][bs3y2-1]==0 and user2grid[bs4x2-1][bs4x2-1]==0:
                    user2grid[bsx2-1][bsy2-1]=3
                    user2grid[bs2x2-1][bs2y2-1]=3
                    user2grid[bs3x2-1][bs3y2-1]=3
                    user2grid[bs4x2-1][bs4y2-1]=3
                    bs2check="valid"

    player2grid()

    ac2check="invalid"
    while ac2check=="invalid":
            print "Enter Coordinates of Starting Location of Aircraft Carrier"
            acx2=input("Enter y-coordinates: ")
            while (acx2>10) or (acx2<1):
                print acx2, "is not on the grid. Try again!"
                acx2=input("Enter y-coordinate: ")
            acy2=input("Enter x-coordinates: ")
            while (acy2>10) or (acy2<1):
                print acy2, "is not on the grid. Try again!"
                acy2=input("Enter x-coordinate: ")
            direction_ac2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_ac2!="up") and (direction_ac2!="down") and (direction_ac2!="left") and (direction_ac2!="right"):
                print "ERROR", direction_ac2, "is not an option. Please try again"
                direction_ac2=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_ac2=="right":
                ac2y2=acy2+1
                ac2x2=acx2
                ac3y2=acy2+2
                ac3x2=acx2
                ac4y2=acy2+3
                ac4x2=acx2
                ac5y2=acy2+4
                ac5x2=acx2
            elif direction_ac2=="left":
                ac2y2=acy2-1
                ac2x2=acx2
                ac3y2=acy2-2
                ac3x2=acx2
                ac4y2=acy2-3
                ac4x2=acx2
                ac5y2=acy2-4
                ac5x2=acx2
            elif direction_ac2=="up":
                ac2x2=acx2-1
                ac2y2=acy2
                ac3x2=acx2-2
                ac3y2=acy2
                ac4x2=acx2-3
                ac4y2=acy2
                ac5x2=acx2-4
                ac5y2=acy2
            else:
                ac2x2=acx2+1
                ac2y2=acy2
                ac3x2=acx2+2
                ac3y2=acy2
                ac4x2=acx2+3
                ac4y2=acy2
                ac5x2=acx2+4
                ac5y2=acy2
            if user2grid[acx2-1][acy2-1]!=0 or user2grid[ac2x2-1][ac2y2-1]!=0 or user2grid[ac3x2-1][ac3y2-1]!=0 or user2grid[ac4x2-1][ac4y2-1]!=0 or user2grid[ac5x2-1][ac5y2-1]!=0:
                    print "ERROR"
                    print "Select again"
                    ac2check="invalid"
            elif user2grid[acx2-1][acy2-1]==0 and user2grid[ac2x2-1][ac2y2-1]==0 and user2grid[ac3x2-1][ac3y2-1]==0 and user2grid[ac4x2-1][ac4y2-1]==0 and user2grid[ac5x2-1][ac5y2-1]==0:
                    user2grid[acx2-1][acy2-1]=4
                    user2grid[ac2x2-1][ac2y2-1]=4
                    user2grid[ac3x2-1][ac3y2-1]=4
                    user2grid[ac4x2-1][ac4y2-1]=4
                    user2grid[ac5x2-1][ac5y2-1]=4
                    ac2check="valid"

    player2grid()
    nocheat()
#Turn time
    turn=1
    print "Player 1's Turn"
    while turn==1 or turn==2:
        if turn==1:
            print "Player 1's Turn!"
            missile="x"
            playergrid()
            playeraimgrid()
            while missile=="x":
                    missile_x=11
                    missile_y=11
                    if player2pb==0 and player2gs==0 and player2ac==0 and player2sm==0 and player2bs==0:
                        turn=3
                        break
                    missile_x=input("Enter x-coordinate of missile: ")
                    if (missile_x>0) and (missile_x<=10):
                        missile_y=input("Enter y-coordinate of missile: ")
                        if (missile_y>0) and (missile_y<=10) and useraimgrid[missile_x-1][missile_y-1]==0:
                            print "Confirming hit..."
                            time.sleep(1.5)
                            if (missile_x==pbx2 and missile_y==pby2) or (missile_x==pb2x2 and missile_y==pb2y2):
                                useraimgrid[missile_x-1][missile_y-1]=6
                                user2grid[missile_x-1][missile_y-1]=6
                                player2pb=player2pb-1
                                playeraimgrid()
                                print "Patrol Boat hit! \nFire again!"
                                if player2pb==0:
                                    print "You have sunk the enemy player's patrol boat!"
                            elif (missile_x==subx2 and missile_y==suby2) or (missile_x==sub2x2 and missile_y==sub2y2) or (missile_x==sub3x2 and missile_y==sub3y2):
                                useraimgrid[missile_x-1][missile_y-1]=6
                                user2grid[missile_x-1][missile_y-1]=6
                                player2sm=player2sm-1
                                playeraimgrid()
                                print "Submarine hit! \nFire again!"
                                if player2sm==0:
                                            print "You have sunk the enemy player's submarine!"                                                                  
                            elif (missile_x==gsx2 and missile_y==gsy2) or (missile_x==gs2x2 and missile_y==gs2y2) or (missile_x==gs3x2 and missile_y==gs3x2):  
                                useraimgrid[missile_x-1][missile_y-1]=6
                                user2grid[missile_x-1][missile_y-1]=6
                                player2gs=player2gs-1
                                playeraimgrid()
                                print "Gunship hit! \nFire again"
                                if player2gs==0:
                                    print "You have sunk the enemy player's gunship!"             
                            elif (missile_x==bsx2 and missile_y==bsy2) or (missile_x==bs2x2 and missile_y==bs2y2) or (missile_x==bs3x2 and missile_y==bs3y2) or (missile_x==bs4x2 and missile_y==bs4y2):
                                useraimgrid[missile_x-1][missile_y-1]=6
                                user2grid[missile_x-1][missile_y-1]=6
                                player2bs=player2bs-1
                                playeraimgrid()
                                print "Battleship hit! \nFire again:"
                                if player2bs==0:
                                    print "You have sunk the enemy player's battleship!"              
                            elif (missile_x==acx2 and missile_y==acy2) or (missile_x==ac2x2 and missile_y==ac2y2) or (missile_x==ac3x2 and missile_y==ac3y2) or (missile_x==ac4x2 and missile_y==ac4y2)or (missile_x==ac5x2 and missile_y==ac5y2):
                                useraimgrid[missile_x-1][missile_y-1]=6
                                user2grid[missile_x-1][missile_y-1]=6
                                player2ac=player2ac-1
                                playeraimgrid()
                                print "Aircraft Carrier hit! \nFire again"
                                if player2ac==0:
                                        print "You have sunk the enemy player's Aircraft Carrier!"
                            else:
                                missile="o"
                        else:
                              print "OUT OF RANGE - RE-ENTER COORDINATE"
                    else:
                          print "OUT OF RANGE - RE-ENTER COORDINATE"
        if turn!=3:
          print "Miss \nPlayer 2's Turn"
          useraimgrid[missile_x-1][missile_y-1]=7
          playeraimgrid()
          time.sleep(1.5)
          nocheat()
          turn=2
        elif turn==3:
          print "The Game has Ended, Player 1 is Victorious!"
          break
        
        
        missile="x"
        if turn==2:
            print "Player 2's turn!"
            player2grid()
            player2aimgrid()
            while missile=="x":
                    missile_x=11
                    missile_y=11
                    if playerpb==0 and playergs==0 and playerac==0 and playersm==0 and playerbs==0:
                        turn=4
                        break
                    missile_x=input("Enter x-coordinate of missile: ")
                    if (missile_x>0) and (missile_x<=10):
                        missile_y=input("Enter y-coordinate of missile: ")
                        if (missile_y>0) and (missile_y<=10) and user2aimgrid[missile_x-1][missile_y-1]==0:
                            print "Confirming hit..."
                            time.sleep(1.5)
                            if (missile_x==pbx and missile_y==pby) or (missile_x==pb2x and missile_y==pb2y):
                                user2aimgrid[missile_x-1][missile_y-1]=6
                                usergrid[missile_x-1][missile_y-1]=6
                                playerpb=playerpb-1
                                player2aimgrid()
                                print "Patrol Boat hit! \nFire again!"
                                if playerpb==0:
                                    print "You have sunk the enemy player's patrol boat!"
                            elif (missile_x==subx and missile_y==suby) or (missile_x==sub2x and missile_y==sub2y) or (missile_x==sub3x and missile_y==sub3y):
                                user2aimgrid[missile_x-1][missile_y-1]=6
                                usergrid[missile_x-1][missile_y-1]=6
                                playersm=playersm-1
                                player2aimgrid()
                                print "Submarine hit! \nFire again!"
                                if playersm==0:
                                    print "You have sunk the enemy player's submarine!"                                                                  
                            elif (missile_x==gsx and missile_y==gsy) or (missile_x==gs2x and missile_y==gs2y) or (missile_x==gs3x and missile_y==gs3y):  
                                user2aimgrid[missile_x-1][missile_y-1]=6
                                usergrid[missile_x-1][missile_y-1]=6
                                playergs=playergs-1
                                player2aimgrid()
                                print "Gunship hit! \nFire again"
                                if playergs==0:
                                    print "You have sunk the enemy player's gunship!"             
                            elif (missile_x==bsx and missile_y==bsy) or (missile_x==bs2x and missile_y==bs2y) or (missile_x==bs3x and missile_y==bs3y) or (missile_x==bs4x and missile_y==bs4y):
                                user2aimgrid[missile_x-1][missile_y-1]=6
                                usergrid[missile_x-1][missile_y-1]=6
                                playerbs=playerbs-1
                                player2aimgrid()
                                print "Battleship hit! \nFire again:"
                                if playerbs==0:
                                    print "You have sunk the enemy player's battleship!"              
                            elif (missile_x==acx and missile_y==acy) or (missile_x==ac2x and missile_y==ac2y) or (missile_x==ac3x and missile_y==ac3y) or (missile_x==ac4x and missile_y==ac4y)or (missile_x==ac5x and missile_y==ac5y):
                                user2aimgrid[missile_x-1][missile_y-1]=6
                                usergrid[missile_x-1][missile_y-1]=6
                                playerac=playerac-1
                                player2aimgrid()
                                print "Aircraft Carrier hit! \nFire again"
                                if playerac==0:
                                        print "You have sunk the enemy player's Aircraft Carrier!"
                            else:
                                missile="o"
                        else:
                            print "OUT OF RANGE - RE-ENTER COORDINATE"
                    else:
                        print "OUT OF RANGE - RE-ENTER COORDINATE"
        if turn!=4:
          print "Miss \nPlayer 1's Turn"
          user2aimgrid[missile_x-1][missile_y-1]=7
          player2aimgrid()
          time.sleep(1.5)
          nocheat()
          turn=1
        elif turn==4:
          print "The Game has Ended, Player 2 is Victorious!"
          break
        
elif playercount=="Singleplayer" or playercount=="singleplayer":
    cstart1x=random.randrange(9)
    cstart1y=random.randrange(9)
    cend1x=cstart1x
    cend1y=cstart1y

    shipvalidcheck1=1
    shipreselect=1

    while shipreselect==1:
        cstart1x=random.randrange(9)
        cstart1y=random.randrange(9)
        cend1x=cstart1x
        cend1y=cstart1y
        while shipvalidcheck1==1:
            direction=random.randrange(2)
            if direction==0:
                cend1x=cstart1x+1
            elif direction==1:
                cend1y=cstart1y-1
            if cend1x<=9 and cend1x>=0 and cend1y>=0 and cend1y<=9:
                shipvalidcheck1=0
                shipreselect=0
            else:
                shipreselect=1
                
    compgrid[cstart1x][cstart1y]=1
    compgrid[cend1x][cend1y]=1

    shipvalidcheck2=1
    ship2reselect=1
    spacecheck2=0


    while ship2reselect==1:
        while shipvalidcheck2==1:
            if spacecheck2==4:
                break
            cstart2x=random.randrange(8)
            cstart2y=random.randrange(8)
            if compgrid[cstart2x][cstart2y]!=0:
               shipvalidcheck2==1
            else:
                shipvalidcheck2=0
                while shipvalidcheck2==0:
                    direction=random.randrange(2)
                    if direction==1:
                        for x in range(cstart2x,cstart2x+3):
                            if x>=0 and x<=9:
                                if compgrid[x][cstart2y]==0:
                                    spacecheck2=spacecheck2+1
                        if spacecheck2==3:
                            for x in range(cstart2x,cstart2x+3):
                                compgrid[x][cstart2y]=5
                        else:
                            spacecheck2=0
                    elif direction==0:
                        for x in range(cstart2y,cstart2y+3):
                            if x>=0 and x<=9:
                                if compgrid[cstart2x][x]==0:
                                    spacecheck2=spacecheck2+1
                        if spacecheck2==3:
                            for x in range(cstart2y,cstart2y+3):
                                compgrid[cstart2x][x]=5
                        else:
                            spacecheck2=0
                    if spacecheck2==3:
                        shipvalidcheck2=2
                        ship2reselect==0
                    else:
                        shipvalidcheck2=1
        break
                        
    shipvalidcheck3=1
    ship3reselect=1
    spacecheck3=0


    while ship3reselect==1:
        while shipvalidcheck3==1:
            if spacecheck3==4:
                break
            cstart3x=random.randrange(7)
            cstart3y=random.randrange(7)
            if compgrid[cstart3x][cstart3y]!=0:
               shipvalidcheck3==1
            else:
                shipvalidcheck3=0
                while shipvalidcheck3==0:
                    direction=random.randrange(2)
                    if direction==1:
                        for x in range(cstart3x,cstart3x+4):
                            if x>=0 and x<=9:
                                if compgrid[x][cstart3y]==0:
                                    spacecheck3=spacecheck3+1
                        if spacecheck3==4:
                            for x in range(cstart3x,cstart3x+4):
                                compgrid[x][cstart3y]=3
                        else:
                            spacecheck3=0
                    elif direction==0:
                        for x in range(cstart3y,cstart3y+4):
                            if x>=0 and x<=9:
                                if compgrid[cstart3x][x]==0:
                                    spacecheck3=spacecheck3+1
                        if spacecheck3==4:
                            for x in range(cstart3y,cstart3y+4):
                                compgrid[cstart3x][x]=3
                        else:
                            spacecheck3=0
                    if spacecheck3==4:
                         break
                    else:
                            spacecheck3=0
                    if spacecheck3==4:
                        shipvalidcheck3=2
                        ship3reselect==0
                    else:
                        shipvalidcheck3=1
        break




    shipvalidcheck4=1
    ship4reselect=1
    spacecheck4=0


    while ship4reselect==1:
        while shipvalidcheck4==1:
            if spacecheck4==5:
                    break
            cstart4x=random.randrange(6)
            cstart4y=random.randrange(6)
            if compgrid[cstart4x][cstart4y]!=0:
               shipvalidcheck4==1
            else:
                shipvalidcheck4=0
                while shipvalidcheck4==0:
                    direction=random.randrange(2)
                    if direction==1:
                        for x in range(cstart4x,cstart4x+5):
                            if x>=0 and x<=9:
                                if compgrid[x][cstart4y]==0:
                                    spacecheck4=spacecheck4+1
                        if spacecheck4==5:
                            for x in range(cstart4x,cstart4x+5):
                                compgrid[x][cstart4y]=4
                        else:
                            spacecheck4=0
                    elif direction==0:
                        for x in range(cstart4y,cstart4y+5):
                            if x>=0 and x<=9:
                                if compgrid[cstart4x][x]==0:
                                    spacecheck4=spacecheck4+1
                        if spacecheck4==5:
                            for x in range(cstart4y,cstart4y+5):
                                compgrid[cstart4x][x]=4
                        else:
                            spacecheck4=0
                    if spacecheck4==5:
                        shipvalidcheck4=2
                        ship4reselect==0
                    else:
                        shipvalidcheck4=1
        if spacecheck4==5:
            break
                        

    shipvalidcheck2=1
    ship2reselect=1
    spacecheck2=0


    while ship2reselect==1:
        while shipvalidcheck2==1:
            if spacecheck2==4:
                break
            cstart2x=random.randrange(8)
            cstart2y=random.randrange(8)
            if compgrid[cstart2x][cstart2y]!=0:
               shipvalidcheck2==1
            else:
                shipvalidcheck2=0
                while shipvalidcheck2==0:
                    direction=random.randrange(2)
                    if direction==1:
                        for x in range(cstart2x,cstart2x+3):
                            if x>=0 and x<=9:
                                if compgrid[x][cstart2y]==0:
                                    spacecheck2=spacecheck2+1
                        if spacecheck2==3:
                            for x in range(cstart2x,cstart2x+3):
                                compgrid[x][cstart2y]=2
                        else:
                            spacecheck2=0
                    elif direction==0:
                        for x in range(cstart2y,cstart2y+3):
                            if x>=0 and x<=9:
                                if compgrid[cstart2x][x]==0:
                                    spacecheck2=spacecheck2+1
                        if spacecheck2==3:
                            for x in range(cstart2y,cstart2y+3):
                                compgrid[cstart2x][x]=2
                        else:
                            spacecheck2=0
                    if spacecheck2==3:
                        shipvalidcheck2=2
                        ship2reselect==0
                    else:
                        shipvalidcheck2=1
        break

    print "Enter your Ship Locations"
    print "Enter Coordinates of Starting Location of Patrol Boat"
    pbx=input("Enter y-coordinate: ")
    pby=input("Enter x-coordinate: ")
    while (pbx>10) or (pbx<1):
        print pbx, "is not on the grid. Try again!"
        pbx=input("Enter y-coordinate: ")
        pby=input("Enter x-coordinate: ")
    while (pby>10) or (pby<1):
        print pby, "is not on the grid. Try again!"
        pby=input("Enter x-coordinate: ")
    direction_pb=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
    while (direction_pb!="up") and (direction_pb!="down") and (direction_pb!="left") and (direction_pb!="right"):
        print "ERROR", direction_pb, "is not an option"
        direction_pb=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")   
    if direction_pb=="right":
        pb2y=pby+1
        pb2x=pbx
    elif direction_pb=="left":
        pb2y=pby-1
        pb2x=pbx
    elif direction_pb=="up":
        pb2x=pbx-1
        pb2y=pby
    else:
        pb2x=pbx+1
        pb2y=pby
    while (pb2x>10) or (pb2x<1) or (pb2y>10) or (pb2y<1):
        print "ERROR, the ships cannot be placed off the grid"
        direction_pb=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
        while (direction_pb!="up") and (direction_pb!="down") and (direction_pb!="left") and (direction_pb!="right"):
            print "ERROR", direction_pb, "is not an option"
            direction_pb=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")   
        if direction_pb=="right":
            pb2y=pby+1
            pb2x=pbx
        elif direction_pb=="left":
            pb2y=pby-1
            pb2x=pbx
        elif direction_pb=="up":
            pb2x=pbx-1
            pb2y=pby
        else:
            pb2x=pbx+1
            pb2y=pby

    usergrid[pbx-1][pby-1]=1
    usergrid[pb2x-1][pb2y-1]=1

    playergrid()  

    subcheck="invalid"
    while subcheck=="invalid":
            print "Enter Coordinates of Stating Location of Submarine"
            subx=input("Enter y-coordinate: ")
            while (subx>10) or (subx<1):
                print subx, "is not on the grid. Try again!"
                subx=input("Enter y-coordinate: ")
            suby=input("Enter x-coordinate: ")
            while (suby>10) or (suby<1):
                print suby, "is not on the grid. Try again!"
                suby=input("Enter x-coordinate: ")
            direction_sub=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_sub!="up") and (direction_sub!="down") and (direction_sub!="left") and (direction_sub!="right"):
                print "ERROR", direction_sub, "is not an option. Please try again"
                direction_sub=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_sub=="right":
                        sub2y=suby+1
                        sub2x=subx
                        sub3y=suby+2
                        sub3x=subx
            elif direction_sub=="left":
                sub2y=suby-1
                sub2x=subx
                sub3y=suby-2
                sub3x=subx
            elif direction_sub=="up":
                sub2x=subx-1
                sub2y=suby
                sub3x=subx-2
                sub3y=suby
            else:
                sub2x=subx+1
                sub2y=suby
                sub3x=subx+2
                sub3y=suby
            while (sub3x>10) or (sub3x<1) or (sub3y>10) or (sub3y<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_sub=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_sub!="up") and (direction_sub!="down") and (direction_sub!="left") and (direction_sub!="right"):
                print "ERROR", direction_sub, "is not an option. Please try again"
                directin_sub=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_sub=="right":
                    sub2y=suby+1
                    sub2x=subx
                    sub3y=suby+2
                    sub3x=subx
                elif direction_sub=="left":
                    sub2y=suby-1
                    sub2x=subx
                    sub3y=suby-2
                    sub3x=subx
                elif direction_sub=="up":
                    sub2x=subx-1
                    sub2y=suby
                    sub3x=subx-2
                    sub3y=suby
                else:
                    sub2x=subx+1
                    sub2y=suby
                    sub3x=subx+2
                    sub3y=suby
            if usergrid[subx-1][suby-1]!=0 or usergrid[sub2x-1][sub2y-1]!=0 or usergrid[sub3x-1][sub3y-1]!=0:
                    print "ERROR"
                    print "Select again"
                    subcheck="invalid"
            elif usergrid[subx-1][suby-1]==0 or usergrid[sub2x-1][sub2y-1]==0 or usergrid[sub3x-1][sub3y-1]==0:
                    usergrid[subx-1][suby-1]=2
                    usergrid[sub2x-1][sub2y-1]=2
                    usergrid[sub3x-1][sub3y-1]=2
                    subcheck="valid"

    playergrid()

    gscheck="invalid"
    while gscheck=="invalid":
            print "Enter Coordinates of Stating Location of Gunship"
            gsx=input("Enter y-coordinate: ")
            while (gsx>10) or (gsx<1):
                print gsx, "is not on the grid. Try again!"
                gsx=input("Enter y-coordinate: ")
            gsy=input("Enter x-coordinate: ")
            while (gsy>10) or (gsy<1):
                print gsy, "is not on the grid. Try again!"
                gsy=input("Enter x-coordinate: ")
            direction_gs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_gs!="up") and (direction_gs!="down") and (direction_gs!="left") and (direction_gs!="right"):
                print "ERROR", direction_gs, "is not an option. Please try again"
                direction_gs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_gs=="right":
                gs2y=gsy+1
                gs2x=gsx
                gs3y=gsy+2
                gs3x=gsx
            elif direction_gs=="left":
                gs2y=gsy-1
                gs2x=gsx
                gs3y=gsy-2
                gs3x=gsx
            elif direction_gs=="up":
                gs2x=gsx-1
                gs2y=gsy
                gs3x=gsx-2
                gs3y=gsy
            else:
                gs2x=gsx+1
                gs2y=gsy
                gs3x=gsx+2
                gs3y=gsy
            while (gs3x>10) or (gs3x<1) or (gs3y>10) or (gs3y<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_gs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_gs=="right":
                    gs2y=gsy+1
                    gs2x=gsx
                    gs3y=gsy+2
                    gs3x=gsx
                elif direction_gs=="left":
                    gs2y=gsy-1
                    gs2x=gsx
                    gs3y=gsy-2
                    gs3x=gsx
                elif direction_gs=="up":
                    gs2x=gsx-1
                    gs2y=gsy
                    gs3x=gsx-2
                    gs3y=gsy
                else:
                    gs2x=gsx+1
                    gs2y=gsy
                    gs3x=gsx+2
                    gs3y=gsy

            if usergrid[gsx-1][gsy-1]!=0 or usergrid[gs2x-1][gs2y-1]!=0 or usergrid[gs3x-1][gs3y-1]!=0:
                    print "ERROR"
                    print "Select again"
                    gscheck="invalid"
            elif usergrid[gsx-1][gsy-1]==0 or usergrid[gs2x-1][gs2y-1]==0 or usergrid[gs3x-1][gs3y-1]==0:
                    usergrid[gsx-1][gsy-1]=5
                    usergrid[gs2x-1][gs2y-1]=5
                    usergrid[gs3x-1][gs3y-1]=5
                    gscheck="valid"

    playergrid()


    bscheck="invalid"
    while bscheck=="invalid":
            print "Enter Coordinates of Stating Location of Battleship"
            bsx=input("Enter y-coordinate: ")
            while (bsx>10) or (bsx<1):
                print bsx, "is not on the grid. Try again!"
                bsx=input("Enter y-coordinate: ")
            bsy=input("Enter x-coordinate: ")
            while (bsy>10) or (bsy<1):
                print bsy, "is not on the grid. Try again!"
                bsy=input("Enter x-coordinate: ")
            direction_bs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_bs!="up") and (direction_bs!="down") and (direction_bs!="left") and (direction_bs!="right"):
                print "ERROR", direction_bs, "is not an option. Please try again"
                direction_bs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_bs=="right":
                bs2y=bsy+1
                bs2x=bsx
                bs3y=bsy+2
                bs3x=bsx
                bs4y=bsy+3
                bs4x=bsx
            elif direction_bs=="left":
                bs2y=bsy-1
                bs2x=bsx
                bs3y=bsy-2
                bs3x=bsx
                bs4y=bsy-3
                bs4x=bsx
            elif direction_bs=="up":
                bs2x=bsx-1
                bs2y=bsy
                bs3x=bsx-2
                bs3y=bsy
                bs4x=bsx-3
                bs4y=bsy
            else:
                bs2x=bsx+1
                bs2y=bsy
                bs3x=bsx+2
                bs3y=bsy
                bs4x=bsx+3
                bs4y=bsy
            while (bs4x>10) or (bs4x<1) or (bs4y>10) or (bs4y<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_bs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_bs=="right":
                    bs2y=bsy+1
                    bs2x=bsx
                    bs3y=bsy+2
                    bs3x=bsx
                    bs4y=bsy+3
                    bs4x=bsx
                elif direction_bs=="left":
                    bs2y=bsy-1
                    bs2x=bsx
                    bs3y=bsy-2
                    bs3x=bsx
                    bs4y=bsy-3
                    bs4x=bsx
                elif direction_bs=="up":
                    bs2x=bsx-1
                    bs2y=bsy
                    bs3x=bsx-2
                    bs3y=bsy
                    bs4x=bsx-3
                    bs4y=bsy
                else:
                    bs2x=bsx+1
                    bs2y=bsy
                    bs3x=bsx+2
                    bs3y=bsy
                    bs4x=bsx+3
                    bs4y=bsy
            if usergrid[bsx-1][bsy-1]!=0 or usergrid[bs2x-1][bs2y-1]!=0 or usergrid[bs3x-1][bs3y-1]!=0 or usergrid[bs4x-1][bs4x-1]!=0:
                    print "ERROR"
                    print "Select again"
                    bscheck="invalid"
            elif usergrid[bsx-1][bsy-1]==0 and usergrid[bs2x-1][bs2y-1]==0 and usergrid[bs3x-1][bs3y-1]==0 and usergrid[bs4x-1][bs4x-1]==0:
                    usergrid[bsx-1][bsy-1]=3
                    usergrid[bs2x-1][bs2y-1]=3
                    usergrid[bs3x-1][bs3y-1]=3
                    usergrid[bs4x-1][bs4y-1]=3
                    bscheck="valid"

    playergrid()

    accheck="invalid"
    while accheck=="invalid":
            print "Enter Coordinates of Starting Location of Aircraft Carrier"
            acx=input("Enter y-coordinate: ")
            while (acx>10) or (acx<1):
                print acx, "is not on the grid. Try again!"
                acx=input("Enter y-coordinate: ")
            acy=input("Enter x-coordinate: ")
            while (acy>10) or (acy<1):
                print acy, "is not on the grid. Try again!"
                acy=input("Enter x-coordinate: ")
            direction_ac=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            while (direction_ac!="up") and (direction_ac!="down") and (direction_ac!="left") and (direction_ac!="right"):
                print "ERROR", direction_ac, "is not an option. Please try again"
                direction_ac=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
            if direction_ac=="right":
                ac2y=acy+1
                ac2x=acx
                ac3y=acy+2
                ac3x=acx
                ac4y=acy+3
                ac4x=acx
                ac5y=acy+4
                ac5x=acx
            elif direction_ac=="left":
                ac2y=acy-1
                ac2x=acx
                ac3y=acy-2
                ac3x=acx
                ac4y=acy-3
                ac4x=acx
                ac5y=acy-4
                ac5x=acx
            elif direction_ac=="up":
                ac2x=acx-1
                ac2y=acy
                ac3x=acx-2
                ac3y=acy
                ac4x=acx-3
                ac4y=acy
                ac5x=acx-4
                ac5y=acy
            else:
                ac2x=acx+1
                ac2y=acy
                ac3x=acx+2
                ac3y=acy
                ac4x=acx+3
                ac4y=acy
                ac5x=acx+4
                ac5y=acy
            if (ac5x>10) or (ac5x<1) or (ac5y>10) or (ac5y<1):
                print "ERROR, the ships cannot be placed off the grid"
                direction_bs=raw_input("Choose an orientation that will fit the ship on the grid with the options: up, down, left, or right\n")
                if direction_ac=="right":
                    ac2y=acy+1
                    ac2x=acx
                    ac3y=acy+2
                    ac3x=acx
                    ac4y=acy+3
                    ac4x=acx
                    ac5y=acy+4
                    ac5x=acx
                elif direction_ac=="left":
                    ac2y=acy-1
                    ac2x=acx
                    ac3y=acy-2
                    ac3x=acx
                    ac4y=acy-3
                    ac4x=acx
                    ac5y=acy-4
                    ac5x=acx
                elif direction_ac=="up":
                    ac2x=acx-1
                    ac2y=acy
                    ac3x=acx-2
                    ac3y=acy
                    ac4x=acx-3
                    ac4y=acy
                    ac5x=acx-4
                    ac5y=acy
                else:
                    ac2x=acx+1
                    ac2y=acy
                    ac3x=acx+2
                    ac3y=acy
                    ac4x=acx+3
                    ac4y=acy
                    ac5x=acx+4
                    ac5y=acy   
            if usergrid[acx-1][acy-1]!=0 or usergrid[ac2x-1][ac2y-1]!=0 or usergrid[ac3x-1][ac3y-1]!=0 or usergrid[ac4x-1][ac4y-1]!=0 or usergrid[ac5x-1][ac5y-1]!=0:
                    print "ERROR"
                    print "Select again"
                    accheck="invalid"
            elif usergrid[acx-1][acy-1]==0 and usergrid[ac2x-1][ac2y-1]==0 and usergrid[ac3x-1][ac3y-1]==0 and usergrid[ac4x-1][ac4y-1]==0 and usergrid[ac5x-1][ac5y-1]==0:
                    usergrid[acx-1][acy-1]=4
                    usergrid[ac2x-1][ac2y-1]=4
                    usergrid[ac3x-1][ac3y-1]=4
                    usergrid[ac4x-1][ac4y-1]=4
                    usergrid[ac5x-1][ac5y-1]=4
                    accheck="valid"

    playergrid()


    
    turn=1
    while turn==1 or turn==2:
        if turn==1:
            print "Player 1's Turn!"
            missile="x"
            playergrid()
            playeraimgrid()
            while missile=="x":
                    missile_x=11
                    missile_y=11
                    if comppb==0 and compgs==0 and compac==0 and compsm==0 and compbs==0:
                        turn=3
                        break
                    missile_x=input("Enter x-coordinate of missile: ")
                    if (missile_x>0) and (missile_x<=10):
                        missile_y=input("Enter y-coordinate of missile: ")
                        if (missile_y>0) and (missile_y<=10) and useraimgrid[missile_y-1][missile_x-1]==0:
                            print "Confirming hit..."
                            time.sleep(1.5)
                            if compgrid[missile_y-1][missile_x-1]==1:
                                useraimgrid[missile_y-1][missile_x-1]=6
                                comppb=comppb-1
                                playeraimgrid()
                                print "Patrol Boat hit! \nFire again!"
                                if comppb==0:
                                    print "You have sunk the computer's patrol boat!"
                            elif compgrid[missile_y-1][missile_x-1]==2:
                                useraimgrid[missile_y-1][missile_x-1]=6
                                compsm=compsm-1
                                playeraimgrid()
                                print "Submarine hit! \nFire again!"
                                if compsm==0:
                                            print "You have sunk the computer's submarine!"                                                                  
                            elif compgrid[missile_y-1][missile_x-1]==5:
                                useraimgrid[missile_y-1][missile_x-1]=6
                                compgs=compgs-1
                                playeraimgrid()
                                print "Gunship hit! \nFire again"
                                if compgs==0:
                                    print "You have sunk the computer's gunship!"             
                            elif compgrid[missile_y-1][missile_x-1]==3:
                                useraimgrid[missile_y-1][missile_x-1]=6
                                compbs=compbs-1
                                playeraimgrid()
                                print "Battleship hit! \nFire again:"
                                if compbs==0:
                                    print "You have sunk the computer's battleship!"              
                            elif compgrid[missile_y-1][missile_x-1]:
                                useraimgrid[missile_y-1][missile_x-1]=6
                                compac=compac-1
                                playeraimgrid()
                                print "Aircraft Carrier hit! \nFire again"
                                if compac==0:
                                        print "You have sunk the computer's Aircraft Carrier!"
                            else:
                                missile="o"
                        else:
                              print "OUT OF RANGE - RE-ENTER COORDINATE"
                    else:
                          print "OUT OF RANGE - RE-ENTER COORDINATE"
        if turn!=3:
          print "Miss \nComputer's Turn"
          useraimgrid[missile_y-1][missile_x-1]=7
          playeraimgrid()
          time.sleep(1.5)
          turn=2
        elif turn==3:
          print "The Game has Ended, You are Victorious!"
          break

        if turn==2: 
            compshot="aiming"
            hitcheck="miss"             
            while compshot=="aiming":
                if playerpb==0 and playergs==0 and playerbs==0 and playerac==0 and playersm==0:
                    turn=4
                    break
                if hitcheck=="hit":
                    if compaimx>1 and compaimx<10:
                        compaimx=random.randrange(compaimx-1,compaimx+2)
                    elif compaimx==1:
                        compaimx=random.randrange(compaimx,compaimx+2)
                    elif compaimx==10:
                        compaimx=random.randrange(compaimx-1,compaimx+1)
                    if compaimy>1 and compaimy<10:
                        compaimy=random.randrange(compaimy-1,compaimy+2)
                    elif compaimy==1:
                        compaimy=random.randrange(compaimy,compaimy+1)
                    elif  compaimy==10:
                        compaimy=random.randrange(compaimy-1,compaimy+1)        
                elif hitcheck=="miss":
                    compaimx=random.randrange(10)+1
                    compaimy=random.randrange(10)+1
                if usergrid[compaimy-1][compaimx-1]==1 or usergrid[compaimy-1][compaimx-1]==2 or usergrid[compaimy-1][compaimx-1]==3 or usergrid[compaimy-1][compaimx-1]==4 or usergrid[compaimy-1][compaimx-1]==5:
                    hitcheck="hit"
                    if usergrid[compaimy-1][compaimx-1]==1:
                        userpb=userpb-1
                        print "The computer has successfully hit your patrol boat at (", compaimx, ",", compaimy, ")!"
                        if userpb==0:
                            print "The computer has sunk your patrol boat!"
                    elif usergrid[compaimy-1][compaimx-1]==2:
                        usersm=usersm-1
                        print "The computer has successfully hit your submarine at (", compaimx, ",", compaimy, ")!"
                        if usersm==0:
                            print "The computer has sunk your submarine!"
                    elif usergrid[compaimy-1][compaimx-1]==3:
                        userbs=userbs-1
                        print "The computer has successfully hit your battleship at (", compaimx, ",", compaimy, ")!"
                        if userbs==0:
                            print "The computer has sunk your battleship!"
                    elif usergrid[compaimy-1][compaimx-1]==4:
                        userac=userac-1
                        print "The computer has successfully hit your aircraft carrier at (", compaimx, ",", compaimy, ")!"
                        if userac==0:
                            print "The computer has sunk your aircraft carrier!"
                    elif usergrid[compaimy-1][compaimx-1]==5:
                        usergs=usergs-1
                        print "The computer has successfully hit your gunship at (", compaimx, ",", compaimy, ")!"
                        if usergs==0:
                            print "The computer has sunk your gunship!"
                    usergrid[compaimy-1][compaimx-1]=6
                elif usergrid[compaimy-1][compaimx-1]==0 and userpseudogrid[compaimy-1][compaimx-1]==0:
                     hitcheck="miss"
                     compshot="notaiming"
                     userpseudogrid[compaimy-1][compaimx-1]==7
                     print "The computer has missed its shot at (", compaimx, ",", compaimy, ")"
                     turn=1
                elif usergrid[compaimy-1][compaimx-1]==6 or userpseudogrid[compaimy-1][compaimx-1]==7:
                    compshot="aiming"
            if turn==4:
                print "You have lost! The Computer has sank all of your ships!"
                break
            turn=1

