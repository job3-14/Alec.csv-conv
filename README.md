# Alec.csv-conv
発送用csvをヤマトB2形式に変換するプログラム
$ python3 -V
Python 3.10.9

ヤマト側(出力)
ヤマト側取込みパターン指定 -> 基本レイアウトcsv
1行目から取り込み開始

| ヤマト側項目                                   | BASE側項目                                                     | プログラム上変数・関数名  |
| ---------------------------------------------- | -------------------------------------------------------------- | ------------------- |
| 出荷予定日                                     | 当日の日付                                                     | date |
| お客様管理番号                                 | 注文ID [0]                                                     | id |
| 送り状種類                                     | 固定0 (発払い)                                                 | deliveryType |
| クール区分                                     | 固定1 : クール冷凍                                             | coolClass |
| お届け先コード                                 | None                                                           | deliveryAddressCode |
| お届け先電話番号                               | 電話番号(配送先) [16]                                          | deliveryPhoneNumber |
| お届け先電話番号枝番                           | None                                                           | deliveryPhoneNumberBranch |
| お届け先名                                     | 氏(配送先) [10] + 名(配送先) [11]                              | deliveryName |
| お届け先郵便番号                               | 郵便番号(配送先) [12]                                          | deliveryPostalCode |
| お届け先住所                                   | 都道府県(配送先) [13] + 住所(配送先) [14] + 住所2(配送先) [15] | deliveryAddress |
| お届け先建物名（アパートマンション名）         | None                                                           | deliveryBuildingName |
| お届け先会社・部門１                           | None                                                           | deliverydepartment1 |
| お届け先会社・部門２                           | None                                                           | deliverydepartment2 |
| お届け先名略称ｶﾅ                             | None                                                           | deliveryAddressAbbreviation |
| 敬称                                           | None                                                           | titlesSalutations |
| ご依頼主コード                                 | MAIN (B2側で事前に依頼主コードを設定)                          | clientCode |
| ご依頼主電話番号                               | None                                                           | clientPhoneNumber |
| ご依頼主電話番号枝番                           | None                                                           | clientPhoneNumberBranch |
| ご依頼主名                                     | None                                                           | clientName |
| ご依頼主郵便番号                               | None                                                           | clientPostalCode |
| ご依頼主住所                                   | None                                                           | clientAddress |
| ご依頼主建物名（アパートマンション名）         | None                                                           | clientBuildingName |
| ご依頼主名略称ｶﾅ                             | None                                                           | clientNameAbbreviation |
| 品名コード１                                   | 0001 (B2側で事前に依頼主コードを設定)0001は鹿肉                | itemCode1 |
| 品名１                                         | None                                                           | item1 |
| 品名コード２                                   | None                                                           | itemCode2 |
| 品名２                                         | None                                                           | item2 |
| 荷扱い１                                       | None                                                           | cargoHandling1 |
| 荷扱い２                                       | None                                                           | cargoHandling2 |
| 記事                                           | None                                                           | cargoMemo |
| お届け予定（指定）日                           | 配送日 [31]                                                    | deliveryDate |
| 配達時間帯区分                                 | 配送時間帯[32]                                                 | deliveryTime |
| 営業所止置き                                   | None                                                           | officeStop |
| 営業所コード                                   | None                                                           | OfficeCode |
| 個数口枠の印字                                 | None                                                           | numberUnits |
| 発行枚数                                       | None                                                           | numberCopiesPrinted |
| ご請求先顧客コード                             | None                                                           | billingCustomerCode |
| ご請求先分類コード                             | None                                                           | billingClassificationCode |
| 運賃管理番号                                   | None                                                           | freightControlNumber |
| お届け予定ｅメール利用区分                     | 0 (利用しない)                                                     | scheduledDeliveryEmailClassification |
| お届け予定ｅメールアドレス                     | None                                                           | scheduledDeliveryEmailAddres |
| 入力機種                                       | None                                                           | InputModel |
| お届け予定ｅメールメッセージ                   | None                                                           | scheduledDeliveryEmailMessage |
| お届け完了ｅメール利用区分                     | 0 (利用しない)                                                  | deliveryCompletionEmailUsageClassification |
| お届け完了ｅメールアドレス                     | None                                                           | deliveryCompletionEmailAddress |
| お届け完了ｅメールメッセージ                   | None                                                           | deliveryCompletionEmailMessage |
| 複数口くくりキー                               | None                                                           | multiMouthedKey |
| 検索キータイトル１                             | None                                                           | searchKeyTitle1 |
| 検索キー１                                     | None                                                           | searchKey1 |
| 検索キータイトル２                             | None                                                           | searchKeyTitle2 |
| 検索キー２                                     | None                                                           | searchKey2 |
| 検索キータイトル３                             | None                                                           | searchKeyTitle3 |
| 検索キー３                                     | None                                                           | searchKey3 |
| 検索キータイトル４                             | None                                                           | searchKeyTitle4 |
| 検索キー４                                     | None                                                           | searchKey4 |
| 投函予定メール利用区分                         | None                                                           | scheduledMailUsageClassification |
| 投函予定メールe-mailアドレス                   | None                                                           | scheduledMailUsageEmailAddress
| 投函予定メールメッセージ                       | None                                                           | scheduledMailUsageEmailMessage |
| 投函完了メール（お届け先宛）利用区分           | None                                                           | MailingCompletionRrecipientUsageCategory |
| 投函完了メール（お届け先宛）e-mailアドレス     | None                                                           | MailingCompletionRrecipientAddres |
| 投函完了メール（お届け先宛）メールメッセージ   | None                                                           | MailingCompletionRrecipientMessage |
| 投函完了メール（ご依頼主宛）利用区分           | None                                                           | MailingCompletionclientUsageCategory |
| 投函完了メール（ご依頼主宛）e-mailアドレス | None                                                           | MailingCompletionclientUsageAddress |
| 投函完了メール（ご依頼主宛）メールメッセージ   | None                                                           | MailingCompletionclientUsageMessage |