import pymysql

def addData(AccessionNo,NameOfBook,NumberOfBooks,IssuedTo,Department,DateOfReturn,DateOfIssue):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql=("INSERT INTO TEACHER_ISSUE_RETURN(ACCESSION_NO,NAME_OF_BOOK,NUMBER_OF_BOOKS,ISSUED_TO,DEPARTMENT,DATE_OF_RETURN,DATE_OF_ISSUE)\
        VALUES('%s','%s','%d','%s','%s','%s','%s')"%(AccessionNo,NameOfBook,NumberOfBooks,IssuedTo,Department,DateOfReturn,DateOfIssue))
    
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
    sql="SELECT * FROM TEACHER_ISSUE_RETURN"
    try:
        cursor.execute(sql)
        row=cursor.fetchall()
        return row
    except:
        print("NO DATA AVAILABLE")
      
    cursor.close()
    conn.close()
   
def DelData(ans):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="""DELETE FROM TEACHER_ISSUE_RETURN WHERE ACCESSION_NO = '%s'"""%(ans)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
def SearchData(AccessionNo="",NameOfBook="",IssuedTo="",Department="",DateOfReturn="",DateOfIssue=""):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="""SELECT * FROM TEACHER_ISSUE_RETURN WHERE Accession_No='%s' OR Name_Of_Book='%s' OR Issued_To='%s' OR Department='%s' OR Date_Of_Return='%s' OR Date_Of_Issue='%s'"""%(AccessionNo,NameOfBook,IssuedTo,Department,DateOfReturn,DateOfIssue)
    try:
        cursor.execute(sql)
        row=cursor.fetchall()
        return row
    except:
        print("NO DATA AVAILABLE")
    cursor.close()
    conn.close()

def updtData(ans,AccessionNo="",NameOfBook="",NumberOfBooks=int(),IssuedTo="",Department="",DateOfReturn="",DateOfIssue=""):
    conn=pymysql.connect(host="localhost",user="root",passwd="12345",db="cis_library")
    cursor=conn.cursor()
    sql="""UPDATE TEACHER_ISSUE_RETURN SET Accession_No='%s',Name_Of_Book='%s',NUMBER_OF_BOOKS='%d',Issued_To='%s',Department='%s',Date_Of_Return='%s',Date_Of_Issue='%s' WHERE Accession_No = '%s' """%(AccessionNo,NameOfBook,NumberOfBooks,IssuedTo,Department,DateOfReturn,DateOfIssue,ans)
    cursor.execute(sql)
    conn.commit()
    conn.close()


























    
