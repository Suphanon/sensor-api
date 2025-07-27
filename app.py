from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/sensor')
def get_sensor_data():
    # ตัวอย่างข้อมูลเซนเซอร์
    return jsonify({
        "temperature": 27.5,
        "humidity": 65
    })

@app.route('/')
def serve_dashboard():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)