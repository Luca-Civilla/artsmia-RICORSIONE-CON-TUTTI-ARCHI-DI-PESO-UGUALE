import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP Exercise on MIA Art database"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("The MIA Collection database", color="orange", size=24)
        self._page.controls.append(self._title)

        # controls

        self._ddRuolo = ft.Dropdown(label = "Ruolo", border_color="orange")
        self._btnCrea = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleAnalizzaOggetti,
                                                  bgcolor="orange",
                                                  color="white",
                                                  width=200)
        self._btnConnessi = ft.ElevatedButton(text="Artisti connessi", on_click=self._controller.handleCompConnessa,
                                          bgcolor="orange",
                                          color="white",
                                          width=200,
                                          disabled=True)
        self._controller.fillDD()
        self._page.controls.append(ft.Row([ft.Container(self._ddRuolo,width=250),
                                           ft.Container(self._btnCrea,width=250)],
                                          alignment=ft.MainAxisAlignment.CENTER))
        self._page.controls.append(ft.Row([ft.Container(self._btnConnessi, width=250)],
                                          alignment=ft.MainAxisAlignment.CENTER))

        #row 2
        self._textID = ft.TextField(label = "Artista ID", border_color="orange",disabled=True)
        self._btnCercaPercorso = ft.ElevatedButton(text="Cerca Oggetti", on_click=self._controller.handleCercaPercorso, bgcolor="orange",
                                                  color="white", disabled=True)
        self._page.controls.append(ft.Row([ft.Container(self._textID, width =250),
                                                        ft.Container(self._btnCercaPercorso,width = 250)],
                                          alignment=ft.MainAxisAlignment.CENTER))
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()


    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()
    @property
    def controller(self):
        return self._controller
    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller
    def update_page(self):
        self._page.update()
