import utils
from flask import Flask

candidate_list = utils.get_candidates_list('candidates.json', 'id', 'name', 'picture', 'position', 'gender', 'age', 'skills')

app = Flask(__name__)

@app.route("/")
def index():
    return utils.print_candidate_list(candidate_list)


@app.route('/candidates/<int:uid>')
def profile(uid):
    return utils.get_person_by_id(uid, candidate_list)


@app.route('/skills/<uid>')
def profile_skill(uid):
    return utils.get_person_by_skill(uid, candidate_list)


app.run()

