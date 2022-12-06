def diva():
    try:
        valor = 1

        div = valor/0
        return div

    except Exception as e:
        return e

def test():
    try:
        diva()
        return 'hola'
    except Exception as e:
        return e


print(test())