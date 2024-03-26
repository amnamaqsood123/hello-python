from flask import Flask, request
import datetime

app = Flask(__student_data_app__)

@app.route('/')
def index():
    # Get current time and date
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    
    
    student_name = "Amna Maqsood"
    
    
    student_id = "S2264480"
    
    return f"Hello, {student_name}!<br>Your Student ID is: {student_id}.<br>Current time: {current_time}<br>Current date: {current_date}"

if __student_data_app__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

