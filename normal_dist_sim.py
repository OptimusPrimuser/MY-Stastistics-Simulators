
import  tkinter as tk
import matplotlib.pyplot as plt
import math

plt.ion()
class normal_dist:
    def __init__(self):
        root = tk.Tk()
        root.geometry("175x100")
        root.title("GUI")
        
        mean_text_lable = tk.Label(root, text="mean")
        mean_text = tk.Entry(root)
        mean_text_lable.place(x=30,y=10)
        mean_text.place(x=30,y=30,width=50)

        standard_deviation_lable = tk.Label(root, text="SD")
        standard_deviation_text = tk.Entry()
        standard_deviation_lable.place(x=30+60,y=10)
        standard_deviation_text.place(x=30+60,y=30,width=50 )

        plotter = tk.Button(root, text="normal distribution plot", command=self.plot_normal)
        plotter.place(x=20,y=60)

        self.root=root
        self.mean_text=mean_text
        self.standard_deviation_text=standard_deviation_text
        self.root.mainloop()

        

    def plot_normal(self):
            mean=float(self.mean_text.get())
            standard_deviation=float(self.standard_deviation_text.get())
            x = mean - (3*standard_deviation)
            y_list = []
            x_list = [i for i in range(int( mean - (3*standard_deviation)), int(mean + (3*standard_deviation)) ) ]
            plt.xlim(int( mean - (4*standard_deviation)), int(mean + (4*standard_deviation)) )
            plt.ylim(0,(math.e ** (0) * (1 / standard_deviation * (2 * math.pi) ** 0.5)))
            while x < mean + (3*standard_deviation):
                z = (x - mean) / standard_deviation
                y = (math.e ** (-(z ** 2) / 2)) * (1 / standard_deviation * (2 * math.pi) ** 0.5)
                y_list.append(y)
                x = x + 1
            plt.fill_between(x_list, y_list,where=y>=0)
            plt.show()         
    
k = normal_dist()
# normal_dist(0,10000)
