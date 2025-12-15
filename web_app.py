import os
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
from rembg import remove
import io

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

# 許可する拡張子
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

# 必要なフォルダを作成
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def remove_background(input_path, output_path):
    """背景を削除する関数"""
    image_input = Image.open(input_path)
    output = remove(image_input)
    output.save(output_path)
    return output_path

@app.route('/')
def index():
    """メインページ"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """画像をアップロードして背景を削除"""
    if 'file' not in request.files:
        return jsonify({'error': 'ファイルが選択されていません'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'ファイルが選択されていません'}), 400

    if file and allowed_file(file.filename):
        # ファイル名を安全にする
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # 元の拡張子を取得して、出力はPNGにする
        name_without_ext = os.path.splitext(filename)[0]
        output_filename = f"{name_without_ext}_nobg.png"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

        # ファイルを保存
        file.save(input_path)

        try:
            # 背景削除処理
            remove_background(input_path, output_path)

            # アップロードした元ファイルを削除（オプション）
            os.remove(input_path)

            return jsonify({
                'success': True,
                'output_filename': output_filename
            })
        except Exception as e:
            return jsonify({'error': f'処理中にエラーが発生しました: {str(e)}'}), 500
    else:
        return jsonify({'error': '許可されていないファイル形式です。png, jpg, jpeg, gif, bmp, webpのみ対応しています'}), 400

@app.route('/download/<filename>')
def download_file(filename):
    """処理済み画像をダウンロード"""
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name=filename)
    else:
        return jsonify({'error': 'ファイルが見つかりません'}), 404

@app.route('/preview/<filename>')
def preview_file(filename):
    """処理済み画像をプレビュー"""
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='image/png')
    else:
        return jsonify({'error': 'ファイルが見つかりません'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
