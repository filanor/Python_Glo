def create_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)
    return field

def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()

def win(field):
    for i in range(3):
        if field[i][0] != '*' and field[i][0] == field[i][1] == field[i][2]:
            return True
        if field[0][i] != '*' and field[0][i] == field[1][i] == field[2][i]:
            return True
        if field[0][0] != '*' and field[0][0] == field[1][1] == field[2][2]:
            return True
        if field[0][2] != '*' and field[0][2] == field[1][1] == field[2][0]:
            return True                
        
        
def end_game(field):
    if(win(field)):
        return True
    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False
    return True


def input_coord():
    while True:
        coord = input()
        if coord.isdigit() == True:
            coord = int(coord)
            if coord > 0 and coord <= 3:
                return coord - 1
            print('номер должен быть в диапазоне от 1 до 3 включительно')
        else:
            print('номер модет состоять только из цифр')

def check_coord(field, coord):
    if field[coord['x']][coord['y']] != '*':
        print('Данная позиция уже занята')
        return False
    return True

def play_xo(): 
    field = create_field()

    current_symbol = 'x'
    coord = {}

    while not win(field):
        print_field(field)
        print(f'Ход {current_symbol}. Введите номер строки и номер столбца')

        coord['x'] = input_coord()
        coord['y'] = input_coord()
        
        if check_coord(field, coord) == False:
            continue

        field[coord['x']][coord['y']] = current_symbol

        if current_symbol == 'x':
            current_symbol = 'o'
        else:
            current_symbol = 'x'

    if current_symbol == 'x':
        print('Ура! Победил 0')
    else:
        print('Ура! Победил x')


# ============= main ==================
print('Крестики нолики')
while True:
    play_xo()
    print('\n\n Хочешь сыграть еще раз?\n')
    play_more = input().lower()
    if play_more != 'да' or play_more != 'yes':
        break