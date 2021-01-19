import pandas as pd
import matplotlib.pyplot as plt


class Decoder:
    def __init__(self):
        self.finaldata = []
        self.data = None

    def readfile(self):
        with open("outputfile.txt", 'r') as file:
            data = file.readlines()
        for i in data:
            self.finaldata.append(i.split(",")[2:-1])
        self.data = pd.DataFrame(self.finaldata)

    def datacleaning(self):
        col = ["yoc_temp", 'yoc_SP', 'yoc_p1', 'yoc_p2', 'yoc_p3', 'yoc_p4', 'yoc_p5', 'yoc_bl1', 'yoc_bl2',
               'yoc_lights', 'yoc_stereo', 'yoc_h1', 'yoc_h2', 'yoc_filter', 'yoc_bl3', 'yoc_bl4', 'yoc_bl5', 'yoc_bl6',
               'yoc_h_adc', 'yoc_bl7', 'yoc_econ', 'yoc_i_adc', 'yoc_all_on', 'yoc_bl8', 'yoc_bl9', 'yoc_bl10']
        self.data.columns = col

    def decode(self):
        for i in self.data.columns:
            self.data[i] = self.data.apply(lambda x: int(x[i], 16), axis=1)

    def plot(self):
        fig, pl = plt.subplots(3)
        p0ax1 = pl[0].twinx()
        p0ax1.plot(self.data.index, self.data["yoc_temp"], label="yoc_temp")
        p0ax1.plot(self.data.index, self.data["yoc_SP"], label="yoc_SP")
        p0ax1.plot(self.data.index, self.data["yoc_h_adc"], label="yoc_h_adc")
        p0ax1.plot(self.data.index, self.data["yoc_h2"], label="yoc_h2", color="brown")
        pl[0].plot(self.data.index, self.data["yoc_h1"], label="yoc_h1", color="purple")
        for i in range(1, 6):
            pl[1].plot(self.data.index, self.data["yoc_p{}".format(i)], label="yoc_p{}".format(i))
        p1ax1 = pl[1].twinx()
        p1ax1.plot(self.data.index, self.data["yoc_i_adc"], label="yoc_i_adc", color="brown")
        pl[2].plot(self.data.index, self.data["yoc_h1"], label="yoc_h1")
        pl[2].plot(self.data.index, self.data["yoc_h2"], label="yoc_h2")
        pl[2].plot(self.data.index, self.data["yoc_filter"], label="yoc_filter")
        p2ax1 = pl[2].twinx()
        p2ax1.plot(self.data.index, self.data["yoc_i_adc"], label="yoc_i_adc", color="brown")
        p2ax1.legend()
        pl[2].legend()
        p1ax1.legend()
        pl[1].legend()
        p0ax1.legend(loc="upper left")
        pl[0].legend(loc="upper right")
        plt.show()

    def makeCSVfile(self):
        self.data.to_csv("sensors.csv", index=True)

z = Decoder()
z.readfile()
z.datacleaning()
z.decode()
z.makeCSVfile()
z.plot()
