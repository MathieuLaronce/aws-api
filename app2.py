import mysql.connector

try:
    connection = mysql.connector.connect(
        host="mysql-1.c1w828ag46u3.eu-north-1.rds.amazonaws.com",
        port=3306,
        user="admin",
        password="isen2025",
        database="cloud"
    )
    print("Connexion réussie !")
except Exception as e:
    print("Erreur connexion :", e)
