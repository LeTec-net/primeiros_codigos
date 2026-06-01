"""
Algoritimo
Como extrair o primeiro nome de uma pessoa
"""

name = ""
for x in "Joca@silva.com":
  if x != "@":
     name = name + x
  else:
     break
  
  print(name)
  