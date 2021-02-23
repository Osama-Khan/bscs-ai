course(1, "CS-205", "Artificial Intelligence").
course(2, "CS-505", "Software Engineering").

student(101, "Asif Khan", "BSCS-5").
student(102, "Kashif Ali", "BSCS-9").
student(103, "Fahad Tariq", "BSCS-5").

course_grade(1, 101, "CS-205", 95, "A").
course_grade(2, 102, "CS-205", 67, "C").
course_grade(3, 103, "CS-205", 78, "A").
course_grade(4, 101, "CS-505", 90, "B").
course_grade(5, 102, "CS-505", 65, "C").
course_grade(6, 103, "CS-505", 75, "B").

courseCode(NAME, CODE):-
    course(_, CODE, NAME).

getAGraders(NAME, COURSE):-
	student(ROLL, NAME, _),
    courseCode(COURSE, CODE),
	course_grade(_, ROLL, CODE, _, "A").

classFellow(WHOSE, WHO):-
    student(_, WHOSE, SEC),
    student(_, WHO, SEC),
	WHOSE \= WHO.

goodStudent(WHO):-
	student(R, WHO, _),
    course_grade(_, R, _, _, "A").

marks(WHO, MARKS, COURSE):-
    student(R, WHO, _),
    courseCode(COURSE, CODE),
    course_grade(_, R, CODE, MARKS, _).