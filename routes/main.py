from flask import Blueprint, render_template, send_from_directory
import os
import random

main = Blueprint('main', __name__)
base_dir = '/workspace/flask_app/dataset/handpicked_dataset'

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/random_image')
def random_image():
    files = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f))]
    selected_file = random.choice(files)
    return render_template('random_image.html', filename=selected_file)

@main.route('/images/<filename>')
def images(filename):
    return send_from_directory(base_dir, filename)