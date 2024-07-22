# Cookiecutter Python Package Template

Este é um template Cookiecutter para criar pacotes Python. Ele fornece uma estrutura básica para um projeto de pacote Python, incluindo testes, configuração de logging, e mais.

## Estrutura do Projeto

```bash
.
├── py-package
│   ├── __init__.py
│   ├── io
│   │   ├── __init__.py
│   │   ├── logging.py
│   ├── main.py
│   ├── runner
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_unit_transformer.py
│   └── transformation
│       ├── capture.py
│       ├── detection.py
│       ├── __init__.py
│       ├── processing.py
│       └── output_write.py
├── Makefile
├── output
│   └── .gitkeep
├── README.md
├── requirements.txt
├── setup.py
└── templates
    └── index.html
```

## Como Usar Este Template

### Pré-requisitos

- Python 3.6 ou superior
- Cookiecutter instalado

Você pode instalar o Cookiecutter usando pip:

```bash
pip install cookiecutter
```

### Passos para Usar o Template

1. **Execute o Cookiecutter com este template**

   No terminal, execute o comando abaixo para usar o template:

   ```bash
   cookiecutter https://github.com/juanengml/cookiecutter-py-template.git
   ```

2. **Responda às Perguntas**

   Você será solicitado a fornecer algumas informações para configurar seu novo projeto. Aqui estão alguns exemplos de perguntas e respostas:

   ```plaintext
   full_name [Your Name]: John Doe
   email [your.email@example.com]: john.doe@example.com
   github_username [yourusername]: johndoe
   project_name [My Emotion Analysis Project]: Video Emotion Analysis
   project_slug [video_emotion_analysis]: video_emotion_analysis
   project_short_description [A short description of the project.]: Analyzing emotions from video data
   version [0.1.0]: 0.1.0
   ```

3. **Estrutura do Projeto Gerado**

   Após responder às perguntas, uma nova pasta será criada com a estrutura do projeto. A estrutura seguirá o modelo descrito na seção anterior.

4. **Instale as Dependências**

   Navegue até o diretório do projeto gerado e instale as dependências:

   ```bash
   cd video_emotion_analysis
   make install
   ```

5. **Rodando Testes**

   Para rodar os testes, use o comando:

   ```bash
   make test
   ```

## Contribuindo

Se você encontrar problemas ou tiver sugestões para melhorar este template, sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório do GitLab.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

### Como Atualizar o `README.md`

1. **Abra o arquivo `README.md` no seu editor de texto favorito**.
2. **Substitua o conteúdo atual pelo conteúdo fornecido acima**.
3. **Faça o commit e push das mudanças**:

   ```bash
   git add README.md
   git commit -m "Adiciona tutorial de uso no README"
   git push origin main
   ```

Isso fornecerá aos desenvolvedores um guia claro e detalhado sobre como usar o template Cookiecutter que você criou.