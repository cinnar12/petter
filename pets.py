from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)
application = app

pet_list = convert_to_dict("pets.csv")

@app.route('/')
def index():
    for pet in pet_list:
        pet_dict = pet
        break
    return render_template('base.html', pet=pet_dict)

@app.route('/dog/<num>.html')
def doginfo(num):
    for pet in pet_list:
        if pet['ID'] == num and 'dog' in pet['Breed']:
            pet_dict = pet
            break
    return jsonify({'data': render_template('profile.html', pet=pet_dict)})

@app.route('/cat/<num>.html')
def catinfo(num):
    for pet in pet_list:
        if pet['ID'] == num and 'dog' not in pet['Breed']:
            pet_dict = pet
            break
    return render_template('profile.html', pet=pet_dict)

if __name__ == '__main__':
    app.run(debug=True)
