# Relatório de Bugs

Este documento registra os defeitos identificados no arquivo `Calculadora.py`.

***

## Bug 1 - Função de adição retorna resultado incorreto

### Identificação do Bug
- **Título do Bug:** A operação de adição soma valores em excesso.
- **Localização do Bug:** `Calculadora.py` - função `adicao(x, y)`.

### Descrição Detalhada
- **Descrição Clara do Bug:** A função está implementada como `return x + np.add(x, y)`. Isso faz com que o valor de `x` seja somado duas vezes.
- **Contexto:** O defeito foi identificado ao analisar a implementação da função e simular a operação com valores simples.

### Passos para Reproduzir
1. Executar a função `adicao(2, 3)`.
2. Observar o valor retornado.

- **Consistência:** Ocorre sempre.

### Resultado Esperado vs. Obtido
- **Resultado Esperado:** O retorno deveria ser `5`.
- **Resultado Obtido:** O retorno é `7`.

### Evidências
- **Logs/saída observada:** `adicao(2, 3) -> 7`

### Severidade e Impacto
- **Severidade do Bug:** Alta.
- **Impacto do Bug:** Compromete uma operação matemática básica da calculadora.

### Sugestões para Correção
- Alterar a implementação para retornar apenas `np.add(x, y)` ou `x + y`.

### Registro e Acompanhamento
- **Data de Identificação:** 30/05/2026
- **Status do Bug:** Não resolvido.

***

## Bug 2 - Função fatorial retorna zero incorretamente

### Identificação do Bug
- **Título do Bug:** Fatorial de números positivos retorna `0`.
- **Localização do Bug:** `Calculadora.py` - função `fatorial(x)`.

### Descrição Detalhada
- **Descrição Clara do Bug:** O laço da função começa em `0`, e isso faz com que `fat *= 0` já na primeira iteração, zerando o resultado final.
- **Contexto:** O defeito foi identificado ao revisar a lógica de cálculo do fatorial.

### Passos para Reproduzir
1. Executar a função `fatorial(5)`.
2. Verificar o valor retornado.

- **Consistência:** Ocorre sempre para números inteiros não negativos maiores que zero.

### Resultado Esperado vs. Obtido
- **Resultado Esperado:** O retorno deveria ser `120`.
- **Resultado Obtido:** O retorno é `0`.

### Evidências
- **Logs/saída observada:** `fatorial(5) -> 0`

### Severidade e Impacto
- **Severidade do Bug:** Alta.
- **Impacto do Bug:** Invalida uma operação matemática essencial da calculadora.

### Sugestões para Correção
- Iniciar o laço em `1`.
- Adicionar teste automatizado para garantir o comportamento esperado.

### Registro e Acompanhamento
- **Data de Identificação:** 30/05/2026
- **Status do Bug:** Resolvido.

***

## Bug 3 - Logaritmo natural usa função inexistente

### Identificação do Bug
- **Título do Bug:** Função de logaritmo natural usa `np.ln`, que não existe.
- **Localização do Bug:** `Calculadora.py` - função `logaritmo_natural(x)`.

### Descrição Detalhada
- **Descrição Clara do Bug:** A implementação chama `np.ln(x)`, mas o NumPy não possui essa função.
- **Contexto:** O defeito foi identificado pela leitura do código.

### Passos para Reproduzir
1. Executar a função `logaritmo_natural(10)`.
2. Observar o erro gerado.

- **Consistência:** Ocorre sempre.

### Resultado Esperado vs. Obtido
- **Resultado Esperado:** O retorno deveria ser o logaritmo natural do número.
- **Resultado Obtido:** O programa gera erro por atributo inexistente.

### Evidências
- **Logs de Erro:** `AttributeError: module 'numpy' has no attribute 'ln'`

### Severidade e Impacto
- **Severidade do Bug:** Alta.
- **Impacto do Bug:** Impede o uso da funcionalidade de logaritmo natural.

### Sugestões para Correção
- Substituir `np.ln(x)` por `np.log(x)`.

### Registro e Acompanhamento
- **Data de Identificação:** 30/05/2026
- **Status do Bug:** Não resolvido.

***

## Bug 4 - Opções do menu chamam funções não implementadas

### Identificação do Bug
- **Título do Bug:** Menu executa funções trigonométricas inexistentes.
- **Localização do Bug:** `Calculadora.py` - função `calculadora_cientifica()`.

### Descrição Detalhada
- **Descrição Clara do Bug:** O menu exibe opções para seno, cosseno e tangente, mas o código não implementa todas essas funções de forma consistente.
- **Contexto:** Problema encontrado ao comparar as opções exibidas no menu com as funções realmente disponíveis no arquivo.

### Passos para Reproduzir
1. Executar o programa.
2. Escolher operações trigonométricas do menu.
3. Verificar o comportamento do sistema.

- **Consistência:** Ocorre sempre nas opções afetadas.

### Resultado Esperado vs. Obtido
- **Resultado Esperado:** A calculadora deveria executar corretamente a operação trigonométrica escolhida.
- **Resultado Obtido:** O programa chama funções inexistentes e pode gerar erro.

### Evidências
- **Logs de Erro:** possível `NameError` para funções não definidas.

### Severidade e Impacto
- **Severidade do Bug:** Alta.
- **Impacto do Bug:** Torna parte do menu inutilizável.

### Sugestões para Correção
- Implementar as funções faltantes ou remover temporariamente essas opções do menu.

### Registro e Acompanhamento
- **Data de Identificação:** 30/05/2026
- **Status do Bug:** Não resolvido.