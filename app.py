from datetime import timedelta
from flask import *
from flask_cors import CORS

import config
from config import *
import os
import logging as rel_log
import shutil
import core.main

app = Flask(__name__)

cors = CORS(app, supports_credentials=True)
app.config['MAX_CONTENT_PATH'] = 1024*1024

werkzeug_logger = rel_log.getLogger('werkzeug')
werkzeug_logger.setLevel(rel_log.ERROR)


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


def process_func(img_name, img_path, num):
    if num == 1:
        print('ok')


# 判断上传有效
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():

    return redirect(url_for('static', filename='./index.html'))


@app.route('/upload/<int:id>', methods=['POST','GET'])
def upload_image(id):
    # 获取上传的文件
    content_image = request.files.get('content_file')

    if content_image:
        content_img_path = os.path.join(app.config['UPLOAD_FOLDER'], content_image.filename)
        content_image.save(content_img_path)
        shutil.copy(content_img_path, './tmp/ct')
        content_path = os.path.join('./tmp/ct', content_image.filename)

        # 50 train
        if id == 50:
            style_image = request.files.get('style_file')
            if style_image:
                # 处理风格图片
                style_img_path = os.path.join(app.config['UPLOAD_FOLDER'], style_image.filename)
                style_image.save(style_img_path)
                shutil.copy(style_img_path, './tmp/ct')
                style_path = os.path.join('./tmp/ct', style_image.filename)

                training_count = request.form.get('training_count')
                learning_rate = request.form.get('learning_rate')

                if training_count and learning_rate:
                    training_count = int(training_count)
                    learning_rate = float(learning_rate)
                    core.main.train_main(content_path,style_path,training_count,learning_rate)
                else:
                    core.main.train_main(content_path,style_path,config.EPOCHS,config.LEARNING_RATE)
                return jsonify({'status': 1,
                                'image_url': 'http://127.0.0.1:5000/tmp/train_output/20.jpg',
                                'draw_url': 'http://127.0.0.1:5000/tmp/train_output/20.jpg'
                                })
        else:
            pid = core.main.c_main(content_path, id, content_image.filename.rsplit('.', 1)[1])

            return jsonify({'status': 1,
                            'image_url': 'http://127.0.0.1:5000/tmp/ct/' + pid,
                            'draw_url': 'http://127.0.0.1:5000/tmp/draw/' + pid
                            })
    return jsonify({'status': 0})


@app.route("/download", methods=['GET'])
def download_file():
    return send_from_directory('data')


@app.route('/tmp/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        if not file is None:
            image_data = open(f'tmp/{file}', 'rb').read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response


if __name__ == '__main__':
    files = [
        'uploads', 'tmp/ct', 'tmp/draw',
         'tmp/train_output'
    ]
    for f in files:
        if not os.path.exists(f):
            os.makedirs(f)

    app.run(debug=True)


