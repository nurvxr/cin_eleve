from PyQt5 import QtWidgets,uic

#Bouton valider
def valid() :
    global call_2
    a=call.np.text()
    b=call.cin.text()
    c=call.age.text()
    d=call.choix.currentText()

    
    call_2.show()
    
    x=f'Nom et prénom : {a}\nCIN : {b}\nAGE : {c}\nDecision: '
    call_2.complete.setText(x)
    
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
call.pushButton_2.clicked.connect(canceling)
call_2.ok1.clicked.connect(quit_2)
call.show()
app.exec()
