import flet as ft
from interface import interface_setup, build_ui

def main(page: ft.Page):
   interface_setup(page)
   build_ui(page)

if __name__ == '__main__':
    ft.app(main)