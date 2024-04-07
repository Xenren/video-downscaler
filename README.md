# Overview

Basic application built for personal use for changing video sizes with an extremely simple GUI.

# Uses:

The `./app` contains two files
1. `app.py` - the primary application that loops through a pre-defined set of sizes
    - was created for use by a non-coder; thus I didn't want the user to have to consider pixel sizes.
    - simply edit the `target_width` array to add sizes
2. `custom_downscaler.py` - secondary version that resizes a single video to a specfied pixel height

    *NOTE: the code for this version needs to be updated to match `app.py` but it is fully functional.*

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

# To Build Executable:

Make sure you have pyinstaller
```sh
pip install pyinstaller
```

Navigate to the `./app` directory and run:

```sh
pyinstaller --onefile --windowed downscaler.py
```

***NOTE: The executable file will only work on the same operating system on which it was created.***