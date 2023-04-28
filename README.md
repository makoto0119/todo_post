# todo_post
todo_post は、クリップボードにコピーした内容を todoist に登録するツールです。

## logic
ソースを見て下さい。そこそこ例外動作は入れてあります。

## Features
1. Todoist に対応しています。
2. クリップボードの中身は空行を詰め、１行目をtodoの名前に、２行目以降があれば中身の記述とします。

## Requirement
ソースを持って行った人は、エラーが出たら個別に対応して下さい。

## Installation
python の実行環境があれば、todo_post_pub.py を DL して使って下さい。
todoist の web にて、設定画面の以下の部分に API token がありますので、これをソースにコピペして下さい。
当然、この token が漏れると、第三者が API であなたの todoist に自由にアクセスできるようになりますので、十分注意して使って下さい。

![image](https://user-images.githubusercontent.com/94595507/235099875-3fdc0692-fb9d-4512-ab6e-fd59848b68d5.png)

todo のレベルなど、必要ならソースを修正して下さい。デフォルトは適当になってます。

## Usage
動かすだけです。特に UI はありません。勝手に クリップボーを参照し、todoist に API でアクセスします。

## Note
todoist APIの仕様が変わると、動かなくなる可能性はあります。自分は日常使っているので、動かなくなったら気付くとは思いますが、何かあれば連絡下さい。

## Author
* 齋藤　誠
* 個人
* makoto0119@gmail.com

## License
自由に使って下さい
