#!/usr/bin/env python
"""
ヤマト運輸CSVを補完するプログラム

orders.csvに情報を補完し、csvを更新後、元ファイルを削除
"""
import csv
import configparser
import os
import sys
import webbrowser

def main():
    # config.ini読み込み
    config_ini = configparser.ConfigParser()
    config_path = os.path.expanduser('~/.alec/config.ini')
    config_ini.read(config_path, encoding='utf-8')

    # メルカリCSV(B2仕様)読み込み
    orders_csv_path = os.path.expanduser('~/Downloads/orders.csv')
    try:
        with open(orders_csv_path) as f:
            reader = csv.reader(f)
            csv_data = [row for row in reader]
    except Exception as e:
        print("エラー：メルカリCSV ファイルを開くことができません.")
        sys.exit()

    # CSVデータの補完処理
    for i in range(1, len(csv_data)):
        data = csv_data[i]
        product_code = data[29]
        data[1] = config_ini[product_code]['package_type']
        data[2] = config_ini[product_code]['cool_type']
        data[19] = config_ini['DEFAULT']['tel']
        data[21] = config_ini['DEFAULT']['zip']
        data[22] = config_ini['DEFAULT']['address']
        data[27] = config_ini[product_code]['name']
        data[39] = config_ini['DEFAULT']['billing_customer_code']
        data[41] = config_ini['DEFAULT']['freight_control_number']
        csv_data[i] = data

    # 補完後のCSVを書き出す
    orders_add_csv_path = os.path.expanduser('~/Desktop/orders_add.csv')
    with open(orders_add_csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)

    # 元のCSVを削除
    os.remove(orders_csv_path)
    print('orders.csv を削除しました')
    print('orders_add.csv を保存しました.')
    print('ヤマトで伝票発行後, 追跡データをダウンロードして一括発送を行なってください.')
    print('ヤマト運輸にアップロード後エンターを押してください')
    yamato_url = 'https://bmypage.kuronekoyamato.co.jp/bmypage/'
    webbrowser.open(yamato_url, new=2, autoraise=True)
    input()
    os.remove(orders_add_csv_path)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("エラー内容:", e)