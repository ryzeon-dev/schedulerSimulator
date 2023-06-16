import customtkinter as ctk

class Interface:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Scheduler Simulator')
        self.mainFrame = ctk.CTkFrame(self.root)

        self.maxIndex = 20
        self.make()

        self.mainFrame.pack(padx=10, pady=10, expand=True, fill='both')#grid(column=0, row=0)
        self.root.mainloop()

    def make(self):
        self.gridFrame = ctk.CTkFrame(self.mainFrame)
        self.gridFrame.grid(column=0, row=0, columnspan=3, padx=5, pady=5)

        for i in range(26):
            ctk.CTkLabel(self.gridFrame, text=str(i)).grid(row=5, column=i+1, padx=5)

        ctk.CTkLabel(self.gridFrame, text='P1').grid(row=1, column=0)
        ctk.CTkLabel(self.gridFrame, text='P2').grid(row=2, column=0)
        ctk.CTkLabel(self.gridFrame, text='P3').grid(row=3, column=0)
        ctk.CTkLabel(self.gridFrame, text='P4').grid(row=4, column=0)

        self.processSelect = ctk.CTkOptionMenu(self.mainFrame, values=['P1', 'P2', 'P3', 'P4'])
        self.processSelect.grid(column=0, row=2, padx=5, pady=5, columnspan=2)

        self.labelText = ctk.CTkEntry(self.mainFrame, placeholder_text='Label')
        self.labelText.grid(column=1, row=2, columnspan=2, padx=1, pady=5)

        self.startIndex = ctk.CTkEntry(self.mainFrame, placeholder_text='Start index')
        self.startIndex.grid(row=3, column=0, padx=5, pady=5)

        self.duration = ctk.CTkEntry(self.mainFrame, placeholder_text='Duration')
        self.duration.grid(row=3, column=1, padx=5, pady=5)

        self.addButton = ctk.CTkButton(self.mainFrame, text='Add', command=self.add)
        self.addButton.grid(row=3, column=2, padx=5, pady=5)

    def add(self):
        index = int(self.startIndex.get())
        duration = int(self.duration.get())

        newBlock = ctk.CTkButton(self.gridFrame, text=self.labelText.get(), command=lambda : [newBlock.destroy()], width=15*duration)
        newBlock.grid(row=int(self.processSelect.get().replace('P', '')), column=index+1, columnspan=duration, padx=5, pady=5)

        if index + duration > self.maxIndex:
            for i in range(self.maxIndex, index + duration + 1):
                ctk.CTkLabel(self.gridFrame, text=str(i)).grid(row=5, column=i+1, padx=5)
            self.maxIndex = index + duration

Interface()