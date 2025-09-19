import csv
import datetime

def NewBooks():    
    with open('Books.csv','w',newline='') as F:
        L=[]
        W=csv.writer(F)
        W.writerow(['BookID','Name','Author','Genre1','Genre2','Genre3','Copies','Issued','SC','Price','Ext URL1','Ext URL2'])
        ID=1001

        
        while True:            
            Name=input('\nEnter the name of book : ')
            Author=input('Enter the name of the author : ')
            Genre1=input('Enter the genre of the book : ')
            Genre2=input('Enter the 2nd genre [press enter if none] : ')
            Genre2='None' if Genre2=='' else Genre2
            Genre3=input('Enter the 3rd genre [press enter if none] : ')
            Genre3='None' if Genre3=='' else Genre3
            Copies=input('Enter the number of copies available in the library : ')
            Issued = 0
            Softcopy=input('Is the soft copy of the book available [Y/N] : ').upper()
            Price=input('Enter the price of the book : ')
            URL1='www.amazon.in/buy-'+Name+'-...'
            URL2='www.flipkart.com/buy-'+Name+'-...'
            L.append([ID,Name,Author,Genre1,Genre2,Genre3,Copies,Issued,Softcopy,Price,URL1,URL2])
            ID+=1
            ask=input('\n\nEnter more books? [Y/N] : ')
            if ask in 'Nn':
                break
                
        W.writerows(L)

def AddBook():

    print('\n'+'-'*15)
    print('   Add Books')
    print('-'*15+'\n')
    
    with open('Books.csv','r+',newline='') as F:
        L=[]
        R=csv.reader(F)
        L.append(next(R))
        for i in R:
            L.append(i)
            ID=int(i[0])
        while True:
            ID+=1
            Name=input('\nEnter the name of book : ')
            Author=input('Enter the name of the author : ')
            Genre1=input('Enter the genre of the book : ')
            Genre2=input('Enter the 2nd genre [press enter if none] : ')
            Genre2='None' if Genre2=='' else Genre2
            Genre3=input('Enter the 3rd genre [press enter if none] : ')
            Genre3='None' if Genre3=='' else Genre3
            Copies=input('Enter the number of copies available in the library : ')
            Issued = 0
            Softcopy=input('Is the soft copy of the book available [Y/N] : ').upper()
            Price=input('Enter the price of the book : ')
            URL1='www.amazon.in/buy-'+Name+'-...'
            URL2='www.flipkart.com/buy-'+Name+'-...'
            L.append([ID,Name,Author,Genre1,Genre2,Genre3,Copies,Issued,Softcopy,Price,URL1,URL2])
            ask=input('\n\nEnter more books? [Y/N] : ')
            if ask in 'Nn':
                break
        F.seek(0)
        F.truncate()
        W=csv.writer(F)
        W.writerows(L)

def ModifyBook():
    print('\n'+'-'*19)
    print('   Modify a Book')
    print('-'*19+'\n')
    with open('Books.csv','r+',newline='') as F:
        L=[]
        count = 0
        ID = input('Enter the book id that is to be modified : ')
        R = csv.reader(F)
        for i in R:
            if i[0]==ID:
                count +=1
                print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')
                print('|%6s |%40s |%20s |%10s |%10s |%10s |%5s |%6s |%3s |%5s |%6s |%6s |' %
                      (i[0],i[1][:40],i[2][:18],i[3][:10],i[4][:10],i[5][:10],i[6][:10],i[7],i[8],i[9],i[10][4:10],i[11][4:10]))
                print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')

                while True:
                    change = input('\n\nOptions :\n\
1. Name of book\n\
2. Author of the book\n\
3. Genre1 of the book\n\
4. Genre2 of the book\n\
5. Genre3 of the book\n\
6. Number of copies in library\n\
7. Availability of softcopy\n\
8. Price of the book\n\
9. Go back\n\
\nEnter the option number : ')
                    if change=='1':
                        i[1] = input('Enter new name of the book : ');print('Data Modified')
                    elif change=='2':
                        i[2] = input('Enter the new author name : ');print('Data Modified')
                    elif change=='3':
                        i[3] = input('Enter the new value for genre1 : ');print('Data Modified')
                    elif change=='4':
                        i[4] = input('Enter the new value for genre2 : ');print('Data Modified')
                    elif change=='5':
                        i[5] = input('Enter the new value for genre3 : ');print('Data Modified')
                    elif change=='6':
                        i[6] = input('Enter the new number of copies : ');print('Data Modified')
                    elif change=='7':
                        i[7] = input('Enter the new status [Y/N] : ');print('Data Modified')
                    elif change=='8':
                        i[8] = input('Enter the new price of the book : ');print('Data Modified')
                    elif change=='9':
                        break
                    else:
                        print('\nPlease enter a valid option')

            L.append(i)
        if count == 0:
            print('\nBook id not found!')
        F.seek(0)
        F.truncate()
        W=csv.writer(F)
        W.writerows(L)

def DeleteBook():
    print('\n'+'-'*19)
    print('   Delete a Book')
    print('-'*19+'\n')
    with open('Books.csv','r+',newline='') as F:
        L=[]
        count = 0
        ID = input('Enter the book id that is to be deleted : ')
        R = csv.reader(F)
        for i in R:
            if i[0]==ID:
                if i[7]>'0':
                    print('Some copies of this book are issued\nIt cannot be deleted')
                else:
                    print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')
                    print('|%6s |%40s |%20s |%10s |%10s |%10s |%5s |%6s |%3s |%5s |%6s |%6s |' %
                          (i[0],i[1][:40],i[2][:18],i[3][:10],i[4][:10],i[5][:10],i[6][:10],i[7],i[8],i[9],i[10][4:10],i[11][4:10]))
                    print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')
                    count +=1
                    print('There are',i[6],'number of copies in the library at the moment')
                    ask = input('Are you sure you want to delete all data for this book? [Y/N] : ')
                    if ask in 'Yy':
                        continue
                    else:
                        print('Book not deleted')
            L.append(i)
        if count == 0:
            print('\nBook id not found!')
        F.seek(0)
        F.truncate()
        W=csv.writer(F)
        W.writerows(L)

def ReadBooks():
    print('\n'+'-'*21)
    print('   The Books Table')
    print('-'*21+'\n')
    with open('Books.csv','r',newline='') as F:
        R = csv.reader(F)
        for i in R:
            print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')
            print('|%6s |%40s |%20s |%10s |%10s |%10s |%5s |%6s |%3s |%5s |%6s |%6s |' %
                  (i[0],i[1][:40],i[2][:18],i[3][:10],i[4][:10],i[5][:10],i[6][:10],i[7],i[8],i[9],i[10][4:10],i[11][4:10]))
        print('+'+'-'*7+'+'+'-'*41+'+'+'-'*21+'+'+'-'*11+'+'+'-'*11+'+'+'-'*11+'+'+'-'*6+'+'+'-'*7+'+'+'-'*4+'+'+'-'*6+'+'+'-'*7+'+'+'-'*7+'+')

def NewUsers():
    with open('Users.csv','w',newline='') as F:
        L=[]
        W = csv.writer(F)
        W.writerow(['UserID','Name','Mobile','Email','Pass','Book1','Book2','Book3','Fine'])
        ID = 10001
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
        L.append([ID,Name,Num,Email,Pass,Book1,Book2,Book3,Fine])
        print('\nThe ID number for',Name,'is',ID)
        W.writerows(L)

def AddUser():
    print('\n'+'-'*14)
    print('   New User')
    print('-'*14+'\n')
    with open('Users.csv','r+',newline='') as F:
        L = []
        R = csv.reader(F)
        L.append(next(R))
        for i in R:
            L.append(i)
            ID = int(i[0])
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
                if not(Pass.isalpha()) and not(Pass.isnumeric()):
                    break
                else:
                    print('\nPlease enter a stronger password with combination of numbers, alphabets and special characters')
            Pass2 = input('\nPlease confirm your password : ')
            if Pass==Pass2:
                break
            else:
                print('\nConfirmation does not match. Please create the password again.')
        Book1 = 'None'
        Book2 = 'None'
        Book3 = 'None'
        Fine = 0
        L.append([ID,Name,Num,Email,Pass,Book1,Book2,Book3,Fine])
        print('\nThe ID number for',Name,'is',ID)
        F.seek(0)
        F.truncate()
        W=csv.writer(F)
        W.writerows(L)

def ModifyUser(UID, Adm):
    print('\n'+'-'*22)
    print('   Modify User Data')
    print('-'*22+'\n')
    with open('Users.csv','r+',newline='') as F:
        L=[]
        count = 0
        R = csv.reader(F)
        for i in R:
            if i[0]==UID:
                count += 1
                if Adm == False:
                    pswd = input('Please enter your password again : ')
                else:
                    pswd = ''
                if pswd==i[4] or Adm==True:
                    print()
                    print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+')
                    print('|%7s |%20s |%11s |%25s |%20s |' % ('UserID','Name','Mobile','Email','Pass'))
                    print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+')
                    print('|%7s |%20s |%11s |%25s |%20s |' % (i[0],i[1][:18],i[2],i[3][:23],i[4][:18]))
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
                            i[1] = input('Enter you new username : ')
                            print('Name edited')
                            break
                        elif change=='2':
                            while True:
                                Num = input('Please enter your new mobile number : ')
                                if Num.isnumeric() and len(Num)==10:
                                    break
                                else:
                                    print('Please enter a valid mobile number')
                            i[2]=Num
                            print('Mobile number modified')
                            break
                        elif change=='3':
                            while True:
                                Email = input('Please enter your new active email address : ')
                                if '@' in Email and (Email.endswith('.com') or Email.endswith('.in') or Email.endswith('.net')):
                                    break
                                else:
                                    print('Please enter a valid email address')
                            i[3]=Email
                            print('Email address is modified')
                            break
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
                            i[4]=Pass
                            print('Password modified')
                            break
                        elif change=='5':
                            break
                        else:
                            print('\nPlease enter a valid option')
                else:
                    print('\nThe password is incorrect\n')
            
            L.append(i)
        if count==0:
            print('ID not found')
        F.seek(0)
        F.truncate()
        W=csv.writer(F)
        W.writerows(L)

def DeleteUser(UID):
    print('\n'+'-'*19)
    print('   Delete a User')
    print('-'*19+'\n')
    with open('Users.csv','r+',newline='') as F:
        L=[]
        count = 0
        R = csv.reader(F)
        for i in R:
            if i[0]==UID:
                count +=1
                if i[5]==i[6]==i[7]=='None' and i[8]=='0':
                    print('User deleted!')
                    continue
                else:
                    print('This user has books issued under this ID and/or they have fine due\nIt cannot be deleted')
            L.append(i)
        if count == 0:
            print('\nUser id not found!')
        F.seek(0)
        F.truncate()
        W=csv.writer(F)
        W.writerows(L)

def ReadUsers():
    print('\n'+'-'*21)
    print('   The Users Table')
    print('-'*21+'\n')
    with open('Users.csv','r',newline='') as F:
        R = csv.reader(F)
        for i in R:
            print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*5+'+')
            print('|%7s |%20s |%11s |%25s |%20s |%20s |%20s |%20s |%4s |' %
                  (i[0],i[1][:18],i[2],i[3][:23],i[4][:18],i[5][:18],i[6][:18],i[7][:18],i[8]))

        print('+'+'-'*8+'+'+'-'*21+'+'+'-'*12+'+'+'-'*26+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*21+'+'+'-'*5+'+')

def NewTrans():
    with open('Transaction.csv','w',newline='') as F:
        L=[]
        W = csv.writer(F)
        W.writerow(['Book ID', 'Issued by [ID]', 'Date of Issue', 'Date of Return','Days left'])

def AddTrans(BID,UID,DOI,DOR,count):
    with open('Transaction.csv','r+',newline='') as F:
        L=[]
        R = csv.reader(F)
        for i in R:
            L.append(i)
        L.append([BID,UID,DOI,DOR,count])
        F.seek(0)
        F.truncate()
        W=csv.writer(F)
        W.writerows(L)

def ReadTrans():
    print('\n'+'-'*27)
    print('   The Transaction Table')
    print('-'*27+'\n')
    with open('Transaction.csv','r',newline='') as F:
        R = csv.reader(F)
        for i in R:
            print('+'+'-'*8+'+'+'-'*16+'+'+'-'*15+'+'+'-'*15+'+'+'-'*11+'+')
            print('|%7s |%15s |%14s |%14s |%10s |' %
                  (i[0],i[1],i[2],i[3],i[4]))

        print('+'+'-'*8+'+'+'-'*16+'+'+'-'*15+'+'+'-'*15+'+'+'-'*11+'+')

def Login(UID):
    with open('Users.csv','r',newline='') as F:
        R = csv.reader(F)
        for i in R:
            if i[0]==UID:
                Pswd = input('Please enter you password : ')
                if i[4]==Pswd:
                    print('\nWelcome!\n')
                    Log_success = True
                    break
                else:
                    print('\nIncorrect Password!')
                    Log_success = False
                    break
        else:
            print('\nUser ID not found!')
            Log_success = False
    return Log_success

def Issued(UID):
    print('\n'+'-'*18)
    print('   Issued Books')
    print('-'*18+'\n')
    with open('Transaction.csv','r',newline='') as F:
        count=0
        R=csv.reader(F)
        print('+'+'-'*51+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
        print('|%50s |%11s |%11s |%9s |' % ('Book Name','Issue Date','Return Date','Days Left'))
        print('+'+'-'*51+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
        for i in R:
            if i[1]==UID:
                count+=1
                with open('Books.csv','r',newline='') as Fb:
                    Rb=csv.reader(Fb)
                    for x in Rb:
                        if x[0]==i[0]:
                            print('|%50s |%11s |%11s |%9s |' % (x[1][:48],i[2],i[3],i[4]))
                            print('+'+'-'*51+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
        if count==0:
            print('\n','No books issued under your name!')

def FineAmt(UID):
    with open('Users.csv','r',newline='') as F:
        R = csv.reader(F)
        for i in R:
            if i[0] == UID:
                print('\nYou have a fine due of rupees',i[8])

def Search():
    print('\n'+'-'*19)
    print('   Search a Book')
    print('-'*19+'\n')
    with open('Books.csv','r',newline='') as F:
        R = csv.reader(F)
        L = []
        search = input('\n\nOptions :\n\
1. Search by name of the book\n\
2. Search by name of the author\n\
3. Search by genre\n\
4. Go back\n\
\nEnter the option number : ')
        if search=='1':
            Name = input('\n\nPlease enter the name of the book : ')
            count=0
            for i in R:
                if Name.lower() in i[1].lower():
                    L.append(i)
                    count+=1
            if count==0:
                print('\n\nNo items match you search.\nCheck your spellings.\nConsider entering lesser phrases.')
                Srch_success = False
        elif search=='2':
            Name = input('\n\nPlease enter the name of the author : ')
            count=0
            for i in R:
                if Name.lower() in i[2].lower():
                    L.append(i)
                    count+=1
            if count==0:
                print('\n\nNo items match you search.\nCheck your spellings.\nConsider entering the last name of the author.')
                Srch_success = False
        elif search=='3':
            Gen = input('\n\nPlease enter the desired genre : ')
            count=0
            for i in R:
                if Gen.lower() in i[3].lower() or Gen.lower() in i[4].lower() or Gen.lower() in i[5].lower():
                    L.append(i)
                    count+=1
            if count==0:
                print('\n\nNo items match your search.\nCheck your spellings.\nConsider entering a single phrase')
                Srch_success = False
        elif search=='4':
            pass
        else:
            print('\nPlease enter a valid option!\n')
            Search()
        if len(L)>0:
            Srch_success = True
            print('\n+'+'-'*7+'+'+'-'*51+'+'+'-'*31+'+'+'-'*20+'+')
            print('|%6s |%50s |%30s |%19s |' % ('BookID','Book Name','Author','Copies available'))
            print('+'+'-'*7+'+'+'-'*51+'+'+'-'*31+'+'+'-'*20+'+')
            for i in L:
                print('|%6s |%50s |%30s |%19s |' % (i[0],i[1],i[2],int(i[6])-int(i[7])))
                print('+'+'-'*7+'+'+'-'*51+'+'+'-'*31+'+'+'-'*20+'+')
            
    return Srch_success

def Info(BID,UID,Admin=0):
    with open('Books.csv','r+',newline='') as F:
        L = []
        count = 0
        R = csv.reader(F)
        for i in R:
            if i[0]==BID:
                count += 1
                while True:
                    if Admin==1:
                        ask='1'
                    else:
                        ask = input('\n\nOptions :\n\
1. Issue the book from the library\n\
2. Get soft copy of the book\n\
3. Buy the book for personal use\n\
4. Go back\n\
\nEnter the option number : ')
                    if ask=='1':
                        if int(i[6])-int(i[7])>0:
                            i[7] = (IssueBook(UID, BID, i[1],i[7]))
                        else:
                            print('\nSorry this book is not available right now')
                            print('Please try after a few days')
                            print('Else you can request a soft copy (if available) or buy the book from our trusted domains')
                        if Admin==1:
                            break
                    elif ask=='2':
                        if i[8]=='Y':
                            Type = input('\n\nOptions :\n\
1. Pdf\n\
2. mobi\n\
3. epub\n\
4. txt\n\
5. fb2\n\
6. azw\n\
\nEnter the option number : ')
                            print('\nThe book',i[1],'will be mailed to you in next 6 hours')
                            print('Please check email for the book')
                            print('PLEASE NOTE THAT THE RIGHT TO COPY AND SELL THE BOOK ONLY RESTS WITH THE RESPECTIVE PUBLISHER')
                            print('IN CASE OF SUCH CHARGES, THE LIBRARY CANNOT BE HELD RESPONSIBLE FOR ANYTHING')
                        else:
                            print('\nSorry, this book is not available as ebook for free.')
                            print('You can issue the book from the library')
                            print('Or you can buy the ebook or paperback from our trusted domains')
                    elif ask=='3':
                        print('\nYou can buy the book from the following e-commerce websites')
                        print(i[10])
                        print(i[11])
                    elif ask=='4':
                        break
                    else:
                        print('\nPlease enter a valid option')
            
            L.append(i)
        if count == 0:
            print('\nThe book ID was not found')
        F.seek(0)
        F.truncate()
        W=csv.writer(F)
        W.writerows(L)

def IssueBook(UID, BID, BName,Copies):
    print('\n'+'-'*18)
    print('   Issue a Book')
    print('-'*18+'\n')
    with open('Users.csv','r+',newline='') as Fu:
        L2 = []
        count = 0
        Ru = csv.reader(Fu)
        for x in Ru:
            if x[0] == UID:
                count += 1
                if BName not in (x[5],x[6],x[7]):
                    if x[5] == 'None':
                        B1,B2,B3 = True,False,False
                    elif x[6] == 'None':
                        B1,B2,B3 = False,True,False
                    elif x[7] == 'None':
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
                    daysleft = (DOR-DOI).days

                    print('+'+'-'*8+'+'+'-'*46+'+'+'-'*8+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
                    print('|%7s |%45s |%7s |%11s |%11s |%9s |' % ('BookID','Book Name','UserID','Issue Date','Return Date','Days Left'))
                    print('+'+'-'*8+'+'+'-'*46+'+'+'-'*8+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')
                    print('|%7s |%45s |%7s |%11s |%11s |%9s |' % (BID, BName, UID, DOI, DOR, daysleft))
                    print('+'+'-'*8+'+'+'-'*46+'+'+'-'*8+'+'+'-'*12+'+'+'-'*12+'+'+'-'*10+'+')

                    AddTrans(BID,UID,DOI,DOR,daysleft)
                    status=int(Copies)+1
                    if B1==True:
                        x[5] = BName
                    elif B2==True:
                        x[6] = BName
                    elif B3==True:
                        x[7] = BName
            L2.append(x)
        if count == 0:
            print('\nUser ID not found')
        Fu.seek(0)
        Fu.truncate()
        Wu=csv.writer(Fu)
        Wu.writerows(L2)
    return status

def Return():
    print('\n'+'-'*19)
    print('   Return a Book')
    print('-'*19+'\n')
    UID = input('\nEnter the User ID for the person : ')
    BID = input('Enter the Book ID : ')
    with open('Books.csv','r+',newline='')as Fb:
        Lb = []
        countb = 0
        Rb = csv.reader(Fb)
        for i in Rb:
            if i[0]==BID:
                countb += 1
                
                with open('Users.csv','r+',newline='')as Fu:
                    Lu=[]
                    countu = 0
                    Ru = csv.reader(Fu)
                    for x in Ru:
                        if UID==x[0]:
                            countu += 1
                            
                            if x[8] !='0':
                                print('\nThe person has a fine of',x[8])
                            if x[5]==i[1]:
                                x[5] = 'None'
                                i[7] = int(i[7])-1
                                print('\nBook returned!')
                            elif x[6]==i[1]:
                                x[6] = 'None'
                                i[7] = int(i[7])-1
                                print('\nBook returned!')
                            elif x[7]==i[1]:
                                x[7] = 'None'
                                i[7] = int(i[7])-1
                                print('\nBook returned!')
                            else:
                                print('This User ID has not issued this book.')
                        Lu.append(x)
                    if countu==0:
                        print('\nUser ID not found')
                    Fu.seek(0)
                    Fu.truncate()
                    Wu=csv.writer(Fu)
                    Wu.writerows(Lu)
                with open('Transaction.csv','r+',newline='')as Ft:
                    Lt = []
                    Rt = csv.reader(Ft)
                    for y in Rt:
                        if BID==y[0]:
                            continue
                        Lt.append(y)
                    Ft.seek(0)
                    Ft.truncate()
                    Wt=csv.writer(Ft)
                    Wt.writerows(Lt)
            Lb.append(i)
        if  countb==0:
            print('Book ID not found')
        Fb.seek(0)
        Fb.truncate()
        Wb=csv.writer(Fb)
        Wb.writerows(Lb)

def CalcFine():
    today = datetime.datetime.now().date()
    with open('Temp.txt','r+') as F:
        A=F.read()
        NL = A.split('-')
        try:
            year,month,date = int(NL[0]),int(NL[1]),int(NL[2])
            Lastcheck = datetime.date(year,month,date)
        except:
            Lastcheck = 0
        F.seek(0)
        F.truncate()
        F.write(str(today))
    with open('Transaction.csv','r+',newline='') as Ft:
        Lt = []
        Rt = csv.reader(Ft)
        Lt.append(next(Rt))
        for i in Rt:
            List = i[3].split('-')
            year,month,date = int(List[0]),int(List[1]),int(List[2])
            DOR = datetime.date(year,month,date)
            if today>DOR:
                new = ((today-DOR).days)*5
                old = 0 if Lastcheck==0 else ((Lastcheck-DOR).days)*5
                amt = new-old
            else:
                amt = 0
            i[4] = (DOR-today).days

            with open('Users.csv','r+',newline='') as Fu:
                Lu = []
                Ru = csv.reader(Fu)
                for x in Ru:
                    if x[0]==i[1]:
                        x[8] = int(x[8])+int(amt)
                    Lu.append(x)
                Fu.seek(0)
                Fu.truncate()
                Wu = csv.writer(Fu)
                Wu.writerows(Lu)
                
            Lt.append(i)
        Ft.seek(0)
        Ft.truncate()
        Wt = csv.writer(Ft)
        Wt.writerows(Lt)

def DepoFine():
    print('\n'+'-'*18)
    print('   Deposit Fine')
    print('-'*18+'\n')
    UID = input('\nEnter the user ID : ')
    with open('Users.csv','r+',newline='') as Fu:
        Lu = []
        Ru = csv.reader(Fu)
        for i in Ru:
            if UID==i[0]:
                print('\nThe due fine amount is',i[8])
                amt = int(input('Enter the amount deposited : '))
                i[8] = int(i[8])-int(amt)
            Lu.append(i)
        Fu.seek(0)
        Fu.truncate()
        Wu = csv.writer(Fu)
        Wu.writerows(Lu)
        
def Admin():
    with open('Users.csv','r',newline='') as F:
        R = csv.reader(F)
        for i in R:
            if i[0]=='10001':
                Pswd = input('Please enter you password : ')
                if i[4]==Pswd:
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
                                    with open('Users.csv','r',newline='')as Fu:
                                        countu=0
                                        Ru = csv.reader(Fu)
                                        for i in Ru:
                                            if i[0]==UID:
                                                countu+=1
                                        if countu==0:
                                            print('\nUser ID not found')
                                        else:
                                            BID = input('Enter the Book ID : ')
                                            with open('Books.csv','r',newline='') as Fb:
                                                countx=0
                                                Rb = csv.reader(Fb)
                                                for i in Rb:
                                                    if i[0]==BID:
                                                        countx+=1
                                                if countx==0:
                                                    print('\nBook ID not found')
                                                else:
                                                    Info(BID,UID,Admin=1)
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
                                        NewBooks()
                                elif ask2=='2':
                                    AddBook()
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
                                       NewUsers()
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
                    break
                else:
                    print('\nIncorrect Password!')
                    break 

def Report():
    while True:
        ask2 = input('\nOptions :\n\
1. Calculate fine amount for all users\n\
2. See all the books issued\n\
3. See all the users who have issued books\n\
4. Read the complete transaction table\n\
5. Go back\n\
\nEnter the option number : ')
        if ask2=='1':
            print('\n'+'-'*20)
            print('   Total Fine Due')
            print('-'*20+'\n')
            print('+'+'-'*7+'+'+'-'*5+'+')
            with open('Users.csv','r+',newline='') as Fu:
                Ru = csv.reader(Fu)
                for x in Ru:
                    print('|%6s |%4s |' % (x[0],x[8]))
                    print('+'+'-'*7+'+'+'-'*5+'+')

        elif ask2=='2':
            with open('Transaction.csv','r',newline='') as Ft:
                R = csv.reader(Ft)
                print('+'+'-'*7+'+'+'-'*51+'+')
                print('|%6s |%50s |' % ('BookID','Book Name'))
                print('+'+'-'*7+'+'+'-'*51+'+')
                for x in R:
                    with open('Books.csv','r',newline='') as F:
                        R = csv.reader(F)
                        for i in R:
                            if i[0]==x[0]:
                                print('|%6s |%50s |' % (i[0],i[1]))
                                print('+'+'-'*7+'+'+'-'*51+'+')
        elif ask2=='3':
            with open('Users.csv','r',newline='') as F:
                R = csv.reader(F)
                next(R)
                print('+'+'-'*7+'+'+'-'*31+'+'+'-'*31+'+'+'-'*31+'+')
                print('|%6s |%30s |%30s |%30s |' % ('UserID','Book 1','Book 2','Book 3'))
                print('+'+'-'*7+'+'+'-'*31+'+'+'-'*31+'+'+'-'*31+'+')
                for i in R:
                    if i[5]!='None' or i[6]!='None' or i[7]!='None':
                        print('|%6s |%30s |%30s |%30s |' % (i[0],i[5][:28],i[6][:28],i[7][:28]))
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
    print('\nPLEASE NOTE THAT IT THE SOLE RESPONSIBILITY OF THE USER TO PICK THE BOOK FROM THE LIBRARY IF THEY ARE ISSUING IT FROM THIS SITE')
    print('THE LIBRARY IS NOT LIABLE TO DELIVER THE BOOKS TO THE USERS\n')
    print('The date of return will be published at the time of the issuing the book')
    print('It is the responsibility of the user to return the book to the library within the informed time')
    print('Extra fine will we applicable for returning the book late')
    print('Strict actions will be taken if the book is not returned within 60 days after date of return')

#========================================================================
    
print('\n'+'=' * 35)
print('     LIBRARY MANAGEMENT SYSTEM')
print('=' * 35)

try:
    f1 = open('Books.csv','r',newline='');f1.close()
    f2 = open('Users.csv','r',newline='');f2.close()
    f3 = open('Books.csv','r',newline='');f3.close()
    CalcFine()
except:
    print('\n\nThis program is being executed for the first time on this device\n\nPlease setup the program\n\nCreate an Admin/Librarian account')
    NewUsers()
    print('\nNow please add books to the program')
    NewBooks()
    NewTrans()
    print('Thank you!\nNow you can login and use this program as intended')
    F = open('Temp.txt','w'); F.close()

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




