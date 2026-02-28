import os
import shutil

def copy_source(src="static", dest="public", clean=True):
    if clean and os.path.exists(dest):
        shutil.rmtree(dest)
    if os.path.isdir(src):
        os.makedirs(dest, exist_ok=True)
        for entry in os.listdir(src):
            src_path = os.path.join(src, entry)
            dest_path = os.path.join(dest, entry)
            copy_source(src_path, dest_path, clean=False)
    else:
        shutil.copy2(src, dest)
        print(f'Copied: {src} > {dest}')