import numpy as np
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk ,Image
import cv2 as cv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class FrameDAta:
    f1_H=0
    f1_W=0
    
    def update(self,f1_H=0,f1_W=0):
        self.f1_H=f1_H
        self.f1_W=f1_W
        print("saboot :",self.f1_H,self.f1_W)

class Main:
    
    def __init__(self):
        self.start()

    def start(self):
        self.root = Tk()
        
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.s_h = int(round(screen_height,-2))
        self.s_w = int(round(screen_width,-2))
        if self.s_w>1500:
            self.s_w=1500
        if self.s_h<500:
            self.s_h=500

        self.s_h-=100

        print('system Screen resolution [w,h]: ',self.s_w,self.s_h)

        self.root.title('DipTool')
        self.root.geometry(f"{self.s_w}x{self.s_h}")
        self.root.config(bg='Aqua')
    #     
        self.mainMenu()
        self.createFrames()
        self.createCanvas(self.sysOptionsFrame)
        self.root.update_idletasks()
        sw.DisplayScreen(self.ImageDispFrame)
        sw.desplMessFrame(self.cFrame)
        sw.deployImpButtons(self.ImageDelButtonFrame)

        self.root.mainloop()

    def createFrames(self):
        self.mf_w = int(self.s_w/1.001)-28
        self.mf_h = int(self.s_h/1.2)
        self.cf_h = int(self.s_h/8)-4


        mFrame = Frame(master=self.root, height=self.mf_h, width=self.mf_w, bg='orange')
        self.cFrame = Frame(master=self.root, height=self.cf_h, width=self.mf_w, bg="blue")
        
        mFrame.grid(row=0,column=0,sticky='ew',padx=15,pady=5)
        self.cFrame.grid(row=1,column=0,sticky='ew',padx=15,pady=5)

        self.ImageDispFrame = Frame(master=mFrame, height=self.mf_h-10 ,width=int(self.mf_w*0.7))
        self.ImageDelButtonFrame = Frame(master=mFrame,height=int(self.mf_h*0.15),width=int(self.mf_w*0.29),bg='lightgreen')
        self.sysOptionsFrame = Frame(master=mFrame,height=int(self.mf_h*0.81),width=int(self.mf_w*0.29))

        self.ImageDispFrame.grid(row=0,column=0,sticky='ew',padx=5,pady=5,rowspan=2)
        self.ImageDelButtonFrame.grid(row=0,column=1,sticky='ew',padx=5,pady=5)
        self.sysOptionsFrame.grid(row=1,column=1,sticky='ew',padx=5,pady=5)
        
        

    def createCanvas(self,frame):
        self.myCanvas = Canvas(frame,bg='white',height=int(self.mf_h*0.81),width=int(self.mf_w*0.29)-15)
        self.myCanvas.grid(column=0,row=0,sticky=NSEW)

        self.myscrollbar = ttk.Scrollbar(frame,orient=VERTICAL, command=self.myCanvas.yview)
        self.myscrollbar.grid(column=1,row=0,sticky=NS)

        self.myCanvas.configure(yscrollcommand=self.myscrollbar.set)

        self.subframe2 = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0),window=self.subframe2,anchor="nw")

        self.myCanvas.bind('<Configure>', func = lambda e: self.myCanvas.configure(scrollregion= self.myCanvas.bbox("all")))


    def mainMenu(self):
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)
        
        #create a menu item

            #option1
        self.option1_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Basic',menu=self.option1_menu)
        self.option1_menu.add_command(label='convolutions',command=self.option1_c1)
        self.option1_menu.add_separator()
        self.option1_menu.add_command(label='Quit',command=self.root.quit)

            #option2
        option2_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='pre-process',menu=option2_menu)
        option2_menu.add_command(label='Quantization',command=self.option2_c1)

        option3_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Enhancement',menu=option3_menu)
        option3_menu.add_command(label='Filters',command=self.option3_c1)
        option3_menu.add_separator()

        option4_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Transformation',menu=option4_menu)
        option4_menu.add_command(label='Simple Transform',command=self.option4_c1)
        option4_menu.add_separator()
        
        option5_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Binary Image Processing',menu=option5_menu)
        option5_menu.add_command(label='Dilation and Erosion',command=self.option5_c1)

        option6_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Colour Image Processing',menu=option6_menu)
        option6_menu.add_command(label='Colour Model',command=self.option6_c1)
        option6_menu.add_separator()
        option6_menu.add_command(label='Colour Segments',command=self.option6_c2)
        
    # #ckick Command
    def option1_c1(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        sofSetup.option_1_c1(self.subframe2)        

    def option2_c1(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        sofSetup.option_2_c1(self.subframe2) 

    def option3_c1(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        sofSetup.option_3_c1(self.subframe2)  

    def option4_c1(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        sofSetup.option_4_c1(self.subframe2)

    def option5_c1(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        sofSetup.option_5_c1(self.subframe2)

    def option6_c1(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        sofSetup.option_6_c1(self.subframe2)
    def option6_c2(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        sofSetup.option_6_c2(self.subframe2)
        
class sysOptionFrameSetup:
    def __init__(self) -> None:
        pass

    def option_1_c1(self,frame):
        inputSeqField = LabelFrame(frame,text='Linear Convolution')
        inputSeq1Label = Label(inputSeqField,text="Enter the sequence 1 : ")
        inputSeq2Label = Label(inputSeqField,text="Enter the sequence 2 : ")
        inputSeq1_1 = Entry(inputSeqField,width=2)
        inputSeq1_2 = Entry(inputSeqField,width=2)
        inputSeq1_3 = Entry(inputSeqField,width=2)
        inputSeq1_4 = Entry(inputSeqField,width=2)
        inputSeq2_1 = Entry(inputSeqField,width=2)
        inputSeq2_2 = Entry(inputSeqField,width=2) 
        inputSeq2_3 = Entry(inputSeqField,width=2)
        inputSeq2_4 = Entry(inputSeqField,width=2)

        inputSeq1_1.grid(row=0,column=1)
        inputSeq1_2.grid(row=0,column=2)
        inputSeq1_3.grid(row=0,column=3)
        inputSeq1_4.grid(row=0,column=4)
        inputSeq2_1.grid(row=1,column=1)
        inputSeq2_2.grid(row=1,column=2)
        inputSeq2_3.grid(row=1,column=3)
        inputSeq2_4.grid(row=1,column=4)

        
        inputSeq1Label.grid(row=0,column=0)
        inputSeq2Label.grid(row=1,column=0)

        inputSeqField.grid(row=0,column=0,pady=10,padx=10)
        
        
        submitButton = Button(frame,text="Go",width=7,command=lambda : ssw.displayPLOTLin(inputSeqField))
        submitButton.grid(row=1,column=0,columnspan=1,sticky="e")


        inputSeqFieldC = LabelFrame(frame,text='Circular Convolution')
        inputSeq1LabelC = Label(inputSeqFieldC,text="Enter the sequence 1 : ")
        inputSeq2LabelC = Label(inputSeqFieldC,text="Enter the sequence 2 : ")
        inputSeq1_1C = Entry(inputSeqFieldC,width=2)
        inputSeq1_2C = Entry(inputSeqFieldC,width=2)
        inputSeq1_3C = Entry(inputSeqFieldC,width=2)
        inputSeq1_4C = Entry(inputSeqFieldC,width=2)
        inputSeq2_1C = Entry(inputSeqFieldC,width=2)
        inputSeq2_2C = Entry(inputSeqFieldC,width=2) 
        inputSeq2_3C = Entry(inputSeqFieldC,width=2)
        inputSeq2_4C = Entry(inputSeqFieldC,width=2)

        inputSeq1_1C.grid(row=0,column=1)
        inputSeq1_2C.grid(row=0,column=2)
        inputSeq1_3C.grid(row=0,column=3)
        inputSeq1_4C.grid(row=0,column=4)
        inputSeq2_1C.grid(row=1,column=1)
        inputSeq2_2C.grid(row=1,column=2)
        inputSeq2_3C.grid(row=1,column=3)
        inputSeq2_4C.grid(row=1,column=4)

        
        inputSeq1LabelC.grid(row=0,column=0)
        inputSeq2LabelC.grid(row=1,column=0)

        inputSeqFieldC.grid(row=2,column=0,pady=10,padx=10)
        
        
        submitButtonC = Button(frame,text="Go",width=7,command=lambda : ssw.displayPLOTCir(inputSeqFieldC))
        submitButtonC.grid(row=3,column=0,columnspan=1,sticky="e")

    def option_2_c1(self,frame):
        QuantField = LabelFrame(frame,text='Quantization')
        self.QuantBitLabelLPF = Label(QuantField,text='Bits/pixel value : ')
        self.QuantBits_SpinboxLPF = ttk.Spinbox(QuantField,from_=2,to=16)

        self.QuantBitLabelLPF.grid(row=0,column=0,columnspan=2)
        self.QuantBits_SpinboxLPF.grid(row=0,column=1,columnspan=2)
        QuantField.grid(row=0,column=0)
        self.GenButtonQuant = Button(frame,text='Generate',bg='lightgreen',command=ssw.Get_DataForQuantization)
        self.GenButtonQuant.grid(row=1,column=0,columnspan=2,sticky=E)


    def option_3_c1(self,frame):
        LowPassField = LabelFrame(frame,text='Low Pass Filter')
        self.kernalLabelLPF = Label(LowPassField,text='Kernel uint :')
        self.kernal_SpinboxLPF = ttk.Spinbox(LowPassField,from_=2,to=5)
        
        self.kernalLabelLPF.grid(row=0,column=0)
        self.kernal_SpinboxLPF.grid(row=0,column=1)

        self.FilterOptionLabelLPF = Label(LowPassField,text='Filter')
        self.Filter_ComboBoxLPF = ttk.Combobox(LowPassField,values=['Boxfilter','convoluted','Blur','GaussianBlur'])
        self.Filter_ComboBoxLPF.set('Blur')
        self.FilterOptionLabelLPF.grid(row=1,column=0)
        self.Filter_ComboBoxLPF.grid(row=1,column=1)
        LowPassField.grid(row=0,column=0,pady=10,padx=10)

        #submitbutton
        self.GenButtonLPF = Button(frame,text='Generate',bg='lightgreen',command=ssw.Get_DataForLPF)
        self.GenButtonLPF.grid(row=1,column=0,columnspan=2,sticky=N)

        #high pass field
        HighPassField = LabelFrame(frame,text='High Pass Filter')

        self.kernalLabelHPF = Label(HighPassField,text='Kernel size :')
        self.kernal_SpinboxHPF = ttk.Spinbox(HighPassField,from_=1,to=31)
        
        self.kernalLabelHPF.grid(row=1,column=0)
        self.kernal_SpinboxHPF.grid(row=1,column=1)

        self.FilterOptionLabelHPF = Label(HighPassField,text='Filter')
        self.Filter_ComboBoxHPF = ttk.Combobox(HighPassField,values=['Laplacian','Sobel','Scharr'])
        self.Filter_ComboBoxHPF.set('Sobel')
        self.FilterOptionLabelHPF.grid(row=2,column=0)
        self.Filter_ComboBoxHPF.grid(row=2,column=1)

        HighPassField.grid(row=2,column=0,pady=10,padx=10)
        #submitbutton
        self.GenButtonHPF = Button(frame,text='Generate',bg='lightgreen',command=ssw.Get_DataForHPF)
        self.GenButtonHPF.grid(row=3,column=0,columnspan=2,sticky=N)        

        for widget in frame.winfo_children():
            widget.grid_configure(pady=10,padx=2)
        pass
    
    def option_4_c1(self,frame):
        HaarTField = LabelFrame(frame,text='Haar Transformation')
        
        HaarKernelLabel = Label(HaarTField,text="kernal size [4,8,..] : ")
        self.HaarKernelEnrty = Entry( HaarTField ,width=5)
        GenButtonHaar = Button(HaarTField,text='Generate',bg='lightgreen',command=ssw.Get_DataForHaarT)

        HaarKernelLabel.grid(row=0,column=0)
        self.HaarKernelEnrty.grid(row=0,column=1)
        GenButtonHaar.grid(row=1,column=1,columnspan=2,sticky=E)   
        HaarTField.grid(row=0,column=0)

        for widget in frame.winfo_children():
            widget.grid_configure(pady=10,padx=2)
            for widgets in widget.winfo_children():
                widgets.grid_configure(pady=10,padx=2)

    def option_5_c1(self,frame):
        DilationField = LabelFrame(frame,text='Dilation')
        kernalLabelDilation = Label(DilationField,text='Kernel size (odd) :')
        self.KernelSizeForDil = Entry(DilationField,width=4)

        ErosionField = LabelFrame(frame,text='Erosion')
        kernalLabelErosion = Label(ErosionField,text='Kernel size (odd) :')
        self.KernelSizeForErosion = Entry(ErosionField,width=4)

        submitButtonDilation = Button(DilationField,text="submit",width=7,command=ssw.Get_DataFordilate)
        submitButtonErosion = Button(ErosionField,text="submit",width=7,command=ssw.Get_DataForerode)
        
        DilationField.grid(row=0,column=0)
        ErosionField.grid(row=1,column=0,pady=2)

        kernalLabelDilation.grid(row=0,column=0)
        self.KernelSizeForDil.grid(row=0,column=1)

        kernalLabelErosion.grid(row=0,column=0)
        self.KernelSizeForErosion.grid(row=0,column=1)

        submitButtonDilation.grid(row=1,column=1,columnspan=1,sticky=E)
        submitButtonErosion.grid(row=1,column=1,columnspan=1,sticky=E)
        for widget in frame.winfo_children():
            widget.grid_configure(pady=10,padx=2)
            for widgets in widget.winfo_children():
                widgets.grid_configure(pady=10,padx=2)
         
        pass

    def option_6_c1(self,frame):
        self.FilterOptionLabelCC = Label(frame,text='Convert To :')
        self.Filter_ComboBoxCC = ttk.Combobox(frame,values=['BGR','GRAY','HSV','HLS'])
        self.Filter_ComboBoxCC.set('BGR')
        self.FilterOptionLabelCC.grid(row=2,column=0)
        self.Filter_ComboBoxCC.grid(row=2,column=1)     

        #submitbutton
        self.GenButtonCC = Button(frame,text='Generate',bg='lightgreen',command=ssw.Get_DataForCC)
        self.GenButtonCC.grid(row=3,column=0,columnspan=2,sticky=N)  

        for widget in frame.winfo_children():
            widget.grid_configure(pady=10,padx=2) 
        pass

    def option_6_c2(self,frame):
        ColorplaneimgLabel = LabelFrame(frame,text='- Different Color planes -')
        self.GenButtonCSegr = Button(ColorplaneimgLabel,text='red',bg='lightgreen',command=ssw.Get_DataForCSegr)
        self.GenButtonCSegr.grid(row=0,column=0)
        self.GenButtonCSegg = Button(ColorplaneimgLabel,text='green',bg='lightgreen',command=ssw.Get_DataForCSegg)
        self.GenButtonCSegg.grid(row=0,column=1)
        self.GenButtonCSegb = Button(ColorplaneimgLabel,text='blue',bg='lightgreen',command=ssw.Get_DataForCSegb)
        self.GenButtonCSegb.grid(row=0,column=2)
        ColorplaneimgLabel.grid(row=0,column=0)

        GreyplaneimgLabel = LabelFrame(frame,text='- Grey scale img of Color plane -')
        self.GenButtonCSegR = Button(GreyplaneimgLabel,text='Red',bg='lightgreen',command=ssw.Get_DataForCSegR)
        self.GenButtonCSegR.grid(row=0,column=0)
        self.GenButtonCSegG = Button(GreyplaneimgLabel,text='Green',bg='lightgreen',command=ssw.Get_DataForCSegG)
        self.GenButtonCSegG.grid(row=0,column=1)
        self.GenButtonCSegB = Button(GreyplaneimgLabel,text='Blue',bg='lightgreen',command=ssw.Get_DataForCSegB)
        self.GenButtonCSegB.grid(row=0,column=2)
        GreyplaneimgLabel.grid(row=1,column=0)


        for widget in frame.winfo_children():
            widget.grid_configure(pady=10,padx=2)
            for widgets in widget.winfo_children():
                widgets.grid_configure(pady=10,padx=12,sticky=N)
    
class imageDetails: 
    img = []
    imageSize=(0,0)
    imagePath=''
    red,green,blue= [0],[0],[0]

    Savedimg = []
    SavedimageSize=(0,0)
    SavedimagePath=''
    Sred,Sgreen,Sblue =[0],[0],[0]

    def __init__(self) -> None:
        pass
    
    def setImageDetails(self,img = [],imageSize = (0,0),imagePath = '',colorsplit=[red,green,blue]):
        self.img = img
        self.imageSize = imageSize
        self.imagePath = imagePath
        self.red,self.green,self.blue = colorsplit[0],colorsplit[1],colorsplit[2]
    
    def SaveImage(self):
        self.Savedimg = self.img
        self.SavedimageSize= self.imageSize
        self.SavedimagePath= self.imagePath
        self.Sred,self.Sgreen,self.Sblue = self.red,self.green,self.blue
    
    def UndoImage(self):
        self.img = self.Savedimg
        self.imageSize= self.SavedimageSize
        self.imagePath= self.SavedimagePath
        self.red,self.green,self.blue = self.Sred,self.Sgreen,self.Sblue
        
class subSystemWork:

    def displayPLOTLin(self,inputSeqField):
        self.Top = Toplevel()
        x = []
        h = []
        for widget in inputSeqField.winfo_children():
            if isinstance(widget, Entry) and len(x) !=4:
                ix = int(widget.get())
                x.append(ix)
            elif isinstance(widget, Entry) and len(x) >=4:
                ih = int(widget.get())
                h.append(ih)
        
        n1=len(x)
        n2=len(h)
        n=n1+n2-1
        
        f= Figure(figsize=(10,5))
        canvas = FigureCanvasTkAgg(f,master=self.Top)
        a = f.add_subplot(311)
        a.plot(x)
        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.title("Graph for x[n]")

        a = f.add_subplot(312)
        a.plot(h)
        plt.xlabel('n')
        plt.ylabel('h[n]')
        plt.title("Graph for h[n]")
        for i in range(n-n2):
            x.append(0)
            h.append(0)
        
        y=np.zeros(n)
        print(x,h)
        
        for i in range (n):
            for k in range(max(0, i-n2+1), min(i+1,n1)):
                y[i]+= x[k]*h[i-k]

        a = f.add_subplot(313)
       
        plt.xlabel('n')
        plt.ylabel('y[n]')
        plt.title("Graph for y[n]")
        a.plot(y)

        canvas.draw()
        canvas.get_tk_widget().pack(side= TOP, fill=BOTH,expand=True)

        ssw.desplMessage(f"linear convolution :\nSequence 1 : {x}\nSequence 2 : {h}\nn : {n}\ny = {y}")
        for widget in inputSeqField.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(widget.index(END)-1)

    def displayPLOTCir(self,inputSeqFieldC):
        self.Top = Toplevel()
        x = []
        h = []
        for widget in inputSeqFieldC.winfo_children():
            if isinstance(widget, Entry) and len(x) !=4:
                ix = int(widget.get())
                x.append(ix)
            elif isinstance(widget, Entry) and len(x) >=4:
                ih = int(widget.get())
                h.append(ih)
        
        n1=len(x)
        n2=len(h)
        n=n1+n2-1
        
        f= Figure(figsize=(10,5))
        canvas = FigureCanvasTkAgg(f,master=self.Top)
        a = f.add_subplot(311)
        a.plot(x)
        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.title("Graph for x[n]")

        a = f.add_subplot(312)
        a.plot(h)
        plt.xlabel('n')
        plt.ylabel('h[n]')
        plt.title("Graph for h[n]")
        
        y=np.zeros(n1)
        print(x,h)
        
        for i in range (n1):
            for k in range(n2):
                y[i]+= x[(i-k)%n1]*h[k]

        a = f.add_subplot(313)
       
        plt.xlabel('n')
        plt.ylabel('y[n]')
        plt.title("Graph for y[n]")
        a.plot(y)

        canvas.draw()
        canvas.get_tk_widget().pack(side= TOP, fill=BOTH,expand=True)

        ssw.desplMessage(f"Circular convolution :\nSequence 1 : {x}\nSequence 2 : {h}\nn : {n1}\ny = {y}")
        for widget in inputSeqFieldC.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(widget.index(END)-1)

#image Transformation
    def Get_DataForHaarT(self):
        self.desplMessage('Haar transformation in Process..')
        def haar_transform(image, kernel_size):
                
                """Perform Haar transformation on input image using given kernel size"""
                # Create Haar kernel
                kernel = np.ones((kernel_size, kernel_size)) / kernel_size
                
                # Initialize transformed image
                transformed = np.zeros_like(image)
                
                # Loop over image blocks and apply Haar transformation
                for i in range(0, image.shape[0], kernel_size):
                    for j in range(0, image.shape[1], kernel_size):
                        block = image[i:i+kernel_size, j:j+kernel_size]
                        block_transformed = np.zeros_like(block)
                        
                        # Apply row-wise Haar transformation
                        for k in range(kernel_size):
                            even = (block[k, 0::2] + block[k, 1::2]) / np.sqrt(2)
                            odd = (block[k, 0::2] - block[k, 1::2]) / np.sqrt(2)
                            block_transformed[k, 0::2] = even
                            block_transformed[k, 1::2] = odd
                        
                        # Apply column-wise Haar transformation
                        for l in range(kernel_size):
                            even = (block_transformed[0::2, l] + block_transformed[1::2, l]) / np.sqrt(2)
                            odd = (block_transformed[0::2, l] - block_transformed[1::2, l]) / np.sqrt(2)
                            block_transformed[0::2, l] = even
                            block_transformed[1::2, l] = odd
                        
                        # Save transformed block to transformed image
                        transformed[i:i+kernel_size, j:j+kernel_size] = block_transformed
                
                return transformed
        
        if IDs.imagePath != '':
            
            img= IDs.img
            img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
            
            # Define the size of the Haar transformation kernel
            kernel_size = int(sofSetup.HaarKernelEnrty.get())

            # Perform the Haar transformation on the input image with the specified kernel size
            haar = haar_transform(img, kernel_size)
            
            # Convert result to image and return
            
            IDs.img=haar
            self.DispalyImg()
            self.desplMessage(f'Haar transformation performed\nkernal size : {kernel_size}x{kernel_size}')
        else:
            self.desplMessage('Image not avalable')

#binary image 
    def Get_DataFordilate(self):
        kernel_size=int(sofSetup.KernelSizeForDil.get())
        img =IDs.img
        # Define kernel
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        # Dilate image
        dilation = cv.dilate(img, kernel, iterations=1)
        IDs.img=dilation
        self.DispalyImg()

    
    def Get_DataForerode(self):
        kernel_size=int(sofSetup.KernelSizeForErosion.get())
        img =IDs.img
        # Define kernel
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        # Erode image
        erosion = cv.erode(img, kernel, iterations=1)
        IDs.img=erosion
        self.DispalyImg()
#image Enhancement
    def Get_DataForLPF(self):
            
            kernal_unit=sofSetup.kernal_SpinboxLPF.get()
            filterTypeLPF=sofSetup.Filter_ComboBoxLPF.get()
            kn = int(kernal_unit)
            flt = filterTypeLPF
            self.desplMessage(f'Kwenal Unit : {kn}x{kn}\nFilter : {flt}')
            if IDs.imagePath != '':
                self.desplMessage('working')
                kernel = np.ones((kn,kn),np.float32)/kn*kn
                if flt == 'Boxfilter':
                    img = cv.boxFilter(IDs.img,-1,(kn,kn))
                    IDs.img = img
                    self.DispalyImg()
                if flt == 'convoluted':
                    img = cv.filter2D(IDs.img,-1,kernel)
                    IDs.img = img
                    self.DispalyImg()
                    pass
                if flt == 'Blur':
                    if kn%2 == 0:
                        kn -=1
                        print(kn)
                    img = cv.blur(IDs.img,(kn,kn))
                    IDs.img = img
                    self.DispalyImg()
                    pass
                if flt == 'GaussianBlur':
                    if kn%2 == 0:
                        kn -=1
                        print(kn)
                    img = cv.GaussianBlur(IDs.img,(kn,kn),0)
                    IDs.img = img
                    self.DispalyImg()
                    pass
            else:
                self.desplMessage('Image not avalable')

    def Get_DataForHPF(self):
        kernal_size=sofSetup.kernal_SpinboxHPF.get()
        kernal_size = int(kernal_size)
        filterTypeHPF=sofSetup.Filter_ComboBoxHPF.get()
        
        img = IDs.img
        if IDs.imagePath != '':
            self.desplMessage('working')
            if filterTypeHPF == 'Laplacian':
                if kernal_size%2 == 0:
                    kernal_size -=1
                    print(kernal_size)
                img = cv.Laplacian(img,-1,ksize=kernal_size,scale=1,delta=0,borderType=cv.BORDER_DEFAULT)
                IDs.img = img
                self.DispalyImg()
            if filterTypeHPF == 'Sobel':
                print(kernal_size%2,kernal_size)
                if kernal_size%2 == 0:
                    kernal_size -=1
                    print(kernal_size)
                imgx = cv.Sobel(img,-1,dx=1,dy=0,ksize=kernal_size,scale=1,delta=0,borderType=cv.BORDER_DEFAULT)
                imgy = cv.Sobel(img,-1,dx=0,dy=1,ksize=kernal_size,scale=1,delta=0,borderType=cv.BORDER_DEFAULT)
                IDs.img = imgx+imgy
                self.DispalyImg()
                # imgy = cv.Sobel(img,-1,dx=1,dy=0,ksize=kernal_size,scale=1,delta=0,borderType=cv.BORDER_DEFAULT)
            if filterTypeHPF == 'Scharr':
                imgx = cv.Scharr(img,-1,dx=1,dy=0,scale=1,delta=0,borderType=cv.BORDER_DEFAULT)
                imgy = cv.Scharr(img,-1,dx=0,dy=1,scale=1,delta=0,borderType=cv.BORDER_DEFAULT)
                IDs.img = imgx+imgy
                self.DispalyImg()
        else:
            self.desplMessage('Image not avalable')

#colour model
    def Get_DataForCC(self):
        FC = sofSetup.Filter_ComboBoxCC.get()
        img = IDs.img
        if IDs.imagePath != '':
            
            if FC == 'GRAY':
                img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
                IDs.img = img
                self.DispalyImg()
            if FC == 'HSV':
                img = cv.cvtColor(img,cv.COLOR_RGB2HSV)
                IDs.img = img
                self.DispalyImg()
            if FC == 'BGR':
                img = cv.cvtColor(img,cv.COLOR_RGB2BGR)
                IDs.img = img
                self.DispalyImg()
            if FC == 'HLS':
                img = cv.cvtColor(img,cv.COLOR_RGB2HLS)
                IDs.img = img
                self.DispalyImg()
    
    def Get_DataForCSegR(self):
        #process the image
        red=IDs.red
        IDs.img=red
        self.DispalyImg()

    def Get_DataForCSegr(self):
        #process the image
        red=IDs.red
        row,col=IDs.imageSize
        print(row,col)
        plane=np.zeros((row,col))
        def cat(red, green, blue):
            return np.stack([red, green, blue], axis=2)
        
        Red = np.uint8(cat(red,plane,plane))
        IDs.img=Red
        self.DispalyImg()

    def Get_DataForCSegG(self):
        #process the image
        green=IDs.green
        IDs.img=green
        self.DispalyImg()

    def Get_DataForCSegg(self):
        #process the image
        green=IDs.green
        row,col=IDs.imageSize
        print(row,col)
        plane=np.zeros((row,col))
        def cat(red, green, blue):
            return np.stack([red, green, blue], axis=2)
        green = np.uint8(cat(plane,green,plane))
        IDs.img=green
        self.DispalyImg()

    def Get_DataForCSegB(self):
        #process the image
        blue=IDs.blue
        IDs.img=blue
        self.DispalyImg()

    def Get_DataForCSegb(self):
        #process the image
        blue=IDs.blue
        row,col=IDs.imageSize
        print(row,col)
        plane=np.zeros((row,col))
        def cat(red, green, blue):
            return np.stack([red, green, blue], axis=2)
        blue = np.uint8(cat(plane,plane,blue))
        IDs.img=blue
        self.DispalyImg()

#pre-process            
    def Get_DataForQuantization(self):
        bitvalue= int(sofSetup.QuantBits_SpinboxLPF.get())
        image=IDs.img
        num_colors = 2 ** (3 * bitvalue)
        f=np.floor(image/(256/(2*bitvalue)))
        quantized=(f*225)/np.max(f)
        quantized = np.uint8(quantized)
        IDs.img =  quantized
        self.DispalyImg()
        self.desplMessage(message=f'Quantization done\nwith bits/pixel value : {bitvalue}\nCalculated number of colors : {num_colors} i.e [ (3 * number of bits)^2 ]')

#system
    def DispalyImg(self):
        h,w = FD.f1_H,FD.f1_W
        print("FD : ",h,w)
        x,size,path = IDs.img,IDs.imageSize,IDs.imagePath
        self.img = Image.fromarray(x)
        self.newimg = self.img.resize((int(w),int(h)),Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.newimg)
        sw.imgLabel.config(image=self.img)
        self.desplMessage(message=f'Image path : {path}\nImage size :{size}')

    def desplMessage(self,message):
        sw.text0.delete(1.0,END)
        sw.text0.insert(1.0,message)

class systemWork:
    def __init__(self) -> None:
        pass

    def DisplayScreen(self,frame):
        h=frame.winfo_height()
        w=frame.winfo_width()
        h,w=int(h-15),int(w-30)
        print(h,w)
        FD.update(h,w)

        self.disCanvas = Canvas(frame,bg='Blue',width=w,height=h)
        self.disCanvas.grid(column=0,row=0)
        
        pImage = cv.imread(filename="demoImg/Demo.jpg")
        pImage = Image.fromarray(pImage)
        self.newimgRz = pImage.resize((w,h),Image.Resampling.LANCZOS)
        print("Df : ",h,w)
        photo_image = ImageTk.PhotoImage(self.newimgRz)
        self.imgLabel = Label(self.disCanvas,image=photo_image)
        self.imgLabel.grid(column=0,row=0)

    def deployImpButtons(self,frame):
        def uploadImage():
            path= filedialog.askopenfilename(title="Select an Image", filetype=(('image    files','*.jpg'),('all files','*.*')))
            img = cv.imread(path)
            h,w=img.shape[0],img.shape[1]
            blue,green,red = cv.split(img)
            img = cv.merge((red,green,blue))
            IDs.setImageDetails(img,(h,w),path,[red,green,blue])
            ssw.DispalyImg()
           
        def saveImage():
            IDs.SaveImage()
            ssw.desplMessage(message=f'Image Saved')
           
        def UndoImage():
            if IDs.img != []:
                IDs.UndoImage()
                ssw.desplMessage(message=f'Retreved last Image')
                ssw.DispalyImg()
            else:
                ssw.desplMessage(message=f'no saved image')
        
        upload = Button(frame,text='Upload',width=20,height=3,command=uploadImage)
        Save = Button(frame,text='Save',width=20,height=3,command=saveImage)
        Reter = Button(frame,text='Retreve',width=20,height=3,command=UndoImage)

        upload.grid(row=0,column=0,padx=1,pady=1,sticky=W)
        Save.grid(row=0,column=1,padx=1,pady=1,sticky=NSEW)
        Reter.grid(row=0,column=2,padx=1,pady=1,sticky=E)
    
    def desplMessFrame(self,frame):
        h=frame.winfo_height()
        w=frame.winfo_width()
        h,w=int(h*0.055),int(w*0.1225)
        print(h,w)

        self.myLabelMes = Label(frame,bg='blue')
        self.myLabelMes.grid(row=0,column=0)
        self.text0 = Text(self.myLabelMes,width=w,height=h,wrap=NONE)
        self.text0.grid(row=0,column=0)

        self.myScrollbary = Scrollbar(self.myLabelMes,command=self.text0.yview)
        self.myScrollbary.grid(row=0,column=1,sticky=NS)

        self.myScrollbarx = Scrollbar(self.myLabelMes,command=self.text0.xview,orient='horizontal')
        self.myScrollbarx.grid(row=1,column=0,columnspan=2,sticky=EW)

        self.text0.config(yscrollcommand=self.myScrollbary.set,xscrollcommand=self.myScrollbarx.set)
        ssw.desplMessage('First Upload Image')

FD = FrameDAta()
IDs = imageDetails()
ssw = subSystemWork()
sofSetup = sysOptionFrameSetup()
sw = systemWork()
main = Main()