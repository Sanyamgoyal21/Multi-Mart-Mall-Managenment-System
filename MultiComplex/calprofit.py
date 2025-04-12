def cal_profit():
    d={}
    sum=0
    while(True):
        x=input("Enter Product Name or (for exit enter a)")
        if(x=='a'):
            break
        else:
            y=int(input("Enter its Cost Price"))
            z=int(input("Enter its Selling Price"))
            l=int(input("Enter no. of qunatity sold"))
            a=[y,z,l]
            d.update({x:a})
    for i in d:
        profitcalculation=lambda costprice,sellingprice,quantitysold:(sellingprice-costprice)*quantitysold
        profit=profitcalculation(d[i][0],d[i][1],d[i][2])
        print("Profit for product",i+"is",profit)
        sum=sum+profit
    print("Net Today's Profit is",sum)
