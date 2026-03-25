while True:
    biblioteca = input("Porfavor escreva o nome do livro no qual você deseja pegar emprestado: ")
    bib2 = int(input("É necessário dizer a ano de lançamento deste livro: "))
    Editora = input("Porfavor diga a editora do livro: ")
    Autor = input("Diga o nome do autor do livro: ")

    if bib2 < 2026:
        print("Livro registrado, obrigado por aluga-lo em nossa biblioteca: ")
        break
    else:
        print("Ano de lançamento do livro incorreto, porfavor reescreva o ano de lançamento: ")



