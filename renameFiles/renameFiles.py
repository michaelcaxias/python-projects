import re
import os
import shutil

mainFolder = r'/home/michael/Downloads/rename' #Pasta em que a ação será feita.

def renameFile(file):

  fileName, fileExtension = os.path.splitext(file) #Puxa o nome do arquivo e a extensão do arquivo(.mp4)
  fileNameNumbers = re.findall(r'\d+', fileName)[0] #Retorna apenas os numeros dos arquivos individualmente

  if fileExtension == '.mkv':
    return f'{fileNameNumbers} - BAIXAR MP4{fileExtension}'

  return f'{fileNameNumbers} - HunterXHunterSeiko - RaitoKira666{fileExtension}' #Adicionar o nome dos arquivos aqui

def fileLoop(root, dirs, files):
  for file in files:
    originFolder = renameFile(file) 
    oldFileFullPath = os.path.join(root, file)
    newFileFullPath = os.path.join(root, originFolder)
    print(f'Renomeando arquivo {file} para {originFolder}')
    shutil.move(oldFileFullPath, newFileFullPath) #!!!!O shutil.move renomeará os arquivos

def mainLoop():
  for root, dirs, files in os.walk(mainFolder):
    fileLoop(root, dirs, files)


if __name__ == '__main__':
  mainLoop()