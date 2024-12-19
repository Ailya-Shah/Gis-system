from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def fetch_images():
    connection = sqlite3.connect('gis_data.db')  
    cursor = connection.cursor()
    cursor.execute("SELECT ImagePath, LandmarkName, Latitude, Longitude, Comments FROM landmarks")
    data = cursor.fetchall()
    connection.close()
    return [
        {
            "ImagePath": row[0],
            "LandmarkName": row[1],
            "Latitude": row[2],
            "Longitude": row[3],
            "Comments": row[4]
        }
        for row in data
    ]

@app.route('/')
def index():
    images = fetch_images()
    return render_template('index1.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)

