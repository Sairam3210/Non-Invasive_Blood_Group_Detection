from flask import Flask, request, jsonify, render_template, flash, redirect, url_for, session
from flask_mysqldb import MySQL
from wtforms.validators import ValidationError
import numpy as np
import tensorflow as tf
import cv2
import os
import ssl
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'Your_password' 
app.config['MYSQL_DB'] = 'Database_name'
app.secret_key = 'your_secret_key_here'

mysql = MySQL(app)

# Load the pre-trained model
model = tf.keras.models.load_model('./notebook/my_model.keras')

# Define allowed extensions
ALLOWED_EXTENSIONS = {'bmp'}

# Check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(file_path):
    img = load_img(file_path, target_size=(64, 64))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/about.html')
def homee():
    if 'user_id' in session:
        return render_template('about.html')#index
    return redirect(url_for('login'))

@app.route('/home.html', methods=['GET', 'POST'])
def home():
    if 'user_id' in session:
        return render_template('home.html')#home
    return redirect(url_for('login'))

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            cursor.close()
            flash('Email Already Taken', 'danger')
            return redirect(url_for('register'))

        cursor.execute('INSERT INTO user (name, email, password) VALUES (%s, %s, %s)', (name, email, password))
        mysql.connection.commit()
        cursor.close()

        flash('Registration Successful!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['user_id'] = user[0]
            return redirect(url_for('homee'))
        else:
            flash("Login failed. Please check your email and password","danger")
            return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route('/chart.html', methods=['GET'])
def chart():
    if 'user_id' in session:
        return render_template('chart.html')
    return redirect(url_for('login'))

@app.route('/', methods=['GET'])
def about():
    if 'user_id' in session:
        return render_template('index.html')#about
    return redirect(url_for('login'))

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    return jsonify({"status": "success", "data": data})

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    flash("you have been logged out successfully")
    return redirect(url_for('login'))

@app.route('/index.html')
def index():
    if 'user_id' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/predict', methods=['POST'])
def predict():
    CONFIDENCE_THRESHOLD = 0.75

    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Allowed types are bmp'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join('uploads', filename)
    file.save(file_path)

    try:
        img = preprocess_image(file_path)
        predictions = model.predict(img)
        confidence = float(np.max(predictions[0]))
        predicted_class = int(np.argmax(predictions[0]))
        class_names = ['A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-']
        predicted_label = class_names[predicted_class]

        if confidence < CONFIDENCE_THRESHOLD:
            return jsonify({
                'error': 'Prediction confidence is too low. Please try with a clearer fingerprint image.',
                'confidence': confidence
            }), 400

        return jsonify({
            'predicted_class': predicted_class,
            'predicted_label': predicted_label,
            'confidence': confidence
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:                                     
        if os.path.exists(file_path):
            os.remove(file_path)
@app.route('/portfolio_details.html', methods=['GET', 'POST'])
def blood_group():
    blood_group = request.args.get('portfolio-content')
    group_data = details.get(blood_group)
    if group_data:
        return render_template('portfolio_details.html', group=group_data)
    else:
        return render_template('404.html', message="Blood group details not available.")
if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
