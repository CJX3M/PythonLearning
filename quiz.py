def getAnswer(question):
    answer = ''
    while answer.lower() != 'a' and answer.lower() != 'b':
        answer = input(question)
    return answer.lower()

def printAnswer(answer, messageA, messageB):
    if answer == 'a':
        print(messageA)
    elif answer == 'b':
        print(messageB)


activity = getAnswer("""1. ¿Cómo prefiere pasar la noche?
    a) Leyendo un libro
    b) Asistiendo a una fiesta""")

printAnswer(activity, "Buena elección", "Sounds fun!")

job = getAnswer("""2. ¿Cuál es su trabajo de ensueño?
    a) Conservador en el Smithsonian
    b) Gerente de un negocio""")

printAnswer(job, "Conservador, buena elección", "Administrar un negocio? Suena bien")

value = getAnswer("""3. ¿Qué es más importante?
a) Money
b) El amor""")

printAnswer(value, "Dinero? Buena elección", "Amor? Suena divertido")

decade = getAnswer("""4. ¿Cuál es su década favorita?
a) 1910
b) 2010""")

printAnswer(decade, "1910? Suena divertido", "2010? Buena elección")

travl = getAnswer("""5. ¿Cuál es su forma de viajar favorita?
a) Conducción
b) Volar""")

printAnswer(travl, "Conducción? Suena divertido", "Volar? Buena elección")

# create some variables for scoring
sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

# update scoring variables based on the activity choice
if activity == "A":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    kai_like = kai_like + 2
else:
    cam_like = cam_like + 1
    indy_like = indy_like + 1

# update scoring variables based on the job choice
if job == "A":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    cam_like = cam_like - 1
else:
    sam_like = sam_like - 1
    kai_like = kai_like + 2
    indy_like = indy_like + 1

# update scoring variables based on the value choice
if value == "A":
    sam_like = sam_like - 1
    kai_like = kai_like + 1
else:
    sam_like = sam_like + 2
    cam_like = cam_like + 2
    indy_like = indy_like + 1

# update scoring variables based on the decade choice
if decade == "A":
    cam_like = cam_like + 2
    sam_like = sam_like + 2
else:
    kai_like = kai_like + 1
    indy_like = indy_like + 2

# update scoring variables based on the travel choice
if travl == "A":
    sam_like = sam_like - 2
    kai_like = kai_like + 1
    indy_like = indy_like - 1
else:
    sam_like = sam_like + 1
    cam_like = cam_like + 1
    kai_like = kai_like - 1

# print the results depending on the score
if sam_like >= 3:
    print( "You're most like Sharp-Eyed Sam!" )
elif cam_like >= 3:
    print( "You're most like Curious Cam!" )
elif kai_like >= 3:
    print( "You're most like Keen Kai!" )
else:
    print( "You're most like Inquisitive Indy!" )