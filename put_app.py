from flask import Flask, request
from flask.json import jsonify

data = [{'name':'Java'},
        {'name':'Python'},
        {'name':'C++'}]

app = Flask(__name__)

@app.route('/home/<string:name>',methods=['PUT'])
def put_req(name):
    print('name',name)
    lan = [data_pnts for data_pnts in data if data_pnts['name']==name]
    lan[0]['name']= request.json['name']
    return jsonify({'languages':lan})

if __name__=='__main__':
    app.run(port=5000, debug=True)