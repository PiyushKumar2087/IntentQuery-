import psycopg2

connection=psycopg2.connect(user="postgres",
                            password="root@123",
                            host="localhost",
                            port="5432",
                            database="NMS")

cursor=connection.cursor()
#Creating table and inserting values
cursor.execute("CREATE TABLE Alarm(ACK BOOLEAN,severity TEXT, nodeName TEXT, nodeId TEXT)")
cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("1","Major","AF","1"))
cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("0","Critical","AMF","2"))
cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("1","Major","PCF","3"))
cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("0","Minor","UPF","4"))
cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("1","Major","SMF","5"))

cursor.execute("select *from Alarm")

print(cursor.fetchall())

### Show functionality in case of Alarms.............................................

def show_all_alarms():
    cursor.execute("SELECT *FROM Alarm")
    all_alarms=cursor.fetchall()
    return all_alarms

def show_major_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Major'")
    major=cursor.fetchall()
    return major
def show_minor_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Minor'")
    major=cursor.fetchall()
    return major

def show_critical_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Critical'")
    major=cursor.fetchall()
    return major

def show_cleared_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared'")
    cleared=cursor.fetchall()
    return cleared

def show_ACK_Major_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Major' AND ACK=true") 
    ACK_Major=cursor.fetchall()
    return ACK_Major  
def show_ACK_Minor_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Minor' AND ACK=true") 
    ACK_Minor=cursor.fetchall()
    return ACK_Minor   

def show_ACK_Critical_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Critical' AND ACK=true") 
    ACK_Critical=cursor.fetchall()
    return ACK_Critical   

def show_ACK_Cleared_alarms():
    cursor.execute("SELECT nodeName FROM Alarm WHERE severity='Cleared' AND ACK==true") 
    ACK_Cleared=cursor.fetchall()
    return ACK_Cleared   

def show_NonACK_Major_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Major' AND ACK=false") 
    NonACK_Major=cursor.fetchall()
    return NonACK_Major  

def show_NonACK_Minor_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Minor' AND ACK=false") 
    NonACK_Minor=cursor.fetchall()
    return NonACK_Minor   

def show_NonACK_Critical_alarms():
    cursor.execute("SELECT *FROM Alarm WHERE severity='Critical' AND ACK=false") 
    NonACK_Critical=cursor.fetchall()
    return NonACK_Critical   

### ACK and NON-ACK alarms based on severity, node name and nodde id............................
def ACK_all_cleared_alarms():
    cursor.execute("UPDATE Alarm SET ACK='1' WHERE severity='Cleared'")
    cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared'")
    cleared=cursor.fetchall()
    return cleared

def ACK_all_minor_alarms():
    cursor.execute("UPDATE Alarm SET ACK='1' WHERE severity='Minor'")
    cursor.execute("SELECT *FROM Alarm WHERE severity='Minor'")
    minor=cursor.fetchall()
    return minor

def ACK_all_major_alarms():
    cursor.execute("UPDATE Alarm SET ACK='1' WHERE severity='Major'")
    cursor.execute("SELECT *FROM Alarm WHERE severity='Major'")
    major=cursor.fetchall()
    return major

def ACK_all_critical_alarms():
    cursor.execute("UPDATE Alarm SET ACK='1' WHERE severity='Critical'")
    cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared'")
    critical=cursor.fetchall()
    return critical

def NonACK_all_cleared_alarms():
    cursor.execute("UPDATE Alarm SET ACK='0' WHERE severity='Cleared'")
    cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared'")
    cleared=cursor.fetchall()
    return cleared
def NonACK_all_major_alarms():
    cursor.execute("UPDATE Alarm SET ACK='0' WHERE severity='Major'")
    cursor.execute("SELECT *FROM Alarm WHERE severity='Major'")
    major=cursor.fetchall()
    return major

def NonACK_all_minor_alarms():
    cursor.execute("UPDATE Alarm SET ACK='0' WHERE severity='Minor'")
    cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared'")
    minor=cursor.fetchall()
    return minor

def NonACK_all_critical_alarms():
    cursor.execute("UPDATE Alarm SET ACK='0' WHERE severity='Critical'")
    cursor.execute("SELECT *FROM Alarm WHERE severity='Critical'")
    critical=cursor.fetchall()
    return critical


def ACK_Node():
    node_name=input("Enter node name that you want to ACK: ")
    cursor.execute("SELECT ACK FROM Alarm WHERE nodeName=node_name")
    ACK_status=cursor.fetchall()
    
    
    if(ACK_status==True):
        print("It's already ACKed")
    else:
        cursor.execute("UPDATE Alarm SET ACK='1' WHERE nodeName=node_name")
        cursor.execute("SELECT *FROM Alarm WHERE nodeName=node_name")
        ACK_node=cursor.fetchall()
        return ACK_node
        
def NonACK_Node():
    node_name=input("Enter node name that you want to NonACK: ")
    cursor.execute("SELECT ACK FROM Alarm WHERE nodeName=node_name")
    ACK_status=cursor.fetchall()
    
    
    if(ACK_status==False):
        print("It's already NonACKed")
    else:
        cursor.execute("UPDATE Alarm SET ACK='0' WHERE nodeName=node_name")
        cursor.execute("SELECT *FROM Alarm WHERE nodeName=node_name")
        ACK_node=cursor.fetchall()
        return ACK_node
        

def ACK_NodeId():
    node_ID=input("Enter node id that you want to ACK: ")
    cursor.execute("SELECT ACK FROM Alarm WHERE nodeId=node_ID")
    ACK_status=cursor.fetchone()[0]
    
    
    if(ACK_status==True):
        print("It's already ACKed")
    else:
        cursor.execute("UPDATE Alarm SET ACK='1' WHERE nodeId=nodeID")
        cursor.execute("SELECT *FROM Alarm WHERE nodeId=nodeID")
        ACK_node=cursor.fetchall()
        return ACK_node
        
def NonACK_NodeId():
    node_ID=input("Enter node id that you want to NON-ACK: ")
    cursor.execute("SELECT ACK FROM Alarm WHERE nodeId=nodeID")
    ACK_status=cursor.fetchone()[0]
    
    
    if(ACK_status==False):
        print("It's already NonACKed")
    else:
        cursor.execute("UPDATE Alarm SET ACK='0' WHERE nodeId=nodeID")
        cursor.execute("SELECT *FROM Alarm WHERE nodeId=nodeID")
        ACK_node=cursor.fetchall()
        return ACK_node
        
### Functionality of Number of online and offline devices....................................

def count_online_node():
    cursor.execute("SELECT COUNT(nodeId) FROM Alarm WHERE ACK ='1' ")
    cnt_online_node=cursor.fetchone()[0]
    return cnt_online_node

def count_offline_node():
    cursor.execute("SELECT COUNT(nodeId) FROM Alarm WHERE ACK ='0' ")
    cnt_offline_node=cursor.fetchone()[0]
    return cnt_offline_node






while True:
   intent=input("Enter your intent: ")
   
   #Intent: Show alarms
   if(intent == 'show alarms' or intent == 'show all alarms' or intent == 'alarms' ):
      print(show_all_alarms())
   elif(intent=='show major alarms' or intent=='show all major alarms' or intent=='major alarms'):
       print(show_major_alarms())
   elif(intent=='show minor alarms' or intent=='show all minor alarms' or intent=='minor alarms'):
       print(show_minor_alarms())
   elif(intent=='show critical alarms' or intent=='show all critical alarms' or intent=='critical alarms'):
       print(show_critical_alarms())
   elif(intent=='show cleared alarms' or intent=='show all cleared alarms' or intent=='cleared alarms'):
    print(show_cleared_alarms())
   elif(intent=='show ACK critical allarms' or intent=='show all ACK critical allarms'):
       print(show_ACK_Critical_alarms())
   elif(intent=='show ACK major allarms' or intent=='show all ACK major allarms'):
       print(show_ACK_Major_alarms())
   elif(intent=='show ACK minor allarms' or intent=='show all ACK minor allarms'):
       print(show_ACK_Minor_alarms()) 
   elif(intent=='show NON-ACK critical allarms' or intent=='show all NON-ACK critical allarms'):
       print(show_NonACK_Critical_alarms())
   elif(intent=='show NON-ACK major allarms' or intent=='show all NON-ACK major allarms'):
       print(show_NonACK_Major_alarms())
   elif(intent=='show NON-ACK minor allarms' or intent=='show all NON-ACK minor allarms'):
       print(show_NonACK_Minor_alarms())   
   
   #ACK OR NON-ACKing the alarms based on severity, node name and node ID.................
   elif(intent=='ACK all cleared alarm' or intent=='ackonwledge all cleared alarm'):
       print(ACK_all_cleared_alarms()) 
   elif(intent=='ACK all major alarm' or intent=='ackonwledge all major alarm'):
       print(ACK_all_major_alarms()) 
   elif(intent=='ACK all minor alarm' or intent=='ackonwledge all minor alarm'):
           print(ACK_all_minor_alarms()) 
   elif(intent=='ACK all critical alarm' or intent=='ackonwledge all critical alarm'):
       print(ACK_all_critical_alarms())
   elif(intent=='NON-ACK all cleared alarm' or intent=='non ackonwledge all cleared alarm'):
       print(NonACK_all_cleared_alarms())      
   elif(intent=='NON-ACK all major alarm' or intent=='non ackonwledge all major alarm'):
       print(NonACK_all_major_alarms()) 
   elif(intent=='NON-ACK all minor alarm' or intent=='non ackonwledge all minor alarm'):
       print(NonACK_all_minor_alarms()) 
   elif(intent=='NON-ACK all critical alarm' or intent=='non ackonwledge all critical alarm'):
       print(NonACK_all_critical_alarms())   
   elif(intent=="ACK using node name"):
       print(ACK_Node())  
   elif(intent=="nonACK using node name"):
       print(NonACK_Node())  
   elif(intent=="ACK using node id"):
       print(ACK_NodeId())  
   elif(intent=="nonACK using node id"):
       print(NonACK_NodeId()) 
       
   ### Number of online or offline device
   elif(intent=="Show total online device" or intent=="total online device" or intent=="online devices"):
       print(count_online_node())  
   elif(intent=="Show total offline device" or intent=="total offline device" or intent=="offline devices"):
       print(count_offline_node())            
   elif(intent=='exit'):
       exit()    
   else:
       print("I am not able to read your intent, plz provide readable intent :\n")
    
connection.commit()



if __name__ == "__main__":
    pass