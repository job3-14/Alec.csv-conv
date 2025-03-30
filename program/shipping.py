#!/usr/bin/env python
"""
ヤマト運輸CSVを補完するプログラム

orders.csvに情報を補完し、csvを更新後、元ファイルを削除
"""

import csv
import os, sys
import webbrowser
import glob
def ignore_ship(orders_add_csv_data):
    """
    ignore_mecrari.csvを読み込み該当する注文IDを削除
    """
    ignore_csv_path = os.path.expanduser('~/.alec/ignore_mercari.csv')
    try:
        with open(ignore_csv_path) as f:
            reader = csv.reader(f)
            ignore_csv_data = [row for row in reader]
    except Exception as e:
        print("エラー： ~/.alec/ignore_merceri.csvを開くことができません.")
        sys.exit()
    
    ignore_data = []
    for i in range(1, len(ignore_csv_data)):
        ignore_data.append(ignore_csv_data[i][0])

    for i in range(len(orders_add_csv_data) - 1, 0, -1):  # 逆順ループ
        if orders_add_csv_data[i][0] in ignore_data:
            del orders_add_csv_data[i]
            
    return orders_add_csv_data

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
            formatted_id = 'ヤマト運輸: ' + row_id[:4] + '-' + row_id[4:8] + '-' + row_id[8:]
            return formatted_id
    print("発送IDが見つかりません. ヤマト運輸側の出力年月日が正しいか確認してください.")
    return None


def find_yamato_csv_file():
    '''
    *_発送済データ.csvを検索し、返す関数
    複数見つかった場合はプログラムを終了する.
    '''
    # ホームディレクトリ内の「Downlods」フォルダを指定
    search_dir = os.path.expanduser("~/Downloads")
    # ワイルドカード * を使用してパターンを指定
    pattern = os.path.join(search_dir, "*_発行済データ.csv")
    
    # パターンに一致するファイルを検索
    files = glob.glob(pattern)
    
    # 複数ファイルが見つかった場合
    if len(files) > 1:
        print("複数の'_発行済データ.csv'見つかりました")
        print("全て削除してください")
        sys.exit(1)
    # 該当ファイルが見つからなかった場合（必要に応じて処理を変更）
    elif len(files) == 0:
        print("ファイルが見つかりません")
        sys.exit(1)
    
    # 単一ファイルが見つかった場合、そのパスを返す
    return files[0]


def main():
    print('ヤマトにログイン後、エンターキーを押してください.')
    yamato_login = 'https://bmypage.kuronekoyamato.co.jp/bmypage/'
    webbrowser.open(yamato_login, new=2, autoraise=True)
    input()

    print('一括発送CSVをダウンロードしてください.')
    print('ダウンロード後エンターキーを押してください.')
    mercari_url = 'https://mercari-shops.com/seller/shops/66LLW6ENCaaEex3Zs7sZde/orders/upload/'
    webbrowser.open(mercari_url, new=2, autoraise=True)
    input()
    # メルカリCSV(B2仕様)読み込み
    orders_csv_path = os.path.expanduser('~/Downloads/orders.csv')
    try:
        with open(orders_csv_path) as f:
            reader = csv.reader(f)
            csv_data_mercari = [row for row in reader]
    except Exception as e:
        print("エラー：メルカリCSV ファイルを開くことができません.")
        sys.exit()
    csv_data_mercari = ignore_ship(csv_data_mercari)
    # ヤマトCSV読み込み
    print('ヤマト発送済みCSVをダウンロードしてください.')
    print('ダウンロード後エンターキーを押してください.')
    yamato_url = 'https://newb2web.kuronekoyamato.co.jp/issue_search.html'
    webbrowser.open(yamato_url, new=2, autoraise=True)
    input()
    yamato_data_path = find_yamato_csv_file()
    print(yamato_data_path)
    try:
        with open(yamato_data_path, encoding='cp932') as f:
            reader = csv.reader(f)
            csv_data_yamato = [row for row in reader]
    except Exception as e:
        print("エラー：ヤマト運輸 発行済データ(csv)ファイルを開くことができません.")
        sys.exit()

    # メルカリCSVに追跡番号情報を追加
    for i in range(1, len(csv_data_mercari)):
        data = csv_data_mercari[i]
        order_id = data[0]
        tracking = search_tracking_id(csv_data_yamato, order_id)
        if tracking is None:
            print("追跡情報が存在しません")
            os.remove(yamato_data_path)
            sys.exit(1)
        data[14] = tracking
        csv_data_mercari[i] = data

    # 補完後のCSVを書き出す
    orders_ship_csv_path = os.path.expanduser('~/Desktop/orders_ship.csv')
    with open(orders_ship_csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data_mercari)
    
    # 元のCSVファイルとヤマトCSVファイルを削除
    os.remove(orders_csv_path)
    os.remove(yamato_data_path)
    print('orders_ship.csv を保存しました.')
    print('メルカリで一括発送を行ってください')
    print('メルカリにアップロード後エンターを押してください')
    input()
    os.remove(orders_ship_csv_path)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("エラー内容:", e)
        print("エラーが発生しました")
