fim = False
while fim is False:
    try:
        a = int(input('numerador: '))
        b = int(input('Denominador: '))
        r = a / b
    except ZeroDivisionError(f'Infelismente tivemos um problema==> {erro.__class__}')

    else:
        print(f'A resposta é {r}.')
        fim = True
    finally:
        if fim is True:
            print('Acabou!')
        else:
            print('Tente novamente!')

