import matplotlib.pyplot as plt
import tkinter as tk
import random



class gui:
    def __init__(self):
        self.occurences=0
        self.events=0
        self.probablity=0
        
        root = tk.Tk()
        root.geometry("175x250")
        root.title("GUI")
        
        events_text_lable = tk.Label(root, text="events")
        events_text = tk.Entry(root)
        events_text_lable.place(x=30,y=10)
        events_text.place(x=30,y=30)

        occurences_lable = tk.Label(root, text="occurences")
        occurences_text = tk.Entry()
        occurences_lable.place(x=30,y=10+40)
        occurences_text.place(x=30,y=30+40)

        sample_size_lable=tk.Label(root, text="Sample Size")
        sample_size_text = tk.Entry()
        sample_size_lable.place(x=30,y=10+40+40)
        sample_size_text.place(x=30,y=30+40+40)

        no_of_experiments_lable=tk.Label(root, text="Number of experiments ")
        no_of_experiments_text = tk.Entry()
        no_of_experiments_lable.place(x=30,y=10+40+40+40)
        no_of_experiments_text.place(x=30,y=30+40+40+40)
                
        bar_plotter = tk.Button(root, text="Bar Graph", command=self.plot_bar)
        bar_plotter.place(x=30,y=30+40+40+40+30)

        self.root=root
        self.events_text=events_text
        self.occurences_text=occurences_text
        self.sample_size_text=sample_size_text
        self.no_of_experiments_text=no_of_experiments_text
        self.root.mainloop()   

    def plot_bar(self):
        plt.ion()
        
        events=self.events_text.get()
        occurneces=self.occurences_text.get()
        events=[float(i) for i in events.split(',')]
        occurneces=[float(i) for i in occurneces.split(',')]
        for i in range(len(occurneces)):
            for x in range(i,len(occurneces)):
                if(occurneces[i]<occurneces[x]):
                    occurneces[i],occurneces[x]=occurneces[x],occurneces[i]
                    events[i],events[x]=events[x],events[i]           
        self.events=events
        self.occurences=occurneces
        plt.bar(self.events,self.occurences)
        plt.show()
        self.get_probablities()
        self.plot_sample()
    
    def get_probablities(self):
        total_experiments=0
        for i in self.occurences:
            total_experiments=total_experiments+i
        self.probablity=[round(i/total_experiments,3) for i in self.occurences]
        
    def plot_sample(self):
        thousand_exp_results=[i*1000 for i in self.probablity]
        sample_size=int(self.sample_size_text.get())
        experiment_size=int(self. no_of_experiments_text.get())
        new_plot=plt.figure(2)
        sample_mean_occurence={}
        for i in range(experiment_size):
            sample_mean=0
            for x in range(sample_size):
                r=random.randint(0,1000)
                temp=0
                for l in range(len(self.events)):
                    temp=temp+thousand_exp_results[l]
                    if(r<=temp):
                        sample_mean=sample_mean+self.events[l]
                        break
            sample_mean=sample_mean/sample_size
            sample_mean_occurence[sample_mean]=sample_mean_occurence.get(sample_mean,0)+1
        plt.cla()
        #plt.xlim(self.events[0]-1,self.events[-1]+1)
        plt.bar(sample_mean_occurence.keys(),sample_mean_occurence.values(),width=1/sample_size)         
        
        new_plot.show()                 
                
        

k=gui()