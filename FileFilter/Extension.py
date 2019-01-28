extension = {
"audio":["mp3","wav"],
"video":["mp4","mkv"],
"data":["doc","docx","pdf","ppt","pptx","txt"]
}



def checkExtension(file):
    try:
        fext = file.split(".")[1]
        for ext in extension:
            for keys in extension.get(ext):
                if keys == fext:
                    status = ext
                    return status
    except:
        pass