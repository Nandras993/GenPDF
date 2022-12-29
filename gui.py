import PySimpleGUI as sg
import functions

sg.theme_background_color("#d50000")
sg.theme_text_color("#ffffff")
sg.theme_text_element_background_color("#d50000")
sg.theme_button_color("#d50000")

welcome = sg.Text("Welcome to GenPDF! Generate a PDF file quickly with me!",
                  font="Times, 14", pad=((0, 0), (5, 5)))
name_text = sg.Text("Name:", font="Times")
name = sg.Input(font="Times", key="name",
         tooltip="This will be the name of your pdf file.")
header_text = sg.Text("Header:", font="Times")
header = sg.Input(font="Times", key="header",
         tooltip="This will be written on your pdf pages at the top left. Leave it blank if you don't need a header.")
footer_text = sg.Text("Footer:", font="Times")
footer = sg.Input(font="Times", key="footer",
         tooltip="This will be written on your pdf page at the bottom right. Leave it blank if you don't need a footer.")
pages_text = sg.Text("Number of pages:", font="Times")
pages = sg.Input(font="Times", key="pages",
         tooltip="The number of pages your PDF will have.")
line = sg.Checkbox("Should the page contain lines?", font="Times", key="line",
            default=False, background_color="#d50000",
            tooltip="If you want your pages to contain lines for writting on them, check this box.")
create = sg.Button("Create PDF", font="Times, 12", size=(20, 1), key="create",
                   enable_events=True, pad=((0, 0), (15, 15)), border_width=3)

folder_input = sg.Input(key="folder", font="Times", pad=((53, 0), (30, 30)))
folder = sg.FolderBrowse("Destination", font="Times", key="folder_browse",
                         tooltip="Choose the destination for your PDF.")

col_left = sg.Image("")
col_middle = sg.Column(layout=[[name_text], [header_text], [footer_text], [pages_text]])
col_right = sg.Column(layout=[[name], [header], [footer], [pages]])

window = sg.Window("GenPDF", layout=[[welcome], [col_middle, col_right], [folder, folder_input], [line], [create]])

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    folder = values["folder"]
    name = values["name"]
    pages = int(values["pages"])
    footer = values["footer"]
    header = values["header"]
    line = values["line"]

    if values["line"] == False:
        functions.create_pdf(header, footer, pages, name, folder)
        window["name"].update(value="")
        window["header"].update(value="")
        window["footer"].update(value="")
        window["folder"].update(value="")
        window["pages"].update(value="")
    else:
        functions.create_pdf_line(header, footer, pages, name, folder)
        window["name"].update(value="")
        window["header"].update(value="")
        window["footer"].update(value="")
        window["folder"].update(value="")
        window["pages"].update(value="")


window.close()