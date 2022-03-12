from tkinter import *
import tkinter as tk 
from tkinter.ttk import Notebook
import asyncio
import threading
import shutil as sh
from functools import partial
from tkinter import messagebox
import os
from tkinter import filedialog
import time

Names = ["Total", "Used", "Free"]
Names_ = ["File type", "Created", "File size"]

class App(tk.Tk):
         
         _stop_update_ = False
         _flag_ = True
         _way_from_ = ""
         _way_from1_ = ""
         _way_from2_ = ""
         _way_from3_ = ""
         _way_to_ = ""
         _list_data_ = list()
         _flag1_ = True
         _flag2_ = True
         
         def __init__(self):
           super().__init__()
        
           self.geometry("305x240+450+180")
           self.resizable(width=False, height=False)
           self.title("file manager")
           self.iconbitmap('folder.ico')
           self.func()
         
         
         def show_message(self):
               value = self.tumb.get()
               self._way_from_ = ""
               self._way_to_ = ""

               if value == 1:
                 self._flag_ = True
                 self.destroy_()

               elif value == 2:
                 self._flag_ = False
                 self.update_func()
                 self.field_for_input.delete("0", END)
          
         def show_message1(self):
               value = self.tumb1.get()
               self._way_from1_ = ""
               if value == 1:
                 self._flag1_ = True
   
               elif value == 2:
        
                 self._flag1_ = False

         def show_message2(self):
               value = self.tumb2.get()
               self._way_from2_ = ""
               self._way_from3_ = ""
               self.field_for_in.delete("0", END)
               if value == 1:
                 self._flag2_ = True
   
               elif value == 2:
                 self._flag2_ = False
         
         def hadler(self, event):

               if event: 
                
                 self._way_from_ = ""
                 self._way_from1_ = ""
                 self._way_from2_ = ""
                 self._way_from3_ = ""
                 self._way_to_ = ""
                
                 try:
                     if self.field_for_input:
                         self.field_for_input.delete("0", END)
                     if self.field_for_in:
                         self.field_for_in.delete("0", END)
                 except:
                     checking = "plug"
                

         def func(self):  

           self.notebook = Notebook(self)
           self.notebook.pack(pady=10, expand=True)
           
           self.frame1 = Frame(self.notebook, width=400, height=250)
           self.frame2 = Frame(self.notebook, width=400, height=250)
           self.frame3 = Frame(self.notebook, width=400, height=250)
           self.frame4 = Frame(self.notebook, width=400, height=250)
           self.frame5 = Frame(self.notebook, width=400, height=250)
           self.frame1.pack(fill='both', expand=True)
           self.frame2.pack(fill='both', expand=True)
           self.tumb = IntVar()
           self.tumb1 = IntVar()
           self.tumb2  = IntVar()
           self.tumb.set(1)
           self.tumb1.set(1)
           self.tumb2.set(1)
           self.notebook.add(self.frame1, text='copy')
           self.notebook.add(self.frame2, text='reomve')
           self.notebook.add(self.frame3, text='rename')
           self.notebook.add(self.frame4, text='files properties') 
           self.notebook.add(self.frame5, text='info about disk') 
           self.copy_files_and_folders()
           self.remove_files_and_folders()
           self.disk_info()
           self.rename_files_and_folders()
           self.files_info()

           self.notebook.bind('<ButtonRelease-1>', self.hadler)
           self.mainloop()
        
         def disk_info(self):
    
           self.text1 = tk.StringVar()
           self.text2 = tk.StringVar()
           self.text3 = tk.StringVar()
           self.text4 = tk.StringVar()
           self.text4.set("Info about of count of memory")
           L = Label(self.frame5, textvariable=self.text1, anchor="center")
           L.place(x=79, y=50)
           L1 = Label(self.frame5, textvariable=self.text2, anchor="center")
           L1.place(x=79, y=90)
           L2 = Label(self.frame5, textvariable=self.text3, anchor="center")
           L2.place(x=79, y=130)
           L3 = Label(self.frame5, textvariable=self.text4, anchor="center")
           L3.place(x=71, y=15)

           L4 = Button(self.frame5, text="stop/begin update",command=self.updating_frame5, width=15, height=1)
           L4.place(x=94, y=160)
           asyncio.run_coroutine_threadsafe(self.data_func(), aioloop)
           
         async def data_func(self):
            
            while True:
                  if not self._stop_update_:
                     if lock_.locked():
                        lock_.release()
                     hdd = sh.disk_usage('/')
                     data = [f"{Names[i]}: {hdd[i] / (2**30)} gb" for i in range(3)]
                     self.text1.set(data[0])
                     self.text2.set(data[1])
                     self.text3.set(data[2])
                   
                  else:
                   #pass
                     if not lock_.locked():
                        lock_.acquire()

                  await asyncio.sleep(1)
               
         def updating_frame5(self):
                if not self._stop_update_:
                   self._stop_update_ = True
                   messagebox.showinfo("Оповещение", "Обновление приостановлено!")
                   return
                else:
                   self._stop_update_ = False
                   messagebox.showinfo("Оповещение", "Обновление возобновлено!")
                   return
              
         def destroy_(self):
            for value in self._list_data_:
               value.destroy()


         def update_func(self):

            self.name_ = Label(self.frame1, text="Destination folder:")
            self.field_for_input = Entry(self.frame1, textvariable=self.way_to, width=18)
            self.field_for_input.place(x=170, y=80)
            self.name_.place(x=55, y=80)
            self._list_data_ = [self.name_,  self.field_for_input]

           
         async def copy(self):
               
               self.button_.config(state="disabled")
               self.switcher.config(state="disabled")
               self.switcher_.config(state="disabled")
               
               if self._flag_:
                  
                  self.btn.config(state="disabled")
                  try:
                     self.btn.config(state="disabled")
                     sh.copy(self._way_from_, self._way_to_)
                     messagebox.showinfo("Оповещение", "Копирование файла выполнено успешно!")
                     
                     
                  except:
                     messagebox.showinfo("Оповещение", "Возникло исключение при копировании файла, повторите попытку ввода путей!")
                  self.btn.config(state="active")  
               else:

                  self.btn.config(state="disabled")
                  try:
                     sh.copytree(self._way_from_, self._way_to_ + "/" + self.way_to.get())
                     messagebox.showinfo("Оповещение", "Копирование директории выполнено успешно!")
                     self.field_for_input.delete("0", END)
                    
                     
                  except:
                     messagebox.showinfo("Оповещение", "Возникло исключение при копировании директории, повторите попытку ввода путей!")
                     self.field_for_input.delete("0", END)
                  self.btn.config(state="active")
                    
               self.button_.config(state="active")
               self.switcher.config(state="active")
               self.switcher_.config(state="active")
               
                  
         def found_data(self):
               
               if self._flag_:
                  self._way_from_ = filedialog.askopenfilename(title="open file")
                  if self._way_from_:
                     self._way_to_ = filedialog.askdirectory(title="open folder")
                
               else:
                  self._way_from_ = filedialog.askdirectory(title="open folder from")
                  if self._way_from_:
                     self._way_to_ = filedialog.askdirectory(title="open folder to")
                  if self._way_from_ and self._way_to_:
                     messagebox.showinfo("Оповещение", "Не забудьте заполнить поле ввода!")
                  
         def found_data1(self):
               if self._flag1_:
                  self._way_from1_ = filedialog.askopenfilename(title="open file")
   
               else:
                  self._way_from1_ = filedialog.askdirectory(title="open folder")

         def parsing_some_data(self):
               if self._way_from2_:
                     self._way_from3_ = self._way_from2_.split("/")[0:-1]
                     value = self._way_from3_[0] + "/"
                     for i in range(1, len(self._way_from3_)):
                         value += (self._way_from3_[i] +"/")
                     self._way_from3_ = value
         
         def found_data2(self):
               if self._flag2_:
                  self._way_from2_ = filedialog.askopenfilename(title="open file")
                  self.parsing_some_data()
                  if self._way_from2_:
                     messagebox.showinfo("Оповещение", "Не забудьте заполнить поле ввода!")
               else:
                  self._way_from2_ = filedialog.askdirectory(title="open folder")
                  self.parsing_some_data()
                  if self._way_from2_:
                     messagebox.showinfo("Оповещение", "Не забудьте заполнить поле ввода!")

         def delete(self):
               while True:
                  if self._flag1_:
                     try:
                        os.remove(self._way_from1_)
                        messagebox.showinfo("Оповещение", "Удаление файла выполнено успешно!")
                        return
                     except:
                        messagebox.showinfo("Оповещение", "Возникло исключение при удалении файла, повторите попытку ввода путей!")
                        return
                  else:
                     try:
                        sh.rmtree(self._way_from1_)
                        messagebox.showinfo("Оповещение", "Удаление директории выполнено успешно!")
                        return
                     except:
                        messagebox.showinfo("Оповещение", "Возникло исключение при удалении директории, повторите попытку ввода путей!")
                        return
                     
         def rename(self):
                  while True:
                     if self._flag2_:
                        try:
                           os.rename(self._way_from2_, self._way_from3_ + self.way.get())
                           messagebox.showinfo("Оповещение", "Переименование файла выполнено успешно!")
                           self.field_for_in.delete("0", END)
                           return
                        except:
                           messagebox.showinfo("Оповещение", "Возникло исключение при переименовании файла, повторите попытку ввода путей!")
                           self.field_for_in.delete("0", END)
                           return
                     else:
                        try:
                           os.rename(self._way_from2_, self._way_from3_ + self.way.get())
                           messagebox.showinfo("Оповещение", "Переименование директории выполнено успешно!")
                           self.field_for_in.delete("0", END)
                           return
                        except:
                           messagebox.showinfo("Оповещение", "Возникло исключение при переименовании директории, повторите попытку ввода путей!")
                           self.field_for_in.delete("0", END)
                           return
         
         def show_info(self):
            file_way = filedialog.askopenfilename()
            if file_way:
               file_name = file_way.split("/")[-1]
               create_date = os.path.getctime(file_way)
               year,month,day,hour,minute,second = time.localtime(create_date)[:-3]
               self.t1.set(f"{Names_[0]}:  {'.' + file_way.split('/')[-1].split('.')[-1]}")
               self.t2.set(f"{Names_[1]}:  " + '%02d/%02d/%d %02d:%02d:%02d' % (day,month,year,hour,minute,second))
               self.t3.set(f"{Names_[2]}:  {'{:.4f}'.format(os.path.getsize(file_way) / 1000000)}Mb")
               self.t4.set(file_name)


         def copy_files_and_folders(self):
            
            self.way_to = StringVar()
            self.button_ = Button(self.frame1, text="select data to copy", command=self.found_data)
            self.btn = Button(self.frame1, text="Accept", command=lambda: asyncio.run_coroutine_threadsafe(self.copy(), aioloop1))
           
            self.switcher = Radiobutton(self.frame1, text="file", value=1, variable=self.tumb, command=self.show_message)
            self.switcher_ = Radiobutton(self.frame1, text="directory", value=2, variable=self.tumb, command=self.show_message)
            self.switcher.place(x=30, y=125)
            self.switcher_.place(x=80, y=125)
            self.button_.place(x=170, y=30)
            self.btn.place(x=170, y=125)

         def remove_files_and_folders(self):
            
            self.but = Button(self.frame2, text="select data to remove", command=self.found_data1)
            self.but_ = Button(self.frame2, text="Accept", command=self.delete) 
            self.sw = Radiobutton(self.frame2, text="file", value=1, variable=self.tumb1, command=self.show_message1)
            self.sw_ = Radiobutton(self.frame2, text="directory", value=2, variable=self.tumb1, command=self.show_message1)
            self.sw.place(x=95, y=85)
            self.sw_.place(x=140, y=85)
            self.but.place(x=92, y=30)
            self.but_.place(x=125, y=128)
         
         def rename_files_and_folders(self):
            
            self.way = StringVar()
            self.butt = Button(self.frame3, text="select data to rename", command=self.found_data2)
            self.butt_ = Button(self.frame3, text="Accept", command=self.rename) 
            self.sww = Radiobutton(self.frame3, text="file", value=1, variable=self.tumb2, command=self.show_message2)
            self.sww_ = Radiobutton(self.frame3, text="directory", value=2, variable=self.tumb2, command=self.show_message2)
            self.nam = Label(self.frame3, text="New name:")
            self.field_for_in = Entry(self.frame3, textvariable=self.way,width=20)
            self.field_for_in.place(x=93, y=55)
            self.nam.place(x=10, y=55)
            self.sww.place(x=95, y=88)
            self.sww_.place(x=140, y=88)
            self.butt.place(x=93, y=10)
            self.butt_.place(x=128, y=131)
         
         def files_info(self):

               self.bu = Button(self.frame4, text="select file to show his info", command=self.show_info)
               self.bu.place(x=81, y=113)
        
               self.t1 = tk.StringVar()
               self.t2 = tk.StringVar()
               self.t3 = tk.StringVar()
               self.t4 = tk.StringVar()
            
               self.n1 = Label(self.frame4, textvariable=self.t1, anchor="center")
               self.n2 = Label(self.frame4, textvariable=self.t2, anchor="center")
               self.n3 = Label(self.frame4, textvariable=self.t3, anchor="center")
               self.n4 = Label(self.frame4, text="file:", anchor="center")
               self.n5 = Label(self.frame4, textvariable=self.t4, anchor="center")
               self.n1.place(x=85, y=15)
               self.n2.place(x=85, y=50)
               self.n3.place(x=85, y=85)
               self.n4.place(x=17, y=148)
               self.n5.place(x=47, y=148)
               
   
if __name__ == "__main__":
   
   def _run_aio_loop(loop):
      asyncio.set_event_loop(loop)
      loop.run_forever()
        
   aioloop = asyncio.new_event_loop()
   aioloop1 = asyncio.new_event_loop()
   t = threading.Thread(target=partial(_run_aio_loop, aioloop), name="Thread_1")
   t.daemon = True  # Необязательно, в зависимости от того, как планируется закрыть приложение
   t.start()    
   t1 = threading.Thread(target=partial(_run_aio_loop, aioloop1), name="Thread_2")
   t1.daemon = True
   t1.start()
   lock_ = threading.Lock()
  
   App()
   
   
   
   