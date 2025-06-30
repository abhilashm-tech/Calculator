from flask import Flask, render_template, request

app = Flask(__name__)

current_expression = ''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    global current_expression

    if request.method == 'POST':
        btn = request.form['btn']

        if btn == 'C':
            current_expression = ''
        elif btn == '=':
            try:
                current_expression = str(eval(current_expression))
            except:
                current_expression = 'Error'
        else:
            if current_expression == 'Error':
                current_expression = ''
            current_expression += btn

    return render_template('index.html', expression=current_expression)

if __name__ == '__main__':
    app.run(debug=True)