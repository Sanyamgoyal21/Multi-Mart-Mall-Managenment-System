import datetime
today=datetime.date.today().strftime("%Y-%m-%d")
time=datetime.datetime.now().strftime("%H:%M:%S")
class Change:
    def __init__(self,file,mn):
        self.filename=file
        self.mn=mn
    def stock(self):
        l=[]
        if(self.mn==1):
            Display(self.filename).display()
            with open(self.filename,"r") as fe:
                p=fe.readlines()
            for i in p:
                g=i.strip().split("\t")
                s=Update_Stock(self.filename,g[0],g[1],g[2],g[3],g[4],g[5])
                l.append(s)
            q=input("Enter the Product Name")
            try:
                z=int(input("Enter new price"))
                for i in l:
                    i.update_price(q,z)
                with open(self.filename,"w") as fe:
                    fe.close()
                with open(self.filename,"a") as fe:
                    for i in l:
                        str=i.a+"\t"+i.b+"\t"+i.c+"\t"+i.d+"\t"+i.f+"\t"+i.g+"\n"
                        fe.write(str)
                Display(self.filename).display()
            except ValueError as ve:
                print("Please Enter integer value")
            except AssertionError as ae:
                print("Please enter positive integer value")
            except Exception as e:
                print("An error occurred:", e)
        elif(self.mn==2):
            Display(self.filename).display()
            with open(self.filename,"r") as fe:
                p=fe.readlines()
            for i in p:
                g=i.strip().split("\t")
                s=Update_Stock(self.filename,g[0],g[1],g[2],g[3],g[4],g[5])
                l.append(s)
            try:
                n=int(input("if you want to increase stock enter 1 and if you want to decrease stock enter 2 and any other integer value for remaining stock same"))
                if(n==1):
                    try:
                        q=input("Enter the Product Name")
                        es=int(input("Enter the amount of new Stock come"))
                        for i in l:
                            i.update_stock(n,es,q)
                        with open(self.filename,"w") as fe:
                            fe.close()
                        with open(self.filename,"a") as fe:
                            for i in l:
                                str=i.a+"\t"+i.b+"\t"+i.c+"\t"+i.d+"\t"+i.f+"\t"+i.g+"\n"
                                fe.write(str)
                    except ValueError as ve:
                        print("Please Enter integer value")
                    except AssertionError as ae:
                        print("Please enter positive integer value")
                    except Exception as e:
                        print("An error occurred:", e)
                elif(n==2):
                    try:
                        q=input("Enter the Product Name")
                        es=int(input("Enter the amount of Stock reduce"))
                        for i in l:
                            i.update_stock(n,es,q)
                        with open(self.filename,"w") as fe:
                            fe.close()
                        with open(self.filename,"a") as fe:
                            for i in l:
                                str=i.a+"\t"+i.b+"\t"+i.c+"\t"+i.d+"\t"+i.f+"\t"+i.g+"\n"
                                fe.write(str)
                    except ValueError as ve:
                        print("Please Enter integer value")
                    except AssertionError as ae:
                        print("Please enter positive integer value")
                    except Exception as e:
                        print("An error occurred:", e)
                else:
                    print("Ok Stock does not Updated")
                Display(self.filename).display()
            except ValueError as ve:
                print("Please Enter integer value")
            except AssertionError as ae:
                print("Please enter positive integer value")
            except Exception as e:
                print("An error occurred:", e)
class Bill:
    def __init__(self,fug):
        self.fug=fug
    def buying(self):
        try:
            with open("cartbill.txt","r") as fg:
                q=fg.readlines()
            l=["bulb.txt","cloth.txt","iron.txt","laptop.txt","phone.txt","beautyproducts.txt","shoe.txt","stationaryproducts.txt","watch.txt"]
            for i in l:
                try:
                    with open(i,"r") as fe:
                        p=fe.readlines()
                    for j in q:
                        g=j.strip().split("\t")
                        for k in p:
                            h=k.strip().split("\t")
                            if(g[0]==h[2]):
                                Abstract(i,g[1],g[0]).updatestock()
                except FileNotFoundError:
                    print("Error: File not found.")
                except PermissionError:
                    print("Error: Permission denied.")
                except Exception as e:
                    print("An error occurred:", e)
            with open("cartbill.txt","w") as fg:
                fg.close()
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
    def bill(self):
        try:
            with open("cartbill.txt", "r") as fe:
                fr = fe.readlines()
            print("*" * 50 + " Invoice " + "*" * 50)
            print("{:<20} {:<10} {:<10} {:<10}".format("Items", "Quantity", "Price", "Amount"))
            print("-" * 60)
            total = 0
            for line in fr:
                fg = line.strip().split("\t")
                print("{:<20} {:<10} Rs.{:<10} Rs.{:<10}".format(fg[0], int(fg[1]), float(fg[2]), int(fg[3])))
                total += int(fg[3])
            print("-" * 60)
            print("{:>52}".format("Total: Rs." + str(total)))
            with open(fug,"a") as fe:
                for i in fr:
                    sx=i.split("\t")
                    fe.write(sx[0]+"\t"+sx[1]+"\t"+sx[2]+"\t"+sx[3]+"\n")
            q=0                   
            Abstract("display.txt",total,q).tillsellamount()
            self.buying()
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
class Cart:
    def __init__(self,file,a,b,c):
        self.filename=file
        self.a=a
        self.b=str(b)
        self.c=str(c)
        self.d=str(int(self.c)*int(self.b))
    def cartdisplay(self):
        Display(self.filename).displays()
    def cartadd(self):
        c=0
        try:
            with open(self.filename,"r") as kl:
                if kl.read().strip()=="":
                    try:
                        with open(self.filename,"a") as fl:
                            fl.write(self.a+"\t"+self.b+"\t"+self.c+"\t"+self.d)
                    except FileNotFoundError:
                        print("Error: File not found.")
                    except PermissionError:
                        print("Error: Permission denied.")
                    except Exception as e:
                        print("An error occurred:", e)
                else:
                    try:
                        with open(self.filename,"r") as kl:
                            pd=kl.readlines()
                        try:
                            k1=open(self.filename,"w")
                            k1.close()
                            try:
                                with open(self.filename,"a") as kl:
                                    for line in pd:
                                        lines=line.strip().split("\t")
                                        if(lines[0]==self.a):
                                            lines[1]=str(int(self.b)+int(lines[1]))
                                            lines[3]=str(int(self.d)+int(lines[3]))
                                            kl.write(lines[0]+"\t"+lines[1]+"\t"+lines[2]+"\t"+lines[3]+"\n")
                                            c=1
                                        else:
                                            kl.write(lines[0]+"\t"+lines[1]+"\t"+lines[2]+"\t"+lines[3]+"\n")
                                    if(c==0):
                                        kl.write(self.a+"\t"+self.b+"\t"+self.c+"\t"+self.d+"\n")        
                            except FileNotFoundError:
                                print("Error: File not found.")
                            except PermissionError:
                                print("Error: Permission denied.")
                            except Exception as e:
                                print("An error occurred:", e)
                        except FileNotFoundError:
                            print("Error: File not found.")
                        except PermissionError:
                            print("Error: Permission denied.")
                        except Exception as e:
                            print("An error occurred:", e)
                    except FileNotFoundError:
                        print("Error: File not found.")
                    except PermissionError:
                        print("Error: Permission denied.")
                    except Exception as e:
                        print("An error occurred:", e)
            print("Item added to the cart")
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
    def cartremove(self):
        Display(self.filename).displays()
        m=input("Enter Product name you want to remove")
        try:
            with open(self.filename,"r") as fl:
                r=fl.readlines()
            try:
                with open(self.filename,"w") as fl:
                    fl.close()
                try:
                    with open(self.filename,"a") as fl:
                        for i in r:
                            g=i.split("\t")
                            if(g[0]==m):
                                continue
                            fl.write(g[0]+"\t"+g[1]+"\t"+g[2]+"\t"+g[3])
                        print("Product remove from the cart")
                        Display(self.filename).displays()
                except FileNotFoundError:
                    print("Error: File not found.")
                except PermissionError:
                    print("Error: Permission denied.")
                except Exception as e:
                    print("An error occurred:", e)
            except FileNotFoundError:
                print("Error: File not found.")
            except PermissionError:
                print("Error: Permission denied.")
            except Exception as e:
                print("An error occurred:", e)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
    def quancartremove(self):
        Display(self.filename).displays()
        m=input("Enter Product name you want to decrease quantity")
        try:
            with open(self.filename,"r") as fl:
                r=fl.readlines()
            try:
                with open(self.filename,"w") as fl:
                    fl.close()
                try:
                    with open(self.filename,"a") as fl:
                        try:
                            n=int(input("Enter how much quantity you want to decrease"))
                            assert n>=0
                            for i in r:
                                g=i.split("\t")
                                if(g[0]==m):
                                    if(n<int(g[1])):
                                        fl.write(g[0]+"\t"+str(int(g[1])-n)+"\t"+g[2]+"\t"+g[3])
                                    elif(n==g[1]):
                                        continue
                                    else:
                                        print("Invalid quantity Enter")
                                        fl.write(g[0]+"\t"+g[1]+"\t"+g[2]+"\t"+g[3])
                                else:
                                    fl.write(g[0]+"\t"+g[1]+"\t"+g[2]+"\t"+g[3])
                            print("Product quantity decrease from the cart")
                            Display(self.filename).displays()
                        except ValueError as ve:
                            print("Please Enter integer value")
                        except AssertionError as ae:
                            print("Please enter positive integer value")
                        except Exception as e:
                            print("An error occurred:", e)
                except FileNotFoundError:
                    print("Error: File not found.")
                except PermissionError:
                    print("Error: Permission denied.")
                except Exception as e:
                    print("An error occurred:", e)
            except FileNotFoundError:
                print("Error: File not found.")
            except PermissionError:
                print("Error: Permission denied.")
            except Exception as e:
                print("An error occurred:", e)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
class Abstract:
    def __init__(self,f,n,h=None):
        self.filename=f
        self.total=n
        self.choice=h
    def tillsellamount(self):
        try:
            with open(self.filename,"r") as fe:
                fl=fe.readlines()
            try:
                with open(self.filename,"a") as fe:
                    for i in fl:
                        fy=i.split("-")
                    self.total=self.total+int(fy[3])
                    fe.write(str(today)+"-"+str(self.total)+"\n")
                if(self.choice==1):
                    print("-"*80)
                    print("Rs.",self.total)
                    print("-"*80)                    
            except FileNotFoundError:
                print("Error: File not found.")
            except PermissionError:
                print("Error: Permission denied.")
            except Exception as e:
                print("An error occurred:", e)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
    def updatestock(self):
        try:
            f=open(self.filename,"r")
            p=f.readlines()
            f.close()
            try:
                f=open(self.filename,"w")
                f.close()
                try:
                    f=open(self.filename,"a")
                    for i in p:
                        y=i.split("\t")
                        if y[2]==self.choice:
                            y[3]=str(int(y[3])-int(self.total))
                            f.write(y[0]+"\t"+y[1]+"\t"+y[2]+"\t"+y[3]+"\t"+y[4]+"\t"+y[5])
                        else:
                            f.write(y[0]+"\t"+y[1]+"\t"+y[2]+"\t"+y[3]+"\t"+y[4]+"\t"+y[5])
                    f.close()
                except FileNotFoundError:
                    print("Error: File not found.")
                except PermissionError:
                    print("Error: Permission denied.")
                except Exception as e:
                    print("An error occurred:", e)
            except FileNotFoundError:
                print("Error: File not found.")
            except PermissionError:
                print("Error: Permission denied.")
            except Exception as e:
                print("An error occurred:", e)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
class Display:
    def __init__(self,file):
        self.filename=file
    def display(self):
        print("-"*80)
        print("It is in sequence from left to right")
        print("S.No. BrandName ProductName Quantity Price Features")
        try:
            with open(self.filename,"r") as fe:
                for i in fe:
                    print(i)
            print("-"*80)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
    def display_worker(self):
        print("-"*80)
        print("It is in sequence from left to right")
        print("S.No. WorkerName Age")
        try:
            with open(self.filename,"r") as fe:
                for i in fe:
                    print(i)
            print("-"*80)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
    def displays(self):
        print("-"*80)
        try:
            with open(self.filename,"r") as fe:
                for i in fe:
                    print(i)
            print("-"*80)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
class Menu(Abstract,Display):
    def __init__(self,file):
        Abstract.__init__(self,file,n,a)
        Display.__init__(self,file)
        self.filename=file
    def menu(self):
        try:
            super().display()
            with open(self.filename,"r") as fl:
                r=fl.readlines()
                k=len(r)
                print(k)
                sum=0
                while(True):
                    q=0
                    print("enter the number shown in menu u want to add else to confirm 0")
                    try:
                        x=int(input())
                        assert x>=0
                        if(0<x<=k):
                            for i in r:
                                g=i.split("\t")
                                if(q==x-1):
                                    try:
                                        y=int(input("enter quantity"))
                                        assert y>=0
                                        if(y>=0):
                                            if(y<=int(g[3])):
                                                Cart("cartbill.txt",g[2],y,g[4]).cartadd()
                                            else:
                                                print("Current Amount of Stock is not available")
                                                break
                                        else:
                                            print("Invalid Stock Amount")
                                            break
                                    except ValueError as ve:
                                        print("Please Enter integer value")
                                    except AssertionError as ae:
                                        print("Please enter positive integer value")
                                    except Exception as e:
                                        print("An error occurred:", e)
                                q=q+1
                        elif(x==0):
                            print("-"*80)
                            print("-"*80)
                            break
                        else:
                            print("Invalid Choice")
                            print("-"*80)
                            print("-"*80)
                            break
                    except ValueError as ve:
                        print("Please Enter integer value")
                    except AssertionError as ae:
                        print("Please enter positive integer value")
                    except Exception as e:
                        print("An error occurred:", e)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
class Update_Stock(Display):
    def __init__(self,file,a,b,c,d,f,g):
        super().__init__(file)
        self.filename=file
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.f=f
        self.g=g
    def update_worker(self):
        try:
            super().display_worker()
            with open(self.filename,"r") as fe:
                r=fe.readlines()
            try:
                n=int(input("if you want to add worker enter 1 and to delete any worker enter any positive integer value other than 1"))
                assert n>=0
                if(n==1):
                    try:
                        with open(self.filename,"a") as fa:
                            try:
                                m=int(input("Enter how many workers do you want to enter"))
                                assert m>=0
                                for i in range(m):
                                    a=input("Enter S.No.")
                                    b=input("Enter Worker Name:")
                                    c=input("Enter Worker Age:")
                                    fa.write(a+"\t"+b+"\t"+c)
                            except ValueError as ve:
                                print("Please Enter integer value")
                            except AssertionError as ae:
                                print("Please enter positive integer value")
                            except Exception as e:
                                print("An error occurred:", e)
                    except FileNotFoundError:
                        print("Error: File not found.")
                    except PermissionError:
                        print("Error: Permission denied.")
                    except Exception as e:
                        print("An error occurred:", e)
                else:
                    try:
                        fl=open(self.filename,"w")
                        fl.close()
                        try:
                            with open(self.filename,"a") as fl:
                                m=input("Enter Worker Name:")
                                for i in r:
                                    g=i.split("\t")
                                    if(g[1]==m):
                                        continue
                                    fl.write(g[0]+"\t"+g[1]+"\t"+g[2])
                        except FileNotFoundError:
                            print("Error: File not found.")
                        except PermissionError:
                            print("Error: Permission denied.")
                        except Exception as e:
                            print("An error occurred:", e)
                    except FileNotFoundError:
                        print("Error: File not found.")
                    except PermissionError:
                        print("Error: Permission denied.")
                    except Exception as e:
                        print("An error occurred:", e)
                print("Worker List Updated")
                Display(self.filename).display_worker()
            except ValueError as ve:
                print("Please Enter integer value")
            except AssertionError as ae:
                print("Please enter positive integer value")
            except Exception as e:
                print("An error occurred:", e)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
    def update_price(self,q,z):
        if(self.c==q):
            self.f=str(z)
            print("Product Price Updated")
    def update_stock(self,n,p,q):
        if(self.c==q):
            if(n==1):
                self.d=str(int(self.d)+int(p))
            elif(n==2):
                self.d=str(int(self.d)-int(p))
            print("Product Stock Updated")
    def update_product(self):
        try:
            super().display()
            with open(self.filename,"r") as fe:
                r=fe.readlines()
            try:
                n=int(input("if you want to add product enter 1 and to delete product enter any positive integer value other than 1"))
                assert n>=0
                if(n==1):
                    try:
                        with open(self.filename,"a") as fa:
                            try:
                                m=int(input("Enter how many products do you want to enter"))
                                assert m>=0
                                for i in range(m):
                                    a=input("Enter S.No.")
                                    b=input("Enter Brand Name")
                                    c=input("Enter Product Name")
                                    d=input("Enter no. of Quantity")
                                    e=input("Enter no. of Prices")
                                    g=input("Enter features")
                                    fa.write(a+"\t"+b+"\t"+c+"\t"+d+"\t"+e+"\t"+g)
                            except ValueError as ve:
                                print("Please Enter integer value")
                            except AssertionError as ae:
                                print("Please enter positive integer value")
                            except Exception as e:
                                print("An error occurred:", e)
                    except FileNotFoundError:
                        print("Error: File not found.")
                    except PermissionError:
                        print("Error: Permission denied.")
                    except Exception as e:
                        print("An error occurred:", e)
                else:
                    try:
                        fl=open(self.filename,"w")
                        fl.close()
                        try:
                            with open(self.filename,"a") as fl:
                                m=input("Enter Product Name")
                                for i in r:
                                    g=i.split("\t")
                                    if(g[2]==m):
                                        continue
                                    fl.write(g[0]+"\t"+g[1]+"\t"+g[2]+"\t"+g[3]+"\t"+g[4]+"\t"+g[5])
                        except FileNotFoundError:
                            print("Error: File not found.")
                        except PermissionError:
                            print("Error: Permission denied.")
                        except Exception as e:
                            print("An error occurred:", e)
                    except FileNotFoundError:
                        print("Error: File not found.")
                    except PermissionError:
                        print("Error: Permission denied.")
                    except Exception as e:
                        print("An error occurred:", e)
                print("Product Updated")
                Display(self.filename).display()
            except ValueError as ve:
                print("Please Enter integer value")
            except AssertionError as ae:
                print("Please enter positive integer value")
            except Exception as e:
                print("An error occurred:", e)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("An error occurred:", e)
print("\t\t\t\t\t\t\tWelcome to Goyal Multi-Complex\t\t\t\t\t\t")
while(True):
    try:
        n=int(input("Enter your choice\n1. You for USER\n2. You are Owner\n3. Exit"))
        assert n>0
        if n==1:
            c=0
            a=0
            while(True):
                if(c==1):
                    break
                try:
                    qw=int(input("Enter your choice\n1. for Login\n2. for Signup\n3. Exit"))
                    assert qw>0
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
                        exit()
                    else:
                        print("Invalid Choice")
                except ValueError:
                    print("Please Enter a valid integer choice")
                except AssertionError:
                    print("Enter choice is negative please enter positive value")
            if(c==1):
                print(today+"\t\t\t\t\t\t\t\t\t"+time)
                print("Welcome {} Sir".format(name))
                fug=phonenumber+".txt"
                print("*"*40+"Your old Purchase History"+"*"*40)
                Display(fug).displays()
                while(True):
                    try:
                        ch=int(input("Enter your choice\n1. you want to buy something\n2. you want to complain of any product you purchase or against any worker or against owner\n\
3. Product is defective and in guarantee period\n4. you want to see cart\n5. You want to make remove products from cart\n6. You want to reduce specific quantity of any product in cart\n7. You want to go back to previous menu\n8. You want to exit"))
                        assert ch>0
                        match ch:
                            case 1:
                                while(True):
                                    try:
                                        l=int(input("Enter your choice what you want to buy\n1. Electric Appliances\n2. Clothes\n3. Shoe store\n4. Watches\n5. Beauty Products\n6. \
Stationary Products\n7. you want to see cart\n8. You want to make remove products from cart\n9. You want to reduce specific quantity of any product in cart\n10. Go back to previous Menu\n11. Exit"))
                                        assert l>0
                                        match l:
                                            case 1:
                                                while(True):
                                                    try:
                                                        ip=int(input("Enter your choice\n1. Bulbes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. you want to see cart\n6. You want to make remove products from cart\n7. You want to reduce specific quantity of any product in cart\n8. Go back to previous Menu\n9. Exit"))
                                                        assert ip>0
                                                        match ip:
                                                            case 1:
                                                                h=Menu("bulb.txt")
                                                                h.menu()
                                                            case 2:
                                                                Menu("laptop.txt").menu()
                                                            case 3:
                                                                Menu("phone.txt").menu()
                                                            case 4:
                                                                Menu("iron.txt").menu()
                                                            case 5:
                                                                Cart("cartbill.txt",0,0,0).cartdisplay()
                                                            case 6:
                                                                Cart("cartbill.txt",0,0,0).cartremove()
                                                            case 7:
                                                                Cart("cartbill.txt",0,0,0).quancartremove()
                                                            case 8:
                                                                break
                                                            case 9:
                                                                q=open("comment.txt","a")
                                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                                q.close()
                                                                print("Your Bill")
                                                                Bill(fug).bill()
                                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                            print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 2:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Clothes\n2. you want to see cart\n3. You want to make remove products from cart\n4. You want to reduce specific quantity of any product in cart\n5. Go back to \
previous menu\n6. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Menu("cloth.txt").menu()
                                                            case 2:
                                                                Cart("cartbill.txt",0,0,0).cartdisplay()
                                                            case 3:
                                                                Cart("cartbill.txt",0,0,0).cartremove()
                                                            case 4:
                                                                Cart("cartbill.txt",0,0,0).quancartremove()
                                                            case 5:
                                                                break
                                                            case 6:
                                                                q=open("fugcomment.txt","a")
                                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                                q.close()
                                                                print("Your Bill")
                                                                Bill(fug).bill()
                                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                            print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 3:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Shoes\n2. you want to see cart\n3. You want to make remove products from cart\n4. You want to reduce specific quantity of any product in cart\n5. Go back to \
previous Menu\n6. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Menu("shoe.txt").menu()
                                                            case 2:
                                                                Cart("cartbill.txt",0,0,0).cartdisplay()
                                                            case 3:
                                                                Cart("cartbill.txt",0,0,0).cartremove()
                                                            case 4:
                                                                Cart("cartbill.txt",0,0,0).quancartremove()
                                                            case 5:
                                                                break
                                                            case 6:
                                                                q=open("comment.txt","a")
                                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                                q.close()
                                                                print("Your Bill")
                                                                Bill(fug).bill()
                                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                            print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 4:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Watches\n2. you want to see cart\n3. You want to make remove products from cart\n4. You want to reduce specific quantity of any product in cart\n5. Go back to \
previous Menu\n6. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Menu("watch.txt").menu()
                                                            case 2:
                                                                Cart("cartbill.txt",0,0,0).cartdisplay()
                                                            case 3:
                                                                Cart("cartbill.txt",0,0,0).cartremove()
                                                            case 4:
                                                                Cart("cartbill.txt",0,0,0).quancartremove()
                                                            case 5:
                                                                break
                                                            case 6:
                                                                q=open("comment.txt","a")
                                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                                q.close()
                                                                print("Your Bill")
                                                                Bill().bill()
                                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                            print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 5:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1.Costmetic products\n2. you want to see cart\n3. You want to make remove products from cart\n4. You want to reduce specific quantity of any product in cart\n5. Go \
back to previous Menu\n6. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Menu("beautyproducts.txt").menu()
                                                            case 2:
                                                                Cart("cartbill.txt",0,0,0).cartdisplay()
                                                            case 3:
                                                                Cart("cartbill.txt",0,0,0).cartremove()
                                                            case 4:
                                                                Cart("cartbill.txt",0,0,0).quancartremove()
                                                            case 5:
                                                                break
                                                            case 6:
                                                                q=open("comment.txt","a")
                                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                                q.close()
                                                                print("Your Bill")
                                                                Bill(fug).bill()
                                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                            print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 6:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Stationary products\n2. you want to see cart\n3. You want to make remove products from cart\n4. You want to reduce specific quantity of any product in cart\n5. Go \
back to previous Menu\n6. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Menu("stationaryproducts.txt").menu()
                                                            case 2:
                                                                Cart("cartbill.txt",0,0,0).cartdisplay()
                                                            case 3:
                                                                Cart("cartbill.txt",0,0,0).cartremove()
                                                            case 4:
                                                                Cart("cartbill.txt",0,0,0).quancartremove()
                                                            case 5:
                                                                break
                                                            case 6:
                                                                q=open("comment.txt","a")
                                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                                q.close()
                                                                print("Your Bill")
                                                                Bill(fug).bill()
                                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                            print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 7:
                                                Cart("cartbill.txt",0,0,0).cartdisplay()
                                            case 8:
                                                Cart("cartbill.txt",0,0,0).cartremove()
                                            case 9:
                                                Cart("cartbill.txt",0,0,0).quancartremove()
                                            case 10:
                                                break
                                            case 11:
                                                q=open("comment.txt","a")
                                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                                ra=input("rate (---/5) our Goyal Super-Market")
                                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                                q.close()
                                                print("Your Bill")
                                                Bill().bill()
                                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                    except ValueError:
                                        print("Please enter a valid integer choice")
                                    except AssertionError:
                                        print("Enter choice is negative please enter positive value")
                            case 2:
                                while(True):
                                    try:
                                        cm=int(input("Enter your choice\n1. You want to complain against any product\n2. You want to complain against any worker\n3. You want to \
complain against owner\n4. you want to see cart\n5. You want to make remove products from cart\n6. You want to reduce specific quantity of any product in cart\n7. You want to go back to previous menu\n8. Exit"))
                                        assert cm>0
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
                                            Cart("cartbill.txt",0,0,0).cartdisplay()
                                        elif(cm==5):
                                            Cart("cartbill.txt",0,0,0).cartremove()
                                        elif(cm==6):
                                            Cart("cartbill.txt",0,0,0).quancartremove()
                                        elif(cm==7):
                                            break
                                        elif(cm==8):
                                            k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                            ra=input("rate (---/5) our Goyal Super-Market")
                                            q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                            q.close()
                                            print("Your Bill")
                                            Bill(fug).bill()
                                            print("ThankYou For Visiting Our Goyal Multi-Complex")
                                            exit()
                                        else:
                                            print("Invalid choice")
                                            break
                                    except ValueError:
                                        print("Please enter a valid integer choice")
                                    except AssertionError:
                                        print("Enter choice is negative please enter positive value")
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
                                Cart("cartbill.txt",0,0,0).cartdisplay()
                            case 5:
                                Cart("cartbill.txt",0,0,0).cartremove()
                            case 6:
                                Cart("cartbill.txt",0,0,0).quancartremove()
                            case 7:
                                break
                            case 8:
                                q=open("comment.txt","a")
                                k=input("Before Exit\nPlease comment anything for our Goyal Super-Market")
                                ra=input("rate (---/5) our Goyal Super-Market")
                                q.write(name+"\t"+phonenumber+"\t"+k+"\t"+ra+"\n")
                                q.close()
                                print("Your Bill")
                                Bill(fug).bill()
                                print("ThankYou For Visiting Our Goyal Multi-Complex")
                                exit()
                            case _:
                                print("Invalid Choice")
                    except ValueError:
                        print("Please enter a valid integer choice")
                    except AssertionError:
                        print("Enter choice is negative please enter positive value")
            else:
                print("Not Login/Signup")
                exit()
        elif(n==2):
            p="1234abcd"
            password=input("Enter the password")
            if(password==p):
                print(today+"\t\t\t\t\t\t\t\t\t"+time)
                while(True):
                    try:
                        che=int(input("Enter your choice\n1.  you want to display products of any section/stock of any product\n2.  you want to update in stock\n3.  you want to update any\
product\n4. you want to update price of any product\n5.  you want to see workers list\n6.  You want to update worker list\n7.  You want to see total sell amount till date \n8.\
You want to see review of your super-market\n9. you want to you want to see complain done by customer against any product or any worker or against you\n10. You want to see return product\
 complains\n11. You want to see how many customers visit site\n12. You want to Exit"))
                        assert che>0
                        match che:
                            case 1:
                                while(True):
                                    try:
                                        le=int(input("Enter your choice in which section you want to diplay\n1 Electric Appliances\n2 Clothes\n3 Shoes\n4 Watches\n5 Costmetics Products\n\
6. Stationary Products\n7. Go Back to Previous Menu\n8. Exit"))
                                        assert le>0
                                        match le:
                                            case 1:
                                                while(True):
                                                    try:
                                                        ip=int(input("Enter your choice\n1. Tubes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. Go Back To Previous Menu\n6. Exit"))
                                                        assert ip>0
                                                        match ip:
                                                            case 1:
                                                                Display("bulb.txt").displays()
                                                            case 2:
                                                                Display("laptop.txt").display()
                                                            case 3:
                                                                Display("phone.txt").display()
                                                            case 4:
                                                                Display("iron.txt").display()
                                                            case 5:
                                                                break
                                                            case 6:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 2:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Clothes\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Display("cloth.txt").display()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 3:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Shoes\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Display("shoe.txt").display()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 4:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Watches\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Display("watch.txt").display()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 5:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Beauty Products\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Display("beautyproducts.txt").display()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 6:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Stationary Products\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Display("stationaryproducts.txt").display()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 7:
                                                break
                                            case 8:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                    except ValueError:
                                        print("Please enter a valid integer choice")
                                    except AssertionError:
                                        print("Enter choice is negative please enter positive value")
                            case 2:
                                while(True):
                                    try:
                                        le=int(input("Enter your choice in which section you want to update stockes in\n1. Electric Appliances\n2. Clothes\n3. Shoes\n4. Watches\n5.\
Costmetics Products\n6. Stationary Products\n7. Go Back To Previous Menu\n8. Exit"))
                                        assert le>0
                                        match le:
                                            case 1:
                                                while(True):
                                                    try:
                                                        ip=int(input("Enter your choice\n1. Tubes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. Go Back To Previous Menu\n6. Exit"))
                                                        assert ip>0
                                                        match ip:
                                                            case 1:
                                                                Change("bulb.txt",2).stock()
                                                            case 2:
                                                                Change("laptop.txt",2).stock()
                                                            case 3:
                                                                Change("phone.txt",2).stock()
                                                            case 4:
                                                                Change("iron.txt",2).stock()
                                                            case 5:
                                                                break
                                                            case 6:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 2:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Clothes\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Change("cloth.txt",2).stock()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 3:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Shoes\n2. Go Back To Previous Menu\n5. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Change("shoe.txt",2).stock()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 4:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Watches\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Change("watch.txt",2).stock()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 5:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Beauty Products\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Change("beautyproducts.txt",2).stock()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 6:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Stationary Products\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Change("stationaryproducts.txt",2).stock()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 7:
                                                break
                                            case 8:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                    except ValueError:
                                        print("Please enter a valid integer choice")
                                    except AssertionError:
                                        print("Enter choice is negative please enter positive value")
                            case 3:
                                while(True):
                                    try:
                                        le=int(input("Enter your choice in which section you want to diplay\n1 Electric Appliances\n2 Clothes\n3 Shoes\n4 Watches\n5 Costmetics Products\n6\
 Stationary Products\n7. Go Back To Previous Menu\n8. Exit"))
                                        assert le>0
                                        match le:
                                            case 1:
                                                while(True):
                                                    try:
                                                        ip=int(input("Enter your choice\n1. Tubes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. Go Back To Previous Menu\n6. Exit"))
                                                        assert ip>0
                                                        match ip:
                                                            case 1:
                                                                Update_Stock("bulb.txt",0,0,0,0,0,0).update_product()
                                                            case 2:
                                                                Update_Stock("laptop.txt",0,0,0,0,0,0).update_product()
                                                            case 3:
                                                                Update_Stock("phone.txt",0,0,0,0,0,0).update_product()
                                                            case 4:
                                                                Update_Stock("iron.txt",0,0,0,0,0,0).update_product()
                                                            case 5:
                                                                break
                                                            case 6:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 2:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Clothes\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Update_Stock("cloth.txt",0,0,0,0,0,0).update_product()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 3:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Shoes\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Update_Stock("shoe.txt",0,0,0,0,0,0).update_product()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 4:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Watches\n2. Go Back To Previous Menu\n5. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Update_Stock("watch.txt",0,0,0,0,0,0).update_product()
                                                            case 4:
                                                                break
                                                            case 5:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 5:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Beauty Products\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Update_Stock("beautyproducts.txt",0,0,0,0,0,0).update_product()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 6:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Stationary Products\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Update_Stock("stationaryproducts.txt",0,0,0,0,0,0).update_product()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 7:
                                                break
                                            case 8:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                    except ValueError:
                                        print("Please enter a valid integer choice")
                                    except AssertionError:
                                        print("Enter choice is negative please enter positive value")
                            case 4:
                                while(True):
                                    try:
                                        le=int(input("Enter your choice in which section you want to diplay\n1 Electric Appliances\n2 Clothes\n3 Shoes\n4 Watches\n5 Costmetics Products\n6 \
Stationary Products\n7 Go back to previous menu\n8 Exit"))
                                        assert le>0
                                        match le:
                                            case 1:
                                                while(True):
                                                    try:
                                                        ip=int(input("Enter your choice\n1. Tubes\n2. Laptop\n3. Mobile Phones\n4. Iron\n5. Go Back To Previous Menu\n6. Exit"))
                                                        assert ip>0
                                                        match ip:
                                                            case 1:
                                                                Change("bulb.txt",1).stock()
                                                            case 2:
                                                                Change("laptop.txt",1).stock()
                                                            case 3:
                                                                Change("phone.txt",1).stock()
                                                            case 4:
                                                                Change("iron.txt",1).stock()
                                                            case 5:
                                                                break
                                                            case 6:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 2:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Clothes\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Change("cloth.txt",1).stock()
                                                            case 4:
                                                                break
                                                            case 5:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 3:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Shoes\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Change("shoe.txt",1).stock()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 4:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Watches\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Change("watch.txt",1).stock()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 5:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Beauty Products\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Change("beautyproducts.txt",1).stock()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 6:
                                                while(True):
                                                    try:
                                                        iu=int(input("Enter your choice\n1. Stationary Products\n2. Go Back To Previous Menu\n3. Exit"))
                                                        assert iu>0
                                                        match iu:
                                                            case 1:
                                                                Update_Stock("stationaryproducts.txt",1).stock()
                                                            case 2:
                                                                break
                                                            case 3:
                                                                exit()
                                                            case _:
                                                                print("Invalid Choice")
                                                    except ValueError:
                                                        print("Please enter a valid integer choice")
                                                    except AssertionError:
                                                        print("Enter choice is negative please enter positive value")
                                            case 7:
                                                break
                                            case 8:
                                                exit()
                                            case _:
                                                print("Invalid Choice")
                                    except ValueError:
                                        print("Please enter a valid integer choice")
                                    except AssertionError:
                                        print("Enter choice is negative please enter positive value")
                            case 5:
                                Display("workers.txt").display_worker()
                            case 6:
                                Update_Stock("workers.txt",0,0,0,0,0,0).update_worker()
                            case 7:
                                Abstract("display.txt",0,1).tillsellamount()
                            case 8:
                                Display("comment.txt").displays()
                            case 9:
                                Display("complain.txt").displays()
                            case 10:
                                Display("guarantee.txt").displays()
                            case 11:
                                Display("userdetails.txt").displays()
                            case 12:
                                exit()
                            case _:
                                print("Invalid Choice")
                    except ValueError:
                        print("Please enter a valid integer choice")
                    except AssertionError:
                        print("Enter choice is negative please enter positive value")
        elif(n==2):
            print("You have entered wrong password")
            try:
                fp=int(input("You have two choice\n1. Forgot Password\n2. Exit"))
                assert fp>0
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
            except ValueError:
                print("Please enter a valid integer choice")
            except AssertionError:
                print("Enter choice is negative please enter positive value")
        elif(n==3):
            exit()
        else:
            print("Invalid Choice enter")
    except ValueError:
        print("Please enter a valid integer choice")
    except AssertionError:
        print("Enter choice is negative please enter positive value")
