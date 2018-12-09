from flask import Flask,jsonify
import pyodbc

app = Flask(__name__)
def getPersons():
    cnxn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-322F0HM\SA1;'
                          'Database=testdb;'
                          'Trusted_Connection=yes;')
    cur = cnxn.cursor()
    query = 'select * from Person'
    cur.execute(query)
    column_header=[meta[0] for meta in cur.description]

    content=[dict(zip(column_header,row)) for row in cur.fetall()]

    cur.close();
    cnxn.close()
    return content

@app.route('/getPerson',methods=['GET'])
def getPerson():
    rows=getPersons()
    jsonify(dict(rows))

@app

if __name__=='__main__':
    app.run(debug=True)