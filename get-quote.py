import random

def principal():
  ##print("Keep it logically awesome.")

  f = open("quotes.txt", 'a')
  f.write('Tentativa de adicionar uma quote \n')
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd = random.randint(0,last)
  print(quotes[rnd], end="")
  ## essa opção de dizer como termina o print está disponível para o python3 e
  ## substitui a newline padrão
  print(quotes[last])

if __name__== "__main__":
  principal()
