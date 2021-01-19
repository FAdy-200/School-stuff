import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


class DataExtractorAndPlotter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = None
        self.rawData = None
        self.headers = ["Time", "yoc_temp", 'yoc_SP', 'yoc_p1', 'yoc_p2', 'yoc_p3', 'yoc_p4', 'yoc_p5', 'yoc_bl1',
                        'yoc_bl2',
                        'yoc_lights', 'yoc_stereo', 'yoc_h1', 'yoc_h2', 'yoc_filter', 'yoc_bl3', 'yoc_bl4', 'yoc_bl5',
                        'yoc_bl6',
                        'yoc_h_adc', 'yoc_bl7', 'yoc_econ', 'yoc_i_adc', 'yoc_all_on', 'yoc_bl8', 'yoc_bl9', 'yoc_bl10']
        self.data = {'Time': [], 'yoc_temp': [], 'yoc_SP': [], 'yoc_p1': [], 'yoc_p2': [], 'yoc_p3': [],
                     'yoc_p4': [], 'yoc_p5': [], 'yoc_bl1': [], 'yoc_bl2': [], 'yoc_lights': [],
                     'yoc_stereo': [], 'yoc_h1': [], 'yoc_h2': [], 'yoc_filter': [], 'yoc_bl3': [],
                     'yoc_bl4': [], 'yoc_bl5': [], 'yoc_bl6': [], 'yoc_h_adc': [], 'yoc_bl7': [],
                     'yoc_econ': [], 'yoc_i_adc': [], 'yoc_all_on': [], 'yoc_bl8': [], 'yoc_bl9': [],
                     'yoc_bl10': []}

    def __readFile(self):
        """
        reads the file and adds the raw data to self.rawData
        :return:
        """
        with open(self.file_name, "r") as g:
            self.rawData = g.readlines()

    def __decoder(self, line):
        """
        takes a line as a list and appends each item to its right list in the data dictionary
        :param line: list
        :return:
        """
        for i in range(27):
            header = self.headers[i]
            data = line[i]
            self.data[header].append(data)

    def __addDataToDict(self):
        """
        take the raw data from the file and adds the data into a dictionary
        :return:
        """
        for line in self.rawData:
            # splitting each line by ',' without keeping the last entry which is a new line character
            lineList = line.split(",")[:-1]
            # combining the date and time entries to be one e.g.  09/29/2020:17:56:53
            time = [lineList[0]] + [":"] + [lineList[1][1:9]]
            # adding the new time entry and removing the non needed entries
            lineList = ["".join(time)] + lineList[2:]
            self.__decoder(lineList)

    def __makeDataFrame(self):
        """
        makes a pandas DataFrame object from the data dictionary
        :return:
        """
        self.df = pd.DataFrame(self.data)

    def __convertToDec(self):
        """
        converts the values in each column from str type in hexa to int in decimal
        :return:
        """
        for i in self.df.columns:
            self.df[i] = self.df.apply(lambda x: int(x[i], 16), axis=1)

    def __convertTimeToTimeFormat(self):
        """
        converts time column from str to pandas dateTime format
        :return:
        """
        temp = pd.to_datetime(self.df["Time"], format='%m/%d/%Y:%H:%M:%S')
        self.df["Time"] = temp

    def __dataCleaning(self):
        """
        cleans the dataFrame
        :return:
        """
        self.__convertTimeToTimeFormat()
        self.df.set_index("Time", inplace=True)
        self.__convertToDec()

    def __firstSubplot(self, plot, date_format):
        """
        plotting the first subplot
        :param plot:
        :param date_format:
        :return:
        """
        ax1 = plot.twinx()  # creating the second y-axis
        ax1.plot(self.df.index, self.df["yoc_temp"], label="yoc_temp")
        ax1.plot(self.df.index, self.df["yoc_SP"], label="yoc_SP")
        ax1.plot(self.df.index, self.df["yoc_h_adc"], label="yoc_h_adc")
        ax1.plot(self.df.index, self.df["yoc_h2"], label="yoc_h2", color="brown")
        plot.plot(self.df.index, self.df["yoc_h1"], "--", label="yoc_h1", color="purple")
        ax1.legend(loc="center left")
        plot.legend(loc="lower right")
        plot.xaxis.set_major_formatter(date_format)  # changing the displayed x-axis labels to a better format

    def __secondSubplot(self, plot, date_format):
        """
        plotting the second subplot
        :param plot:
        :param date_format:
        :return:
        """
        for i in range(1, 6):
            plot.plot(self.df.index, self.df[f"yoc_p{i}"], label=f"yoc_p{i}")
        ax1 = plot.twinx()  # creating the second y-axis
        ax1.plot(self.df.index, self.df["yoc_i_adc"], "--", label="yoc_i_adc", color="brown")
        ax1.legend(loc="upper right")
        plot.legend(loc="upper left")
        plot.xaxis.set_major_formatter(date_format)  # changing the displayed x-axis labels to a better format

    def __thirdSubplot(self, plot, date_format):
        """
        plotting the third subplot
        :param plot:
        :param date_format:
        :return:
        """
        plot.plot(self.df.index, self.df["yoc_h1"], label="yoc_h1")
        plot.plot(self.df.index, self.df["yoc_h2"], label="yoc_h2")
        ax1 = plot.twinx()  # creating the second y-axis
        ax1.plot(self.df.index, self.df["yoc_i_adc"], "--", label="yoc_i_adc", color="brown")
        ax1.legend(loc="upper right")
        plot.legend(loc="upper left")
        plot.xaxis.set_major_formatter(date_format)  # changing the displayed x-axis labels to a better format

    def plot(self):
        """
        calling teh plots functions in the right order
        :return:
        """
        figure, plots = plt.subplots(3)  # creating the plotting template
        date_format = DateFormatter("%d:%H:%M:%S")  # setting the date format that will be displayed
        self.__firstSubplot(plots[0], date_format)
        self.__secondSubplot(plots[1], date_format)
        self.__thirdSubplot(plots[2], date_format)
        plt.show()

    def Decode(self):
        """
        decoding the raw sensor data
        :return:
        """
        self.__readFile()
        self.__addDataToDict()
        self.__makeDataFrame()
        self.__dataCleaning()

    def convertToCSV(self, fileName):
        """
        converts the dataframe to csv
        :param fileName: name of the files to be saved
        :return:
        """
        self.df.to_csv(f"{fileName}.csv", index=True)

#### TEST CASE ###
ex = DataExtractorAndPlotter("outputfile.txt")
ex.Decode()
# ex.plot()
ex.convertToCSV("Sensors data")
