import sys
from itertools import product

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (ConfusionMatrixDisplay, accuracy_score,
                             confusion_matrix)


def calculate_probs(data):
    """
    Calculates probabilities of winning and draws for each team
    """
    keys = list(np.union1d(
        data['HomeTeam'].unique(), data['AwayTeam'].unique()))
    team_side = ['H', 'A']
    draws = [f"{team}_D" for team in keys]

    keys = [' / '.join(vals) for vals in product([*keys, *draws], team_side)]

    probs = dict(zip(keys, [0]*len(keys)))

    home_games = data.groupby(by='HomeTeam').size()
    away_games = data.groupby(by='AwayTeam').size()

    home_group = data.query("FTR != 'A'").groupby(by=['HomeTeam', 'FTR'])
    for key, group in home_group:
        team, result = key
        if result != 'D':
            probs[' / '.join(key)] = round(len(group) /
                                           home_games.loc[team], 4)
        else:
            probs[f"{team}_D / H"] = round(len(group) /
                                           home_games.loc[team], 4)

    away_group = data.query("FTR != 'H'").groupby(by=['AwayTeam', 'FTR'])
    for key, group in away_group:
        team, result = key
        if result != 'D':
            probs[' / '.join(key)] = round(len(group) /
                                           away_games.loc[team], 4)
        else:
            probs[f"{team}_D / A"] = round(len(group) /
                                           away_games.loc[team], 4)

    return probs


def get_result(teamH, teamA):
    """
    Gets predicted outcome of a match
    """
    H_wins = probs[f"{teamH} / H"] * \
        (1 - probs[f"{teamA} / A"]) * (1 - probs[f"{teamA}_D / A"])
    A_wins = probs[f"{teamA} / A"] * \
        (1 - probs[f"{teamH} / H"]) * (1 - probs[f"{teamH}_D / H"])
    draw = (probs[f"{teamH}_D / H"] * probs[f"{teamA}_D / A"]) + 0.115

    scores = [H_wins, A_wins, draw]
    win_ind = scores.index(max(scores))

    if win_ind == 0:
        return 'H'
    elif win_ind == 1:
        return 'A'
    else:
        return 'D'


def test_dataset(data):
    """
    Function for testing accuracy on the entire dataset
    """
    scores = []
    predicted, true_vals = [], []
    for ind, match in data[['HomeTeam', 'AwayTeam', 'FTR']].iterrows():
        home, away, score = match.values

        # broad = f"{home} vs {away} : {get_result(home, away)}"
        # print(f"{broad:<40} ==> true: {score}")
        pred = get_result(home, away)

        predicted.append(pred)
        true_vals.append(score)
        scores.append(pred == score)

    print("\nScore: ", round(accuracy_score(true_vals, predicted) * 100, 2), "%", sep='')

    labels = ['H', 'A', 'D']
    cm = confusion_matrix(true_vals, predicted, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

    disp.plot()
    plt.show()


if __name__ == '__main__':
    try:
        data = pd.read_csv('data.csv')
    except:
        print(
            "Please provide dataset named: data.csv in " +
            "the same directory as main.py"
        )
        sys.exit()

    probs = calculate_probs(data)

    # test_dataset(data)

    _, date, home, away = sys.argv
    print(get_result(home, away))
