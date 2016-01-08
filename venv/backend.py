from flask import Flask, jsonify, request, abort
from flask.ext.cors import CORS
"""import pudb; pudb.set_trace()"""
app = Flask(__name__)
CORS(app)
comments = [
{
'name': 'a',
'message': 'asdflakjsdflakjsdf',
'like': 0,
'id': 0
},
{
'name': 'b',
'message': 'asdlfkajsdlfkjalkj',
'like': 0,
'id': 1
},
{
'name': 'c',
'message': 'asdlfkajsdlfkjalkj',
'like': 10,
'id': 2
},
{
'name': 'd',
'message': 'asdlfkajsdlfkjalkj',
'like': 5,
'id': 3
},
{
'name': 'e',
'message': 'asdlfkajsdlfkjalkj',
'like': 3,
'id': 4
},
{
'name': 'f',
'message': 'asdlfkajsdlfkjalkjdasddasssssdwqrwegfrghherherwerwyugbwergivruibgvreogiopoiefnqwfpeohgoirpoopm[jvyuwefobuicweivybiponhubviasdfwegehefqrfefwrgehrthrgtwregrthrtjtygrefgsdfvsdcsdcsdcassfdwertewtwefgsdfsdfas',
'like': 8,
'id': 5
}
]

empty = []

def liked(c):
    return c['like']

for comment in sorted(comments, key = liked, reverse = True)[0:5]:
    if comment['like'] >= 5:
        empty.append(comment)

id = len(comments)


@app.route('/comments', methods=['GET'])
def show_comments():
    return jsonify(
    {
    'data': comments
    }
    )


@app.route('/comment', methods=['POST'])
def new_comment():
    d = request.json["data"]
    """
    d['id'] = len(comments)
    comments.append(d)
    """
    global id
    d['id'] = id
    comments.append(d)
    comments.sort()
    print sorted(comments, key = liked, reverse = True)[0:5]
    id = id + 1
    return jsonify(
    d
    )


@app.route('/comment/<id>', methods=['PUT', 'DELETE'])
def like_comment(id):
    """abort(403)"""
    if request.method == 'PUT':
        for comment in comments:
            if int(comment['id']) == int(id):
                comment['like'] += 1

    else:
        for comment in comments:
            if int(comment['id']) == int(id):
                comments.pop(comments.index(comment))
    return 'Done'


@app.route('/most_liked_comments', methods=['GET'])
def most_liked_comments():
    print empty
    return jsonify(
    {
    'data': empty
    }
    )

if __name__ == '__main__':
    app.run(debug=True)
