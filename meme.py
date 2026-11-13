meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD" : "Reaccion para cuando algo es gracioso"
            "FOMO" : "Cuando te da envidia algo que no pudiste hacer o algun lugar que no pudiste ir"
            "AURA" : "Una vibra o puntos de fama o de una sensacion de satisfaccion en algo o alguien"
            }
word = input("Escribe una palabra que no entiendas (¡con mayusculas!): ")
if word in memedict.keys() :
    print(word, ": ", meme_dict[word])
else :
    print("palabra no encontrada")
