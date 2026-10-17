import sys
from tkinter import *
import time

# French weekday names
jours = [
    "Lundi", "Mardi", "Mercredi", "Jeudi",
    "Vendredi", "Samedi", "Dimanche"
]

def tick():
    try:
        t = time.time()
        local_time = time.localtime(t)

        # Date et heure
        date_string = time.strftime("%Y-%m-%d", local_time)
        weekday = jours[local_time.tm_wday]
        time_string = time.strftime("%H:%M:%S", local_time)
        milliseconds = int((t - int(t)) * 1000)

        # Informations supplémentaires
        timezone_name = time.strftime("%Z", local_time)
        day_of_year = time.strftime("%j", local_time)
        week_number = time.strftime("%U", local_time)

        # Affichage en français
        full_string = (
            f"Date : {date_string} ({weekday})\n"
            f"Heure : {time_string}.{milliseconds:03d}\n"
            f"Fuseau horaire : {timezone_name}\n"
            f"Jour de l'année : {day_of_year}\n"
            f"Numéro de semaine : {week_number}"
        )

        clock.config(text=full_string)

        # Actualisation toutes les millisecondes
        clock.after(1, tick)

    except Exception as e:
        clock.config(text=f"Erreur : {e}")


# Création de la fenêtre principale
root = Tk()
root.title("Horloge - Informations complètes")

# Style de l'horloge
clock = Label(
    root,
    font=("Courier", 20, "bold"),
    bg="#00ffae",
    fg="black",
    justify="left",
    anchor="w"
)
clock.grid(row=0, column=0, padx=20, pady=20)

# Démarrage de l'horloge
tick()

# Boucle principale
root.mainloop()
