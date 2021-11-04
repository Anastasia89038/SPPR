import sys
from pathlib import Path
from fpdf import FPDF
from tkinter import *
from tkinter import filedialog

def editDir():
    dir = filedialog.askdirectory()
    folderEdit.delete(0, END)
    folderEdit.insert(0, dir)

def makeFile():
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)

    pdf.multi_cell(0, 10, txt="Министерство науки и высшего образования Российской Федерации", align="C")
    pdf.multi_cell(0, 10, txt="Федеральное государственное бюджетное образовательное учреждение высшего образования", align="C")
    pdf.multi_cell(200, 10, txt="«Волгоградский государственный технический университет»", align="C")
    pdf.multi_cell(200, 10, txt="", align="C")
    pdf.set_font('DejaVu', 'B', 14)
    pdf.multi_cell(200, 10, txt="ТИТУЛ", align="C")
    pdf.set_font('DejaVu', '', 14)
    pdf.multi_cell(200, 10, txt="", align="C")
    pdf.multi_cell(200, 10, txt="Выполнил: " + fioEdit.get())
    pdf.multi_cell(200, 10, txt="Группа: " + groupEdit.get())
    pdf.multi_cell(200, 10, txt="Тема проекта: " + themeEdit.get())
    
    pdf.multi_cell(200, 10, txt="", align="C")
    pdf.multi_cell(200, 10, txt="", align="C")
    pdf.multi_cell(200, 10, txt="", align="C")
    
    pdf.multi_cell(200, 10, txt="г. Волгоград, 2021", align="C")
    
    source_dir = Path(folderEdit.get())
    files = list(source_dir.glob('*.png'))
    
    if len(files) > 0:
        for file in files:
            add_image(pdf, str(file))
    
    pdf.output("document.pdf")
    
def add_image(pdf, image_path):
    if selectedFormat.get() == 2:
        pdf.add_page('L', (297, 420))
        pdf.multi_cell(200, 10, txt="Чертеж " + image_path.split('\\')[-1])
        pdf.image(image_path, h=240)
    elif selectedFormat.get() == 1:
        pdf.add_page('P', (210, 297))
        pdf.multi_cell(200, 10, txt="Чертеж " + image_path.split('\\')[-1])
        pdf.image(image_path, w=190, h=240)

window = Tk()
window.title("Формирование документа")

fioLabel = Label(window, text="ФИО")  
fioLabel.grid(column=0, row=0, padx=2.5, pady=5)
fioEdit = Entry(window, width=40)
fioEdit.grid(column=1, row=0, padx=2.5, pady=5)

groupLabel = Label(window, text="Группа")  
groupLabel.grid(column=0, row=1, padx=2.5, pady=5)
groupEdit = Entry(window, width=40)
groupEdit.grid(column=1, row=1, padx=2.5, pady=5)

themeLabel = Label(window, text="Тема")  
themeLabel.grid(column=0, row=2, padx=2.5, pady=5)
themeEdit = Entry(window, width=40)
themeEdit.grid(column=1, row=2, padx=2.5, pady=5)

folderLabel = Label(window, text="Директория")  
folderLabel.grid(column=0, row=3, padx=2.5, pady=5)
folderEdit = Entry(window, width=40)
folderEdit.grid(column=1, row=3, padx=2.5, pady=5)
folderBtn = Button(window, text="Обзор", command=editDir)
folderBtn.grid(column=3, row=3, padx=2.5, pady=5)

selectedFormat = IntVar()
radioA4 = Radiobutton(window, text='А4', value=1, variable=selectedFormat)
radioA3 = Radiobutton(window, text='А3', value=2, variable=selectedFormat)
radioA4.grid(column=0, row=4, padx=2.5, pady=5)
radioA3.grid(column=1, row=4, padx=2.5, pady=5)

startBtn = Button(window, text="Запуск", command=makeFile)
startBtn.grid(column=1, row=5, padx=2.5, pady=5)

window.mainloop()