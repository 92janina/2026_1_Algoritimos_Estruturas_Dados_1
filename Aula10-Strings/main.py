txt = "Python"
print( txt.upper() )
print( txt.upper().lower() )
print( txt.swapcase() )
txt = "aula de string"
print( txt. capitalize() )
print( txt.title() )

txt = "python"
txt2 = "-" + txt.strip() + "-"
print( txt2 )
txt2 = "-" + txt.lstrip() + "-"
print( txt2 )
txt2 = "-" + txt.rstrip() + "-"
print( txt2 )

url = "https://senacrs.com.br"
print( url.removeprefix("https://") )
print( url.removeprefix("https://").removesuffix(".com.br"))

txt = "python"
print( txt[ 1:3 ] )
print( txt[ -1 ] )
print( txt[ -4 : ] )
print( txt[ :3 ] )

nomes = "João , Maria, José"
lista = nomes.split(",")
print( lista )

carros = "Doblo-Uno-Jeep"
print( carros.rsplit("-" , -1 ))

txt = "python"
print( txt.find( "yth" ) )
print( txt.find( "ta" ) )

txt = "banana"
print( txt.find( "a" ) )
print( txt.rfind( "a" ) )
print( txt.count( "a" ) )

print( "-", "python123".isalpha())
print( "python".isnumeric() )
print( "python".islower() )
print( "python".isupper() )
print( "Aula de Python".istitle() )


