from flask import Flask, send_file

app = Flask(__name__)

@app.route('/downloadCsv')
def downloadCsv():
    try:
        return send_file('/home/rahultarak12345/hashcat/temp.csv',
                         mimetype='text/csv',
                         attachment_filename='temp.csv',
                         as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')


