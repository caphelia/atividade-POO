# Simulando uma carteira de investimentos
iniciamos a atividade criando uma classe "AtivoFinanceiro" com atributos "nome", "valor investido" e "valor atual" <br />
<br />
depois, atualizamos o código ao adicionar um meio de atualizar o valor do ativo e um meio de calcular o retorno do ativo <br />
<br />
até esse ponto não houveram dificuldades pois foi possível seguir os exemplos para guiar a sintaxe e aplicar uma lógica semelhante para os cálculos<br />
<br />
no primeiro exercício extra, foi necessário utilizar "str" para imiprimir as informações de um ativo. o maior problema aqui foi a sintaxe e os detalhes, como limitar a reposta a dois decimais ou lembrar de quebrar a linha para facilitar a visualização depois do print.<br />
<br />
na parte 3 ocorreu a criação de uma nova classe "CatreiraInvestimentos". houveram algumas partes que não estavam encaixando como o esperado, mas estas foram deixadas para serem corrigidas mais para frente<br />
<br />
o exercício extra 2, assim como o extra 1, foi focado em criar um "str" de modo que as informações sejam apresentadas ao utilizar "print". os erros do passo anterior foram mantidos.<br />
<br />
por fim, foi necessário testar a carteira. aqui houveram alguns problemas que precisaram ser corrigidos. a maior dificuldade ocorreu em uma confusão na parte de sintaxe, devido aos nomes similares que coloquei em algumas partes. outra dificuldade foi em fazer com que as somas no "investimento total" e no "valor total" funcionassem e também no "retorno carteira", que necessitava da utilização do "self". a última dificuldade notável foi ao retornar os nomes dos ativos que estavam incuídos na carteira, foi necessário criar uma linha nova para que os nomes aparecessem de modo correto no print.

# Projeto Final
Após pesquisar diferentes estratégias de Algorithmic Trading em finanças, decidi utilizar a Mean Reverse strategy como base para o projeto <br />
Essa escolha foi feita pois a estratégia tem uma lógica simples e parecida com os exemplos dados na aula de programação orientada a objetos<br />
<br />
A mean reverse strategy assume que os preços de um ativo tendem a retornar à sua média de preço.<br />
Assim, o investidor pode comprar quando os preços estiverem abaixo da média e vender quando estiverem acima<br />
<br />
Para escrever um código que realize essa lógica, foi necessário utilizar os parâmetros (param) do backtrader para definir o período para calcular a média móvel e o desvio para considerar se a compra / venda deve ocorrer<br />
Descobrir como criar esses parâmetros foi uma parte complicada<br />
<br />
Depois disso, foi necessário um ajuste simples para que o "param" period e o period do simple moving average fossem o iguais<br />
<br />
A ideia de utilizar uma "data atual" está presente no código, mesmo que ela não vá ser atualizada a não ser que o "pip install --upgrade yfinance" seja rodado antes do resto do código<br />
<br />
O restante do código é o mesmo dos exemplos, exceto que utiliza a estratégia baseada no Mean Reverse<br />
