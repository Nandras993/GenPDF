import PySimpleGUI as sg
import functions

sg.theme_background_color("#d50000")
sg.theme_text_color("#ffffff")
sg.theme_text_element_background_color("#d50000")
sg.theme_button_color("#d50000")

welcome = sg.Text("Welcome to GenPDF! Generate a PDF file quickly with me!",
                  font="Times, 14", pad=((0, 0), (0, 70)))
name_text = sg.Text("Name:", font="Times")
name = sg.Input(font="Times", key="name", pad=((35, 0), (0, 0)),
         tooltip="This will be the name of your pdf file.")
header_text = sg.Text("Header:", font="Times")
header = sg.Input(font="Times", key="header", pad=((27, 0), (0, 0)),
         tooltip="This will be written on your pdf pages at the top left. Leave it blank if you don't need a header.")
footer_text = sg.Text("Footer:", font="Times")
footer = sg.Input(font="Times", key="footer", pad=((31, 0), (0, 0)),
         tooltip="This will be written on your pdf page at the bottom right. Leave it blank if you don't need a footer.")
pages_text = sg.Text("Pages:", font="Times")
pages = sg.Input(font="Times", key="pages", pad=((36, 0), (0, 0)),
         tooltip="The number of pages your PDF will have.")
line = sg.Checkbox("Should the page contain lines?", font="Times", key="line",
            default=False, background_color="#d50000", pad=((0, 0), (0, 0)),
            tooltip="If you want your pages to contain lines for writting on them, check this box.")
create = sg.Button("Create PDF", font="Times, 12", size=(20, 1), key="create",
                   enable_events=True, pad=((0, 0), (15, 15)), border_width=3)

folder_input = sg.Input(key="folder", font="Times", pad=((10, 0), (0, 0)))
folder = sg.FolderBrowse("Destination", font="Times", key="folder_browse",
                         tooltip="Choose the destination for your PDF.",
                         pad=((0, 0), (0, 0)))

page_value_error = sg.Text("", font="Times, 14", key="value_error", pad=((0, 0), (10, 10)) )

col_left = sg.Image("3_2.png")
col_middle = sg.Column(layout=[[welcome], [name_text, name], [header_text, header], [footer_text, footer], [pages_text, pages], [folder, folder_input], [page_value_error], [line], [create]])
col_right = sg.Column(layout=[[]])

window = sg.Window("GenPDF", size=(810, 400),
                   layout=[[col_left, col_middle, col_right]])

while True:
    try:
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
            window["value_error"].update(value="")
        else:
            functions.create_pdf_line(header, footer, pages, name, folder)
            window["name"].update(value="")
            window["header"].update(value="")
            window["footer"].update(value="")
            window["folder"].update(value="")
            window["pages"].update(value="")
            window["value_error"].update(value="")
    except ValueError:
        window["value_error"].update(value="Please, enter a valid number for the amount of pages.")

    except FileNotFoundError:
        window["value_error"].update(value="Please, enter a valid destination path for your file.")

window.close()