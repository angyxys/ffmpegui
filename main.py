import os
import ffmpeg
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo, showerror, showwarning

class FrmMain():
  form = tk.Tk()
  def __init__(self):
    self.form.title('FFMPEG Simple GUI')
    self.form.geometry('320x100')
    self.ConfigUI()
    self.form.eval('tk::PlaceWindow . center')
    self.form.mainloop()
  def OpenFileAction(self):
    try:
      filename = filedialog.askopenfilename(
        title='Select Video',
        initialdir='/',
      )
      self.tbxFileName.delete(0, tk.END)
      self.tbxFileName.insert(0, filename)
    except Exception as ex:
      showerror(
        title='Error on file opened',
        message=str(ex)
      )
  def Convert(self):
    output_dir = os.path.join(os.getcwd(), 'output')
    toConvert = self.tbxFileName.get()
    if len(toConvert) > 0:
      if not os.path.exists(output_dir):
        os.mkdir(output_dir)
      out = os.path.join(output_dir, datetime.now().strftime('%Y%m%d%H%M%S') + '.' + self.cbxFormat.get())
      ffmpeg.input(toConvert).output(out).run()
      showinfo(
        title='Complete',
        message='File success converted in ' + out
      )
    else:
      showwarning(
        title='Convert',
        message='Video to convert and Video to Save we needed',
      )
  def ConfigUI(self):
    self.btnOpenFile = tk.Button(self.form, text='Open File', command=self.OpenFileAction)
    self.btnOpenFile.grid(row=0, column=0)
    self.tbxFileName = tk.Entry(self.form)
    self.tbxFileName.grid(row=0, column=1, sticky=tk.E)
    self.lblFormat = tk.Label(self.form, text='Convert To')
    self.lblFormat.grid(row=1, column=0)
    self.cbxFormat = ttk.Combobox(self.form, state='readonly', values=('mp4', 'mov', 'mkv', 'mp3'))
    self.cbxFormat.current(0)
    self.cbxFormat.grid(row=1, column=1)
    self.btnConvert = tk.Button(self.form, text='Convert', command=self.Convert)
    self.btnConvert.grid(row=2, column=0, columnspan=2)

if __name__ == '__main__':
  FrmMain()