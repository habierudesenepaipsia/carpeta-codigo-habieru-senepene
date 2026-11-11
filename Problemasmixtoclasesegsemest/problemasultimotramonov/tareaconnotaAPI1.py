import requests

URL_MED = "https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term=asthma"


answer = requests.get(URL_MED)

data = answer.json()
querys = data.get("results")

#PARAMETERS
#db = Database to search -> healthTopics ? healthTopicsSpanish
#term = Text query submitted to the Web service ->
#EXAMPLE URL
#https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term=asthma 


#TA MAL0/ TEST TEST TEST TEST TEST
#for query in querys:
#    original_question = query["question"]
#
#    parameter = {"q": original_question, "langpair": "en|es"}
#    res_traduccion = requests.get(URL_API_TRADUCCION, params=parametros, timeout=5) 
#
#
#    print(es_question, "->", query.get("correct_answer"))    

#TEST 2TEST 2TEST 2TEST 2TEST 2

print("results")