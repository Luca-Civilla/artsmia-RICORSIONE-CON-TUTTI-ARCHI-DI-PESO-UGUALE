import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ruolo = None

    def fillDD(self):
        ruoli = self._model.ruoli
        for r in ruoli:
            self._view._ddRuolo.options.append(ft.dropdown.Option(text=r,data=r, on_click=self.readDDRuolo))

    def readDDRuolo(self,e):
        if e.control.data is None:
            self._ruolo= None
        else:
            self._ruolo= e.control.data
            print(f"readDD chiamato {self._ruolo}")

    def handleAnalizzaOggetti(self, e):
        if self._ruolo == None:
            self._view.create_alert("SELEZIONARE UN RUOLO")
            return
        self._model.buildGraph(self._ruolo)
        nodi, archi = self._model.graphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"GRAFO CREATO CORRETTAMENTE CON {nodi} NODI E {archi} ARCHI "))
        self._view._btnConnessi.disabled = False
        self._view._textID.disabled=False
        self._view._btnCercaPercorso.disabled = False
        self._view.update_page()


    def handleCompConnessa(self,e):
        lista = self._model.Connessi()
        for l in lista:
            self._view.txt_result.controls.append(ft.Text(f"{l[0].name}<--->{l[1].name}  peso -->{l[2]["weight"]}"))
        self._view.update_page()



    def handleCercaPercorso(self,e):
        try:
            int(self._view._textID.value)
        except ValueError:
            self._view.create_alert("ERRORE, VALORE NON NUMERICO")
            return

        id =  int(self._view._textID.value)
        check = False
        nodo = None
        for e in self._model._grafo.nodes:
            if e.artist_id == id:
                check = True
                nodo= e
        if check == False:
            return self._view.create_alert("L'ARTISTA NON E' PRESENTE NEL GRAFO")

        percorso,score,peso = self._model.getPath(nodo)
        self._view.txt_result.controls.append(ft.Text(f"IL PERCORSO E' LUNGO {score} CON NUMERO DI MOSTRE -->{peso}(peso arco) E CONTIENE: "))
        for ele in percorso:
            self._view.txt_result.controls.append(ft.Text(ele.name))

        self._view.update_page()

