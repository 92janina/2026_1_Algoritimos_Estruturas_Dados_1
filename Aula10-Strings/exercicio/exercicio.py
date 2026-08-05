texto = "João da Silva - Rua A, 132; Maria dos Santos - Rua B, 225"
##Construa um código em Python que manipule a string texto, a fim de construir um JSON conforme o exemplo a seguir
JSON =[ 
        { 
             "nome" : "João da Silva" ,
             "endereco" : "Rua A" ,
             "numero" : "132" 
        } ,
        { 
            "nome" : "Maria dos Santos" , 
            "endereco" : "Rua B" ,
            "numero" :  "225"
        }
    ]

dados= [
    {
        "nome": parte.split(" - ")[0],
        "endereco": parte.split(" - ")[1].split(", ")[0],
        "numero": parte.split(", ")[1].split(", ")[1]
    }
    for parte in texto.split(";")
]
print(JSON.dumps(dados,ensure_ascii=False, indent=4))


