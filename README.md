# 画像背景削除アプリ

画像をアップロードすると自動的に背景を削除するWebアプリケーションです。

## 機能

- 画像ファイル（PNG, JPG, JPEG, GIF, BMP, WEBP）のアップロード
- 自動背景削除処理
- 処理済み画像のプレビュー表示
- 処理済み画像のダウンロード
- レスポンシブデザイン対応

## 構成

```
removebg/
├── app.py              # オリジナルのTkinter GUIアプリ
├── web_app.py          # FlaskベースのWebアプリ
├── templates/
│   └── index.html      # Webアプリのフロントエンド
├── static/
│   └── style.css       # スタイルシート
├── uploads/            # アップロードされた画像の一時保存先（自動生成）
├── outputs/            # 処理済み画像の保存先（自動生成）
└── requirements.txt    # Python依存パッケージ
```

## インストール

1. リポジトリをクローン（または既にクローン済み）

2. 依存パッケージをインストール:
```bash
pip install -r requirements.txt
```

## 使い方

### Webアプリケーション（推奨）

1. Webアプリを起動:
```bash
python web_app.py
```

2. ブラウザで以下のURLにアクセス:
```
http://localhost:5000
```

3. 画像ファイルを選択して「背景を削除」ボタンをクリック

4. 処理が完了したら、プレビューを確認してダウンロード

### デスクトップGUIアプリ（従来版）

```bash
python app.py
```

## 技術スタック

- **バックエンド**: Flask (Python)
- **画像処理**: rembg, Pillow
- **フロントエンド**: HTML5, CSS3, JavaScript (Vanilla)

## 注意事項

- アップロード可能な最大ファイルサイズ: 16MB
- 処理には数秒かかる場合があります
- 初回実行時、rembgが必要なモデルをダウンロードするため時間がかかる場合があります

## ライセンス

MIT License
