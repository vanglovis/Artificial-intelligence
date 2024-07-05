import cv2
import pytesseract      #Εισαγωγη του pytesseract το οποιο διαβαζει τις λεξεις μεσα σε φωτογραφιες

pytesseract.pytesseract.tesseract_cmd ='/usr/bin/tesseract'         
img = cv2.imread('eik1.png')        #Μεσω του cv2 φορτωνει την εικονα
img_str = pytesseract.image_to_string(img)  #Αποθηκευει ολες τις λεξεις που υπαρχουν στην εικοντα στην μεταβλητη img_str
print(img_str)      
Fytros_First = img_str[0]
Petridis_First= img_str[8]
if(img_str[0]!=img_str[8]):     #Εχοντας εισαγει δυο επιθετα τσεκαρουμε εαν το πρωτο γραμμα των δυο επιθετων ειναι το ιδιο.
    print("To prwto gramma twn epithetwn diaferei")
    print(Fytros_First , Petridis_First)
    cv2.imshow('Image Show',img)    #Εφοσον ειναι διαφορετικα εμφανιζει την φωτογραφια
    cv2.waitKey(0)                  #Εμφανιζει την φωτογραφια μεχρι να την κλεισει ο χρηστης
else:
    exit()              #Εαν τα δυο γραμματα ειναι ιδια τοτε το προγραμμα τερματιζεται
