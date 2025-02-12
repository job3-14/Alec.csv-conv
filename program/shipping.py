"""
ヤマト運輸CSVを補完するプログラム

orders.csvに情報を補完し、csvを更新後、元ファイルを削除
"""

import csv
#import configparser
import os, sys


def search_tracking_id(data, key):
    """
    data : 2次元リスト（例：[[key1, ..., value1, ...], [key2, ..., value2, ...], ...]）
    key  : 各行の0番目の要素と比較する値
    
    各行の0番目の要素が key と一致した場合、その行の3番目の要素を返す。
    見つからなかった場合は None を返す。
    """
    for row in data:
        # 行が十分な要素数を持っているかチェック
        if len(row) > 3 and row[0] == key:
            row_id = str(row[3])
            formatted_id = 'ヤマト運輸: '+row_id[:4] + '-' + row_id[4:8] + '-' + row_id[8:]
            return formatted_id
    print("発送IDが見つかりません. ヤマト運輸側の出力年月日が正しいか確認してください.")
    return None


# config.ini読み込み
#config_ini = configparser.ConfigParser()
#config_ini.read('config.ini', encoding='utf-8')
def main():
    # メルカリCSV(B2仕様)読み込み
    try:
        with open('~/Desktop/orders.csv') as f:
            reader = csv.reader(f)
            csv_data_mercari = [row for row in reader]
    except Exception as e:
        print("エラー：メルカリCSV ファイルを開くことができません.")
        sys.exit()

    # ヤマトCSV読み込み
    print("ヤマト運輸 発行済データ(csv)をドラッグ&ドロップしてください.")
    yamato_data_path = input()
    try:
        with open(yamato_data_path) as f:
            reader = csv.reader(f)
            csv_data_yamato = [row for row in reader]
    except Exception as e:
        print("エラー：ヤマト運輸 発行済データ(csv)ファイルを開くことができません.")
        sys.exit()


    for i in range(1,len(csv_data_mercari)):
        data = csv_data_mercari[i]
        id = data[0]
        tracking = search_tracking_id(csv_data_yamato, id)
        data[14] = tracking
        csv_data_mercari[i] = data


    with open('~/Desktop/orders_ship.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data_mercari)
    
    os.remove('~/Desktop/orders.csv')
    os.remove(yamato_data_path)
    print('orders_ship.csv を保存しました.')
    print('メルカリで一括発送を行ってください')
    print('メルカリにアップロード後エンターを押してください')
    input()
    os.remove('~/Desktop/orders_ship.csv')


'''


print('orders.csv を削除しました')
print('orders_add.csv を保存しました.')

'''

'''
0 order_id
14 shipping_tracking_info
'''
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("エラー内容:", e)
        print("エラーが発生しました")