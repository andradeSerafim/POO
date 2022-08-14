def adiciona_txt(produto_novo):
    # akhen é o nome de meu usuário no Windows.
    # Ao utilizar meu código, favor adaptar o caminho do arquivo.
    nome_arquivo = r"C:\Users\akhen\PycharmProjects\produto_forum\todos_produtos.txt"
    produto_str = str(produto_novo)

    with open(nome_arquivo, "r") as arquivo_leitura:
        adicionar = True
        for linha in arquivo_leitura:
            if produto_str in linha:
                adicionar = False
                print(f'Ítem {produto_novo["descricao"]} já existe. ')
        else:
            with open(nome_arquivo, "a") as arquivo:
                if adicionar:
                    print(f'Adicionando ítem {produto_novo["descricao"]}. ')
                    arquivo.write(produto_str + '\n')


class Produto:
    def __init__(self, codigo: str, descricao: str, preco: float, estoque: int, observacoes: str = ''):
        self.produto_adicionado = {
            'codigo': codigo,
            'descricao': descricao,
            'preco': preco,
            'estoque': estoque,
            'observacoes': observacoes
        }
        print("Lembrete que o preço é sempre em R$.")

    def __str__(self) -> str:
        return str(self.produto_adicionado)

    def __getitem__(self, item):
        erro = "Existem apenas 'codigo', 'descricao', 'preco', 'estoque' e 'observacoes'."
        if item in self.produto_adicionado:
            return self.produto_adicionado[item]
        else:
            raise ValueError(erro)


produto = Produto('SK1012',
                  'Caneta esferográfica azul',
                  1.59,
                  10000,
                  '16 cm, retrátil, ponta fina')
produto_2 = Produto('SK12646',
                    'Caneta esferográfica prateada',
                    1.29,
                    2000,
                    '133 mm, acionada por giro, ponta fina')

print(produto['codigo'])  # Para buscar o nome do código
adiciona_txt(produto)
adiciona_txt(produto_2)

onde_esta = r"C:\Users\akhen\PycharmProjects\produto_forum\todos_produtos.txt"
with open(onde_esta, "r") as arquivo_lido:
    for linha_lida in arquivo_lido:
        print(linha_lida)
