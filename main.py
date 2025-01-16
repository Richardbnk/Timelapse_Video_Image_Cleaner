import os
import shutil

rootdir = r"C:\..." # folder of the image repositorie

destination = r"C:\..." # folder destination for the correct images

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        origin = os.path.join(subdir, file)

        ano = file[16:20]
        mes = file[20:22]
        dia = file[22:24]
        hora = file[24:26]
        minuto = file[26:28]
        destination_file = os.path.join(
            destination, f"{ano}-{mes}-{dia}_{hora}-{minuto}.jpg"
        )

        print(destination_file)

        if file == "Thumbs.db":
            continue

        if hora in ("12, 13, 14, 15"):  # and int(minuto) <= 20: # get only files from the hours 12, 13, 14 and 15 (only daytime images)
            shutil.copyfile(origin, destination_file)

num_file = 7450

minutos_video = (num_file / 60) / 60
