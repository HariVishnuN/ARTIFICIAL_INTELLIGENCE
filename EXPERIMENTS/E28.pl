
symptom(flu, fever).
symptom(flu, cough).
symptom(flu, headache).

symptom(cold, sneezing).
symptom(cold, cough).
symptom(cold, runny_nose).

symptom(malaria, fever).
symptom(malaria, chills).
symptom(malaria, sweating).

diagnose(flu) :-
    symptom(flu, fever),
    symptom(flu, cough),
    symptom(flu, headache).

diagnose(cold) :-
    symptom(cold, sneezing),
    symptom(cold, runny_nose).

diagnose(malaria) :-
    symptom(malaria, fever),
    symptom(malaria, chills),
    symptom(malaria, sweating).
