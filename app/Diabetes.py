import pickle
with open('model_pickle','rb') as f:
    mp=pickle.load(f)
import tkinter as tk
from tkinter import ttk
win = tk.Tk()

win.title('Diabetes Predictions')
#Column 1 
Preg=ttk.Label(win,text="Pregnancies")
Preg.grid(row=0,column=0,sticky=tk.W)
Preg_var=tk.StringVar()
Preg_entrybox=ttk.Entry(win,width=16,textvariable=Preg_var)
Preg_entrybox.grid(row=0,column=1)
#Column 2
Glus=ttk.Label(win,text="Glucose")
Glus.grid(row=1,column=0,sticky=tk.W)
Glus_var=tk.StringVar()
Glus_entrybox=ttk.Entry(win,width=16,textvariable=Glus_var)
Glus_entrybox.grid(row=1,column=1)
#Column 3
Pres=ttk.Label(win,text="BloodPressure")
Pres.grid(row=2,column=0,sticky=tk.W)
Pres_var=tk.StringVar()
Pres_entrybox=ttk.Entry(win,width=16,textvariable=Pres_var)
Pres_entrybox.grid(row=2,column=1)
#Column 4
skin=ttk.Label(win,text="skinThickness")
skin.grid(row=3,column=0,sticky=tk.W)
skin_var=tk.StringVar()
skin_entrybox=ttk.Entry(win,width=16,textvariable=skin_var)
skin_entrybox.grid(row=3,column=1)
#Column 5
insulin=ttk.Label(win,text="insulin")
insulin.grid(row=4,column=0,sticky=tk.W)
insulin_var=tk.StringVar()
insulin_entrybox=ttk.Entry(win,width=16,textvariable=insulin_var)
insulin_entrybox.grid(row=4,column=1)
#Column 6
BMI=ttk.Label(win,text="BMI")
BMI.grid(row=5,column=0,sticky=tk.W)
BMI_var=tk.StringVar()
BMI_entrybox=ttk.Entry(win,width=16,textvariable=BMI_var)
BMI_entrybox.grid(row=5,column=1)
#Column 7
pedi=ttk.Label(win,text="pedigreeFunction")
pedi.grid(row=6,column=0,sticky=tk.W)
pedi_var=tk.StringVar()
pedi_entrybox=ttk.Entry(win,width=16,textvariable=pedi_var)
pedi_entrybox.grid(row=6,column=1)
#Column 8
age=ttk.Label(win,text="age")
age.grid(row=7,column=0,sticky=tk.W)
age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=7,column=1)

import pandas as pd
DF = pd.DataFrame()
def predict():

    import pandas as pd
    DF = pd.DataFrame(columns=['Preg','Glus','Pres','skin','insulin','BMI','pedigree','age'])
    PREG=Preg_var.get()
    DF.loc[0,'Preg']=PREG
    GLUCOS=Glus_var.get()
    DF.loc[0,'Glus']=GLUCOS
    PRES=Pres_var.get()
    DF.loc[0,'Pres']=PRES
    SKIN=skin_var.get()
    DF.loc[0,'skin']=SKIN
    INSULIN=insulin_var.get()
    DF.loc[0,'insulin']=INSULIN
    BMIV=BMI_var.get()
    DF.loc[0,'BMI']=BMIV
    PEDI=pedi_var.get()
    DF.loc[0,'pedigree']=PEDI
    AGE=age_var.get()
    DF.loc[0,'age']=AGE
    DF["Glus"] = pd.to_numeric(DF["Glus"])
    DF["Pres"] = pd.to_numeric(DF["Pres"])
    DF["skin"] = pd.to_numeric(DF["skin"])
    DF["insulin"] = pd.to_numeric(DF["insulin"])
    DF["BMI"] = pd.to_numeric(DF["BMI"])
    DF["pedigree"] = pd.to_numeric(DF["pedigree"])
    DF["age"] = pd.to_numeric(DF["age"])
    if mp.predict(DF)==1:
       Predict_entrybox.insert(0,"Diabetes")
    else:
       Predict_entrybox.insert(0,"No Diabetes")
Predict_entrybox=ttk.Entry(win,width=16)
Predict_entrybox.grid(row=20,column=1)
Predict_button=ttk.Button(win,text="Predict",command=predict)
Predict_button.grid(row=20,column=0)

win.mainloop()