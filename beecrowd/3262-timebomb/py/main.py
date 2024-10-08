digits = {'''***
* *
* *
* *
***
''' : '0', '''  *
  *
  *
  *
  *
''' : '1', '''***
  *
***
*  
***
''': '2', '''***
  *
***
  *
***
''': '3', '''* *
* *
***
  *
  *
''': '4', '''***
*  
***
  *
***
''': '5', '''***
*  
***
* *
***
''': '6', '''***
  *
  *
  *
  *
''': '7','''***
* *
***
* *
***
''': '8','''***
* *
***
  *
***
''': '9'
}

def main():
    DIGIT_HEIGHT = 5
    DIGIT_WIDTH = 3

    display = []
    for _ in range(DIGIT_HEIGHT):
        display.append(input())

    number = ''
    explode = False
    j = 0
    while j < len(display[0]):
        current_digit = ''
        for i in range(DIGIT_HEIGHT):
            current_digit += display[i][j:j+DIGIT_WIDTH] + '\n'

        if current_digit in digits:
            number += digits[current_digit]
        else:
            explode = True
            break
        j += DIGIT_WIDTH + 1
    print('BOOM!!' if explode or int(number) % 6 != 0 else 'BEER!!')

if __name__ == "__main__":
    main()