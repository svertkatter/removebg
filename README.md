# 画像背景削除アプリ

画像をアップロードすると自動的に背景を削除するWebアプリケーションです。

## 🌐 オンラインデモ

**GitHub Pages版（インストール不要）**: [https://svertkatter.github.io/removebg/](https://svertkatter.github.io/removebg/)

- サーバー不要、完全にブラウザ内で動作
- 画像はサーバーにアップロードされず、プライバシー保護
- インストールや設定なしで即座に利用可能

## 機能

- 画像ファイル（PNG, JPG, JPEG, GIF, BMP, WEBP）のアップロード
- 自動背景削除処理（AI搭載）
- 処理済み画像のプレビュー表示
- 処理済み画像のダウンロード
- ドラッグ&ドロップ対応
- レスポンシブデザイン対応（スマホ・タブレット対応）

## 構成

```
removebg/
├── docs/               # GitHub Pages用静的サイト
│   └── index.html      # ブラウザ完結版（サーバー不要）
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

### 📱 オンライン版（最も簡単・推奨）

GitHub Pagesで公開されているバージョンをブラウザで開くだけ:

👉 **[https://svertkatter.github.io/removebg/](https://svertkatter.github.io/removebg/)**

- インストール不要
- サーバー不要
- 完全にブラウザ内で動作
- プライバシー保護（画像はアップロードされません）

### 🖥️ ローカルWebアプリケーション

サーバーをローカルで動かす場合:

1. 依存パッケージをインストール:
```bash
pip install -r requirements.txt
```

2. Webアプリを起動:
```bash
python web_app.py
```

3. ブラウザで以下のURLにアクセス:
```
http://localhost:5000
```

### 🪟 デスクトップGUIアプリ（従来版）

```bash
pip install -r requirements.txt
python app.py
```

## 技術スタック

### GitHub Pages版（docs/）
- **画像処理**: @imgly/background-removal (TensorFlow.js)
- **フロントエンド**: HTML5, CSS3, JavaScript ES6 Modules
- **特徴**: 完全クライアントサイド処理、サーバー不要

### ローカルWebアプリ版（web_app.py）
- **バックエンド**: Flask (Python)
- **画像処理**: rembg, Pillow
- **フロントエンド**: HTML5, CSS3, JavaScript (Vanilla)

### デスクトップGUI版（app.py）
- **GUI**: tkinter
- **画像処理**: rembg, Pillow

## 注意事項

- アップロード可能な最大ファイルサイズ: 16MB
- 処理には数秒かかる場合があります
- 初回実行時、rembgが必要なモデルをダウンロードするため時間がかかる場合があります

## ライセンス

MIT License
