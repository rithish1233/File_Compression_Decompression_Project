import PySimpleGUI as sg
from zip_creator import make_archive, extract_archive
import os

# Set theme
sg.theme("LightPurple")

# Create GUI layout
layout = [
    [sg.Text("Select files to compress: "), sg.Input(), sg.FilesBrowse("Choose Files", key="files")],
    [sg.Text("Select a folder to compress: "), sg.Input(), sg.FolderBrowse("Choose Folder", key="folder")],
    [sg.Text("Select destination folder: "), sg.Input(), sg.FolderBrowse("Choose", key="dest_folder")],
    [sg.Button("Compress")],
    [sg.Text("Select ZIP file to extract: "), sg.Input(), sg.FileBrowse("Choose", key="zip_file")],
    [sg.Text("Select extraction folder: "), sg.Input(), sg.FolderBrowse("Choose", key="extract_folder")],
    [sg.Button("Extract")],
    [sg.Text(key="output", text_color="green")],
    [sg.Button("Exit")]
]

# Create the main window
window = sg.Window("File Compressor & Extractor", layout)

# Event loop
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Compress":
        filepaths = values['files'].split(";") if values['files'] else []
        folder = values['folder']
        dest_folder = values['dest_folder']

        sources = filepaths  
        if folder and os.path.exists(folder):  
            sources.append(folder)  

        if sources and dest_folder:
            make_archive(sources, dest_folder)
            window["output"].update("Compression completed!")
        else:
            window["output"].update("Please select files or a folder and a destination folder.", text_color="red")
    elif event == "Extract":
        zip_path = values['zip_file']
        extract_folder = values['extract_folder']
        if zip_path and extract_folder:
            extract_archive(zip_path, extract_folder)
            window["output"].update("Extraction completed!")
        else:
            window["output"].update("Please select a ZIP file and an extraction folder.", text_color="red")

window.close()
