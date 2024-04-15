import zipfile

mi_zip = zipfile.ZipFile('miTextoAComprimido.zip', 'w')
mi_zip.write('resources/dia9_ProgramaUnBuscadorDeNumerosDeSerie/mi_texto_A.txt')
mi_zip.write('resources/dia9_ProgramaUnBuscadorDeNumerosDeSerie/mi_texto_B.txt')
mi_zip.close()