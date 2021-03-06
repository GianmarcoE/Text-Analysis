import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = '#0000a0')
canvas1.pack()

def getFile ():

    import_file_path = filedialog.askopenfilename()
    #can implement a partial check of sentences instead of words by words
    positive = ["high salary", "inspiring people", "'m happy", "are happy", "am happy", "friendly", "improve skills", "amazing", "I appreciate", "stable company", "are available",
                    "helpful", "open culture", "easy", "good", "positive", "nice", "kind", "great", "cool", "pleasent"
                    ]
    negative = ["low salary", "noisy", "going down", "not understanding", "unfortunate", "sad", "not appreciate", "I don't appreciate", "are not available", "heavy bureaucracy",
                     "downside", "downsizing", "high bureaucracy", "cutting", "cuts", "cuttings","lack","unclear", "bad", "poor", "negative", "rude", "worse", "worst"
                     ]
    salary = ["remuneration", "compensation", "salary"]

    people = ["manager", "leader", "people", "colleague"]

    culture = ["atmoshpere", "culture"]

    development = ["learning", "development", "growing", "developing", "opportunities"]

    development_count = 0
    culture_count = 0
    people_count = 0
    salary_count = 0
    positive_count = 0
    negative_count = 0

    fopen = open(import_file_path, 'r', encoding="Latin-1")
    fileinput = fopen.read()

    already_printed_positive = set()
    already_printed_negative = set()    

    for i in positive:
        for line in fileinput.splitlines():
            if i in line:
                positive_count += 1
                #if line not in already_printed_positive:
                 #   print(f"{line}\n")
                  #  already_printed_positive.add(line)
                    
    for i in negative:
        for line in fileinput.splitlines():
            if i in line:
                negative_count += 1
                #if line not in already_printed_negative:
                  # print(f"{line}\n")
                   #already_printed_negative.add(line)

    for i in salary:
        for line in fileinput.splitlines():
            if i in line:
                salary_count += 1

    for i in people:
        for line in fileinput.splitlines():
            if i in line:
                people_count += 1

    for i in culture:
        for line in fileinput.splitlines():
            if i in line:
                culture_count += 1

    for i in development:
        for line in fileinput.splitlines():
            if i in line:
                development_count += 1

    def seeSalary ():
        comments=tk.Tk()
        comments.title("Salary - Comments")
        comments.geometry('600x500')
        container = Frame(comments)
        canvas = tk.Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        salary = ["remuneration", "compensation", "salary"]
        already_printed_salary = set()
        for i in salary:
            for line in fileinput.splitlines():
                if i in line:
                    if line not in already_printed_salary:
                        comment=Message(scrollable_frame, text=f"{line}\n", anchor= 'w', width=430, font=12)
                        comment.pack(ipadx=15)
                        sep = Separator(scrollable_frame, orient="horizontal")
                        sep.pack(fill='x')
                        already_printed_salary.add(line)

        container.pack(fill=BOTH, expand=YES)
        canvas.pack(side="left", fill="both", expand=YES)
        scrollbar.pack(side="right", fill="y")

    def seePeople ():
        comments=tk.Tk()
        comments.title("People - Comments")
        comments.geometry('600x500')
        container = Frame(comments)
        canvas = tk.Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        people = ["manager", "leader", "people", "colleague"]
        already_printed_people = set()
        for i in people:
            for line in fileinput.splitlines():
                if i in line:
                    if line not in already_printed_people:
                        comment=Message(scrollable_frame, text=f"{line}\n", anchor= 'w', width=430, font=12)
                        comment.pack(ipadx=15)
                        sep = Separator(scrollable_frame, orient="horizontal")
                        sep.pack(fill='x')
                        already_printed_people.add(line)

        container.pack(fill=BOTH, expand=YES)
        canvas.pack(side="left", fill="both", expand=YES)
        scrollbar.pack(side="right", fill="y")

    def seeCulture ():
        comments=tk.Tk()
        comments.title("Culture - Comments")
        comments.geometry('600x500')
        container = Frame(comments)
        canvas = tk.Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        culture = ["atmoshpere", "culture"]
        already_printed_culture = set()
        for i in culture:
            for line in fileinput.splitlines():
                if i in line:
                    if line not in already_printed_culture:
                        comment=Message(scrollable_frame, text=f"{line}\n", anchor= 'w', width=430, font=12)
                        comment.pack(ipadx=15)
                        sep = Separator(scrollable_frame, orient="horizontal")
                        sep.pack(fill='x')
                        already_printed_culture.add(line)

        container.pack(fill=BOTH, expand=YES)
        canvas.pack(side="left", fill="both", expand=YES)
        scrollbar.pack(side="right", fill="y")

    def seeDevelopment ():
        comments=tk.Tk()
        comments.title("Development - Comments")
        comments.geometry('600x500')
        container = Frame(comments)
        canvas = tk.Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        development = ["learning", "development", "growing", "developing", "opportunities"]
        already_printed_development = set()
        for i in development:
            for line in fileinput.splitlines():
                if i in line:
                    if line not in already_printed_development:
                        comment=Message(scrollable_frame, text=f"{line}\n", anchor= 'w', width=430, font=12)
                        comment.pack(ipadx=15)
                        sep = Separator(scrollable_frame, orient="horizontal")
                        sep.pack(fill='x')
                        already_printed_development.add(line)

        container.pack(fill=BOTH, expand=YES)
        canvas.pack(side="left", fill="both", expand=YES)
        scrollbar.pack(side="right", fill="y")

    overall = Label(root, text="Overall feedback")
    overall.pack()
    positive = Label(root, text=f"Positive mentions: {positive_count} - {(positive_count/(positive_count+negative_count))*100:.2f}%")
    positive.pack()
    negative = Label(root, text=f"Negative mentions: {negative_count} - {(negative_count/(positive_count+negative_count))*100:.2f}%")
    negative.pack()
    topics = Label(root, text="\nTopics")
    topics.pack()
    salary = tk.Button(text=f"Mentions about salary: {salary_count}", command=seeSalary)
    salary.pack(fill='x')
    people = tk.Button(text=f"Mentions about people: {people_count}", command=seePeople)
    people.pack(fill='x')
    culture = tk.Button(text=f"Mentions about culture: {culture_count}", command =seeCulture)
    culture.pack(fill='x')
    development = tk.Button(text=f"Mentions about development: {development_count}", command=seeDevelopment)
    development.pack(fill='x')

    fopen.close()
    
browseButton_Excel = tk.Button(text='Import File', command=getFile, bg='lightsteelblue', fg='white', font=('helvetica', 12))
canvas1.create_window(150, 150, window=browseButton_Excel)


root.mainloop()
