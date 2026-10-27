teaches(smith, cs101).
teaches(jones, ai102).
studies(bob, cs101).
studies(eve, ai102).
start :- write('Enter student name (lowercase, with period): '), read(Student), 
         (studies(Student, Sub), teaches(Teacher, Sub) -> 
         write('Teacher: '), write(Teacher), write(', Subject: '), write(Sub) ; write('Not found')), nl.