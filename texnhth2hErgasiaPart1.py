from math import fabs
from random import randrange,randint
from typing import Sized
import random as randi
temp=[]
def GenTemp():
    global temp
    temp=[]
    bitakis=""
    for k in range (0,71):      #Προσθετουμε στην λιστα temp 11 εφταψηφιους αριθμους με τα ψηφια τους να ειναι 0 ή 1
        ranbool=randi.getrandbits(1)
        bitakis+=str(ranbool)
        if(len(bitakis)==7):
            temp.append(bitakis)
            bitakis=""
temp1=[]
temp2=[]
gridP=[]
stop=0
def GenAlgoP(grammh,endofloop): #Μπαινουμε στην GenAlgoP ωστε να βρουμε το γραμμα Π
    global stop
    stop=0
    while(endofloop):
        oxitosorandom=0
        global temp
        global temp2
        temp1=[]
        stop+=1
        countnum=0
        visited=[] 
        for i in range(0,len(temp)):
            if(grammh==1):                              #Εαν ειμαστε στην πρωτη γραμμη
                visited.append(temp[i].count('01'))     #Προσθετει στην visited τις φορες που βρηκε το '01'΄και το '10' στο temp
                visited[i]+=temp[i].count('10')
            if(grammh%2 ==0):                           #Εαν ειμαστε στην δευτερη γραμμη
                visited.append(temp[i].count('00'))     #Προσθετει στην visited ποσες φορες βρηκε το '00' στο temp
            if(grammh!=1 and grammh%2!=0):
                visited.append(temp[i].count('01'))     #Εαν ειμαστε σε οποιαδηποτε αλλη γραμμη
                visited[i]+=temp[i].count('10')         #Προσθετει στην visited τις φορες που βρηκε το '01'΄και το '10' στο temp
        for i in range(0,len(visited)):
            oxitosorandom += visited[i]
            if(6 in visited and "1010101" in temp and grammh==1 ):  #Εαν υπαρχει το '1010101' στο temp και ειμαστε στην πρωτη γραμμη
                toswsto = temp.index("1010101")                     #αποθηκευει στην μεταβλητη toswsto σε ποιο στοιχειο της temp βρισκεται
                gridP.append(temp[toswsto])
                print(temp)
                print("Vrethike sthn ",stop," genia","sto ",toswsto," stoixeio")
                endofloop=False                                     #Κανει το endofloop=false και βγαινει απο την while
                break
            if("0000000" in temp and grammh%2 ==0):                 #Εαν υπαρχει το '0000000' στο temp και ειμαστε σε γραμμη οπου εαν διαιρεθει με το 2 το υπολοιπο ειναι 0
                toswsto = temp.index("0000000")                     #αποθηκευει στην μεταβλητη toswsto σε ποιο στοιχειο της temp βρισκεται
                gridP.append(temp[toswsto])
                print(temp)
                print("Vrethike sthn ",stop," genia","sto ",toswsto," stoixeio")
                endofloop=False                                     #Κανει το endofloop=false και βγαινει απο την while
                break
            if("1000001" in temp and grammh!=1 and grammh%2!=0):    #Εαν υπαρχει το '1000001' στο temp και ειμαστε σε οποιαδηποτε αλλη γραμμη
                toswsto = temp.index("1000001")                     #αποθηκευει στην μεταβλητη toswsto σε ποιο στοιχειο της temp βρισκεται
                gridP.append(temp[toswsto])
                print(temp)
                print("Vrethike sthn ",stop," genia","sto ",toswsto," stoixeio")
                endofloop=False                                     #Κανει το endofloop=false και βγαινει απο την while
                break
        if(endofloop):                                              #Εαν το endofloop δεν ειναι false 
            for i in range(0,len(temp)):            
                random=(randrange(1, oxitosorandom))                #Δημιουργει εναν τυχαιο αριθμο απο το 1 εως τον αριθμο που εχει η visited
                for j in range(0,len(temp)): 
                    countnum+=visited[j]                            #Προσθετει στο countnum τις τιμες του visited 
                    if(countnum>=random):                           #Εαν το countnum γινει μεγαλυτερο ή ισο του τυχαιου αριθμου τοτε το temp αποθηκευεται στην temp1
                        temp1.append(temp[j])
                        break
                countnum=0
            lengi=len(temp1)-1
            p = randrange(1, 6)
            for i in range(0,lengi,2):                              #Σπανε οι αριθμοι που υπαρχουν στο temp1 στα δυο με p μεγεθος
                temp2.append(temp1[i][0:p]+temp1[i+1][p:])          #Ενωνονται χιαστη με τον αριθμο της temp1 που υπαρχει απο κατω
                temp2.append(temp1[i][p:]+temp1[i+1][0:p])          #Και εν τελη οι νεοι αυτοι αριθμοι αποθηκευονται στην temp2
            temp=temp2
            temp1=[]
            temp2=[]

gridF=[]
def GenAlgoF(grammh,endofloop):             #Μπαινει στην GenAlgoF και κανει παρομοια λειτουργια με την GenAlgoP
    global stop
    stop=0
    while(endofloop):
        oxitosorandom=0
        global temp
        global temp2
        temp1=[]
        stop+=1
        countnum=0
        visited=[] 
        for i in range(0,len(temp)):
            if(grammh==1 or grammh==5):
                visited.append(temp[i].count('01'))
                visited[i]+=temp[i].count('10')
            if(grammh%2 ==0):
                visited.append(temp[i].count('00'))
            if(grammh!=1 and grammh%2!=0 and grammh!=5):
                visited.append(temp[i].count('10'))
        for i in range(0,len(visited)):
            oxitosorandom += visited[i]
            if(6 in visited and "1010101" in temp and (grammh==1 or grammh==5)):
                toswsto = temp.index("1010101")
                #print(temp[toswsto])
                gridF.append(temp[toswsto])
                print(temp)
                print("Vrethike sthn ",stop," genia","sto ",toswsto," stoixeio")
                endofloop=False
                break
            if("0000000" in temp and grammh%2 ==0):
                toswsto = temp.index("0000000")
                gridF.append(temp[toswsto])
                print(temp)
                print("Vrethike sthn ",stop," genia","sto ",toswsto," stoixeio")
                endofloop=False
                break
            if("1000000" in temp and grammh!=1 and grammh%2!=0 and grammh!=5):
                toswsto = temp.index("1000000")
                gridF.append(temp[toswsto])
                print(temp)
                print("Vrethike sthn ",stop," genia","sto ",toswsto," stoixeio")
                endofloop=False
                break
        if(endofloop):
            for i in range(0,len(temp)):
                random=(randrange(1, oxitosorandom))
                for j in range(0,len(temp)): 
                    countnum+=visited[j]
                    if(countnum>=random):
                        temp1.append(temp[j])
                        break
                countnum=0
            lengi=len(temp1)-1
            p = randrange(1, 6)
            for i in range(0,lengi,2):
                temp2.append(temp1[i][0:p]+temp1[i+1][p:])
                temp2.append(temp1[i][p:]+temp1[i+1][0:p])
            temp=temp2
            temp1=[]
            temp2=[]
for i  in range(1,12):  #Καλει την GenAlgoP 11 φορες ωστε να μπει και στις 11 γραμμες
    GenTemp()
    GenAlgoP(i,True)
print("To Π einai auths ths morfhs:")
for i in range(0,11):
    print(gridP[i])     #Εκτυπωνει τους 11 εφταψηφιους αριθμους οι οποιοι σχηματιζουν το Π
for i  in range(1,12):
    GenTemp()
    GenAlgoF(i,True)    #Καλει την GenAlgoF 11 φορες ωστε να μπει και στις 11 γραμμες
print("To F einai auths ths morfhs:")
for i in range(0,11):
    print(gridF[i])     #Εκτυπωνει τους 11 εφταψηφιους αριθμους οι οποιοι σχηματιζουν το F