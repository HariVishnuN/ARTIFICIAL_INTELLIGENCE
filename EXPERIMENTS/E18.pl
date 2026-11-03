dob(john, '2001-05-12').
dob(mary, '2002-08-23').
dob(alice, '2000-11-05').
start :- write('Enter name (lowercase, with period): '), read(Name), 
         (dob(Name, Date) -> write('DOB is: '), write(Date) ; write('Not found')), nl.