import requests

URL_TRIVIA = "https://opentdb.com/api.php?amount=15&category=21&difficulty=easy"
URL_API_TRADUCCION = "https://api.mymemory.translated.net/get"


respuesta = requests.get(URL_TRIVIA)

datos = respuesta.json()
preguntas = datos.get("results")

for la_pregunta in preguntas:
    #parametros = {"q": la_pregunta.get("question"), "langpair": "en|es"}
    original_question = la_pregunta["question"]

    parametros = {"q": original_question, "langpair": "en|es"}
    res_traduccion = requests.get(URL_API_TRADUCCION, params=parametros, timeout=5) 

    es_question = res_traduccion.json().get("responseData").get("translatedText", original_question)

    print(es_question, "->", la_pregunta.get("correct_answer"))



                                            #TAREA#
#busquen una APP API donde se pueda consultar cualquier patologia, 
# ie: "síndrome de tourette", y que entregue
#cuáles son los síntomas y los tratamientos de aquella enfermedad

                                            #TAREA2#


#usando cualquiera de las 2 (dogapi o catapi), consumir 
# (mostrar todos los datos de una raza de animal específica, junto con la foto),
#