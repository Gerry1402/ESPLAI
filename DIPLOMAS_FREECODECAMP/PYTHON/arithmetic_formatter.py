def arithmetic_arranger(problems, show_answers=False):
    arriba = []
    abajo = []
    suma = []
    guiones = []
    if len(problems)>5:
        return 'Error: Too many problems.'
    for problema in problems:
        comprobar_suma = '+' in problema
        if len(problema.split(' + ')) == 2:
            problema = problema.split(' + ')
            suma.append(comprobar_suma)
        elif len(problema.split(' - ')) == 2:
            problema = problema.split(' - ')
            suma.append(comprobar_suma)
        else:
            return "Error: Operator must be '+' or '-'."
        arriba.append(problema[0])
        abajo.append(problema[1])
        if not arriba[-1].isnumeric() or not abajo[-1].isnumeric():
            return 'Error: Numbers must only contain digits.'
        guiones.append('-'*(max([len(problema[0]),len(problema[1])])+2))
        if len(guiones [-1])>6:
            return 'Error: Numbers cannot be more than four digits.'
    string_arriba = ''
    string_abajo = ''
    string_guiones = ''
    string_resultados = ''
    for i in range(len(problems)):
        string_arriba += ' '*(len(guiones[i])-len(arriba[i]))+arriba[i]
        if suma[i]:
            string_abajo += '+'+' '*(len(guiones[i])-len(abajo[i])-1)+abajo[i]
            resultado = str(int(arriba[i])+int(abajo[i]))
        else:
            string_abajo += '-'+' '*(len(guiones[i])-len(abajo[i])-1)+abajo[i]
            resultado = str(int(arriba[i])-int(abajo[i]))
        string_guiones += guiones[i]
        string_resultados += ' '*(len(guiones[i])-len(resultado))+resultado
        if i != len(problems)-1:
            string_arriba += ' '*4
            string_abajo += ' '*4
            string_guiones += ' '*4
            string_resultados += ' '*4
        else:
            string_arriba += '\n'
            string_abajo += '\n'
            if show_answers:
                string_guiones += '\n'
                return string_arriba+string_abajo+string_guiones+string_resultados
            else:
                return string_arriba+string_abajo+string_guiones

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')