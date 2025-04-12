from MultiComplex import calprofit
import datetime
today=datetime.date.today().strftime("%Y-%m-%d")
time=datetime.datetime.now().strftime("%H:%M:%S")
def tillsellamount(f,n,h):
    with open(f,"r") as fe:
        fl=fe.readlines()
    with open(f,"a") as fe:
        for i in fl:
            fy=i.split("-")
        n=n+int(fy[3])
        fe.write(str(today)+"-"+str(n)+"\n")
    if(h==1):
        print("-"*80)
        print("Rs.",n)
        print("-"*80)
def updatestock(x,a,b):
    q=0
    f=open(x,"r")
    p=f.readlines()
    f.close()
    f=open(x,"w")
    f.close()
    f=open(x,"a")
    for i in p:
        y=i.strip().split("\t")
        if q==b:
            y[3]=str(int(y[3])-a)
            for n in range(6):
                if n==5:
                    f.write(str(y[n])+"\n")
                    q=q+1
                else:
                    f.write(str(y[n])+"\t")
        else:
            q=q+1  
            for n in range(6):
                if n==5:
                    f.write(str(y[n])+"\n")
                else:
                    f.write(str(y[n]+"\t"))
    f.close()
def update_worker(f):
    display_worker(f)
    with open(f,"r") as fe:
        r=fe.readlines()
    n=int(input("if you want to add worker enter 1 and to delete any worker enter any integer value other than 1"))
    if(n==1):
        with open(f,"a") as fa:
            m=int(input("Enter how many workers do you want to enter"))
            for i in range(m):
                a=input("Enter S.No.")
                b=input("Enter Worker Name:")
                c=input("Enter Worker Age:")
                fa.write(a+"\t"+b+"\t"+c)     
    else:
        fl=open(f,"w")
        fl.close()
        with open(f,"a") as fl:
            m=input("Enter Worker Name:")
            for i in r:
                g=i.split("\t")
                if(g[1]==m):
                    continue
                fl.write(g[0]+"\t"+g[1]+"\t"+g[2])
    print("Worker List Updated")
    display_worker(f)
def update_price(f):
    display(f)
    with open(f,"r") as fe:
        r=fe.readlines()
    q=input("Enter the Product Name")
    n=int(input("Enter the new price"))
    with open(f,"w") as fe:
        fe.close()
    with open(f,"a") as fe:
        for i in r:
            s=i.split("\t")
            if(q==s[2]):
                fe.write(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+str(n)+"\t"+s[5])
            else:
                fe.write(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5])
    print("Product Price Updated")
    display(f)
def update_stock(f):
    display(f)
    n=int(input("if you want to increase stock enter 1 and if you want to decrease stock enter 2 and any other integer value for remaining stock same"))
    q=input("Enter the Product Name")
    if(n==1):
        l=int(input("Enter the amount of new Stock come"))
    elif(n==2):
        p=int(input("Enter the amount of Stock reduce"))
    with open(f,"r") as fe:
        r=fe.readlines()
    with open(f,"w") as fe:
        fe.close()
    with open(f,"a") as fe:
        for i in r:
            s=i.split("\t")
            b=int(s[3])
            if(n==1):
                a=b+l
                if(q==s[2]):
                    fe.write(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+str(a)+"\t"+s[4]+"\t"+s[5])
                else:
                    fe.write(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5])
            elif(n==2):
                a=b-p
                if(q==s[2]):
                    fe.write(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+str(a)+"\t"+s[4]+"\t"+s[5])
                else:
                    fe.write(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5])
            else:
                fe.write(s[0]+"\t"+s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5])
    print("Product Stock Updated")
    display(f)
def update_product(f):
    display(f)
    with open(f,"r") as fe:
        r=fe.readlines()
    n=int(input("if you want to add product enter 1 and to delete product enter any integer value other than 1"))
    if(n==1):
        with open(f,"a") as fa:
            m=int(input("Enter how many products do you want to enter"))
            for i in range(m):
                a=input("Enter S.No.")
                b=input("Enter Brand Name")
                c=input("Enter Product Name")
                d=input("Enter no. of Quantity")
                e=input("Enter no. of Prices")
                g=input("Enter features")
                fa.write(a+"\t"+b+"\t"+c+"\t"+d+"\t"+e+"\t"+g)
    else:
        fl=open(f,"w")
        fl.close()
        with open(f,"a") as fl:
            m=input("Enter Product Name")
            for i in r:
                g=i.split("\t")
                if(g[2]==m):
                    continue
                fl.write(g[0]+"\t"+g[1]+"\t"+g[2]+"\t"+g[3]+"\t"+g[4]+"\t"+g[5])
    print("Product Updated")
    display(f)
def display(f):
    print("-"*80)
    print("It is in sequence from left to right")
    print("S.No. BrandName ProductName Quantity Price Features")
    with open(f,"r") as fe:
        for i in fe:
            print(i)
    print("-"*80)
def display_worker(f):
    print("-"*80)
    print("It is in sequence from left to right")
    print("S.No. WorkerName Age")
    with open(f,"r") as fe:
        for i in fe:
            print(i)
    print("-"*80)
def displays(f):
    print("-"*80)
    with open(f,"r") as fe:
        for i in fe:
            print(i)
    print("-"*80)
def menu(f):
    display(f)
    with open(f,"r") as fl:
        r=fl.readlines()
        k=len(r)
        print(k)
        sum=0
        while(True):
            q=0
            print("enter the number shown in menu u want to add else to confirm 0")
            x=int(input())
            if(0<x<=k):
                for i in r:
                    g=i.split("\t")
                    if(q==x-1):
                        y=int(input("enter quantity"))
                        if(y>=0):
                            if(y<=int(g[3])):
                                sum=sum+(int(g[4]))*y
                                updatestock(f,y,x-1)
                            else:
                                print("Current Amount of Stock is not available")
                                break
                        else:
                            print("Invalid Stock Amount")
                            break
                    q=q+1
                if(x==0):
                    print("-"*80)
                    print("Your Total Bill is=Rs.",sum)
                    print("-"*80)
                    q=0
                    tillsellamount("display.txt",sum,q)
                    break
            else:
                print("Invalid Choice")
                print("-"*80)
                print("Your Total Bill is=Rs.",sum)
                print("-"*80)
                break
print("\t\t\t\t\t\t\tWelcome to Goyal Multi-Complex\t\t\t\t\t\t")
while(True):
    n=int(input("Enter your choice\n1. You for USER\n2. You are Owner\n3. Exit"))
    if n==1:
        c=0
        a=0
        while(True):
            if(c==1):
                break
            qw=int(input("Enter your choice\n1. for Login\n2. for Signup\n3.Go back to previous menu\n4.Exit"))
            if(qw==1):
                name=input("Enter your name")
                phonenumber=input("Enter your Phone number")
                w=open("userdetails.txt","r")
                fe=w.readlines()
                w.close()
                for i in fe:
                    fl=i.strip().split("\t")
                    if(fl[0] == name and fl[1] == phonenumber):
                        print("Login Successfull")
                        c=1
                        break
                if(c==0):
                    print("User not found, please signup.")
                    print("SignUp")
                    w=open("userdetails.txt","a")
                    name=input("Enter your name")
                    while(True):
                        phonenumber=input("Enter your Phone number")
                        e=len(phonenumber)
                        if(e==10):
                            for i in phonenumber:
                                if(0<=int(i)<=9):
                                    a=a+1
                            if(a==10):
                                w.write(name+"\t"+str(phonenumber)+"\n")
                                c=1
                                break
                            else:
                                print("Invalid Phone Number")
                        else:
                            print("Invalid Phone Number")
                    w.close()
            elif(qw==2):
                z=0
                print("SignUp")
                a=open("userdetails.txt","a")
                name=input("Enter your name")
                while(True):
                    phonenumber=input("Enter your Phone number")
                    e=len(phonenumber)
                    if(e==10):
                        for i in phonenumber:
                            if(0<=int(i)<=9):
                                z=z+1
                        if(z==10):
                            a.write(name+"\t"+str(phonenumber)+"\n")
                            c=1
                            break
                        else:
                            print("Invalid Phone Number")
                    else:
                        print("Invalid Phone Number")
                a.close()
            elif(qw==3):
                break
            else:
                print("Invalid Choice")
                exit()
        if(c==1):
            print(today+"\t\t\t\t\t\t\t\t\t"+time)
            print("Welcome {} Sir".format(name))
            while(True):
                ch=int(input("Enter your choice\n1. you want to buy something\n2. you want to complain of any product you purchase or against any worker or against owner\n3. Product is\
 defective and in guarantee period\n4. you want to exit"))
                match ch:
                    case 1:
                        while(True):
                            l=int(input("Enter your choice what you want to buy\n1. Electric Appliances\n2. Clothes\n3. Shoe store\n4. Watches\n5. Beauty Products\n6. Stationary\
 Products\n7. Go back to previous Menu\n8. Exit"))
                            match l:
                                case 1:
                                    while(True):
                                        ip=int(input("Enter your choice\n1. Bulbes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. Go back to previous menu\n6. Exit"))
                                        match ip:
                                            case 1:
                                                menu("bulb.txt")
                                            case 2:
                                                menu("laptop.txt")
                                            case 3:
                                                menu("phone.txt")
                                            case 4:
                                                menu("iron.txt")
                                            case 5:
                                                break
                                            case 6:
                                                q=open("comment.txt","a")
                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                q.close()
                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 2:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Clothes\n2. Go back to previous menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                menu("cloth.txt")
                                            case 2:
                                                break
                                            case 3:
                                                q=open("comment.txt","a")
                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                q.close()
                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 3:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Shoes\n2. Go back to previous menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                menu("shoe.txt")
                                            case 2:
                                                break
                                            case 3:
                                                q=open("comment.txt","a")
                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                q.close()
                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 4:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Watches\n2. Go back to previous menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                menu("watch.txt")
                                            case 2:
                                                break
                                            case 3:
                                                q=open("comment.txt","a")
                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                q.close()
                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 5:
                                    while(True):
                                        iu=int(input("Enter your choice\n1.Costmetic products\n2. Go back to previous menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                menu("beautyproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                q=open("comment.txt","a")
                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                q.close()
                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 6:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Stationary products\n2. Go back to previous menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                menu("stationaryproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                q=open("comment.txt","a")
                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                q.close()
                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 7:
                                    break
                                case 8:
                                    q=open("comment.txt","a")
                                    k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                    ra=input("rate (---/5) our Goyal Super-Market")
                                    q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                    q.close()
                                    print("ThankYou For Visiting Our Goyal Multi-Complex")
                                    exit()
                                case _:
                                    print("Invalid Choice")
                    case 2:
                        while(True):
                            cm=int(input("Enter your choice\n1. You want to complain against any product\n2. You want to complain against any worker\n3. You want to complain against owner\n\
4. You want to go back to previous menu\n5. Exit"))
                            if(cm==1):
                                fe=open("complain.txt","a")
                                pr=input("Enter Product name")
                                cp=input("Enter the complain")
                                print(name,phonenumber)
                                vr=int(input("Verify you name and phonenumber if your name and phonenumber is correct enter 1 and if your name or phonenumber is wrong enter 2"))
                                if(vr==1):
                                    fe.write(name+"\t"+phonenumber+"\t"+pr+"\t"+cp+"\n")
                                    print("We have registered your complain\nSorry for this next time we will make ensure this thing never happen\nWe will contact you as soon as possible")
                                elif(vr==2):
                                    name=input("Enter your name")
                                    phonenumber=("Enter your phonenumber")
                                    fe.write(name+"\t"+phonenumber+"\t"+pr+"\t"+cp+"\n")
                                    print("We have registered your complain\nSorry for this next time we will make ensure this thing never happen\nWe will contact you as soon as possible")
                                else:
                                    print("You have entered wrong choice")
                                fe.close()
                            elif(cm==2):
                                fl=open("complain.txt","a")
                                wr=input("Enter Worker name")
                                cpn=input("Enter the complain")
                                fl.write(wr+"\t"+cpn+"\n")
                                print("Sorry for this next time we will make ensure this thing never happen")
                                fl.close()
                            elif(cm==3):
                                fd=open("complain.txt","a")
                                pd="Owner"
                                cd=input("Enter the complain")
                                fd.write(pd+"\t"+cd+"\n")
                                print("Sorry for this next time we will make ensure this thing never happen")
                                fd.close()
                            elif(cm==4):
                                break
                            elif(cm==5):
                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                ra=input("rate (---/5) our Goyal Super-Market")
                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                q.close()
                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                exit()
                            else:
                                print("Invalid choice")
                                break
                    case 3:
                        fp=open("guarantee.txt","a")
                        pp=input("Enter Product name")
                        rr=input("What defect is coming in product")
                        print(name,phonenumber)
                        vv=int(input("Verify you name and phonenumber if your name and phonenumber is correct enter 1 and if your name or phonenumber is wrong enter 2"))
                        if(vv==1):
                            fp.write(name+"\t"+phonenumber+"\t"+pp+"\t"+rr+"\n")
                            print("We have registered your complain\nWe will replace the product if found faulty at the guarntee period...\nWe will contact you as soon as possible")
                        elif(vv==2):
                            name=input("Enter your name")
                            phonenumber=("Enter your phonenumber")
                            fp.write(name+"\t"+phonenumber+"\t"+pp+"\t"+rr+"\n")
                            print("We have registered your complain\nWe will replace the product if found faulty at the guarntee period...\nWe will contact you as soon as possible")
                        else:
                            print("You have entered wrong choice")
                        fp.close()
                    case 4:
                        q=open("comment.txt","a")
                        k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                        ra=input("rate (---/5) our Goyal Super-Market")
                        q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                        q.close()
                        print("ThankYou For Visiting Our Goyal Multi-Complex")
                        exit()
                    case _:
                        print("Invalid Choice")
        else:
            print("Not Login/Signup")
            exit()
    elif(n==2):
        p="1234abcd"
        password=input("Enter the password")
        if(password==p):
            print(today+"\t\t\t\t\t\t\t\t\t"+time)
            while(True):
                che=int(input("Enter your choice\n1.  you want to display products of any section/stock of any product\n2.  you want to update in stock\n3.  you want to update any product\n4.\
  you want to update price of any product\n5.  you want to see workers list\n6.  You want to update worker list\n7.  You want to see total sell amount till date \n8.  Profit Calculator\n9.\
  You want to see review of your super-market\n10. you want to you want to see complain done by customer against any product or any worker or against you\n11. You want to see return product\
complains\n12. You want to see how many customers visit site\n13. You want to Exit"))
                match che:
                    case 1:
                        while(True):
                            le=int(input("Enter your choice in which section you want to diplay\n1 Electric Appliances\n2 Clothes\n3 Shoes\n4 Watches\n5 Costmetics Products\n6 Stationary\
 Products\n7. Go Back to Previous Menu\n8. Exit"))
                            match le:
                                case 1:
                                    while(True):
                                        ip=int(input("Enter your choice\n1. Tubes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. Go Back To Previous Menu\n6. Exit"))
                                        match ip:
                                            case 1:
                                                display("bulb.txt")
                                            case 2:
                                                display("laptop.txt")
                                            case 3:
                                                display("phone.txt")
                                            case 4:
                                                display("iron.txt")
                                            case 5:
                                                break
                                            case 6:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 2:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Clothes\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                display("cloth.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 3:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Shoes\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                display("shoe.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 4:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Watches\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                display("watch.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 5:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Beauty Products\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                display("beautyproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 6:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Stationary Products\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                display("stationaryproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 7:
                                    break
                                case 8:
                                    exit()
                                case _:
                                    print("Invalid Choice")
                    case 2:
                        while(True):
                            le=int(input("Enter your choice in which section you want to update stockes in\n1 Electric Appliances\n2 Clothes\n3 Shoes\n4 Watches\n5 Costmetics Products\n\
6. Stationary Products\n7. Go Back To Previous Menu\n8. Exit"))
                            match le:
                                case 1:
                                    while(True):
                                        ip=int(input("Enter your choice\n1. Tubes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. Go Back To Previous Menu\n6. Exit"))
                                        match ip:
                                            case 1:
                                                update_stock("bulb.txt")
                                            case 2:
                                                update_stock("laptop.txt")
                                            case 3:
                                                update_stock("phone.txt")
                                            case 4:
                                                update_stock("iron.txt")
                                            case 5:
                                                break
                                            case 6:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 2:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Clothes\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_stock("cloth.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 3:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Shoes\n2. Go Back To Previous Menu\n5. Exit"))
                                        match iu:
                                            case 1:
                                                update_stock("shoe.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 4:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Watches\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_stock("watch.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 5:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Beauty Products\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_stock("beautyproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 6:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Stationary Products\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_stock("stationaryproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 7:
                                    break
                                case 8:
                                    exit()
                                case _:
                                    print("Invalid Choice")
                    case 3:
                        while(True):
                            le=int(input("Enter your choice in which section you want to diplay\n1 Electric Appliances\n2 Clothes\n3 Shoes\n4 Watches\n5 Costmetics Products\n6 Stationary\
 Products\n7. Go Back To Previous Menu\n8. Exit"))
                            match le:
                                case 1:
                                    while(True):
                                        ip=int(input("Enter your choice\n1. Tubes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. Go Back To Previous Menu\n6. Exit"))
                                        match ip:
                                            case 1:
                                                update_product("bulb.txt")
                                            case 2:
                                                update_product("laptop.txt")
                                            case 3:
                                                update_product("phone.txt")
                                            case 4:
                                                update_product("iron.txt")
                                            case 5:
                                                break
                                            case 6:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 2:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Clothes\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_product("cloth.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 3:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Shoes\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_product("shoe.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 4:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Watches\n2. Go Back To Previous Menu\n5. Exit"))
                                        match iu:
                                            case 1:
                                                update_product("watch.txt")
                                            case 4:
                                                break
                                            case 5:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 5:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Beauty Products\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_product("beautyproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 6:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Stationary Products\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_product("stationaryproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 7:
                                    break
                                case 8:
                                    exit()
                                case _:
                                    print("Invalid Choice")
                    case 4:
                        while(True):
                            le=int(input("Enter your choice in which section you want to diplay\n1 Electric Appliances\n2 Clothes\n3 Shoes\n4 Watches\n5 Costmetics Products\n6 Stationary\
 Products"))
                            match le:
                                case 1:
                                    while(True):
                                        ip=int(input("Enter your choice\n1. Tubes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. Go Back To Previous Menu\n6. Exit"))
                                        match ip:
                                            case 1:
                                                update_price("bulb.txt")
                                            case 2:
                                                update_price("laptop.txt")
                                            case 3:
                                                update_price("phone.txt")
                                            case 4:
                                                update_price("iron.txt")
                                            case 5:
                                                break
                                            case 6:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 2:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Clothes\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_price("cloth.txt")
                                            case 4:
                                                break
                                            case 5:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 3:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Shoes\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_price("shoe.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 4:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Watches\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_price("watch.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 5:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Beauty Products\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_price("beautyproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 6:
                                    while(True):
                                        iu=int(input("Enter your choice\n1. Stationary Products\n2. Go Back To Previous Menu\n3. Exit"))
                                        match iu:
                                            case 1:
                                                update_price("stationaryproducts.txt")
                                            case 2:
                                                break
                                            case 3:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                case 7:
                                    break
                                case 8:
                                    exit()
                                case _:
                                    print("Invalid Choice")
                    case 5:
                        display_worker("workers.txt")
                    case 6:
                        update_worker("workers.txt")
                    case 7:
                        tillsellamount("display.txt",0,1)
                    case 8:
                        calprofit.cal_profit()
                    case 9:
                        displays("comment.txt")
                    case 10:
                        displays("complain.txt")
                    case 11:
                        displays("guarantee.txt")
                    case 12:
                        displays("userdetails.txt")
                    case 13:
                        exit()
                    case _:
                        print("Invalid Choice")
    elif(n==2):
        print("You have entered wrong password")
        fp=int(input("You have two choice\n1. Forgot Password\n2. Exit"))
        t=("sanyam goyal","500125279","r2142231332")
        if(fp==1):
            print("Enter Owner Details")
            np=input("Enter my name")
            sap_id=input("Enter Owner Private Id(Sap Id)")
            rollno=input("Enter Multi-Complex Shop no.(enrollment no.)")
            if(np==t[0] and sap_id==t[1] and rollno==t[2]):
                print("Password is",p)
            else:
                print("You have entered Wrong Details\n Exiting....")
                exit()
        elif(fp==2):
            exit(0)
        else:
            print("You have entered wrong choice")
            exit()
    elif(n==3):
        exit()
    else:
        print("Invalid Choice enter")
