# Imports
import os
import subprocess
import pathlib

# FFMPEG Directory
ffmpegPath = pathlib.Path('Your FFMPEG Installation here') # Specify your ffmpeg installation here

dirIn=input("Enter the folder name with the files you want to convert : ") # Said in the window
# dirIn="toConvert"
print(dirIn)
inExt=input("Enter the files extension : ") # Said in the window - When it appears make sure to enter just one file extension
# inExt="mp3"
print(inExt)

dirOut=input("Enter the output folder : ") # Said in the window
# dirOut="converted"
print(dirOut)
outExt=input("Enter the new file extension : ") # Said in the window
# outExt="ogg"
print(outExt)

inputDir = 'F:/PythonConverter/'+dirIn+'/'
print(inputDir)

outputPath = 'F:/PythonConverter/'+dirOut+'/'
print(outputPath)

flist = []
for p in pathlib.Path(str(inputDir)).glob("*." + inExt): # Convert all files and upload them
    if p.is_file():
        theFileName = '.'.join((p.name).split('.')[:-1])
        print(theFileName)
        print(str(p))
        print(str(ffmpegPath))
        print(str(theFileName))
        print(str(outExt))
        print('"'+str(ffmpegPath) + '" -i "' + str(p) + '" "' + str(outputPath) + theFileName + '.' + outExt + '"')
        subprocess.check_output('"'+str(ffmpegPath) + '" -i "' + str(p) + '" "' + str(outputPath) + theFileName + '.' + outExt + '"', encoding = 'utf8')
        flist.append(p)
