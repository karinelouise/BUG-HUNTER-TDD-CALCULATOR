# BUG-HUNTER-TDD-CALCULATOR
Parada Obrigatória 2 - Alta Qualidade em Software

Este repositório foi criado para a atividade da disciplina de **Alta Qualidade em Software**, com foco em identificação de bugs, documentação de defeitos, aplicação de TDD e uso de Git/GitHub para versionamento.

## Objetivos da atividade

- Identificar defeitos no código da calculadora.
- Elaborar relatórios detalhados de bugs.
- Corrigir um dos defeitos usando a metodologia TDD.
- Garantir que a correção não introduza novos problemas.
- Utilizar Git e GitHub para registrar e publicar a evolução do projeto.

## Arquivos do projeto

```text
BUG-HUNTER-TDD-CALCULATOR/
├── Calculadora.py
├── Bugs.md
├── README.md
└── tests/
    └── test_calculadora.py
```

## Bug escolhido para correção com TDD

O bug escolhido foi o da função **fatorial(x)**.

### Problema encontrado
A implementação original inicia o laço em `0`:

```python
for i in range(x+1):
    fat *= i
```

Como qualquer número multiplicado por zero resulta em zero, a função retornava `0` para praticamente todos os valores positivos, o que está incorreto.

### Comportamento esperado
- `fatorial(5)` deve retornar `120`
- `fatorial(0)` deve retornar `1`

## Etapas do TDD aplicadas

### 1. Red
Foi criado um teste automatizado para verificar que `fatorial(5)` deve retornar `120`.
Nesse momento, o teste falha, evidenciando o bug.

### 2. Green
A função foi corrigida para calcular corretamente o fatorial, iniciando o laço em `1`.

### 3. Refactor
Após a correção, a lógica foi mantida simples e legível, preservando o comportamento esperado e sem alterar desnecessariamente outras partes do código.

## Como executar os testes

No terminal, dentro da pasta do projeto:

```bash
python -m unittest discover -s tests
```

## Como versionar e enviar para o GitHub

Depois de salvar os arquivos e validar os testes:

```bash
git add .
git commit -m "Corrige bug do fatorial com TDD e adiciona documentação"
git push origin main
```

## Reflexão sobre o processo com Scrum

Mesmo sendo uma atividade individual, o processo pode ser relacionado ao framework Scrum:

- **Planejamento:** definição do bug a corrigir e preparação do ambiente.
- **Execução incremental:** criação do teste, correção do código e validação.
- **Inspeção:** análise dos resultados dos testes.
- **Adaptação:** ajustes na implementação até a solução correta.

Esse fluxo ajudou a tornar o desenvolvimento mais organizado, verificável e orientado à qualidade.
