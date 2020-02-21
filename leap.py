def leapyear(yr):
    flag=0
    while flag<15:
        if(yr%4==0 and yr%100!=0 or yr%400==0):
            print(yr)
            flag=flag+1
        yr=yr+1        
yr=eval('input("Enter the year :- ")')        
leapyear(yr+1)