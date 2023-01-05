import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model_file = open('SVM.pkl', 'rb')
model = pickle.load(model_file)


@app.route('/')
def index():
    return render_template('index.html', output='belum diprediksi')


@app.route('/pred`ict', methods=['POST'])
def predict():
    away_team_mean_defense_score, away_team_mean_midfield_score, away_team_mean_offense_score, away_team_total_fifa_points, home_team_mean_defense_score, home_team_mean_midfield_score, home_team_mean_offense_score= [
        x for x in request.form.values()]
    data = []

    data.append(int(away_team_mean_defense_score))
    data.append(int(away_team_mean_midfield_score))
    data.append(int(away_team_mean_offense_score))
    data.append(int(away_team_total_fifa_points))
    data.append(int(home_team_mean_defense_score))
    data.append(int(home_team_mean_midfield_score))
    data.append(int(home_team_mean_offense_score))

    prediction = model.predict([data])
    output = (prediction[0])
    if output == 2.0:
        hasil = "Home Team Diprediksi Menang"
    else :
        hasil = "Home Team Diprediksi Kalah"

    return render_template('index.html', output=hasil, away_team_mean_defense_score=away_team_mean_defense_score, away_team_mean_midfield_score=away_team_mean_midfield_score, away_team_mean_offense_score=away_team_mean_offense_score, away_team_total_fifa_points=away_team_total_fifa_points, home_team_mean_defense_score=home_team_mean_defense_score, home_team_mean_midfield_score=home_team_mean_midfield_score, home_team_mean_offense_score=home_team_mean_offense_score)

    if __name__ == '__main__':
        app.run(debug=True)