# ----- CONFIGURE YOUR EDITOR TO USE 4 SPACES PER TAB ----- #
import settings
import sys,os
sys.path.append(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'lib'))
import pymysql as db
import random

def connection():
    ''' User this function to create your connections '''
    con = db.connect(
        settings.mysql_host, 
        settings.mysql_user, 
        settings.mysql_passwd, 
        settings.mysql_schema)
    
    return con

def create_ngrams (text, num):
    result=[]
    
    stopWords=['my','on','for','in','your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their','theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at','','i', 'to']
    punctions="!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    theText=text.lower()

    removePunctions=[]
    count=0
    for i in range(len(theText)):
        
        if theText[i] in punctions:
            if theText[count:i]!='':
                removePunctions.append(theText[count:i])

            count=i+1
            continue

    removePunctions.append(theText[count:i+1])
    
    removedStopWords=[]
    for i in removePunctions:
        if i in stopWords:
            continue
        removedStopWords.append(i)
    
    result=removedStopWords

    if num==1:
        return result
    elif num==2:
        space=" "
        newResult=[]
        for i in range(1,len(result)):
            newResult.append(result[i-1]+space+result[i])
        return newResult
    elif num==3: 
        space=" "
        newResult=[]
        for i in range(2,len(result)):
            newResult.append(result[i-2]+space+result[i-1]+space+result[i])
        return newResult
    return []

def mostcommonsymptoms(vax_name):
    
    # Create a new connection
    con=connection()
    # Create a cursor on the connection
    cur=con.cursor()

    sql=        "SELECT v.Symptoms "
    sql= sql +  "FROM Vaccination v " 
    sql= sql +  "WHERE v.Vaccines_Vax_Name = \""+ str(vax_name)+ "\"" 
    try:
        cur.execute(sql)
        results=cur.fetchall()
    except:
        results=[("ERROR","ERROR")]

    InTextForm=[]
    for i in results:
        InTextForm.append(i[0])

    keyWords={}
    for i in InTextForm:
        words=create_ngrams(i,3)
        for j in words:
            if j in keyWords.keys():
                keyWords[j]+=1
            else:
                keyWords[j]=1

    theList=[]
    for j in range(30):
        maxkey=0
        maxvalue=-1
        for i in keyWords.keys():
            if keyWords[i]>maxvalue:
                maxkey=i
                maxvalue=keyWords[i]

        theList.append(maxkey)
        keyWords[maxkey]=0

    print(theList)
    print()
    theReturn=[("vax_name","result"),(vax_name,theList)]
    print(theReturn)
    return theReturn

def buildnewblock(blockfloor):
   # Create a new connection
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    
    sql = " SELECT count(bl.BlockCode) "
    sql = sql + " FROM Block bl "
    sql = sql + " WHERE bl.BlockFloor = "+ str(blockfloor) +" "

    try:
        cur.execute(sql)
        results=cur.fetchall()
    except:
        results=("ERROR")

    for row in results:
        numOfBlocks = row[0]
    
    if(numOfBlocks > 8):
        answer = "error"
    else:
        answer = "ok"
        flag = True
        for i in range(1, 9, 1):
            sql = "SELECT b.BlockCode FROM Block b WHERE b.BlockFloor = "+ str(blockfloor) +""
            cur.execute(sql)
            res = cur.fetchall()
            for row in res:
                num = row[0]
                if(num == i):
                    flag = False
            if(flag == True):
                numOfBlocks = i
            flag = True    
        
        try:
            sql="INSERT INTO BLOCK (BlockFloor, BlockCode) VALUES("+ str(blockfloor) +" , "+ str(numOfBlocks) +" ) "
            cur.execute(sql)
            con.commit()
        except:
            results = ("ERROR")
            return [("result:",),("error",)]

        entries = []
        rooms = ["single", "double", "triple", "quadruple"]
        num = random.randint(1, 5)
        for i in range(0, num, 1):
            entries.append(1000*int(blockfloor,10) + 100*(numOfBlocks) + 10*0 + i)
            num = random.randint(0, 3)
            sql=" INSERT INTO ROOM(RoomNumber, RoomType, BlockFloor, BlockCode, Unavailable) VALUES("+ str(entries[i]) +" , \""+ str(rooms[num]) +"\" , "+ str(blockfloor) +", "+ str(numOfBlocks) +", 0 ) "
            cur.execute(sql)

    try:
        con.commit()
    except:
        return[("result:",),("Wrong with Database",)]
    return [("result:",),(answer,)]

def findnurse(x,y):

    # Create a new connection
    
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    sql=        "SELECT n.Name,n.EmployeeID,count(distinct v.Patient_SSN) "
    sql= sql +  "FROM Nurse n, On_Call o, Appointment a, Vaccination v " 
    sql= sql +  "WHERE n.EmployeeID=o.Nurse and n.EmployeeID=a.PrepNurse and n.EmployeeID=v.nurse_EmployeeID and o.BlockFloor="+ str(x)+ " " 
    sql= sql +  "group by n.EmployeeID having count(a.Patient)>="+ str(y)+ " and count(distinct o.BlockCode)=(select count(distinct b.BlockCode) from block b where b.BlockFloor="+str(x)+") "

    try:
        cur.execute(sql)
        results=cur.fetchall()
    except:
        results=[("ERROR","ERROR","ERROR")]
        con.rollback()

    theReturn=[("Nurse", "ID", "Number of patients")]
    for i in results:
        theReturn.append(i)
    
    return theReturn

def patientreport(patientName):
    # Create a new connection
    con=connection()

    # Create a cursor on the connection
    cur = con.cursor()
    sql = " SELECT ph.Name , nr.Name, tr.Name, tr.Cost, st.StayEnd, st.Room, r.BlockFloor, r.BlockCode "
    sql = sql + " FROM Physician ph, Nurse nr, Treatment tr, Stay st, Room r, Undergoes u, Patient p "
    sql = sql + " WHERE strcmp(p.Name, '%s') = 0 and u.Patient = p.SSN and u.Physician = ph.EmployeeID and u.AssistingNurse = nr.EmployeeID and u.Treatment = tr.Code and st.StayID = u.stay  and st.Room = r.RoomNumber " % (patientName)

    try:
        cur.execute(sql)
        results=cur.fetchall()
    except:
        results=[("ERROR","ERROR","ERROR","ERROR","ERROR","ERROR","ERROR","ERROR")]
        con.rollback()

    theReturn = [("Physician", "Nurse","Treatement", "Cost", "Stay End", "Room", "Floor", "Block"),]
    for i in results:
        theReturn.append(i)
    
    return theReturn