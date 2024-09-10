'''
🌿 FEUILLE-UNLINKER
(2024 FeuilleDev team)
'''
import os
import re


def unlink(input_file,output_folder):
    '''Thank to GPT for the regex and some help'''
    print("[LEGAL WARNING] : Unlinking a app is considered a copyright infringement (if the author copyrigthed the app) and can lead to legal consequences. Use at your own risk.")
    print("And this can take some time...")
    input("Press enter to continue")
    os.makedirs(output_folder, exist_ok=True)


    with open(input_file, "r") as file:
        content_f = file.read()

    pattern = re.compile(r"-- === (.*?) ===\n(.*?)\n", re.DOTALL)

    seen_files = set()
    i = 0

    for match in pattern.finditer(content_f):
        name = match.group(1)
        content_f = match.group(2)

        if name not in seen_files:
            with open(f"{output_folder}/{i}.lua", "w") as tempd:
                tempd.write(content_f)
            seen_files.add(name)  
            i += 1
    print(f"DONE : Processed {i} unique files.")
print("Feuille Unlinker")
print("[WARNING] : This is not stable yet.")
x=input("File main path : ")
e=input("Output folder : ")
unlink(x,e)
