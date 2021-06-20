# SiWR2021

Projekt polegał na stworzeniu systemu przewidującego wyniki meczów piłki nożnej wykorzystującego probablistyczne modele grafowe. 
System miał przewidywać jaki będzie wynik następnego meczu, mając do dyspozycji wyniki już rozegranych meczy.

W pierwszej kolejności przy tworzeniu algorytmu zastosowałem 'Bayessian model', aczkolwiek wyniki nie były satysfakcjonujące, a skuteczność zaledwie na poziomie ~45%.

Aktualnie skuteczność algorytmu na wybranych data-setach wynosi nawet ~60%, więc jest to bardzo pozytywny wynik biorąc pod uwagę że mamy aż 3 możliwości.
Poniższy wykres przedstawia zależności pomiędzy wynikami przewidywanymi a prawdziwymi. Jak możemy zaobserwować algorytm popełnia najwięcej błędów dla wyników typu 'draw', natomiast przy obliczaniu czy wygra H (HomeTeam) czy A (AwayTeam) radzi sobie całkiem nieźle.



![test](https://user-images.githubusercontent.com/82948715/122416087-bee34780-cf88-11eb-89f2-215a90fb92fb.PNG)
