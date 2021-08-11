import re
import os
import shutil

mainFolder = r'/home/michael/Downloads/rename'

def renameFile(file):

  fileName, fileExtension = os.path.splitext(file)
  fileNameNumbers = re.findall(r'\d+', fileName)[0]

  if fileExtension == '.mkv':
    return f'{fileNameNumbers} - BAIXAR MP4{fileExtension}'

  return f'{fileNameNumbers} - HunterXHunterSeiko - RaitoKira666{fileExtension}'

def fileLoop(root, dirs, files):
  for file in files:

    oldFileFullPath = os.path.join(root, file)
    newFileFullPath = os.path.join(root, renameFile(file))
    print(f'Renomeando arquivo {file} para {renameFile(file)}')
    # shutil.move(oldFileFullPath, newFileFullPath)

def mainLoop():
  for root, dirs, files in os.walk(mainFolder):
    fileLoop(root, dirs, files)


if __name__ == '__main__':
  mainLoop()