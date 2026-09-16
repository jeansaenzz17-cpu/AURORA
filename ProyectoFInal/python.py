from flask import Flask

# Crea la instancia de la aplicación
app = Flask(__name__)


# Define la ruta principal
@app.route("/")
def inicio():
  return "¡Hola mundo con Flask!"


# Ejecuta el servidor en modo local
if __name__ == "__main__":
  app.run(debug=True)
