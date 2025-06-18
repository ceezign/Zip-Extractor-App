import FreeSimpleGUI as sg
from  zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("select archive")
input_label= sg.Input()
button1 = sg.FileBrowse("choose", key="archive")

label2 = sg.Text("select dest dir")
input_label2= sg.Input()
button2 = sg.FolderBrowse("choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="Green")

window = sg.Window("Archive Extractor", layout=[[label1, input_label, button1],
                                                [label2, input_label2, button2],
                                                [extract_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed")

window.close()