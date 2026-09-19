from flask import Flask, render_template, abort

app = Flask(__name__)

# Liste semplici gestite da Python
PROGETTI = [
    {"id": "amadriadi", "titolo": "A M A D R I A D I", "nota_it": "Performance", "nota_en": "Performance"},
    {"id": "cuma", "titolo": "C U M A", "nota_it": "Performance / Video Art", "nota_en": "Performance / Video Art"},
    {"id": "citerone", "titolo": "C I T E R O N E", "nota_it": "Performance / Short Film", "nota_en": "Performance / Short Film"},
    {"id": "atteone", "titolo": "A T T E O N E", "nota_it": "Debutto 2027", "nota_en": "Premiere 2027"},
    {"id": "salmace", "titolo": "S A L M A C E", "nota_it": "work in progress", "nota_en": "work in progress"}
]

@app.route('/')
def home_it():
    return render_template('index.html', lang='it', opere=PROGETTI)

@app.route('/en')
def home_en():
    return render_template('index.html', lang='en', opere=PROGETTI)

@app.route('/progetto/<string:progetto_id>')
def dettaglio_progetto(progetto_id):
    progetto_selezionato = next((p for p in PROGETTI if p["id"] == progetto_id), None)
    if progetto_selezionato is None:
        abort(404)
    return render_template('progetto.html', opera=progetto_selezionato, lang='it')

if __name__ == '__main__':
    app.run(debug=True)
