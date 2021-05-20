import pandas as pd

from pgmpy.models import BayesianModel
# from pgmpy.factors.discrete import TabularCPD
# from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator

from pgmpy.sampling import BayesianModelSampling #IMPORTANTE


f = pd.read_csv('data.csv', parse_dates=['Date'])

# print(f)
# print(f['HomeTeam'].describe)
# print(f['HomeTeam'].nunique()) #Ilosc druzyn

cut_data = f[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']] #najważniejsze informacje
# print(cut_data)


# model = BayesianModel()
#
#
# samples = BayesianModelSampling(model).forward_sample(size=int(1e3))
# samples.head()


# data = pd.DataFrame(data={'A': [0, 0, 1], 'B': [0, 1, 0], 'C': [1, 1, 0]})
# print(data)

model = BayesianModel([('Date', 'HomeTeam'), ('Date', 'AwayTeam')])
model.fit(cut_data)
model.get_cpds()