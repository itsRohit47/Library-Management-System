import pymysql


def addData(AccessionNo,NameOfBook,NumberOfBooks,IssuedTo,Class,DateOfReturn,DateOfIssue,cardid):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql=("INSERT INTO student_issue_return VALUES('%s','%s','%d','%s','%s','%s','%s','%s')"%(AccessionNo,NameOfBook,NumberOfBooks,IssuedTo,Class,DateOfReturn,DateOfIssue,cardid))
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()
    
         
def Display():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM student_issue_return"
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row  
    cursor.close()
    conn.close()
   
def DelData(ans,ANS):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="DELETE FROM STUDENT_ISSUE_RETURN WHERE Card_id='%s' AND Accession_No='%s'"%(ans,ANS)
    cursor.execute(sql)
    conn.commit()
    conn.close()

def DelData2(ans,ANS):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="DELETE FROM STUDENT_ISSUE_RETURN WHERE Card_id='%s' AND Accession_No='%s'"%(ans,ANS)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
def SearchData(AccessionNo="",NameOfBook="",IssuedTo="",Class="",cardid=""):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM STUDENT_ISSUE_RETURN WHERE Card_id='%s' OR Name_Of_Book='%s' OR Issued_To='%s' OR Class='%s' OR Accession_No='%s'"%(cardid,NameOfBook,IssuedTo,Class,AccessionNo)
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no relevent data"]
    else:
        return row 
    cursor.close()
    conn.close()

def updtData(ans,AccessionNo="",NameOfBook="",NumberOfBooks=int(),IssuedTo="",Class="",DateOfReturn="",DateOfIssue=""):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="""UPDATE STUDENT_ISSUE_RETURN SET Accession_No='%s',Name_Of_Book='%s',NUMBER_OF_BOOKS='%d',Issued_To='%s',Class='%s',Date_Of_Return='%s',Date_Of_Issue='%s' WHERE Accession_No = '%s' """%(AccessionNo,NameOfBook,NumberOfBooks,IssuedTo,Class,DateOfReturn,DateOfIssue,ans)
    cursor.execute(sql)
    conn.commit()
    conn.close()






def add_book(BookName,AccessionNo,inStock):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql=("INSERT INTO STOCK VALUES('%s','%s','%d')"%(BookName,AccessionNo,inStock))
    
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()
    
def remove_book(AssessionNo):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql=("DELETE FROM STOCK WHERE AccessionNO='%s'"%(AssessionNo))
    
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    


def stock_books(AssessionNo):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM STOCK WHERE AccessionNo='%s'"%(AssessionNo)
    cursor.execute(sql)
    row=cursor.fetchall()
    return row
    cursor.close()
    conn.close()

def stock_books2(bookname):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM STOCK WHERE BookName='%s'"%(bookname)
    cursor.execute(sql)
    row=cursor.fetchall()
    return row
    cursor.close()
    conn.close()

def stockupdate(instock,number_of_books,AssessionNo,BookName):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql1=("DELETE FROM STOCK WHERE AccessionNo='%s'"%(AssessionNo))
    sql="INSERT INTO STOCK VALUES('%s','%s','%d')"%(BookName,AssessionNo,instock-number_of_books)
    try:
        cursor.execute(sql1)
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    
    conn.close()

def stockupdate2(instock,numberofbooks,AssessionNo):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    ans=instock+numberofbooks
    sql="UPDATE STOCK SET INSTOCK = '%d' WHERE AccessionNo= '%s'" %(ans,AssessionNo)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    
    conn.close()
    



def add_card(studentname,admissionno,cardid,default="......"):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql=("INSERT INTO CARDS VALUES('%s','%s','%s','%s')"%(studentname,admissionno,cardid,default))
    
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()
    
def remove_card(admissionnod):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql=("DELETE FROM CARDS WHERE admission_number='%s'"%(admissionnod))
    
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()




def getassc():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT AccessionNo FROM STOCK"
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row  
    cursor.close()
    conn.close()

def getassc3(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT BookName FROM STOCK where AccessionNo='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row  
    cursor.close()
    conn.close()

def getassc4(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT  AccessionNo FROM STOCK where BookName='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row  
    cursor.close()
    conn.close()




def currentstock(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT instock FROM STOCK where AccessionNo='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row  
    cursor.close()
    conn.close()

def getassc2():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT BookName FROM STOCK"
    
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row  
    cursor.close()
    conn.close()

def getcrdid():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT card_id FROM cards"
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row
    cursor.close()
    conn.close()

def getcrdid2():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT Student_name from cards"
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row
    cursor.close()
    conn.close()
   


def getdata(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT Student_name FROM cards where card_id='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row  
    cursor.close()
    conn.close()

    
def getdata2(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT card_id FROM cards where Student_name='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["no data"]
    else:
        return row  
    cursor.close()
    conn.close()




def show_books():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM STOCK"
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["n"]
    else:
        return row  
    cursor.close()
    conn.close()
    



def show_stu():
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM cards"
    cursor.execute(sql)
    row=cursor.fetchall()
    if len(row)==0:
        return ["n"]
    else:
        return row  
    cursor.close()
    conn.close()
    


def one1(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM STUDENT_ISSUE_RETURN WHERE issued_to='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    return row
    cursor.close()
    conn.close()

    

def one2(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM STUDENT_ISSUE_RETURN WHERE Accession_no='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    return row
    cursor.close()
    conn.close()

def one3(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM STUDENT_ISSUE_RETURN WHERE Card_id='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    return row
    cursor.close()
    conn.close()

def one4(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM STUDENT_ISSUE_RETURN WHERE Date_Of_Issue='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    return row
    cursor.close()
    conn.close()

def one5(value):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="SELECT * FROM STUDENT_ISSUE_RETURN WHERE Date_Of_return='%s'"%(value)
    cursor.execute(sql)
    row=cursor.fetchall()
    return row
    cursor.close()
    conn.close()














    

    
