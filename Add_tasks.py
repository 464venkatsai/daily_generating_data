try:
    import data_connector
    from tkinter import * 
    top = Tk()
    task =5
    top.geometry("350x500")
    fr=Frame(top)
    value=[]
    values=[]
    def Add_task():
        ans=StringVar()
        global task
        task = task+1
        def delete_task():
            e1.grid_forget()
            b1.grid_forget()
            ans.set("Deleted")
        e1 = Entry(fr,textvariable=ans,width=12,font="bold 15")
        e1.grid(row=task,column=1,padx=10,pady=5)
        b1=Button(fr,text="Delete",command=delete_task,bd=4,relief=RAISED,width=15)
        b1.grid(row=task,column=3,padx=10,pady=15)
        value.append(ans)
        
    def end():
        for i in value:
            if i.get()!='Deleted':
                values.append(i.get())
                data_connector.columns.append(i.get())
        clear_frame()
        top.geometry("580x180")
        Label(fr,text="Completed Successfully | Thank You !",foreground="green",font="bold 18").grid(row=1,column=1,padx=80,pady=50)
        Button(fr,text="Exit",command=quit,width=10,bd=4,relief=RAISED).grid(row=2,column=1)
        

    def clear_frame():
        for i in fr.winfo_children():
            i.destroy()
    l2=Label(fr,text="Your Tasks : ",font="Bold 10")
    l2.grid(rowspan=1,column=1,padx=1,pady=10)
    for i in range(0,len(data_connector.columns)):
        l2=Label(fr,text=f"{data_connector.columns[i]}")
        l2.grid(row=i+1,column=1,padx=1,pady=1)
    l1=Label(fr,text="Add task",font="Bold 18",width=11)
    l1.grid(row=5,column=1,padx=1,pady=10)
    Button(fr,text="+",command=Add_task,width=3,border=1,font="Bold 10",bd=4,relief=RAISED).grid(row=5,column=2,padx=2)
    Button(fr,text="Submit",command=end,width=15).grid(row=5,column=3,padx=15)
    fr.grid()
    top.mainloop()
except :
    pass
