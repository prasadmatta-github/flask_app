from flask import Flask, request, jsonify

app = Flask(__name__)

data = [{'name':'John'}]

@app.route('/',methods=['POST'])
@app.route('/home',methods=['POST'])
def home():
    user_data = request.json['name']
    data.append({"name":user_data})
    return jsonify({'response':data})

if __name__=='__main__':
    app.run(debug=True, port=5000)