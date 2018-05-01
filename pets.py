from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)

pet_list = convert_to_dict("pets.csv")

@app.route('/')
def detail():
    for pet in pet_list:
        pet_dict = pet
        break
    return render_template('profile.html', pet=pet_dict)

if __name__ == '__main__':
    app.run(debug=True)
