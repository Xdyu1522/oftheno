from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.messagebox import *
import sys, time, random
import os
root = Tk()
onlyb = BooleanVar()
nums = IntVar()
def dispipn():
    if onlyb.get() == True:
        pupn.config(state=DISABLED)
    else:
        pupn.config(state=NORMAL)

def start():
    global nums
    global pupn
    global pupi
    global info_text

    try: 
        int(pupi.get())
    except:
        info_text.set('请输入正确的全班人数！')
        return

    try: 
        int(pupn.get())
    except: 
        info_text.set('请输入正确的抽取人数！')
        return

    if int(pupn.get()) > int(pupi.get()):
        info_text.set('抽取人数大于全班人数，请重新输入！')
        return

    if int(pupi.get()) <= 0: 
        info_text.set('请输入正确的全班人数！')
        return
    
    if int(pupn.get()) <= 0: 
        info_text.set('请输入正确的抽取人数！')
        return 

    info_text.set('请输入班级人数与抽号人数开始抽号！')

    if int(pupn.get()) == 1:
        nums.set(random.randint(1, int(pupi.get())))
    else: 
        a = []
        for i in range(int(pupn.get())): 
            b = random.randint(1, int(pupi.get()))
            if not b in a:
                a.append(b)
            else: 
                # b = random.randint(1, int(pupi.get()))
                while b in a:
                    b = random.randint(1, int(pupi.get()))
                a.append(b)
        # nownum = []
        # for i in range(int(pupn.get())):
        #     a = random.randint(1, int(pupi.get()))
        #     if not a in nownum: 
        #         while not a in nownum:
        #             a = random.randint(1, int(pupi.get()))
        #             nownum.append(a)

        # if len(nownum) < int(pupn.get()): 
        #     b = random.randint(1, int(pupi.get()))
        #     if not b in nownum: 
        #         while not b in nownum: 
        #             b = random.randint(1, int(pupi.get()))
        #             nownum.append(b)

        printnum = ''
        for d in range(len(a)):
            printnum = f'{str(printnum)}  {str(a[d])}'

        fina = Toplevel()
        fina.iconbitmap('oftheno.ico')
        fina.geometry('500x500')
        fina.title('抽号器')
        tex = Text(fina, height=5, width=60)
        tex.insert(END, printnum.strip())
        tex.config(state=DISABLED)
        tex.pack(fill=BOTH, expand=True)


    return
        
def wtq():
    res = askokcancel('退出', '确定要退出？')
    if res == True:
        root.destroy()
        sys.exit()
    else:...

def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# print(resource_path(os.path.join('.', 'oftheno.ico')))

root.iconbitmap(resource_path(os.path.join('.', 'oftheno.ico')))
root.geometry('410x200')
root.title('抽号器')
info_text = StringVar()
info_text.set('请输入班级人数与抽号人数开始抽号！')
info = Label(root, textvariable=info_text, font='微软雅黑 15', relief='groove', fg='red')
info.grid(row=0, column=0, columnspan=4, sticky=N)
Label(root, text='班级人数', font='微软雅黑 10').grid(row=1, column=0)
pupi = Spinbox(root, from_=1, to=10000, increment=1)
pupi.grid(row=2, column=0)
Label(root, text='抽号人数', font='微软雅黑 10').grid(row=1, column=1)
pupn = Spinbox(root, from_=1, to=10000, increment=1)
pupn.grid(row=2, column=1)
only = Checkbutton(root, text='锁定抽取人数',variable=onlyb, command=dispipn)
only.grid(row=1,rowspan=2, column=3)
nums.set(None)
num = Label(root, textvariable=nums, font='微软雅黑 30 bold', fg='blue')
num.grid(row=4, column=0, columnspan=4, sticky=N)
startbtn = Button(root, text='开始抽号', font='微软雅黑 20', command=start)
startbtn.grid(row=5, column=0, columnspan=4, sticky=N)
root.protocol('WM_DELETE_WINDOW', wtq)
root.mainloop()