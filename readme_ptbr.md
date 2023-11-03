<p align="center">
    <a href="#"><img src="pictures/header.jpg" alt="Logo" width=80%/></a>
</p>
<p align="center">
    ⚙️ Em Desenvolvimento ⚙️
</p>


>PyProductivity é um script que monitora o tempo de uso de aplicações e salva o tempo gasto em cada uma, altomaticamente, gerando reports de usos diários. O script pode te ajudar a analizar onde está perdendo mais tempo podendo focar nas aplicações corretas


## Funcionalidades Planejadas

~~- [x] Converter dados antigos para .csv~~

~~- [x] Ler dados a partir de um .csv~~ # Mudanças na lógica

- [x] Salvar dados em csv

- [ ] Interface com tkinter

- [ ] Manipular dados com pandas

- [ ] Criar análises de dados salvos

- [ ] Metas de tempos com visualização do progresso em tempo real

- [ ] Limitar o tempo de uso de aplicativos

## Funcionalidades 🌟

- Monitorar e salvar o tempo de uso de janelas ativas.

- Detectar inatividades

- Salvar o tempo, janela e status de inatividade em um arquivo csv. 

# Pré-requisitos 📋

Antes de usar o PyProductivity, certifique-se de ter os seguintes pré-requisitos:

- Python 3.x instalado no seu sistema.
- Ter as bibliotecas pyautogui, pygetwindow instaladas. Você pode instalar usando o comando:

``` shell
pip install pyautogui pygetwindow
```

# Como usar 🚀

1. Clone ou faça o download do repositório no seu computador.

2. Abra o terminal e navegue até o diretório onde o script está localizado.

3. Execute o script com o seguinte comando:

```shell
 python pyproductivity.py
```

4. O aplicativo irá começar a monitorar suas janelas ativas e salvar os reports.

5. Você pode parar o script apertando Ctrl + C no terminal ou fechando ele.

6. Os dados de uso serão salvos na pasta `logs` com o formato "YYYY-MM-DD.csv".

## Examplo de saída 📊

```csv

timestamp,app_name,minutes_away
2023-11-03 16:08:04,Windows PowerShell,0
2023-11-03 16:08:08,Windows PowerShell,0
2023-11-03 16:08:08,tracker_data.py - PyWindows - Visual Studio Code,0
2023-11-03 16:08:08,Visual Studio Code,0

```

O report vai conter o horário, o nome da janela do aplicativo e a duração da inatividade em minutos (que pode ser utilizado como filtro para analises).

## Note 📝

- ⚠️ O script registra o tempo gasto nas janelas ativas. Ele pode não capturar processos ou aplicativos em segundo plano executados sem uma janela visível.
- ⚠️ Antes de executar o script, certifique-se de ter configurado um ambiente Python e instalado as bibliotecas necessárias.
- ⚠️ O script criará arquivos de relatório de uso para cada dia no formato "AAAA-MM-DD.csv" na pasta de logs. Certifique-se de ter permissões de gravação nesse diretório.
- ✔️ Você pode ajustar as variáveis loop_interval e write_data_interval no script para alterar a frequência de monitoramento e registro de dados.
