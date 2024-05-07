import datetime as dt
def dates_h(DateOfReturn):
    def imp_dates():
        now=(dt.datetime.now())
        Y=str(now.year)
        M=str(now.month)
        D=str(now.day)
        if int(now.day)==24 and int(now.month)==1:
            D=str(31)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==3:
            D=str(31)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==4:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==5:
            D=str(31)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==6:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==7:
            D=str(31)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==8:
            D=str(31)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==9:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==10:
            D=str(31)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==11:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==12:
            D=str(31)
            Y=str(int(now.year)+1)
            
            DateOfReturn.set(D+"/"+"1"+"/"+Y)

        #===============================================
        if int(now.day)==25 and int(now.month)==1:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==2:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==3:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==4:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==5:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==6:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==7:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==8:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==9:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==10:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==11:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==25 and int(now.month)==12:
            D=str(1)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+"1"+"/"+Y)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            
        if int(now.day)==26 and int(now.month)==1:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==2:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==3:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==4:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==5:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==6:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==7:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==8:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==9:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==10:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==11:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==26 and int(now.month)==12:
            D=str(2)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+"1"+"/"+Y)

        #=====================================================
        if int(now.day)==27 and int(now.month)==1:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==2:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==3:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==4:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==5:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==6:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==7:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==8:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==9:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==10:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==11:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==27 and int(now.month)==12:
            D=str(3)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+"1"+"/"+Y)
        
        #====================================================
        if int(now.day)==28 and int(now.month)==1:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==2:
            D=str(7)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==3:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==4:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==5:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==6:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==7:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==8:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==9:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==10:
            D=str(4)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==11:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==28 and int(now.month)==12:
            D=str(4)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+"1"+"/"+Y)
        #===============================================
        if int(now.day)==29 and int(now.month)==1:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==3:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==4:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==5:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==6:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==7:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==8:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==9:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==10:
            D=str(5)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==11:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==29 and int(now.month)==12:
            D=str(5)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+"1"+"/"+Y)
        #==============================================
        if int(now.day)==30 and int(now.month)==1:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==3:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==4:
            D=str(7)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==5:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==6:
            D=str(7)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==7:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==8:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==9:
            D=str(7)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==10:
            D=str(6)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==11:
            D=str(7)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==30 and int(now.month)==12:
            D=str(6)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+"1"+"/"+Y)
        #===============================================
        if int(now.day)==31 and int(now.month)==1:
            D=str(7)
            M=str(int(now.month)+1)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==31 and int(now.month)==3:
            D=str(7)
            M=str(int(now.month)+1)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==31 and int(now.month)==5:
            D=str(7)
            M=str(int(now.month)+1)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==31 and int(now.month)==7:
            D=str(7)
            M=str(int(now.month)+1)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==31 and int(now.month)==8:
            D=str(7)
            M=str(int(now.month)+1)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==31 and int(now.month)==10:
            D=str(7)
            M=str(int(now.month)+1)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==31 and int(now.month)==12:
            D=str(31)
            Y=str(int(now.year)+1)
            DateOfReturn.set(D+"/"+"1"+"/"+Y)
    imp_dates()



def dates_feb(DateOfReturn):
    def imp_dates():
        now=(dt.datetime.now())
        Y=str(now.year)
        M=str(now.month)
        D=str(now.day)
        if int(now.day)==22 and int(now.month)==2:
            D=str(1)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==23 and int(now.month)==2:
            D=str(2)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
        if int(now.day)==24 and int(now.month)==2:
            D=str(3)
            M=str(int(now.month)+1)
            DateOfReturn.set(D+"/"+M+"/"+Y)
    imp_dates()

        
