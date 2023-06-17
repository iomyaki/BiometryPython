from reader import Reader
from counter import Counter
from saver import Saver
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class Run(object):
    def __init__(self, inputFilePath, outputDirPath, sep):
        self.reader = Reader(path=inputFilePath, sep=sep)
        self.name = self.reader.getName()
        self.reader.read()

        if self.reader.error != None:
            raise self.reader.error

        self.counter = Counter(self.reader.DataFrame)

        self.saver = Saver(path=outputDirPath, sep=";", format=self.reader.format)
        self.saver.parseFileName(name=self.name)
        self.saver.makeDir(self.saver.dir)

    def getAllResults(self):
        self.counter.getStatisticsFrom1To11()
        self.counter.getStatisticsFrom12To18()
        self.counter.getStatisticsFrom19To20()
        self.counter.getStatisticsFrom22()
        self.counter.getStatisticsFrom23To26()
        self.counter.getStatisticsFrom27To28()
        self.counter.getStatisticsFrom29To31()
        self.counter.getStatisticsFrom32To33()
        self.counter.getStatisticsFrom34To36()
        self.counter.formatToFinalLine(name=self.name)

    def saveFiles(self):
        self.saver.save(dataframe=self.counter.from1To11DF, numbers="_1_to_11", name=self.name)
        self.saver.save(dataframe=self.counter.from12To18DF, numbers="_12_to_18", name=self.name)
        self.saver.save(dataframe=self.counter.from19To20DF, numbers="_19_to_20", name=self.name)
        self.saver.save(dataframe=self.counter.spearman, numbers="_22", name=self.name)
        self.saver.save(dataframe=self.counter.from23To26DF, numbers="_23_to_26", name=self.name)
        self.saver.save(dataframe=self.counter.from27To28DF, numbers="_27_to_28", name=self.name)
        self.saver.save(dataframe=self.counter.from29To31DF, numbers="_29_to_31", name=self.name)
        self.saver.save(dataframe=self.counter.from32To33DF, numbers="_32_to_33", name=self.name)
        self.saver.save(dataframe=self.counter.from34To36DF, numbers="_34_to_36", name=self.name)
        self.saver.save(dataframe=self.counter.finalLine, numbers="_FINAL", name=self.name)


# функция для считывания исходного файла
def open_file():
    return filedialog.askopenfilename()

# функция для выбора места сохранения файла с ответом
def save_file():
    return filedialog.askdirectory()

# функция для вызова скрипта
def run_script():
    inputFilePath = open_file()
    outputDirPath = save_file()

    run = Run(inputFilePath=inputFilePath, outputDirPath=outputDirPath, sep=";")
    run.getAllResults()

    run.saveFiles()
    return

if __name__ == "__main__":
    root = tk.Tk()

    label_style = ttk.Style(root)
    label_style.configure(
        ".",          
        font="helvetica 14",   
        foreground="#004D40",   
        padding=10,            
        background="#B2DFDB",
    )

    # кнопки для запуска программы и выбора файлов
    run_button = tk.Button(root, text="Run Script", command=run_script)

    # размещение кнопок на экране
    run_button.pack(side=tk.LEFT)

    root.mainloop()
