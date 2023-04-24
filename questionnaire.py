import json

class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromJsonData(data):

        choix = [i[0] for i in data['choix'] ]
        bonne_reponse = [i[0] for i in data['choix'] if i[1]]
        if len(bonne_reponse) != 1:
            return None
        q = Question(data['titre'], choix , bonne_reponse[0])
        return q

    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[(reponse_int-1)] == self.bonne_reponse:
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score

#Charger un fichier JSON
filename = "cinema_starwars_debutant.json"
file = open(filename, "r")
json_data = file.read()
file.close()

Questionnaire_data = json.loads(json_data) #  On transforme le fichier json en un dictionnaire python(déserialiser)

Questionnaire_data_question = Questionnaire_data["questions"]

q = Question.FromJsonData(Questionnaire_data_question[0])
q.poser()


