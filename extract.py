import zipfile

local_zip = './tabular-playground-series-nov-2022.zip'
zip_ref   = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('./input/')
zip_ref.close()
