class hotelmanage:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',address='',cindate='',coutdate='',rno=1):

        print ("\n\n*****WELCOME TO HOTEl MANIKA AUBERGE*****\n")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s

        self.a=a

        self.name=name

        self.address=address

        self.cindate=cindate

        self.coutdate=coutdate

        self.rno=rno

    def inputdata(self):

        self.name=input("\nEnter your Fullname:")

        self.address=input("\nEnter your address:")

        self.cindate=input("\nEnter your check in date:")

        self.coutdate=input("\nEnter your checkout date:")

        print("Your room no.:",self.rno,"\n")

       

    def roomrent(self):#sel1353

        deluxeprice=11000

        executiveprice=13000

        studioprice=16000

        buisnessprice=20000

        sauna=1500

        breakfast=3000

        print('Select 1 for Deluxe room') #preferred for solo travellers

        print('Select 2 for Executive Launge')#preferred for family

        print('Select 3 for Studio rooms')#preferred for content creaters

        print('Select 4 for Buisness Suite')#preferred for buisness class

        roomprice=0

        roomtype=int(input('Please select the preferred room type:'))

        if roomtype==1:

            print('Your choice was Deluxe Room')

            print('The amenities provided')

            print('City view, Seperate Shower/Bathtub,1 king Bed, Free Wifi')

            norooms=int(input('Enter the no. of rooms required:'))

            print('Select the futher services if required')

            print('select 101 for Sauna')

            print('Select 102 for breakfast inclusion')

            print('select 000 for none of these')

            extraser=[int(x) for x in input().split()]

            if 101 and 102 in extraser:

                roomprice=(deluxeprice+roomprice+sauna+breakfast)*norooms

            elif 101 in extraser:

                roomprice=(deluxeprice+roomprice+sauna)*norooms

            elif 102 in extraser:

                roomprice=(deluxeprice+roomprice+breakfast)*norooms

            else:

                roomprice=deluxeprice*norooms

            print('The projected price is:',roomprice)

        if roomtype==2:

            print('Ypur choice was executive launge')

            print('The amenities provided')

            print('City view, Shower& Bathtub,1 king Bed or 2 single beds, Free Wifi')

            norooms=int(input('Enter the no. of rooms required:'))

            print('Select the futher services if required')

            print('select 101 for Sauna')

            print('Select 102 for breakfast inclusion')

            print('select 000 for none of these')

            extraser=[int(x) for x in input().split()]

            if 101 and 102 in extraser:

                roomprice=(executiveprice+roomprice+sauna+breakfast)*norooms

            elif 101 in extraser:

                roomprice=(executiveprice+roomprice+sauna)*norooms

            elif 102 in extraser:

                roomprice=(executiveprice+roomprice+breakfast)*norooms

            else:

                roomprice=executiveprice*norooms

            print('The projected price is:',roomprice)

        if roomtype==3:

            print('Your choice is Studio Rooms')

            print('The amenities provided')

            print('Outdoor view, Seperate Shower/Bathtub,1 king Bed, Free Wifi,sound proof walls')

            norooms=int(input('Enter the no. of rooms required:'))

            print('Select the futher services if required')

            print('select 101 for Sauna')

            print('Select 102 for breakfast inclusion')

            print('select 000 for none of these')

            extraser=[int(x) for x in input().split()]

            if 101 and 102 in extraser:

                roomprice=(studioprice+roomprice+sauna+breakfast)*norooms

            elif 101 in extraser:

                roomprice=(studioprice+roomprice+sauna)*norooms

            elif 102 in extraser:

                roomprice=(studioprice+roomprice+breakfast)*norooms

            else:

                roomprice=studioprice*norooms

            print('The projected price is:',roomprice)

        if roomtype==4:

            print('Your choice was Buisness suite')

            print('The amenities provided')

            print('City view, Seperate Shower/Bathtub,1 king Bed, Free Wifi,conference room')

            norooms=int(input('Enter the no. of rooms required:'))

            print('Select the futher services if required')

            print('select 101 for Sauna')

            print('Select 102 for breakfast inclusion')

            print('select 000 for none of these')

            extraser=[int(x) for x in input().split()]

            if 101 and 102 in extraser:

                roomprice=(buisnessprice+roomprice+sauna+breakfast)*norooms

            elif 101 in extraser:

                roomprice=(buisnessprice+roomprice+sauna)*norooms

            elif 102 in extraser:

                roomprice=(buisnessprice+roomprice+breakfast)*norooms

            else:

                roomprice=buisnessprice*norooms

            print('The projected price is:',roomprice)

           

                

    def foodpurchased(self):

        f=0

        r=0

        for i in range(1):

       

            f=1

            print("-------------------------------------------------------------------------")

            print("                           Hotel The Manika ")

            print("-------------------------------------------------------------------------")

            print("                            Menu Card")

            print("-------------------------------------------------------------------------")

            print("\n BEVARAGES                              26 Dal Fry................ 140.00")

            print("----------------------------------      27 Dal Makhani............ 150.00")

            print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00")

            print(" 2  Masala Tea.............. 25.00")

            print(" 3  Coffee.................. 25.00      ROTI")

            print(" 4  Cold Drink.............. 25.00     ----------------------------------")

            print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00")

            print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00")

            print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00")

            print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00")

            print(" 9  Cheese Toast Sandwich... 70.00")

            print(" 10 Grilled Sandwich........ 70.00      RICE")

            print("                                       ----------------------------------")

            print(" SOUPS                                  33 Plain Rice.............. 90.00")

            print("----------------------------------      34 Jeera Rice.............. 90.00")

            print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00")

            print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00")

            print(" 13 Veg. Noodle Soup....... 110.00")

            print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN")

            print(" 15 Veg. Munchow........... 110.00     ----------------------------------")

            print("                                        37 Plain Dosa............. 100.00")

            print(" MAIN COURSE                            38 Onion Dosa............. 110.00")

            print("----------------------------------      39 Masala Dosa............ 130.00")

            print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00")

            print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00")

            print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00")

            print(" 19 Palak Paneer........... 120.00")

            print(" 20 Chilli Paneer.......... 140.00      ICE CREAM")

            print(" 21 Matar Mushroom......... 140.00     ----------------------------------")

            print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00")

            print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00")

            print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00")

            print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")

            print("Press 0 -to end ")

            ch=1

            while(ch!=0):

                

                ch=int(input(" select your food no: "))

           

                if ch==1 or ch==31 or ch==32:

                    rs=20

                    r=r+rs

                elif ch<=4 and ch>=2:

                    rs=25

                    r=r+rs

                elif ch<=6 and ch>=5:

                    rs=30

                    r=r+rs

                elif ch<=8 and ch>=7:

                    rs=50

                    r=r+rs

                elif ch<=10 and ch>=9:

                    rs=70

                    r=r+rs

                elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:

                    rs=110

                    r=r+rs

                elif ch<=19 and ch>=18:

                    rs=120

                    r=r+rs

                elif (ch<=26 and ch>=20) or ch==42:

                    rs=140

                    r=r+rs

                elif ch<=28 and ch>=27:

                    rs=150

                    r=r+rs

                elif ch<=30 and ch>=29:

                    rs=15

                    r=r+rs

                elif ch==33 or ch==34:

                    rs=90

                    r=r+rs

                elif ch==37:

                    rs=100

                    r=r+rs

                elif ch<=41 and ch>=39:

                    rs=130

                    r=r+rs

                elif ch<=46 and ch>=43:

                    rs=60

                    r=r+rs

                elif ch==0:

                    pass

                else:

                    print("Wrong Choice..!!")

            print("Total Bill: ",r)

 

       

    def display(self):

        print ("******HOTEL BILL******")

        print ("Customer details:")

        print ("Customer name:",self.name)

        print ("Customer address:",self.address)

        print ("Check in date:",self.cindate)

        print ("Check out date",self.coutdate)

        print ("Room no.",self.rno)

        print ("Your Room rent is:",self.s)

        print ("Your Food bill is:",self.r)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total Purchased is:",self.rt)

        print ("Additional Service Charges is",self.a)

        print ("Your grandtotal Purchased is:",self.rt+self.a,"\n")

        self.rno+=self.rno

def main():

    a=hotelmanage()

    while (1):

        print("1.Enter Customer Data")

        print("2.Calculate Room Rent")

        print("3.Calculate Food Purchased")

        print("4.Show total cost")

        print("5.EXIT")

        b=int(input("\nEnter the number of your choice:"))

        if (b==1):

            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.foodpurchased()

        if (b==4):

            a.display()

        if (b==5):

            quit()

main()
