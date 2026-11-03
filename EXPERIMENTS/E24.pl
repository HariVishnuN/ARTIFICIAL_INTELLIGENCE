
diet(diabetes, 'Low sugar food, vegetables and whole grains').
diet(obesity, 'Low calorie food, fruits and vegetables').
diet(anemia, 'Iron rich food like spinach and beans').
diet(hypertension, 'Low salt food, fruits and vegetables').
diet(heart_disease, 'Low fat food, vegetables and whole grains').

suggest_diet(Disease) :-
    diet(Disease, Food),
    write('Recommended diet: '),
    write(Food).

suggest_diet(Disease) :-
    \+ diet(Disease, _),
    write('No diet recommendation available.').
