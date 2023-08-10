from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora_idade():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']

        if name.strip() == '':
            result = 'Por favor, digite o nome!'
        else:
            today = datetime.date.today()
            dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d').date()

            # Calcula a idade em anos
            age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

            # Calcula a quantidade de dias até o próximo aniversário
            this_year_birthday = datetime.date(today.year, dob_date.month, dob_date.day)
            next_birthday = this_year_birthday if this_year_birthday > today else datetime.date(today.year + 1, dob_date.month, dob_date.day)
            days_until_next_birthday = (next_birthday - today).days

            # Calcula quantos dias vividos
            days_lived = (today - dob_date).days

            anos = 'ano' if age == 1 else 'anos'

            result = f'{name}, você tem {age} {anos} ou {days_lived} dias!<br><br>Faltam {days_until_next_birthday} dias para o seu próximo aniversário! 🎂🎉'
            return render_template('index.html', result=result)

    return render_template('index.html', result='')

app.run(host='0.0.0.0', debug=True)