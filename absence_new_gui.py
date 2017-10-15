#!/usr/bin/env python

from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
import tkinter.scrolledtext
import shelve

class Gui: #Constructing the GUI
    def __init__(self,mainWindow):
        frame = Frame(mainWindow)
        
        frame.pack()

        self.openButton = Button(frame,text="Obnovit data ze souboru",command=self.getFilename)
        self.openButton.pack(fill=BOTH)

        self.saveButton = Button(frame,text="Uložit data do souboru",command=self.saveFilename)
        self.saveButton.pack(fill=BOTH)

        self.addsButton = Button(frame,text="Přidat studenta",command=self.enterStudent)
        self.addsButton.pack(fill=BOTH)

        self.edisButton = Button(frame,text="Editovat studenta",command=self.editStudent)
        self.edisButton.pack(fill=BOTH)

        self.dispsButton = Button(frame,text="Zobrazit studenty",command=self.swStud)
        self.dispsButton.pack(fill=BOTH)

        self.addaButton = Button(frame,text="Přidat absenci",comman=self.enterAbs)
        self.addaButton.pack(fill=BOTH)

        self.edaButton = Button(frame,text="Editovat absenci",command=self.editAbs)
        self.edaButton.pack(fill=BOTH)

        self.shwaButton = Button(frame,text="Přehled absence",command=self.absOverview)
        self.shwaButton.pack(fill=BOTH)

        self.expoButton = Button(frame,text="Export absence jednotlivých lekcí",command=self.expLessons)
        self.expoButton.pack(fill=BOTH)

        self.quitButton = Button(frame,text="Ukončit program",command=quit)
        self.quitButton.pack(fill=BOTH)

        self.Students = Students() # These are variables for functionality.
        self.Absences = Absences()
        #self.Functions = Functions()

    def getFilename(self):
        try:
            filename = filedialog.askopenfilename(title="Otevřít soubor")
        except AttributeError:
            filename = ""
        self.Database = dBase(filename)
        self.Database.opendb()
        studenti,absence = self.Database.readdb()
        self.Students.acceptSelf(studenti)
        self.Absences.acceptSelf(absence)
        self.Database.close()


    def saveFilename(self):
        filename = filedialog.asksaveasfilename(title="Uložit soubor")
        self.Database = dBase(filename)
        studenti = self.Students.copySelf()
        absence = self.Absences.copySelf()
        self.Database.writedb(studenti,absence)
        self.Database.sync()
        self.Database.close()




    def enterStudent(self): #Enter Student Window
        self.esWin = Toplevel()
        self.esWin.title("Přidat studenta")
        self.esWin.focus_set()

        self.esFrame = Frame(self.esWin)
        self.esFrame.grid(column=0,row=0)

        self.nLabel = Label(self.esFrame,text="Jméno:")
        self.nLabel.grid(column=0,row=0,sticky=W)

        self.sLabel = Label(self.esFrame,text="Příjmení:")
        self.sLabel.grid(column=0,row=1,sticky=W)

        self.cLabel = Label(self.esFrame,text="Kód:")
        self.cLabel.grid(column=0,row=2,sticky=W)

        self.cdLabel = Label(self.esFrame,text="Třída:")
        self.cdLabel.grid(column=0,row=3,sticky=W)

        self.nEntry = Entry(self.esFrame,width=30)
        self.nEntry.grid(column=1,row=0,sticky=W)

        self.sEntry = Entry(self.esFrame,width=30)
        self.sEntry.grid(column=1,row=1,sticky=W)

        self.cEntry = Entry(self.esFrame,width=30)
        self.cEntry.grid(column=1,row=2,sticky=W)

        self.cdEntry = Entry(self.esFrame,width=30)
        self.cdEntry.grid(column=1,row=3,sticky=W)

        self.esbFrame = Frame(self.esWin)
        self.esbFrame.grid(column=0,row=1)

        self.enterButton = Button(self.esbFrame,text="Budiž",command=self.saveEditStud)
        self.enterButton.grid(column=1,row=0,sticky=W+E)

        cancelButton = Button(self.esbFrame,text="Zrušit",command=self.esWin.destroy)
        cancelButton.grid(column=0,row=0,sticky=W+E)

    def saveEditStud(self): #Save the student into the database.
        name = self.nEntry.get()
        sur = self.sEntry.get()
        code = self.cEntry.get()
        clas = self.cdEntry.get()

        if name != "" and sur != "" and code != "" and clas != "":
            student = Student(name,sur,code,clas)
            self.Students.addStudent(student)

            self.nEntry.delete(0,END)
            self.sEntry.delete(0,END)
            self.cEntry.delete(0,END)
            self.cdEntry.delete(0,END)

        else:
            tkinter.messagebox.showerror("Neúplné údaje","Nejsou vyplněny všechny údaje! Student neuložen.")

    def editStudent(self): #Edit Student Window
        self.esWin = Toplevel()
        self.esWin.title("Editovat studenta")
        self.esWin.focus_set()

        self.esFrame = Frame(self.esWin)
        self.esFrame.grid(column=0,row=0)

        self.nLabel = Label(self.esFrame,text="Jméno:")
        self.nLabel.grid(column=0,row=0,sticky=W)

        self.sLabel = Label(self.esFrame,text="Příjmení:")
        self.sLabel.grid(column=0,row=1,sticky=W)

        self.cLabel = Label(self.esFrame,text="Kód:")
        self.cLabel.grid(column=0,row=2,sticky=W)

        self.cdLabel = Label(self.esFrame,text="Třída:")
        self.cdLabel.grid(column=0,row=3,sticky=W)

        self.nEntry = Entry(self.esFrame,width=30)
        self.nEntry.grid(column=1,row=0,sticky=W)

        self.sEntry = Entry(self.esFrame,width=30)
        self.sEntry.grid(column=1,row=1,sticky=W)

        self.cEntry = Entry(self.esFrame,width=30)
        self.cEntry.grid(column=1,row=2,sticky=W)

        self.cdEntry = Entry(self.esFrame,width=30)
        self.cdEntry.grid(column=1,row=3,sticky=W)

        self.esbFrame = Frame(self.esWin)
        self.esbFrame.grid(column=0,row=1)

        self.enterButton = Button(self.esbFrame,text="Budiž",command=self.saveEditStudent)
        self.enterButton.grid(column=1,row=0,sticky=W+E)

        self.cancelButton = Button(self.esbFrame,text="Zrušit",command=self.esWin.destroy)
        self.cancelButton.grid(column=0,row=0,sticky=W+E)

        code = self.cEntry.get()
        
        self.fillButton = Button(self.esbFrame,text="Hledat (kód)",command=self.fillStudent)
        self.fillButton.grid(column=2,row=0,sticky=W+E)


    def fillStudent(self):
        self.nEntry.delete(0,END)
        self.sEntry.delete(0,END)
        self.cdEntry.delete(0,END)
        code = self.cEntry.get()
        student = self.Students.showStudent(code)
        self.nEntry.insert(END,student[0])
        self.sEntry.insert(END,student[1])
        self.cdEntry.insert(END,student[2])

    def saveEditStudent(self):
        name = self.nEntry.get()
        sur = self.sEntry.get()
        code = self.cEntry.get()
        clas = self.cdEntry.get()
        student = [name,sur,clas]
        io = self.Students.editStudent(code,student)
        if io == 0:
            ok = tkinter.messagebox.showinfo("Záznam změněn","Záznam byl úspěšně změněn.")
        else:
            na = tkinter.messagebox.showerror("Student neexistuje!","Tento student (kód) neexistuje, změna nebyla uložena.")
        self.nEntry.delete(0,END)
        self.sEntry.delete(0,END)
        self.cdEntry.delete(0,END)
        self.cEntry.delete(0,END)
        
    def enterAbs(self): #Enter Absence Window
        self.esWin = Toplevel()
        self.esWin.title("Přidat absenci")
        self.esWin.focus_set()
        self.pard = IntVar()
        self.pard.set(0)

        self.esFrame = Frame(self.esWin)
        self.esFrame.grid(column=0,row=0)

        self.cdLabel = Label(self.esFrame,text="Kód studenta:")
        self.cdLabel.grid(column=0,row=0,sticky=W)

        self.adLabel = Label(self.esFrame,text="Datum absence:")
        self.adLabel.grid(column=0,row=1,sticky=W)

        self.hLabel = Label(self.esFrame,text="Hodiny:")
        self.hLabel.grid(column=0,row=2,sticky=W)

        self.paRbutton = Radiobutton(self.esFrame,variable=self.pard,value=1,text="Omluveno")
        self.paRbutton.grid(column=0,row=3,sticky=W)

        self.cdEntry = Entry(self.esFrame,width=30)
        self.cdEntry.grid(column=1,row=0,sticky=W)

        self.adEntry = Entry(self.esFrame,width=30)
        self.adEntry.grid(column=1,row=1,sticky=W)

        self.hEntry = Entry(self.esFrame,width=30)
        self.hEntry.grid(column=1,row=2,sticky=W)

        self.pbButton = Radiobutton(self.esFrame,variable=self.pard,value=0,text="Neomluveno")
        self.pbButton.grid(column=1,row=3,sticky=W)

        self.esbFrame = Frame(self.esWin)
        self.esbFrame.grid(column=0,row=1)

        self.enterButton = Button(self.esbFrame,text="Budiž",command=self.saveEnterAbs)
        self.enterButton.grid(column=1,row=0,sticky=W+E)

        self.cancelButton = Button(self.esbFrame,text="Zrušit",command=self.esWin.destroy)
        self.cancelButton.grid(column=0,row=0,sticky=W+E)

    def saveEnterAbs(self):
        code = self.cdEntry.get()
        studenti = self.Students.copySelf()
        if code in studenti.keys():
            date = int(self.adEntry.get())
            lessons = list(self.hEntry.get())
            count = len(lessons)
            pard = self.pard.get()
            if pard == 1:
                pard = "O"
            else:
                pard = "N"
            absence = [code,date,count,pard,lessons]
            self.Absences.addAbsence(absence)
            tkinter.messagebox.showinfo("Absence přidána","Absence byla přidána.")
        else:
            tkinter.messagebox.showerror("Student neexistuje!","Tento student neexistuje. Nelze mu přiřadit absenci.")

    def editAbs(self): #Edit Absence Window
        self.esWin = Toplevel()
        self.esWin.title("Editovat absenci")
        self.esWin.focus_set()
        self.pard = StringVar()
        
        self.esFrame = Frame(self.esWin)
        self.esFrame.grid(column=0,row=0)

        self.nLabel = Label(self.esFrame,text="ID absence:")
        self.nLabel.grid(column=0,row=0,sticky=W)

        self.cdLabel = Label(self.esFrame,text="Kód studenta:")
        self.cdLabel.grid(column=0,row=1,sticky=W)

        self.adLabel = Label(self.esFrame,text="Datum absence:")
        self.adLabel.grid(column=0,row=2,sticky=W)

        self.hLabel = Label(self.esFrame,text="Hodiny:")
        self.hLabel.grid(column=0,row=3,sticky=W)

        self.paRbutton = Radiobutton(self.esFrame,variable=self.pard,value=1,text="Omluveno")
        self.paRbutton.grid(column=0,row=4,sticky=W)

        self.nEntry = Entry(self.esFrame,width=30)
        self.nEntry.grid(column=1,row=0,sticky=W)

        self.loadButton = Button(self.esFrame,text="Načíst",command=self.loadAbs)
        self.loadButton.grid(column=2,row=0,sticky=W)

        self.cdEntry = Entry(self.esFrame,width=30)
        self.cdEntry.grid(column=1,row=1,sticky=W)

        self.adEntry = Entry(self.esFrame,width=30)
        self.adEntry.grid(column=1,row=2,sticky=W)

        self.hEntry = Entry(self.esFrame,width=30)
        self.hEntry.grid(column=1,row=3,sticky=W)

        self.pbButton = Radiobutton(self.esFrame,variable=self.pard,value=0,text="Neomluveno")
        self.pbButton.grid(column=1,row=4,sticky=W)

        self.esbFrame = Frame(self.esWin)
        self.esbFrame.grid(column=0,row=1)

        self.enterButton = Button(self.esbFrame,text="Budiž",command=self.saveEditAbs)
        self.enterButton.grid(column=2,row=0,sticky=W+E)

        self.adelButton = Button(self.esbFrame,text="Smazat",command=self.delAbs)
        self.adelButton.grid(column=1,row=0,sticky=W+E)

        self.cancelButton = Button(self.esbFrame,text="Zrušit",command=self.esWin.destroy)
        self.cancelButton.grid(column=0,row=0,sticky=W+E)

    def loadAbs(self):
        code = int(self.nEntry.get())
        print(code)
        absence = self.Absences.provideAbsEdit(code)
        cod = absence[1]
        date = absence[2]
        count = absence[3]
        pard = absence[4]
        lessons = absence[5]
        lessons = ''.join(lessons)
        if pard == "O":
            pard = 1
        else:
            pard = 0
        self.cdEntry.insert(END,cod)
        self.adEntry.insert(END,date)
        self.hEntry.insert(END,lessons)
        self.pard.set(pard)
        self.nEntry.config(state="readonly")

    def delAbs(self):
        code = int(self.nEntry.get())
        self.Absences.deleteAbsences(code)
        tkinter.messagebox.showinfo("Absence smazána","Absence byla smazána!")

        self.nEntry.config(state="normal")
        self.nEntry.delete(0,END)
        self.adEntry.delete(0,END)
        self.cdEntry.delete(0,END)
        self.hEntry.delete(0,END)
        self.pard.set(0)
        
    def saveEditAbs(self):
        idd = int(self.nEntry.get())
        code = self.cdEntry.get()
        date = int(self.adEntry.get())
        lessons = list(self.hEntry.get())
        count = len(lessons)
        pard = int(self.pard.get())
        print(pard)
        if pard == 1:
            pard = "O"
        else:
            pard = "N"
        print(pard)

        absrecord = [idd,code,date,count,pard,lessons]
        self.Absences.editAbsence(idd,absrecord)

        self.nEntry.config(state="normal")
        self.nEntry.delete(0,END)
        self.adEntry.delete(0,END)
        self.cdEntry.delete(0,END)
        self.hEntry.delete(0,END)
        self.pard.set(0)


    def swStud(self):
        showWin = Toplevel()
        showWin.title("Přehled studentů")
        showWin.focus_set()

        self.esFrame = Frame(showWin)
        self.esFrame.grid(column=0,row=0)

        self.nLabel = Label(self.esFrame,text="Jméno:")
        self.nLabel.grid(column=0,row=0,sticky=W)

        self.sLabel = Label(self.esFrame,text="Příjmení:")
        self.sLabel.grid(column=0,row=1,sticky=W)

        self.cLabel = Label(self.esFrame,text="Kód:")
        self.cLabel.grid(column=0,row=2,sticky=W)

        self.cdLabel = Label(self.esFrame,text="Třída:")
        self.cdLabel.grid(column=0,row=3,sticky=W)

        self.nEntry = Entry(self.esFrame,width=30)
        self.nEntry.grid(column=1,row=0,sticky=W)

        self.sEntry = Entry(self.esFrame,width=30)
        self.sEntry.grid(column=1,row=1,sticky=W)

        self.cdEntry = Entry(self.esFrame,width=30)
        self.cdEntry.grid(column=1,row=2,sticky=W)

        self.cEntry = Entry(self.esFrame,width=30)
        self.cEntry.grid(column=1,row=3,sticky=W)

        self.esbFrame = Frame(showWin)
        self.esbFrame.grid(column=0,row=1)

        self.enterButton = Button(self.esbFrame,text="Budiž",command=self.ukazStudenta)
        self.enterButton.grid(column=1,row=0,sticky=W+E)

        self.cancelButton = Button(self.esbFrame,text="Zrušit",command=showWin.destroy)
        self.cancelButton.grid(column=0,row=0,sticky=W+E)

        self.textFrame = Frame(showWin,background="white")
        self.textFrame.grid(column=0,row=2,sticky=W+E)

        self.text = Text(self.textFrame,width=60)
        self.text.grid(column=0,row=0)
        self.hbar = Scrollbar(self.textFrame,orient="vertical",command=self.text.yview)
        self.hbar.grid(column=1,row=0,sticky=N+S)
        self.text.configure(yscrollcommand=self.hbar)

    def ukazStudenta(self):
        name = self.nEntry.get()
        if name == '':
            name = 0
        sur = self.sEntry.get()
        if sur == '':
            sur = 0
        code = self.cdEntry.get()
        if code == '':
            code = 0
        clasz = self.cEntry.get()
        if clasz == '':
            clasz = 0
        
        informace = self.Students.showStudents(code,name,sur,clasz)
        self.text.delete(1.0,END)
        for i in informace:
            data = self.Students.copySelf()
            info = data[i]
            line = i,"-",info[0],info[1],"("+info[2]+")"
            self.text.insert(END,line)
            self.text.insert(END,"\n")

    def absOverview(self):
        showWin = Toplevel()
        showWin.title("Přehled absence")
        showWin.focus_set()

        self.pard = IntVar()
        self.nepard = IntVar()
        self.latex = IntVar()

        self.esFrame = Frame(showWin)
        self.esFrame.grid(column=0,row=0)

        self.sdLabel = Label(self.esFrame,text="Počáteční datum:")
        self.sdLabel.grid(column=0,row=0,sticky=W)

        self.fdLabel = Label(self.esFrame,text="Konečné datum:")
        self.fdLabel.grid(column=0,row=1,sticky=W)

        self.cLabel = Label(self.esFrame,text="Kód:")
        self.cLabel.grid(column=0,row=2,sticky=W)

        self.cdLabel = Label(self.esFrame,text="Třída:")
        self.cdLabel.grid(column=0,row=3,sticky=W)

##        self.pardLabel = Label(self.esFrame,text="Omluveno (O/N/ON):")
##        self.pardLabel.grid(column=0,row=4,sticky=W)

        self.sdEntry = Entry(self.esFrame,width=30)
        self.sdEntry.grid(column=1,row=0,sticky=W)

        self.fdEntry = Entry(self.esFrame,width=30)
        self.fdEntry.grid(column=1,row=1,sticky=W)

        self.cEntry = Entry(self.esFrame,width=30)
        self.cEntry.grid(column=1,row=2,sticky=W)

        self.cdEntry = Entry(self.esFrame,width=30)
        self.cdEntry.grid(column=1,row=3,sticky=W)

        self.esbFrame = Frame(showWin)
        self.esbFrame.grid(column=0,row=1)

        self.enterButton = Button(self.esbFrame,text="Budiž",command=self.ukazAbsOver)
        self.enterButton.grid(column=2,row=0,sticky=W+E)

        self.cancelButton = Button(self.esbFrame,text="Zrušit",command=showWin.destroy)
        self.cancelButton.grid(column=0,row=0,sticky=W+E)

        self.allButton = Button(self.esbFrame,text="Celkem",command=self.ukazAbsSum)
        self.allButton.grid(column=1,row=0,sticky=W+E)

        self.paRbutton = Checkbutton(self.esFrame,variable=self.pard,text="Omluveno")
        self.paRbutton.grid(column=0,row=5,sticky=W)

        self.pbRbutton = Checkbutton(self.esFrame,variable=self.nepard,text="Neomluveno")
        self.pbRbutton.grid(column=1,row=5,sticky=W)

        self.LButton = Checkbutton(self.esFrame,variable=self.latex,text="Výstup pro LaTeX")
        self.LButton.grid(column=0,row=6,sticky=W)

        self.textFrame = Frame(showWin)
        self.textFrame.grid(column=0,row=2,sticky=W+E)

        self.text = Text(self.textFrame,width=120)
        self.text.tag_config("a",background="white")
        self.text.grid(column=0,row=0)
        self.hbar = Scrollbar(self.textFrame,orient="vertical",command=self.text.yview)
        self.hbar.grid(column=1,row=0,sticky=N+S)
        self.text.configure(yscrollcommand=self.hbar.set)

    def ukazAbsSum(self):
        self.text.delete(1.0,END)
        nepard = self.nepard.get()
        latex = self.latex.get()
        
        pard = "N"

        name = 0
        sur = 0

        self.tisk = Printer(15)

        fromdate = self.sdEntry.get()
        if fromdate == "":
            fromdate = 0
        fromdate = int(fromdate)
        todate = self.fdEntry.get()
        if todate == "":
            todate = 0
        todate = int(todate)
        code = 0
        clasz = self.cdEntry.get()
        if clasz == "":
            tkinter.messagebox.showwarning("Třída nezadána","Přehled nebude zobrazovat konkrétní třídu.")
            clasz = 0
        print(latex)
        if latex == 1:
            graphics = "L"
        else:
            graphics = "O"

        studlist = self.Students.copySelf()
        studvyber = self.Students.showStudents(code,name,sur,clasz)
        studvyber.sort()
        dates = self.Absences.pickDates(fromdate,todate)

        if graphics != "L":

            self.tisk.setWidth(["Průměrná absence:"])
            tr = self.tisk.formatTR(["Příjmení:","Absence (hodin):","Neomluveno (hodin):"])
            self.decoline = self.tisk.formatLine('-',8)
            self.text.insert(END,tr)
            self.text.insert(END,"\n")
            self.text.insert(END,self.decoline)
            self.text.insert(END,"\n")
            for student in studvyber:
                data = self.Students.showStudent(student)
                name,sur = data[0],data[1]
                student = [student]
                absvyber = self.Absences.pickStudents(student,dates)
                absvyber.sort()
                studsum = self.Absences.calculateSum()
                parvyber = self.Absences.showPard(pard)
                pardsum = self.Absences.calculateSum()
                studavg = self.Absences.calculateAvg()
                tr = self.tisk.formatTR([str(sur),str(studsum),str(pardsum)])
                self.text.insert(END,tr)
                self.text.insert(END,"\n")
        else:
            print(" ")
            print("Příjmení: & Absence (hodin) & Neomluveno (hodin)")
            print("\\hline")
            for student in studvyber:
                data = self.Students.showStudent(student)
                name,sur = data[0],data[1]
                student = [student]
                absvyber = self.Absences.pickStudents(student,dates)
                absvyber.sort()
                studsum = self.Absences.calculateSum()
                parvyber = self.Absences.showPard(pard)
                pardsum = self.Absences.calculateSum()
                studavg = self.Absences.calculateAvg()
                print(sur,"&",studsum,"&",pardsum," \\\\")

    def ukazAbsOver(self):
        self.text.delete(1.0,END)
        pard = self.pard.get()
        nepard = self.nepard.get()
        latex = self.latex.get()
        
        if pard == 1 and nepard == 0:
            pardoned = "O"
        elif nepard == 1 and pard == 0:
            pardoned = "N"
        else:
            pardoned = "ON"

        name = 0
        sur = 0

        self.tisk = Printer(15)

        fromdate = self.sdEntry.get()
        if fromdate == "":
            fromdate = 0
        fromdate = int(fromdate)
        todate = self.fdEntry.get()
        if todate == "":
            todate = 0
        todate = int(todate)
        code = self.cEntry.get()
        if code == "":
            code = 0
        clas = self.cdEntry.get()
        if clas == "":
            clas = 0
        print(latex)
        if latex == 1:
            graphics = "L"
        else:
            graphics = "O"
        dates = self.Absences.pickDates(fromdate,todate)
        codes = self.Students.showStudents(code,name,sur,clas)
        students = self.Absences.pickStudents(codes,dates)
        finals = self.Absences.showPard(pardoned)
        celkem = self.Absences.calculateSum()
        prumer = self.Absences.calculateAvg()
        prumerall = self.Absences.calculateAvgAll(self.Students.countClass(clas))

        if graphics != "L":
            self.tisk.setWidth(["Kód studenta"])
            self.decoline = self.tisk.formatLine('-',8)
            self.text.insert(END,self.decoline)
            self.text.insert(END,"\n")
            tr = self.tisk.formatTR(["Id:","Jméno:","Příjmení:","Kód studenta:","Datum:","Hodin:","Omluva:"])
            self.text.insert(END,tr)
            self.text.insert(END,"\n")
            self.text.insert(END,self.decoline)
            self.text.insert(END,"\n")

            for item in finals:
                name = self.Students.showStudent(item[1])
                tr = self.tisk.formatTR([str(item[0]),name[0],name[1],item[1],str(item[2]),str(item[3]),item[4]])
                self.text.insert(END,tr)
                self.text.insert(END,"\n")
            self.text.insert(END,self.decoline)
            self.text.insert(END,"\n")
            tr = self.tisk.formatTR(["Celkem absencí:",str(self.Absences.sumAll())])
            self.text.insert(END,tr)
            self.text.insert(END,"\n")
            tr = self.tisk.formatTR(["Průměrná absence:",str(prumer)])
            self.text.insert(END,tr)
            self.text.insert(END,"\n")
            tr = self.tisk.formatTR(["Průměr (žák/tř.):",str(prumerall)])
            self.text.insert(END,tr)
            self.text.insert(END,"\n")
            tr = self.tisk.formatTR(["Celkem:",str(celkem)])
            self.text.insert(END,tr)
            self.text.insert(END,"\n")
            self.text.insert(END,self.decoline)
            self.text.insert(END,"\n")

        else:
            self.text.insert(END," ")
            self.text.insert(END,"\n")
            self.text.insert(END,"Jméno: & Příjmení: & Datum: & Hodin: \\\\")
            self.text.insert(END,"\n")
            self.text.insert(END,"\\hline")
            self.text.insert(END,"\n")
            for item in finals:
                name = self.Students.showStudent(item[1])
                self.text.insert(END,name[0]+" & "+name[1]+" & "+str(item[2])+" & "+str(item[3])+" \\\\")
                self.text.insert(END,"\n")
            self.text.insert(END," ")
            self.text.insert(END,"\n")
            self.text.insert(END,"Celkem absencí: "+str(self.Absences.sumAll()))
            self.text.insert(END,"\n")
            self.text.insert(END,"Průměrná absence: "+str(prumer))
            self.text.insert(END,"\n")
            self.text.insert(END,"Průměr (žák/třída): "+str(prumerall))
            self.text.insert(END,"\n")
            self.text.insert(END,"Celkem: "+str(celkem))
            self.text.insert(END,"\n")

    def expLessons(self):
        showWin = Toplevel()
        showWin.title("Přehled absence")
        showWin.focus_set()

        self.pard = IntVar()
        self.nepard = IntVar()
        self.latex = IntVar()

        self.esFrame = Frame(showWin)
        self.esFrame.grid(column=0,row=0)

        self.sdLabel = Label(self.esFrame,text="Počáteční datum:")
        self.sdLabel.grid(column=0,row=0,sticky=W)

        self.fdLabel = Label(self.esFrame,text="Konečné datum:")
        self.fdLabel.grid(column=0,row=1,sticky=W)

        self.cLabel = Label(self.esFrame,text="Kód:")
        self.cLabel.grid(column=0,row=2,sticky=W)

        self.cdLabel = Label(self.esFrame,text="Třída:")
        self.cdLabel.grid(column=0,row=3,sticky=W)

        self.sdEntry = Entry(self.esFrame,width=30)
        self.sdEntry.grid(column=1,row=0,sticky=W)

        self.fdEntry = Entry(self.esFrame,width=30)
        self.fdEntry.grid(column=1,row=1,sticky=W)

        self.cEntry = Entry(self.esFrame,width=30)
        self.cEntry.grid(column=1,row=2,sticky=W)

        self.cdEntry = Entry(self.esFrame,width=30)
        self.cdEntry.grid(column=1,row=3,sticky=W)

        self.esbFrame = Frame(showWin)
        self.esbFrame.grid(column=0,row=1)

        self.enterButton = Button(self.esbFrame,text="Budiž",command=self.ukazExpLess)
        self.enterButton.grid(column=2,row=0,sticky=W+E)

        self.cancelButton = Button(self.esbFrame,text="Zrušit",command=showWin.destroy)
        self.cancelButton.grid(column=0,row=0,sticky=W+E)

        self.paRbutton = Checkbutton(self.esFrame,variable=self.pard,text="Omluveno")
        self.paRbutton.grid(column=0,row=5,sticky=W)

        self.pbRbutton = Checkbutton(self.esFrame,variable=self.nepard,text="Neomluveno")
        self.pbRbutton.grid(column=1,row=5,sticky=W)

        self.textFrame = Frame(showWin)
        self.textFrame.grid(column=0,row=2,sticky=W+E)

        self.text = Text(self.textFrame,width=120)
        self.text.tag_config("a",background="white")
        self.text.grid(column=0,row=0)
        self.hbar = Scrollbar(self.textFrame,orient="vertical",command=self.text.yview)
        self.hbar.grid(column=1,row=0,sticky=N+S)
        self.text.configure(yscrollcommand=self.hbar.set)

    def ukazExpLess(self):
        self.text.delete(1.0,END)
        pard = self.pard.get()
        nepard = self.nepard.get()
                
        if pard == 1 and nepard == 0:
            pardoned = "O"
        elif nepard == 1 and pard == 0:
            pardoned = "N"
        else:
            pardoned = "ON"

        name = 0
        sur = 0

        self.tisk = Printer(15)

        fromdate = self.sdEntry.get()
        if fromdate == "":
            fromdate = 0
        fromdate = int(fromdate)
        todate = self.fdEntry.get()
        if todate == "":
            todate = 0
        todate = int(todate)
        code = self.cEntry.get()
        if code == "":
            code = 0
        clas = self.cdEntry.get()
        if clas == "":
            clas = 0
        
        dates = self.Absences.pickDates(fromdate,todate)
        codes = self.Students.showStudents(code,name,sur,clas)
        students = self.Absences.pickStudents(codes,dates)
        finals = self.Absences.showPard(pardoned)
        
        self.text.insert(END,"\n")
        self.text.insert(END,"Kód,Datum,Hodiny")
        self.text.insert(END,"\n")
        for item in finals:
            lessons = ''.join(item[5])
            self.text.insert(END,str(item[1])+","+str(item[2])+","+lessons)
            self.text.insert(END,"\n")
        
            
#Classes and methods for the functionality
        
class Student:
    def __init__(self,name,surname,code,clasz):
        self.Name = name
        self.Surname = surname
        self.Code = code
        self.Class = clasz

    def editName(self,name):
        self.Name = name

    def editSurname(self,surname):
        self.Surname = surname

    def editClass(self,clasz):
        self.Class = clasz

    def show(self):
        infolist = [self.Code,self.Name,self.Surname,self.Class]
        return infolist
        

class Students:
    def __init__(self):
        self.Studentlist = {}
        self.Pickedlist = []

    def addStudent(self,student): # This method adds students to the pool. (Passed.)
        self.Student = student
        info = self.Student.show()
        
        scode = info[0]
        sname = info[1]
        ssurname = info[2]
        sclass = info[3]
        if scode not in self.Studentlist.keys():
            self.Studentlist[scode] = [sname,ssurname,sclass]
            print("Student",ssurname+",",sname,"("+scode+") byl úspěšně přidán do databáze.")
        else:
            print("Pozor, student s tímto kódem existuje. ")

    def editStudent(self,code,student): # Editing of the student.
        if code in self.Studentlist.keys():
            self.Studentlist[code] = student
            return 0
        else:
            return 100

    def deleteStudent(self,code): # Deleting the student.
        try:
            del self.Studentlist[code]
            print("Student byl vymazán.")
        except KeyError:
            print("Tento student neexistuje. Možná byl již smazán.")

    def showStudent(self,code):
        try:
            data = self.Studentlist[code]
            return data[0],data[1],data[2]
        except KeyError:
            print("Tento student neexistuje. Špatně zadaný kód.")

    def showStudents(self,code=0,name=0,surname=0,clasz=0): # This method finds a student according to given criteria and returns the code. (Passed)
        infolist = []
        if code == 0:
            for key in self.Studentlist.keys():
                infolist.append(key)
        else:
            infolist.append(code)
        
        if name != 0:
            newlist = []
            for key in infolist:
                line = self.Studentlist[key]
                
                if line[0] == name:
                    newlist.append(key)
            infolist = newlist

        if surname != 0:
            newlist = []
            for key in infolist:
                line = self.Studentlist[key]
                
                if line[1] == surname:
                    newlist.append(key)
            infolist = newlist

        if clasz != 0:
            newlist = []
            for key in infolist:
                line = self.Studentlist[key]
                
                if line[2] == clasz:
                    newlist.append(key)
            infolist = newlist
            self.Pickedlist = newlist
        infolist.sort()
        return infolist
            
        
    def copySelf(self):
        return self.Studentlist

    def countClass(self,clasz):
        classlist = self.showStudents(0,0,0,clasz)
        count = len(classlist)
        return count

    def acceptSelf(self,stulist):
        self.Studentlist = stulist
        

class Absence:
    def __init__(self,who,when,howmany,pardoned,lessons):
        self.Code = who
        self.Date = int(when)
        self.Sum = int(howmany)
        self.Pardoned = pardoned
        self.Lessons = lessons

    def editCode(self,who):
        self.Code = who

    def editDate(self,when):
        self.Date = int(when)

    def editCount(self,howmany):
        self.Sum = int(howmany)

    def editPardon(self,pardoned):
        self.Pardoned = pardoned

    def editLessons(self,lessons):
        self.Lessons = lessons

    def show(self):
        infolist = [self.Code,self.Date,self.Sum,self.Pardoned,self.Lessons]
        return infolist


class Absences:
    def __init__(self):
        self.Absencelist = []
        self.Chosenlist = [] # All absences according to the dates.
        self.Pickedlist = [] # All absences of selected students.
        self.Wishlist = [] # Selected absences (students/dates).
        self.Pardonlist = [] # All pardoned or unpardoned absences.
    
    def addAbsence(self,absence): # This method adds absences into the pool. (Passed)
        count = 0
        idlist = []
        for item in self.Absencelist:
            idlist.append(item[0])
        idlist.sort()
        count = len(idlist)-1
        try:
            idd = idlist[count]
        except IndexError:
            idd = 0
        idd = idd+1
        absrecord = [idd,absence[0],absence[1],absence[2],absence[3],absence[4]]
        self.Absencelist.append(absrecord)
        print("Absence byla úspěšně přidána!")

    def showPard(self,pard):
        newlist = []
        if pard == "ON" or pard == "NO":
            return self.Wishlist
        else:
            for absence in self.Wishlist:
                if absence[4] == pard:
                    newlist.append(absence)
                    #print("Absence: ",absence)
        self.Wishlist = newlist  # Zde jsem udělal změnu, která by měla počítat i neomluvené hodiny.
        return newlist    

    def pickDates(self,fro=0,to=0):     # Passed
        if fro == 0:
            dates = []
            for absence in self.Absencelist:
                dates.append(absence[2])
            dates.sort()
            fro = dates[0]

        if to == 0:
            dates = []
            for absence in self.Absencelist:
                dates.append(absence[2])
            dates.sort(reverse=True)
            to = dates[0]

        infolist = []
        for absence in self.Absencelist:
            if int(fro) == absence[2] or int(fro) < absence[2]:
                infolist.append(absence)

        newlist = []    
        for line in infolist:
            if int(to) > line[2] or int(to) == line[2]:
                newlist.append(line)
        infolist = newlist
        self.Chosenlist = newlist
        return newlist
    
    def pickStudents(self,codes,dates): # Passed
        studlist = []
        for name in codes:
            #print("Name in pickstudents je:",name)
            for absence in dates:
                if name in absence:
                    studlist.append(absence)

        self.Pickedlist = studlist
        self.Wishlist = studlist
        #print("Wishlist:",self.Wishlist)
        #print("Studlist:",studlist)

        self.Wishlist = sorted(self.Wishlist, key=lambda rec: rec[2]) #This is to be tried.
        return self.Wishlist
                 
    def deleteAbsences(self,code):
        for absence in self.Absencelist:
            if code in absence:
                index = self.Absencelist.index(absence)
                popped = self.Absencelist.pop(index)

    def provideAbsEdit(self,idd):
        for absence in self.Absencelist:
            if idd == absence[0]:
                index = self.Absencelist.index(absence)
                break
        return absence

    def editAbsence(self,idabs,absence):
        self.deleteAbsences(idabs)
        self.Absencelist.append(absence)
        

    def calculateSum(self): # Passed
        hourlist = []
        for line in self.Wishlist:
            lesson = line[3]
            hourlist.append(lesson)
        return sum(hourlist)

    def sumAll(self): #Passed
        return len(self.Wishlist)

    def calculateAvg(self): #Passed
        hourlist = []
        for line in self.Wishlist:
            lesson = line[3]
            hourlist.append(lesson)
        try:
            avg = sum(hourlist)/len(hourlist)
        except ZeroDivisionError:
            avg = 0
        avg = round(avg,2)
        return avg

    def calculateAvgAll(self,students): #Passed
        hourlist = []
        for line in self.Wishlist:
            lesson = line[3]
            hourlist.append(lesson)
        avg = sum(hourlist)/students
        avg = round(avg,2)
        return avg

    def copySelf(self):
        return self.Absencelist

    def acceptSelf(self,abslist):
        self.Absencelist = abslist

class dBase:
    def __init__(self,filename):
        self.Filename = filename

    def opendb(self):
        try:
            self.database = shelve.open(self.Filename)
        except:
            print('No database was has been opened. Program terminated?')

    def sync(self):
        self.database.sync()

    def close(self):
        try:
            self.database.close()
        except:
            pass

    def readdb(self):
        try:
                studenti = self.database['studenti']
                absence = self.database['absence']
        except:
                studenti = {}
                absence = []
        return(studenti,absence)

    def writedb(self,studenti,absence):
        self.database = shelve.open(self.Filename)
        self.database['studenti'] = studenti
        self.database['absence'] = absence
        self.sync()


class Printer:
    def __init__(self,cwidth):
        self.cwidth = cwidth
        self.filler = ' '

    def setWidth(self,strlist):
        for word in strlist:
            if len(word) > self.cwidth:
                self.cwidth = len(word)+5

    def formatTR(self,strlist):
        tr = []
        #print("self.cwidth je",self.cwidth)
        for word in strlist:
            if len(word) < self.cwidth:
                diff = self.cwidth - len(word)
                spacer = ' '*diff
                tr.append(word+spacer)
            else:
                tr.append(word)
        formstring = ''    
        #print(tr)
        for cell in tr:
            formstring = formstring+cell
        return formstring

    def formatLine(self,symbol,ccol):
        string = symbol*self.cwidth*ccol
        self.ccol = ccol
        return string


#Main program

if __name__=="__main__":
    root = Tk()
    root.title("Sledování absence 2.0")
    aplikace = Gui(root)
    root.mainloop()
        
