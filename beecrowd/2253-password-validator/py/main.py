import re

def main():
  while True:
    try:
      password = input()
      checkLength = lambda password : len(password) < 6 or len(password) > 32
      hasMinChars = lambda password : re.search('[A-Z]', password) and re.search('[a-z]', password) and re.search('\d', password)
      if checkLength(password) or not password.isalnum() or not hasMinChars(password):
        print('Senha invalida.')
      else:
        print('Senha valida.')
    except EOFError:
      break

if __name__ == "__main__":
  main()