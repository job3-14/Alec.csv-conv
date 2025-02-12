"""
ヤマト運輸CSVを補完するプログラム

orders.csvに情報を補完し、csvを更新後、元ファイルを削除
"""

import csv
import configparser
import os

def main():
    # config.ini読み込み
    config_ini = configparser.ConfigParser()
    config_ini.read('~/.alec/config.ini', encoding='utf-8')

    # メルカリCSV(B2仕様)読み込み
    try:
        with open('~/Desktop/orders.csv') as f:
            reader = csv.reader(f)
            csv_data = [row for row in reader]
    except Exception as e:
        print("エラー：メルカリCSV ファイルを開くことができません.")
        sys.exit()



    for i in range(1,len(csv_data)):
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


    with open('~/Desktop/orders_add.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)

    os.remove('~/Desktop/orders.csv')

    print('orders.csv を削除しました')
    print('orders_add.csv を保存しました.')
    print('ヤマトで伝票発行後, 追跡データをダウンロードして一括発送を行なってください.')
    print('ヤマト運輸にアップロード後エンターを押してください')
    input()
    os.remove('~/Desktop/orders_add.csv')




'''
不足分
1 送り状種類
2 クール区分
19 ご依頼主電話番号
21 ご依頼主郵便番号
22 ご依頼主住所
27 品名１
39 請求先顧客コード
41 運賃管理番号



読み込み
29 品名２ == MIX
'''

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("エラー内容:", e)