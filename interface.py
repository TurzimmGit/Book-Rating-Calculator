import flet as ft
from calculus import get_final_rating, validate_grade
from notion_api import search_for_pageID, update_Notion_grades

def create_input_field(label,width=None,expand=False,is_grade=False):
    
    def on_blur_validate(e):
        if is_grade:
            e.control.value = validate_grade(e.control.value)
            e.control.update()
    return ft.TextField(
        label=label,
        width=width,
        expand=expand,
        text_align= ft.TextAlign.RIGHT if is_grade else ft.TextAlign.LEFT,
        on_blur=on_blur_validate if is_grade else None,
        keyboard_type= ft.KeyboardType.NUMBER if is_grade else ft.KeyboardType.TEXT
    )

def interface_setup(page):
    page.title= "Avaliação livros"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 500
    page.window_height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()
    
def build_ui(page):
    
    #title
    titulo = ft.Text("Calcular nota de livros", size=32,weight="bold")
    
    # book info
    txt_name = create_input_field("Nome do livro",expand=True)
    txt_autor = create_input_field("Autor", expand=True)
    
    # Grades side by side in a row
    
    txt_write = create_input_field("Escrita",expand=True,is_grade=True)
    txt_flux = create_input_field("Fluidez",expand=True,is_grade=True)
    txt_plot = create_input_field("Plot/Clareza",expand=True,is_grade=True)
    
    # Final result
    
    lbl_result = ft.Text("---",size=40,weight="bold",color="blue")
    lbl_status_notion = ft.Text("", italic=True, size=12)
    
    def calculate_click(e):
        try:
            res = get_final_rating(
                float(txt_write.value or 0),
                float(txt_flux.value or 0),
                float(txt_plot.value or 0)
            )
            lbl_result.value = f"{res:.1f}"
            if res < 3:
                lbl_result.color = "red"
            elif res < 5:
                lbl_result.color = "orange"
            elif res < 7:
                lbl_result.color = "yellow"
            else:
                lbl_result.color = "green"
            
            btn_enviar.visible = True
            page.update()
        except:
            lbl_result.value = "Erro"
        page.update()
        
    def enviar_notion_click(e):
        
        lbl_status_notion.value = "Conectando ao Notion..."
        lbl_status_notion.color = "blue"
        page.update()
        
        p_id = search_for_pageID(txt_name.value, txt_autor.value)
        
        if p_id:
            grades = {
                "final": float(lbl_result.value),
                "escrita" : float(txt_write.value),
                "fluidez" : float(txt_flux.value),
                "plot": float(txt_plot.value)
            }
            if update_Notion_grades(p_id, grades):
                
                lbl_status_notion.value = f"Enviado ao Notion: A nota do livro '{txt_name.value}' é {lbl_result.value}"
                lbl_status_notion.color = "green"
            else:
                lbl_status_notion.value = "Erro na atualização das Colunas"
                lbl_status_notion.color = "red"
        else:
            lbl_status_notion.value = "Livro não encontrado na tabela"
            lbl_status_notion.color = "orange"
        page.update()
        
    btn_enviar = ft.ElevatedButton(
        "Confirmar e Enviar",
        icon="cloud_upload",
        visible=False,
        on_click=enviar_notion_click
    )

    btn_calcular = ft.ElevatedButton(
        "Calcular",
        on_click = calculate_click,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        
    )
    
    container_result = ft.Container(
        content=lbl_result,
        alignment=ft.Alignment(0, 0),
        width=150,
        height=100,
        border=ft.border.all(2,"blue"),
        border_radius=15,
        bgcolor="surfacevariant"
    )
    
    
    layout = ft.Container(
        content=ft.Column(
            [
            titulo,
            ft.Divider(height=20,color="transparent"),
            txt_name,
            txt_autor,
            ft.Divider(height=10,color="transparent"),
            ft.Row([txt_write,txt_flux,txt_plot], spacing=20),
            ft.Divider(height=30),
            ft.Text("Nota Final",size=18,weight="w500"),
            container_result,
            btn_calcular,
            btn_enviar,
            lbl_status_notion
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        width=700,
        padding=40,
        border=ft.border.all(1,ft.Colors.WHITE_24),
        border_radius=20,
        bgcolor=ft.Colors.with_opacity(0.05,ft.Colors.WHITE_24)
    )
       
    
    page.add(ft.Container(
        content=layout,
        alignment=ft.Alignment(0, 0),
        expand=True
    ))