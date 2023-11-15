<p align="center">
    <a href="#"><img src="pictures/header.jpg" alt="Logo" width=80%/></a>
</p>
<p align="center">
    ⚙️ Work in Progress ⚙️
</p>
PyProductivity é um script que monitora o tempo de uso de aplicações e salva o tempo gasto em cada uma, automaticamente, gerando reports de usos diários. O script pode te ajudar a analizar onde está perdendo mais tempo podendo focar nas aplicações corretas.

🖥️ Interface principal                                        | 🖥️ Console do monitorador                                        | 🖥️ Interface de análise   
:----------:                                            | :--------------:                                        | :--------------: 
<img src="pictures/screenshots/main_interface_screenshot.jpg" /> <img src="pictures/screenshots/main_interface_menu_screenshot.jpg" />   | <img src="pictures/screenshots/console_screenshot.jpg" />   | <img src="pictures/screenshots/analysis_interface_screenshot.jpg" /> 

## ⚙️ Funcionalidades

- ✅ Monitorar e registra o tempo de uso de janelas ativas.
- ✅ Detecta inatividade
- ✅ Registra em um arquivo csv o tempo, janela e status de inatividade
- ☑️ Lê e analisa dados dos reportes diários

## 🧰 Bibliotecas

- ✅ __pygetwindow__: Identifica a janela ativa
- ✅ __pyautogui__: Ajuda a identificar inatividades
- ✅ __matplotlib__: Gera gráficos
- ✅ __pandas__: Analisa e manipula dados
- ✅ __numpy__: Ajuda a lidar com calculos matemáticos com dados
- ✅ __pywin32__: Permite esconder o console (opcional)


## ⬇️ Como usar

1. Clone ou faça o download do repositório no seu computador..

2. Abra o terminal e navegue até o diretório onde o script está localizado.

3. Execute o script com o seguinte comando:


```shell
 python main.py
```
ou

4. Execute o arquivo __exec_main.bat__

5. Na interface principal você pode escolher entre:
    - Iniciar diretamente o script de monitoramento
    - Abrir a interface de análise
    - Instalar o script de monitoramento na inicialização do sistema

# 📋 Pré-requisitos

Antes de usar o PyProductivity, certifique-se de ter os seguintes pré-requisitos:

- Python 3.x instalado no seu sistema.
- Ter as bibliotecas instaladas. Você pode instalar usando o comando:

``` shell
pip install -r requirements.txt
```
ou

- Execute o arquivo __update_libs.bat__ 

## Exemplos de analises de relatorio e saidas no arquivo csv 📊

<img src="pictures/screenshots/analysis_interface_screenshot.jpg" width="49%"/> <img src="pictures/screenshots/analysis_interface_screenshot_2.jpg" width="49%" />

```csv

timestamp,app_name,minutes_away
2023-11-03 16:08:04,Windows PowerShell,0
2023-11-03 16:08:08,Windows PowerShell,0
2023-11-03 16:08:08,tracker_data.py - PyWindows - Visual Studio Code,0
2023-11-03 16:08:08,Visual Studio Code,0

```

O report vai conter o horário, o nome da janela do aplicativo e a duração da inatividade em minutos (que pode ser utilizado como filtro para analises).


## ⌛ Progresso de desenvolvimento

- [x] Monitorar e registrar o tempo de atividade das janelas ativas
- [x] Detectar inatividade
- [x] Registrar dados em um arquivo CSV
- [x] Ler relatórios de datas e plotar gráficos de tempo total de uso
- [ ] Gráficos mais informativos
- [ ] Metas de tempo com visualização de progresso em tempo real
- [ ] Limitar o tempo diário de uso do aplicativo pelo nome do aplicativo

E talvez algumas funcionalidades a mais


## 🙏 Agradecimentos especiais

O readme deste repositório foi inspirado no readme template do [repo-full-readme](https://github.com/Dener-Garcia/repo-full-readme/) por [Dener Garcia](https://github.com/Dener-Garcia)


## 💬 Vamos conectar?

<div align="left">
  <a href="https://linkedin.com/in/moscarde" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-333333?style=flat&logo=linkedin&logoColor=0072b1" alt="Linkedin logo" height="30px" />
  </a>
  <a href="https://github.com/moscarde" target="_blank">
    <img src="https://img.shields.io/badge/-Github-333333?style=flat&logo=github&logoColor=00000"  alt="Linkedin logo" height="30px"  />
  </a>
    
  
</div>