import tkinter, random, winsound, time

root = tkinter.Tk()
root.title("Visual Sorting - By Nick Kipshidze")
root.geometry("1000x700")
root.configure(background="Black")
root.resizable(False, False)

def clear():
    for widget in root.winfo_children():
        widget.destroy()
    try: drawUI(False)
    except: pass

class array():
    def findMax():
        global arr
        arrM = arr[0]
        for i in range(0, len(arr)):
            if arrM<arr[i]: arrM = arr[i]
        return arrM
    def refreshList(mode):
        global arr
        plx, arrM = 0, array.findMax()
        clear()
        if mode==1: bkg="White"
        if mode==2: bkg="Red"
        if mode==3: bkg="Green"
        if mode==4: bkg="Blue"
        for i in range(0, len(arr)):
            plx += 24; lbl_line = tkinter.Label(root, borderwidth=0, bg=bkg, pady=arr[i]*8, padx=10).place(x=plx, y=666-(arr[i]*16))
    def listSelect(index, *color):
        global arr
        plx, arrM = 0, array.findMax()
        try:
            if color[0]==1: bkg="White"
            if color[0]==2: bkg="Red"
            if color[0]==3: bkg="Green"
            if color[0]==4: bkg="Blue"
        except: bkg = "Red"
        for i in range(0, len(arr)):
            plx += 24
            if i==index: lbl_line = tkinter.Label(root, borderwidth=0, bg=bkg, pady=arr[i]*8, padx=10).place(x=plx, y=666-(arr[i]*16))
array = array;

def genArray():
    global arr
    arr = []
    arrLen = 30

    while len(arr)<arrLen+1:
        num = random.randint(0, arrLen)
        if num in arr: pass
        else: arr.append(num)
    array.refreshList(1)
    try: drawUI(True)
    except: pass
genArray()

def startVisualBubbleSort():
    global arr
    loop = 0
    while True:
        for i in range(0, len(arr)-loop):
            try:
                if arr[i]>arr[i+1]:
                    tmp = arr[i]; arr[i] = arr[i+1]; arr[i+1] = tmp
            except: pass
            array.refreshList(1); array.listSelect(i); array.listSelect(i+1); root.update(); time.sleep(0.001)
        cor = 0
        for i in range(0, len(arr)):
            try:
                if arr[i]>arr[i+1]: pass
                else: cor += 1;
            except: pass
        if cor==len(arr)-1: break
        loop += 1
    array.refreshList(1); root.update()
    for i in range(0, len(arr)):
        array.listSelect(i, 3); root.update(); array.listSelect(i+2); time.sleep(0.01); root.update()
    array.refreshList(3); root.update()
    drawUI(True)

def startVisualQuickSort():
    global arr
    def partition(arr, low, high):
        i = (low-1)
        pivot = arr[high]
        array.listSelect(pivot, 4); root.update()
        for j in range(low, high):
            array.refreshList(1); array.listSelect(pivot, 4); array.listSelect(i); array.listSelect(j); root.update()
            if arr[j] <= pivot:
                i = i+1
                array.refreshList(1); array.listSelect(pivot, 4); array.listSelect(i); array.listSelect(j); root.update()
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1);     
    def quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            quickSort(arr, low, pi-1)
            quickSort(arr, pi+1, high)
    n = len(arr)
    quickSort(arr, 0, n-1)
    array.refreshList(1); root.update()
    for i in range(0, len(arr)):
        array.listSelect(i, 3); root.update(); array.listSelect(i+2); time.sleep(0.01); root.update()
    array.refreshList(3); root.update()
    drawUI(True)

def drawUI(buttons):
    lbl_note = tkinter.Label(root, text="Hello! My name is Nick Kipshidze. Heres app I wrote with python. What you are looking at now is randomly generated unsorted list. Press buttons on the left to start sorting or regenerate array.",
                             font=("Conolas", 15), wrap=870, foreground="white", bg="Black"); lbl_note.place(x=10, y=10)
    if buttons==True:
        btn_refresh = tkinter.Button(root, text="Regenerate", borderwidth=0, bg="Grey", foreground="White", padx=20, font=("Conolas", 20), command=genArray).place(x=790, y=100)
        btn_bubble = tkinter.Button(root, text="Bubble Sort", borderwidth=0, bg="Grey", foreground="White", padx=20, font=("Conolas", 20), command=startVisualBubbleSort).place(x=790, y=170)
        btn_quick = tkinter.Button(root, text="Quick Sort", borderwidth=0, bg="Grey", foreground="White", padx=27, font=("Conolas", 20), command=startVisualQuickSort).place(x=790, y=240)
drawUI(True)

root.mainloop()
