import PySimpleGUI as sg

class dashboard():
    def __init__(self, labels):
        self.labels=labels
        layout=[]
        for label in labels:
            layout.append([sg.Text(label+":"), sg.Text(0,key=label.lower())])
        self.window=sg.Window(title="Output", layout=layout, margins=(30,30),size=(300, 500))
    def read(self, dtheta):
        event, values= self.window.read(timeout=dtheta*1000)
        if event == sg.WIN_CLOSED:
            return False
    def update(self,dict):
        for x in dict:
            self.window[x.lower()].update(round(dict[x]))
