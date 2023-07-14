import csv
import sys

class ConvertCSV:
    def __init__(self,fileName):
        self.fileName = fileName

    def fileOpen(self):
        """
        引数に指定されているファイルを読み込み
        """
        try:
            with open(self.fileName, 'r') as file:
                reader = csv.reader(file)
                self.readerData = list(reader)  # CSVファイル全体を変数に格納
        except Exception as e:
            print("ファイルを開く際にエラーが発生しました。")
            print("実行時引数にcsvファイルを指定しているか確認してください。")
            sys.exit()
        
        csv_count = 0
        for row in self.readerData:
            csv_count += 1
            if csv_count == 1001:
                print("csvファイルが1000行を超えています。")
                sys.exit()
    
    def convert(self):
        """
        変換を行う
        """
        for row in self.readerData:
            print(row)





def main():
    args = sys.argv
    execution = ConvertCSV(args[1])
    execution.fileOpen()
    execution.convert()




if __name__ == '__main__':
    main()
