# Overview

Basic application for changing video sizes with an extremely simple GUI.

# Before Use:

You have to change line 37 in resize.py of the moviepy package from:
```py
resized_pil = pilim.resize(newsize[::-1], Image.ANTIALIAS)
```

to:
```py
resized_pil = pilim.resize(newsize[::-1], Image.LANCZOS)
``` 

and it will work just fine. `ANTIALIAS is depricated and moviepy has not changed their code yet.