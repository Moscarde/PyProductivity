# pylint: disable=import-error
import pygetwindow as gw
import psutil





# Obter a janela ativa
active_window = gw.getActiveWindow()
process_id = active_window._hWnd
print(active_window._hWnd)

process = psutil.Process(process_id)
print(process)