from src import logic2,utils
from src.aima.utils import expr
from src.aima import logic,utils



#---------------
q_1=list()

#(1)color(carrots, orange).
q_1.append(expr("carrots(c) ==> color(c,orange)"))

# (2) likes(Person, carrots):-vegetarian(Person). 
q_1.append(expr("veget(Pe) & carrots(c) ==> likes(Pe,c)"))

# (3) pass(Student) :- study_hard(Student).
# (4) ?- pass(Who). 
q_1.append(expr("studend(St) & study_hard(St) ==> pass(St)"))

# (5) ?- teaches(professor, Course).
q_1.append(expr("professor(Pr) ==> teaches(Pr,course)"))

# (6) enemies(X, Y) :- hates(X, Y), fights(X, Y).
q_1.append(expr("hates(x,y) & fights(x,y) ==> enemies(x,y)"))

#---------------
q_2=list()

#(1) Maria reads logic programming book by author peter lucas.
q_2.append(expr("read(Maria,logic programming book) & author(peter lucas,logic progamming book)"))

#(2) Anyone likes shopping if she is a girl.
#(3) Who likes shopping?
q_2.append(expr("girl(Gi) ==> likes(Gi,Shopping)"))


#(4) kirke hates any city if it is big and crowdy
q_2.append(expr("city(Ci) & big(Ci) & crowdy(CI) ==> hates(Kirke,Ci)"))

#-----------------

q_3=list()

# (1) hates(X,Y), hates(Y,X) :- enemies(X, Y)
q_3.append(expr("hates(x,y) & hates(y,x) ==> enemies(x,y)"))

# (2) p(X):-(q(X):-r(X))
q_3.append(expr("(r(X) ==> q(X)) ==> p(X)"))

#-------------------
q_4=list()

# (1) jia is a woman.
q_4.append(expr("woman(jia)"))

# (2) john is a man.
q_4.append(expr("man(jhon)"))

# (3) john is healthy.
q_4.append(expr("healthy(jhon)"))

# (4) jia is healthy.
q_4.append(expr("healthy(jia)"))

# (5) john is wealthy.
q_4.append(expr("wealthy(jhon)"))

# (6) anyone is a traveler if he is healthy and wealthy.
q_4.append(expr("( healthy(x) & wealthy(x) ) ==> traveler(x) "))

# (7) anyone can travel if he is a traveler
q_4.append(expr("traveler(y) ==> can_travel(y)"))

#create Knowledge base (KB) from previous q_4es.
KB=logic.FolKB(q_4)

goal_1=logic.fol_fc_ask(KB,expr("can_travel(y)"))
print("(1) who can travel ? : ",list(goal_1))

goal_2=logic.fol_fc_ask(KB,expr("healthy(x) & wealthy(x)"))
print("(2) who is healthy and wealthy ? : ",list(goal_2))

#