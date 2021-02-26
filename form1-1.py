from PyQt5 import QtWidgets,uic

#Bouton valider
def valid() :
    global call_2
    n=call.np.text()
    b=call.cin.text()
    c=call.age.text()
    d=call.choix.currentText()

    
    call_2.show()
    
    x=f'Nom et prénom : {n}\nCIN : {b}\nAGE : {c}\nDecision: {d}'
    call_2.complete.setText(x)
    f=open("valid.txt","a")
    f.write("        nom&prenom :"+n)
    f.write("\n")
    f.write("        CIN :"+b)
    f.write("\n")
    f.write("        Age :"+c)
    f.write("\n")
    f.write("        decision :"+d)
    f.write("\n")
    f.close()
def modifier():
    cin=call.cin.text()
    a=open('valid.txt','r+')
    p=a.readlines()
    x=f''
    for i in range(len(p)):
        if cin in p[i]:
            p[i-1]=x
            p[i]=x
            p[i+1]=x
            p[i+2]=x

    ch="".join(p)
    a.close()
    a=open('valid.txt','w+')
    a.write(ch)
    a.close()
    n=call.np.text()
    b=call.cin.text()
    c=call.age.text()
    d=call.choix.currentText()

    
    call_2.show()
    
    x=f'Nom et prénom : {n}\nCIN : {b}\nAGE : {c}\nDecision: {d}'
    call_2.complete.setText(x)
    f=open("valid.txt","a")
    f.write("        nom&prenom :"+n)
    f.write("\n")
    f.write("        CIN :"+b)
    f.write("\n")
    f.write("        Age :"+c)
    f.write("\n")
    f.write("        decision :"+d)
    f.write("\n")
    f.close()
def suprimer():
    cin=call.cin.text()
    a=open('valid.txt','r+')
    p=a.readlines()
    x=f''
    for i in range(len(p)):
        if cin in p[i]:
            p[i-1]=x
            p[i]=x
            p[i+1]=x
            p[i+2]=x

    ch="".join(p)
    a.close()
    a=open('valid.txt','w+')
    a.write(ch)
    a.close()
def quit_2():
    app.quit()

#Boutton annuler
def canceling():
    app.quit()


#Program principal
app=QtWidgets.QApplication([])
call=uic.loadUi("main.ui")
call_2=uic.loadUi("okform.ui")
call.pushButton.clicked.connect(valid)
call.pushButton_2.clicked.connect(modifier)
call.ok1.clicked.connect(suprimer)
call_2.ok1.clicked.connect(quit_2)
call.show()
app.exec()
