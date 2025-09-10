import MySQLdb
import datetime

db = MySQLdb.connect(host='localhost', user='root', password='pass4MySQL')
cur = db.cursor()

def AddBooks():
    print('\n'+'-'*15)
    print('   Add Books')
    print('-'*15+'\n')
    
    cur.execute('SELECT MAX(BID) FROM Books')
    row = cur.fetchone()
    ID = 1000 if row==(None,) else int(row[0])

    while True:
        
        ID+=1
        
        Name=input('\nEnter the name of book : ')
        
        Author=input('Enter the name of the author : ')
        Genre1=input('Enter the genre of the book : ')
        Genre2=input('Enter the another genre [press enter if none] : ')
        Genre2='None' if Genre2=='' else Genre2
        Genre3=input('Enter the another genre [press enter if none] : ')
        Genre3='None' if Genre3=='' else Genre3
        Copies = input('Enter the number of copies in the library : ')
        Issued = 0
        Soft=input('Is the soft copy of the book available [Y/N] : ').upper()
        Price=input('Enter the price of the book : ')
        URL1='www.amazon.in/buy-'+Name+'-...'
        URL2='www.flipkart.com/buy-'+Name+'-...'

        sql = 'INSERT INTO Books VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (ID,Name,Author,Genre1,Genre2,Genre3,Copies,Issued,Soft,Price,URL1,URL2)
        cur.execute(sql,val); db.commit()
        ask=input('\n\nEnter more books? [Y/N] : ')
        if ask in 'Nn':
            break



def ModifyBook():
    print('\n'+'-'*19)
    print('   Modify a Book')
    print('-'*19+'\n')
    ID = input('Enter the Book ID that is to be modified : ')

    cur.execute('SELECT * FROM Books WHERE BID=%s',(ID,))
    row = cur.fetchone()
    if row not in ((None,),None):
        print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')
        print('|%6s |%40s |%20s |%10s |%10s |%10s |%5s |%6s |%3s |%5s |%6s |%6s |' %
              (row[0],row[1][:40],row[2][:18],row[3][:10],row[4][:10],row[5][:10],row[6],row[7],row[8],row[9],row[10][4:10],row[11][4:10]))
        print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')
        while True:
            change = input('\n\nOptions :\n\
1. Name of book\n\
2. Author\'s name\n\
3. Genre1 of the book\n\
4. Genre2 of the book\n\
5. Genre3 of the book\n\
6. Number of copies\n\
7. Availability of softcopy\n\
8. Price of the book\n\
\nEnter the option number : ')
            if change=='1':
                new = input('Enter new name of the book : ')
                sql = 'UPDATE Books SET Name=%s WHERE BID=%s'
                break
            elif change=='2':
                new = input('Enter the new author name : ')
                sql = 'UPDATE Books SET Author=%s WHERE BID=%s'
                break
            elif change=='3':
                new = input('Enter the new value of genre1 : ')
                sql = 'UPDATE Books SET Genre1=%s WHERE BID=%s'
                break
            elif change=='4':
                new = input('Enter the new value of genre2 : ')
                sql = 'UPDATE Books SET Genre2=%s WHERE BID=%s'
                break
            elif change=='5':
                new = input('Enter the new value of genre3 : ')
                sql = 'UPDATE Books SET Genre3=%s WHERE BID=%s'
                break
            elif change=='6':
                new = input('Enter the updated number of copies : ')
                sql = 'UPDATE Books SET Copies=%s WHERE BID=%s'
                break
            elif change=='7':
                new = input('Enter the updated status : ')
                sql = 'UPDATE Books SET Soft=%s WHERE BID=%s'
                break
            elif change=='8':
                new = input('Enter the new price : ')
                sql = 'UPDATE Books SET Price=%s WHERE BID=%s'
                break
            else:
                print('Please enter a valid option!')

        cur.execute(sql,(new,ID)); db.commit()
        print('\nData modified\n')
    else:
        print('\nBook ID not found!')

def DeleteBook():
    print('\n'+'-'*19)
    print('   Delete a Book')
    print('-'*19+'\n')
    
    ID = input('Enter the Book ID that is to be deleted : ')

    cur.execute('SELECT * FROM Books WHERE BID=%s',(ID,))
    row=cur.fetchone()
    if row not in ((None,),None):
        cur.execute('SELECT * FROM Transaction WHERE BID=%s',(ID,))
        rows = cur.fetchall()
        print(rows)
        if rows not in ((),None):
            print(len(rows),'number of copies of this book are issued\nIt cannot be deleted')
        else:
            print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')
            print('|%6s |%40s |%20s |%10s |%10s |%10s |%10s |%3s |%5s |%6s |%6s |' % 
                  (row[0],row[1][:40],row[2][:18],row[3][:10],row[4][:10],row[5][:10],row[6],row[7],row[8],row[9],row[10][4:10],row[11][4:10]))
            print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')
            ask = input('Are you sure you want to delete this book? [Y/N] : ')
            if ask in 'Yy':
                cur.execute('DELETE FROM Books WHERE BID=%s',(ID,)); db.commit()
            else:
                print('\nBook not deleted')
    else:
        print('\nBook ID not found!')

def ReadBooks():
    print('\n'+'-'*21)
    print('   The Books Table')
    print('-'*21+'\n')
    print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')
    print('|%6s |%40s |%20s |%10s |%10s |%10s |%5s |%6s |%3s |%5s |%6s |%6s |' %
          ('BID','Book Name','Author','Genre 1','Genre 2','Genre 3','Total','Issued','SC','Price','URL1','URL2'))
    print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')

    cur.execute('SELECT * FROM Books')
    rows = cur.fetchall()
    for i in rows:
        print('|%6s |%40s |%20s |%10s |%10s |%10s |%5s |%6s |%3s |%5s |%6s |%6s |' %
              (i[0],i[1][:40],i[2][:18],i[3][:10],i[4][:10],i[5][:10],i[6],i[7],i[8],i[9],i[10][4:10],i[11][4:10]))
        print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')

def AddUser():
    print('\n'+'-'*14)
    print('   New User')
    print('-'*14+'\n')

    cur.execute('SELECT MAX(UID) FROM Users')
    row = cur.fetchone()
    ID = 10000 if row==(None,) else int(row[0])

    ID+=1
    Name = input('\n\nPlease enter your name : ')
    while True:
        Num = input('\nPlease enter your mobile number : ')
        if Num.isnumeric() and len(Num)==10:
            break
        else:
            print('\nPlease enter a valid mobile number')
    while True:
        Email = input('\nPlease enter your active email address : ')
        if '@' in Email and (Email.endswith('.com') or Email.endswith('.in') or Email.endswith('.net')):
            break
        else:
            print('\nPlease enter a valid email address')
    while True:
        while True:
            Pass = input('\nPlease create a password : ')
            if not(Pass.isalpha()) and not(Pass.isnumeric()) and len(Pass)>=8:
                break
            else:
                print('\nPlease enter a stronger password with combination of numbers, alphabets and at least 8 characters')
        Pass2 = input('\nPlease confirm your password : ')
        if Pass==Pass2:
            break
        else:
            print('\nConfirmation does not match. Please create the password again.')
    Book1 = 'None'
    Book2 = 'None'
    Book3 = 'None'
    Fine = 0

    sql = 'INSERT INTO Users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    val = (ID,Name,Num,Email,Pass,Book1,Book2,Book3,Fine)
    cur.execute(sql,val); db.commit()

    print('\nThe ID number for',Name,'is',ID)


def ModifyUser(UID, Adm):
    print('\n'+'-'*22)
    print('   Modify User Data')
    print('-'*22+'\n')

    cur.execute('SELECT * FROM Users WHERE UID=%s',(UID,))
    row = cur.fetchone()
    if row not in ((None,),None):
        if Adm == False:
            pswd = input('Please enter your password again : ')
        else:
            pswd = ''
        if pswd==row[4] or Adm==True:
            print()
            print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+')
            print('|%7s |%20s |%11s |%25s |%20s |' %
                  ('UserID','Name','Mobile','Email','Pass'))
            print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+')
            print('|%7s |%20s |%11s |%25s |%20s |' %
                  (row[0],row[1][:18],row[2],row[3][:23],row[4][:18]))
            print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+')
            while True:
                change = input('\n\nOptions :\n\
1. Name\n\
2. Mobile Number\n\
3. Email ID\n\
4. Password\n\
5. Go back\n\
\nEnter the option number : ')
                if change=='1':
                    new = input('Enter you new username : ')
                    sql = 'UPDATE Users SET Name=%s WHERE UID=%s'
                elif change=='2':
                    while True:
                        Num = input('Please enter your new mobile number : ')
                        if Num.isnumeric() and len(Num)==10:
                            break
                        else:
                            print('Please enter a valid mobile number')
                    new=Num
                    sql = 'UPDATE Users SET Mobile=%s WHERE UID=%s'
                elif change=='3':
                    while True:
                        Email = input('Please enter your new active email address : ')
                        if '@' in Email and (Email.endswith('.com') or Email.endswith('.in') or Email.endswith('.net')):
                            break
                        else:
                            print('Please enter a valid email address')
                    new=Email
                    sql = 'UPDATE Users SET Email=%s WHERE UID=%s'
                elif change=='4':
                    while True:
                        while True:
                            Pass = input('Please create a new password : ')
                            if not(Pass.isalpha()) and not(Pass.isnumeric()):
                                break
                            else:
                                print('\nPlease enter a stronger password with combination of numbers, alphabets and special characters')
                        Pass2 = input('\nPlease confirm your password : ')
                        if Pass==Pass2:
                            break
                        else:
                            print('\nConfirmation does not match. Please create the password again.\n')
                    new=Pass
                    sql = 'UPDATE Users SET Pass=%s WHERE UID=%s'
                elif change=='5':
                    break
                else:
                    print('\nPlease enter a valid option')
                if change in '1234':
                    cur.execute(sql,(new,UID)); db.commit()
                    print('\nData modified\n')

        else:
            print('\nThe password is incorrect\n')

    else:
        print('\nUser ID not found!')

def DeleteUser(UID):
    cur.execute('SELECT * FROM Users WHERE UID=%s',(UID,))
    row = cur.fetchone()
    if row not in ((None,),None):
        if row[5]==row[6]==row[7]=='None' and row[8]==0:
            print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*5+'+')
            print('|%7s |%20s |%11s |%25s |%20s |%20s |%20s |%20s |%4s |' %
                  (row[0],row[1][:18],row[2],row[3][:23],row[4][:18],row[5][:18],row[6][:18],row[7][:18],row[8]))
            print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*5+'+')
            ask = input('Are you sure you want to continue? [Y/N] : ')
            if ask in 'Yy':
                cur.execute('DELETE FROM Users WHERE UID=%s',(UID,)); db.commit()
                print('User deleted!')
            else:
                print('User not deleted!')
        else:
            print('This user has books issued under this ID and/or they have fine due\nIt cannot be deleted')
    else:
        print('User ID not found!')

def ReadUsers():
    print('\n'+'-'*21)
    print('   The Users Table')
    print('-'*21+'\n')
    print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*5+'+')
    print('|%7s |%20s |%11s |%25s |%20s |%20s |%20s |%20s |%4s |' %
          ('UID','Name','Number','Email','Password','Book1','Book2','Book3','Fine'))
    print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*5+'+')

    cur.execute('SELECT * FROM Users')
    rows = cur.fetchall()
    for i in rows:
        print('|%7s |%20s |%11s |%25s |%20s |%20s |%20s |%20s |%4s |' %
              (i[0],i[1][:18],i[2],i[3][:23],i[4][:18],i[5][:18],i[6][:18],i[7][:18],i[8]))
        print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*5+'+')

def AddTrans(BID,UID,DOI,DOR,count):
    cur.execute('SELECT MAX(Sno) FROM Transaction')
    row = cur.fetchone()
    Sno = 1 if row==(None,) else int(row[0])
    sql = 'INSERT INTO Transaction VALUES (%s, %s, %s, %s, %s, %s)'
    val = (Sno,BID,UID,DOI,DOR,count)
    cur.execute(sql,val); db.commit()

def ReadTrans():
    print('\n'+'-'*27)
    print('   The Transaction Table')
    print('-'*27+'\n')
    print('+'+'-'*5+'+'+'-'*8+'+'+'-'*16+'+'+'-'*15+'+'+'-'*15+'+'+'-'*11+'+')
    print('|%4s |%7s |%15s |%14s |%14s |%10s |' % ('Sno','BID','UID','DOI','DOR','Days left'))
    print('+'+'-'*5+'+'+'-'*8+'+'+'-'*16+'+'+'-'*15+'+'+'-'*15+'+'+'-'*11+'+')

    cur.execute('SELECT * FROM Transaction')
    rows = cur.fetchall()
    for i in rows:
        print('|%4s |%7s |%15s |%14s |%14s |%10s |' % (i[0],i[1],i[2],i[3],i[4],i[5]))
        print('+'+'-'*5+'+'+'-'*8+'+'+'-'*16+'+'+'-'*15+'+'+'-'*15+'+'+'-'*11+'+')

def Login(UID):
    cur.execute('SELECT * FROM Users WHERE UID=%s',(UID,))
    row = cur.fetchone()
    if row not in ((None,),None):
        Pswd = input('Please enter your password : ')
        if row[4]==Pswd:
            Log_success=True
        else:
            print('\nIncorrect Password!')
            Log_success=False
    else:
        print('User ID not found!')
        Log_success=False
    return Log_success

def Issued(UID):
    print('\n'+'-'*18)
    print('   Issued Books')
    print('-'*18+'\n')
    cur.execute('SELECT * FROM Transaction WHERE UID=%s',(UID,))
    rows = cur.fetchall()

    if rows!=(None,):
        print('+'+'-'*51+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
        print('|%50s |%11s |%11s |%9s |' % ('Book Name','Issue Date','Return Date','Days Left'))
        print('+'+'-'*51+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
        for i in rows:
            cur.execute('SELECT Name FROM Books WHERE BID=%s',(i[1],))
            row = cur.fetchone()
            print('|%50s |%11s |%11s |%9s |' % (row[0][:48],i[3],i[4],i[5]))
            print('+'+'-'*51+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
    else:
        print('No books issued under your ID!')

def FineAmt(UID):
    cur.execute('SELECT * FROM Users WHERE UID=%s',(UID,))
    row = cur.fetchone()
    print('\nYou have a fine due of rupees',row[8])

def Search():
    print('\n'+'-'*19)
    print('   Search a Book')
    print('-'*19+'\n')

    while True:
        search = input('\n\nOptions :\n\
1. Search by name of the book\n\
2. Search by name of the author\n\
3. Search by genre\n\
4. Go back\n\
\nEnter the option number : ')
        if search=='1':
            Name = '%'+input('\n\nPlease enter the name of the book : ')+'%'
            cur.execute('SELECT * FROM Books WHERE Name LIKE %s',(Name,))
            rows = cur.fetchall()
            if rows==():
                print('\n\nNo items match you search.\nCheck your spellings.\nConsider entering lesser phrases.')
                Srch_success = False
            break
        elif search=='2':
            Name = '%'+input('\n\nPlease enter the name of the author : ')+'%'
            cur.execute('SELECT * FROM Books WHERE Author LIKE %s',(Name,))
            rows = cur.fetchall()
            if rows==():
                print('\n\nNo items match you search.\nCheck your spellings.\nConsider entering the last name of the author.')
                Srch_success = False
            break
        elif search=='3':
            Gen = '%'+input('\n\nPlease enter the desired genre : ')+'%'
            cur.execute('SELECT * FROM Books WHERE Genre1 LIKE %s OR Genre2 LIKE %s OR Genre3 LIKE %s',(Gen,Gen,Gen))
            rows = cur.fetchall()
            if rows==():
                print('\n\nNo items match your search.\nCheck your spellings.\nConsider entering a single phrase')
                Srch_success = False
            break
        elif search=='4':
            rows=()
            Srch_success = False
            break
        else:
            print('\nPlease enter a valid option!\n')
    if len(rows)>0:
        Srch_success = True
        print('\n+'+'-'*7+'+'+'-'*51+'+'+'-'*31+'+'+'-'*20+'+')
        print('|%6s |%50s |%30s |%19s |' % ('BookID','Book Name','Author','Copies available'))
        print('+'+'-'*7+'+'+'-'*51+'+'+'-'*31+'+'+'-'*20+'+')
        for i in rows:
            print('|%6s |%50s |%30s |%19s |' % (i[0],i[1],i[2],int(i[6])-int(i[7])))
            print('+'+'-'*7+'+'+'-'*51+'+'+'-'*31+'+'+'-'*20+'+')
            
    return Srch_success

def Info(BID,UID,Admin=0):
    cur.execute('SELECT * FROM Books WHERE BID=%s',(BID,))
    row = cur.fetchone()
    if row not in ((None,),None):
        while True:
            cur.execute('SELECT * FROM Books WHERE BID=%s',(BID,))
            row = cur.fetchone()
            if Admin==1:
                ask = '1'
            else:
                ask = input('\n\nOptions :\n\
1. Issue the book from the library\n\
2. Get soft copy of the book\n\
3. Buy the book for personal use\n\
4. Go back\n\
\nEnter the option number : ')
            if ask=='1':
                if int(row[6])-int(row[7])>0:
                    status = (IssueBook(UID, BID, row[1],row[7]))
                    cur.execute('UPDATE Books SET Issued=%s WHERE BID=%s',(status,BID)); db.commit()
                else:
                    print('\nSorry this book is not available right now')
                    print('Please try after a few days')
                    print('Else you can request a soft copy (if available) or buy the book from our trusted domains')
                if Admin==1:
                    break
            elif ask=='2':
                if row[8]=='Y':
                    Type = input('\n\nOptions :\n\
1. Pdf\n\
2. mobi\n\
3. epub\n\
4. txt\n\
5. fb2\n\
6. azw\n\
\nEnter the option number : ')
                    print('\nThe book',row[1],'will be mailed to you in next 6 hours')
                    print('Please check email for the book')
                    print('PLEASE NOTE THAT THE RIGHT TO COPY AND SELL THE BOOK ONLY RESTS WITH THE RESPECTIVE PUBLISHER')
                    print('IN CASE OF SUCH CHARGES, THE LIBRARY CANNOT BE HELD RESPONISBLE FOR ANYTHING')
                else:
                    print('\nSorry, this book is not available as ebook for free.')
                    print('You can issue the book from the library')
                    print('Or you can buy the ebook or paperback from our trusted domains')
            elif ask=='3':
                print('\nYou can buy the book from the following e-commerce webistes')
                print(row[10])
                print(row[11])
            elif ask=='4':
                break
            else:
                print('\nPlease enter a valid option')
    else:
        print('\nThe book ID was not found')

def IssueBook(UID, BID, BName,Copies):
    print('\n'+'-'*18)
    print('   Issue a Book')
    print('-'*18+'\n')

    cur.execute('SELECT * FROM Users WHERE UID=%s',(UID,))
    row = cur.fetchone()
    if row not in ((None,),None):
        if BName not in (row[5],row[6],row[7]):
            if row[5] == 'None':
                B1,B2,B3 = True,False,False
            elif row[6] == 'None':
                B1,B2,B3 = False,True,False
            elif row[7] == 'None':
                B1,B2,B3 = False,False,True
            else:
                print('\nYou have currently issued 3 books from the library')
                print('You cannot issue more books')
                print('Please return the previous books first to issue more books')
                B1,B2,B3 = False,False,False
                status=Copies
        else:
            print('You already have issued one copy of this book.\nYou cannot issue another one')
            B1,B2,B3 = False,False,False
            status=Copies
            
        if B1==True or B2==True or B3==True:
            DOI = datetime.datetime.now().date()
            DOR = DOI+datetime.timedelta(days=15)
            daysleft = 15

            print('+'+'-'*8+'+'+'-'*46+'+'+'-'*8+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
            print('|%7s |%45s |%7s |%11s |%11s |%9s |' % ('BookID','Book Name','UserID','Issue Date','Return Date','Days Left'))
            print('+'+'-'*8+'+'+'-'*46+'+'+'-'*8+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
            print('|%7s |%45s |%7s |%11s |%11s |%9s |' % (BID, BName, UID, DOI, DOR, daysleft))
            print('+'+'-'*8+'+'+'-'*46+'+'+'-'*8+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')

            AddTrans(BID,UID,DOI,DOR,daysleft)
            status=int(Copies)+1
            if B1==True:
                sql = 'UPDATE Users SET Book1=%s WHERE UID=%s'; val=(BName,UID)
            elif B2==True:
                sql = 'UPDATE Users SET Book2=%s WHERE UID=%s'; val=(BName,UID)
            elif B3==True:
                sql = 'UPDATE Users SET Book3=%s WHERE UID=%s'; val=(BName,UID)
            cur.execute(sql,val); db.commit
    else:
        print('\nUser ID not found')
    return status

def Return():
    print('\n'+'-'*19)
    print('   Return a Book')
    print('-'*19+'\n')
    BID = input('Enter the Book ID : ')
    cur.execute('SELECT * FROM Books WHERE BID=%s',(BID,))
    B_row = cur.fetchone()
    if B_row not in ((None,),None):
        UID = input('\nEnter the User ID for the person : ')
        cur.execute('SELECT * FROM Users WHERE UID=%s',(UID,))
        U_row = cur.fetchone()
        if U_row not in ((None,),None):
            if U_row[8] !=0:
                print('\nThe person has a fine of',U_row[8])
            if U_row[5]==B_row[1]:
                cur.execute('UPDATE Users SET Book1="None" WHERE UID=%s',(UID,)); db.commit()
                cur.execute('UPDATE Books SET Issued=Issued-1 WHERE BID=%s',(BID,)); db.commit()
                print('\nBook returned!')
            elif U_row[6]==B_row[1]:
                cur.execute('UPDATE Users SET Book2="None" WHERE UID=%s',(UID,)); db.commit()
                cur.execute('UPDATE Books SET Issued=Issued-1 WHERE BID=%s',(BID,)); db.commit()
                print('\nBook returned!')
            elif U_row[7]==B_row[1]:
                cur.execute('UPDATE Users SET Book3="None" WHERE UID=%s',(UID,)); db.commit()
                cur.execute('UPDATE Books SET Issued=Issued-1 WHERE BID=%s',(BID,)); db.commit()
                print('\nBook returned!')
            else:
                print('This User ID has not issued this book.')

            cur.execute('DELETE FROM Transaction WHERE BID=%s AND UID=%s',(BID,UID)); db.commit()

        else:
            print('User ID not found!')
    else:
        print('Book ID not found!')

def CalcFine():
    today = datetime.datetime.now().date()
    with open('Temp.txt','r+') as F:
        A=F.read()
        List = A.split('-')
        try:
            year,month,date = int(List[0]),int(List[1]),int(List[2])
            Lastcheck = datetime.date(year,month,date)
        except:
            Lastcheck = 0
        F.seek(0)
        F.write(str(today))
    cur.execute('SELECT * FROM Transaction')
    rows = cur.fetchall()
    for i in rows:
        DOR = i[4]
        if today>DOR:
            new = ((today-DOR).days)*5
            old = 0 if Lastcheck==0 else ((Lastcheck-DOR).days)*5
            amt = new-old
        else:
            amt = 0
        cur.execute('UPDATE Transaction SET DaysLeft=%s WHERE Sno=%s',((DOR-today).days,i[0])); db.commit()
        cur.execute('UPDATE Users SET Fine=Fine+%s WHERE UID=%s',(amt,i[2])); db.commit()

def DepoFine():
    print('\n'+'-'*18)
    print('   Deposit Fine')
    print('-'*18+'\n')
    UID = input('\nEnter the user ID : ')

    cur.execute('SELECT Fine FROM Users WHERE UID=%s',(UID,))
    result = cur.fetchone()
    if result not in ((None,),None):
        print('The due fine amount is',result)
        amt = input('Enter the amount deposited : ')
        cur.execute('UPDATE Users SET Fine=Fine-%s WHERE UID=%s',(amt,UID)); db.commit()
    else:
        print('User ID not found!')

def Admin():
    cur.execute('SELECT * FROM Users WHERE UID=10001')
    U_row = cur.fetchone()

    Pswd = input('Please Enter you password : ')
    if U_row[4]==Pswd:
        print('\n'+'-'*11)
        print('   ADMIN')
        print('-'*11+'\n')
        while True:
            ask = input('\nOptions :\n\
1. General functions\n\
2. Help the user\n\
3. Functions for books table\n\
4. Functions for users table\n\
5. Report generation\n\
6. Go back\n\
\nEnter the option number : ')
            if ask == '1':
                while True:
                    ask2 = input('\nOptions :\n\
1. Issue a book\n\
2. Return a book\n\
3. Deposit fine for a user\n\
4. Register new user\n\
5. Go back\n\
\nEnter the option number : ')
                    if ask2 == '1':
                        UID = input('\nEnter the User ID : ')
                        cur.execute('SELECT * FROM Users WHERE UID=%s',(UID,))
                        U_row = cur.fetchone()
                        if U_row not in ((None,),None):
                            BID = input('Enter the Book ID : ')
                            cur.execute('SELECT Name,Issued FROM Books WHERE BID=%s',(BID,))
                            B_row = cur.fetchone()
                            if B_row not in ((None,),None):
                                Info(BID,UID,Admin=1)
                            else:
                                print('\nBook ID not found!')
                        else:
                            print('\nUser ID not found!')
                    elif ask2=='2':
                        Return()
                    elif ask2=='3':
                        DepoFine()
                    elif ask2=='4':
                        AddUser()
                    elif ask2=='5':
                        break
                    else:
                        print('\nPlease enter a valid option')
            elif ask == '2':
                while True:
                    ask2 = input('\nOptions :\n\
1. Modify the user data\n\
2. Delete a user\n\
3. See issued books under a user\n\
4. Calculate the fine amount under a user\n\
5. Go back\n\
\nEnter the option number : ')
                    
                    if ask2=='1':
                        UID = input('\nEnte the User ID : ')
                        Adm = True
                        ModifyUser(UID, Adm)
                    elif ask2=='2':
                        UID = input('\nEnte the User ID : ')
                        DeleteUser(UID)
                    elif ask2=='3':
                        UID = input('\nEnte the User ID : ')
                        Issued(UID)
                    elif ask2=='4':
                        UID = input('\nEnte the User ID : ')
                        FineAmt(UID)
                    elif ask2=='5':
                        break
                    else:
                        print('\nPlease enter a valid option')
            elif ask == '3':
                while True:
                    ask2 = input('\nOptions :\n\
1. Clear the book table and enter new records\n\
2. Add new books to existing record\n\
3. Modify a book\n\
4. Delete a book\n\
5. Read the books table\n\
6. Return a book\n\
7. Go back\n\
\nEnter the option number : ')
                    if ask2=='1':
                        confirm = input('\nAre you sure you want to DELETE ALL THE BOOKS from the database? [Y/N] : ')
                        if confirm in'Yy':
                            print('File cleared')
                            cur.execute('DELETE FROM Books'); db.commit()
                            AddBooks()
                        else:
                            print('Books not deleted!')
                    elif ask2=='2':
                        AddBooks()
                    elif ask2=='3':
                        ModifyBook()
                    elif ask2=='4':
                        DeleteBook()
                    elif ask2=='5':
                        ReadBooks()
                    elif ask2=='6':
                        Return()
                    elif ask2=='7':
                        break
                    else:
                        print('\nPlease enter a valid option')
            elif ask == '4':
                while True:
                    ask2 = input('\nCOptions :\n\
1. Clear the user table and enter new records\n\
2. Add new user\n\
3. Read the user table\n\
4. Go back\n\
\nEnter the option number : ')
                    if ask2=='1':
                       confirm = input('\nAre you sure you want to DELETE ALL THE USERS from the database? [Y/N] : ')
                       if confirm in 'Yy':
                           print('File cleared')
                           cur.execute('DELETE FROM Users'); db.commit()
                           AddUser()
                       else:
                           print('Users not deleted!')
                    elif ask2=='2':
                        AddUser()
                    elif ask2=='3':
                        ReadUsers()
                    elif ask2=='4':
                        break
                    else:
                        print('\nPlease enter a valid option')
            elif ask == '5':
                Report()
            elif ask == '6':
                break
            else:
                print('\nEnter a valid command')
    else:
        print('\nIncorrect Password!')

def Report():
    while True:
        ask2 = input('\nOptions :\n\
1. Calculate fine amount for all users\n\
2. See all the books issued\n\
3. See all the users who have issued books\n\
4. Read the complete transaction table\n\
5. GO back\n\
\nEnter the option number : ')
        if ask2=='1':
            print('\n'+'-'*20)
            print('   Total Fine Due')
            print('-'*20+'\n')
            print('+'+'-'*7+'+'+'-'*5+'+')
            print('|%6s |%4s |' % ('UserID','Fine'))
            print('+'+'-'*7+'+'+'-'*5+'+')
            cur.execute('SELECT * FROM Users')
            rows = cur.fetchall()
            for i in rows:
                print('|%6s |%4s |' % (i[0],i[8]))
                print('+'+'-'*7+'+'+'-'*5+'+')

        elif ask2=='2':
            cur.execute('SELECT a.BID, Name FROM Books a,Transaction b WHERE a.BID=b.BID')
            result = cur.fetchall()
            print('+'+'-'*7+'+'+'-'*51+'+')
            print('|%6s |%50s |' % ('BookID','Book Name'))
            print('+'+'-'*7+'+'+'-'*51+'+')
            for i in result:
                print('|%6s |%50s |' % (i[0],i[1]))
                print('+'+'-'*7+'+'+'-'*51+'+')

        elif ask2=='3':
            cur.execute('SELECT UID,Book1,Book2,Book3 FROM Users')
            rows = cur.fetchall()
            print('+'+'-'*7+'+'+'-'*31+'+'+'-'*31+'+'+'-'*31+'+')
            print('|%6s |%30s |%30s |%30s |' % ('UserID','Book1','Book2','Book3'))
            print('+'+'-'*7+'+'+'-'*31+'+'+'-'*31+'+'+'-'*31+'+')
            for i in rows:
                if i[1]!='None' or i[2]!='None' or i[3]!='None':
                    print('|%6s |%30s |%30s |%30s |' % (i[0],i[1][:28],i[2][:28],i[3][:28]))
                    print('+'+'-'*7+'+'+'-'*31+'+'+'-'*31+'+'+'-'*31+'+')
        elif ask2=='4':
            ReadTrans()
        elif ask2=='5':
            break
        else:
            print('\nPlease enter a valid option')

def Help():
    print('\n'+'-'*10)
    print('   HELP')
    print('-'*10+'\n')
    print('You can register here to our library and issue books.')
    print('Free ebooks can also be downloaded for many books from this site')
    print('This site also help you to find the e-commerce website from where you can buy the book if not interested in issuing')

def TC():
    print('\n'+'-'*26)
    print('   TERMS AND CONDITIONS')
    print('-'*26+'\n')
    print('\nPLEASE NOTE THAT IT THE SOLE RESPOSIBILITY OF THE USER TO PICK THE BOOK FROM THE LIBRARY IF THEY ARE ISSUING IT FROM THIS SITE')
    print('THE LIBRARY IS NOT LIABLE TO DELIVER THE BOOKS TO THE USERS\n')
    print('The date of return will be published at the time of the issuing the book')
    print('It is the responibity of the user to return the book to the library within the informed time')
    print('Extra fine will we applicable for returning the book late')
    print('Strict actions will be taken if the book is not returned within 60 days after date of return')

#================================================================================================================================================================

print('\n'+'=' * 35)
print('     LIBRARY MANAGEMENT SYSTEM')
print('=' * 35)

try:
    cur.execute('CREATE DATABASE MyLibrary')
    cur.execute('USE MyLibrary')
    cur.execute('CREATE TABLE Books (BID INT PRIMARY KEY, Name VARCHAR(50), Author VARCHAR(25), Genre1 VARCHAR(25), Genre2 VARCHAR(25),\
Genre3 VARCHAR(25), Total INT,Issued INT, Soft CHAR(1), Price float(6,2), ExtURL1 VARCHAR(75),ExtURL2 VARCHAR(75))')
    cur.execute('CREATE TABLE Users (UID INT PRIMARY KEY, Name VARCHAR(25), Mobile CHAR(10), Email VARCHAR(20), Pass VARCHAR(20),\
Book1 VARCHAR(50), Book2 VARCHAR(50), Book3 VARCHAR(50), Fine INT)')
    cur.execute('CREATE TABLE Transaction (Sno INT PRIMARY KEY, BID INT, UID INT, DOI DATE, DOR DATE, DaysLeft INT)')
    print('\n\nThis program is being executed for the first time on this device\n\nPlease setup the program\n\nCreate an Admin/Librarian account')
    AddUser()
    print('\nNow please add books to the program')
    AddBooks()
    print('\nThank you!\nNow you can login and use this program as intended')
    F = open('Temp.txt','w'); F.close()
except:
    cur.execute('USE MyLibrary')
    CalcFine()
while True:
    start = input('\n\nOptions :\n\
1. Register as new user\n\
2. Login\n\
3. Help\n\
4. Terms and Conditions\n\
5. Quit\n\
\nEnter the option number : ')
    if start=='1':
        AddUser()
    elif start=='2':
        print('\n'+'-'*11)
        print('   Login')
        print('-'*11)
        UID = input('\nPlease enter your User ID : ')
        if UID=='10001':
            Admin()
        else:
            Log_success = Login(UID)
            if Log_success == True:
                while True:
                    ask = input('\n\nOptions :\n\
1. Search\n\
2. Modify your personal data\n\
3. See the books issued under your ID\n\
4. See the total fine due under your ID\n\
5. Go back\n\
\nEnter the option number : ')
                    if ask == '1':
                        Srch_success=(Search())
                        if Srch_success==True:
                            BID = input('\nPlease enter the Book ID from above to see options : ')
                            Info(BID,UID)
                    elif ask == '2':
                        Adm = False
                        ModifyUser(UID, Adm)
                    elif ask == '3':
                        Issued(UID)
                    elif ask == '4':
                        FineAmt(UID)
                    elif ask == '5':
                        break
                    else:
                        print('\nEnter a valid option')

    elif start=='3':
        Help()
    elif start=='4':
        TC()
    elif start=='5':
        print('\nThank you for visiting!')
        break
    else:
        print('\nPlease enter a valid option')


