from tkinter import *
from tkinter import messagebox as msgb
from sql_functions import sql_func
import pandas as pd
from recommend import recommend
import os

rec = recommend()
if not os.path.exists('output.xlsx'):
	new_df = pd.DataFrame(columns=['Event','Recommended Employee'])
else:
	new_df = pd.read_excel('output.xlsx')

class input_win:
    def __init__(self):
        self.sq = sql_func()
        self.window = Tk()
        self.window.geometry('500x450')
        self.window.title('Employee Interest Input')

        self.uname = StringVar()
        self.domain = StringVar()
        self.event1 = StringVar()
        self.event2 = StringVar()

        self.new_win = None
        uname_label = Label(self.window,text='Name',height=3,width=10).grid(column=0,row=1)
        uname_entry = Entry(self.window,textvariable=self.uname,width=30).grid(column=1,row=1,padx=20)

        domain_label = Label(self.window,text='Domain').grid(column=0,row=2)
        self.domain.set('Artificial Intelligence')
        domain_drop = OptionMenu(self.window, self.domain, "Artificial Intelligence", "Blockchain", "C",\
            "C++", "Cloud Computing", "Coding", "Data Science", "Development processes",\
            "Finance", "Hardware", "Higher Education", "IoT", "Java", "JavaScript",\
            "Machine learning", "Management", "Mobile Applications", "Networking",\
            "Python", "Security", "Software Architecture", "Web Development", "Other")
        domain_drop.grid(column=1,row=2)

        event1_label = Label(self.window,text='Event1').grid(column=0,row=3)
        self.event1.set('Certifications')
        event1_drop = OptionMenu(self.window, self.event1, "Certifications", "Competitions", "Courses",\
            "Expos", "Fests", "Hackathons", "Internships", "Jobs", "Seminars", "Talks",\
            "Trainings", "Webinars", "Workshops")
        event1_drop.grid(column=1,row=3)

        event2_label = Label(self.window,text='Event2').grid(column=0,row=3)
        self.event2.set('Certifications')
        event2_drop = OptionMenu(self.window, self.event2, "Certifications", "Competitions", "Courses",\
        "Expos", "Fests", "Hackathons", "Internships", "Jobs", "Seminars", "Talks",\
        "Trainings", "Webinars", "Workshops")
        event2_drop.grid(column=1,row=4)


        submit_btn = Button(self.window,text='Submit',command=self.submit).grid(column=1,row=5)

        self.window.mainloop()

    def submit(self):
        self.sq.insert_data(self.uname.get(),self.domain.get(),self.event1.get(),self.event2.get())
        self.sq.close()

        MsgBox = msgb.askquestion('Submitted','Submitted and stored successfully',icon='warning')
        if MsgBox == 'yes':
            self.window.destroy()
            st = start_win()
            st.st()
            return
        else:
            msgb.showinfo('Return','You will now return to the screen')
            return

class predict_window:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x450')
        self.window.title('Predict window')
        self.event = StringVar()
        self.num = StringVar()
        self.df = pd.read_csv('data.csv')

        main_label = Label(self.window,text='event',height=3,width=10).grid(column=0,row=1)
        main_text = Entry(self.window,textvariable=self.event).grid(column=1,row=1)
        num_pep = Label(self.window,text='How many people to select').grid(column=0,row=2)
        num_text = Entry(self.window,textvariable=self.num).grid(column=1,row=2)
        # generate = partial(self.generate,self.event,self.num)
        get = Button(self.window,text='get record',command=self.generate).grid(column=1,row=3)
        self.window.mainloop()

    def generate(self):
        s = self.event.get()
        n = self.num.get()
        n = int(n)
        r = rec.predict(s,n)
        rec.close()
        r = r[1:n+1]
        x = []
        for i in r:
            z = i[0]
            x.append(self.df['Name'].iloc[z])
        
        q = ''
        for i in x:
        	q += f'{i} '
        q = q.rstrip()
        q = q.replace(' ',',')
        
        newf = new_df.append({'Event':s,'Recommended Employee':q},ignore_index=True) 
        writer = pd.ExcelWriter('output.xlsx',engine='xlsxwriter')
        newf.to_excel(writer,sheet_name='sheet_1')
        writer.save()

        MsgBox = msgb.askquestion(f'Submitted',f'Data generated and stored in output.xlsx file',icon='warning')
        if MsgBox == 'yes':
            self.window.destroy()
            st = start_win()
            st.st()
        else:
            msgb.showinfo('Return','You will now return to the screen')
            return

class start_win:
    def __init__(self):
        self.hi = 'hi'

    def st(self):
        self.window = Tk()
        self.window.title('Welcome to Cloud Counselage Pvt. Ltd.')
        self.window.geometry("500x500")
        inp = Button(self.window, text = "Click here to enter the Input", height = 2, width = 30,command=self.call)      #Input button
        inp.pack(side=TOP, padx=50, pady=50)

        pred = Button(self.window, text = "Click here to get the Recommendations", height = 2, width = 40,command=self.pred)       #Predict button
        pred.pack(side=TOP, padx=50, pady=50)
        self.window.mainloop()

    def call(self):
        self.window.destroy()
        input_win()
        
        
    def pred(self):
        self.window.destroy()
        predict_window()





        
st = start_win()
st.st()

# Create buttons for Input and Predict