kuukausi = input("anna kuukausi lyhenne: ")


monthConversions = {
    "Tam": "Tammikuu",
    "Hel": "Helmikuu",
    "Maa": "Maaliskuu",
}

print(monthConversions.get(kuukausi))