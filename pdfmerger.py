import PySimpleGUI as sg
import PyPDF2

sg.theme('LightBlue2')

layout = [
    [sg.Text('Select two PDF files to merge')],
    [sg.Input(key='file1', enable_events=True, visible=False), sg.FileBrowse('Browse', file_types=(('PDF Files', '*.pdf'),))],
    [sg.Input(key='file2', enable_events=True, visible=False), sg.FileBrowse('Browse', file_types=(('PDF Files', '*.pdf'),))],
    [sg.Button('Merge', disabled=True)]
]

window = sg.Window('PDF Merger', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if values['file1'] and values['file2']:
        window['Merge'].update(disabled=False)
    else:
        window['Merge'].update(disabled=True)

    if event == 'Merge':
        file1 = values['file1']
        file2 = values['file2']
        output_file = sg.popup_get_file('Save As', save_as=True, file_types=(('PDF Files', '*.pdf'),))

        if output_file:
            with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(output_file, 'wb') as f:
                pdf1 = PyPDF2.PdfFileReader(f1)
                pdf2 = PyPDF2.PdfFileReader(f2)
                merger = PyPDF2.PdfFileMerger()
                merger.append(pdf1)
                merger.append(pdf2)
                merger.write(f)

            sg.popup('PDF files merged successfully!', title='Success')

window.close()
