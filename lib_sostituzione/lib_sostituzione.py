


###########################################################################################################
#  /$$    /$$                              /$$                                      /$$$$$$      /$$$$$$  #
# | $$   | $$                             |__/                                     /$$$_  $$    /$$__  $$ #
# | $$   | $$ /$$$$$$   /$$$$$$   /$$$$$$$ /$$  /$$$$$$  /$$$$$$$   /$$$$$$       | $$$$\ $$   |__/  \ $$ #
# |  $$ / $$//$$__  $$ /$$__  $$ /$$_____/| $$ /$$__  $$| $$__  $$ /$$__  $$      | $$ $$ $$     /$$$$$$/ #
#  \  $$ $$/| $$$$$$$$| $$  \__/|  $$$$$$ | $$| $$  \ $$| $$  \ $$| $$$$$$$$      | $$\ $$$$    /$$____/  #
#   \  $$$/ | $$_____/| $$       \____  $$| $$| $$  | $$| $$  | $$| $$_____/      | $$ \ $$$   | $$       #
#    \  $/  |  $$$$$$$| $$       /$$$$$$$/| $$|  $$$$$$/| $$  | $$|  $$$$$$$      |  $$$$$$//$$| $$$$$$$$ #
#     \_/    \_______/|__/      |_______/ |__/ \______/ |__/  |__/ \_______/       \______/|__/|________/ #
###########################################################################################################



def sostituzione(file1, file2, sep1=",", sep2="."):
    """
    Sostituisce due simboli nei documenti
        file1 (str): Nome del file da cui prendere i numeri
        file2 (str): Nome del file dove scrivere il testo convertito
        sep1 (str): Simbolo da sostituire -> Default: ","
        sep2 (str): Nuovo simbolo -> Default: "."
    """
    reading_file = open(file1, "r")
    writing_file = open(file2, "w")
    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace(sep1, sep2)
        new_file_content += new_line +"\n"
    reading_file.close()
    writing_file.write(new_file_content)
    writing_file.close()
