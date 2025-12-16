from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    total = data.get('total', 0)
    grades = {
        '5': data.get('5', 0),
        '4': data.get('4', 0),
        '3': data.get('3', 0),
        '2': data.get('2', 0),
    }
    graded_total = sum(grades.values())
    not_graded = max(total - graded_total, 0)
    if not_graded > 0:
        grades['Не оценено'] = not_graded

    # считаем проценты
    percents = {k: round(v / total * 100, 1) for k, v in grades.items()}
    return jsonify({'grades': grades, 'percents': percents})

if __name__ == '__main__':
    app.run(debug=True)
