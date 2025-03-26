from flask import Flask, render_template, request

app = Flask(__name__)

# Data om fjelloverganger
fjelloverganger = [
    {'navn': 'Gaustatoppen', 'status': 'Åpen', 'sted': 'Telemark'},
    {'navn': 'Haukeli', 'status': 'Stengt', 'sted': 'Vestland'},
    {'navn': 'Dovrefjell', 'status': 'Åpen', 'sted': 'Trøndelag'},
    {'navn': 'Strynefjell', 'status': 'Stengt', 'sted': 'Vestland'},
    {'navn': 'Rondane', 'status': 'Åpen', 'sted': 'Innlandet'},
    {'navn': 'Hardangervidda', 'status': 'Stengt', 'sted': 'Vestland'},
    {'navn': 'Valdresflya', 'status': 'Åpen', 'sted': 'Innlandet'},
    {'navn': 'Filefjell', 'status': 'Åpen', 'sted': 'Viken'},
    {'navn': 'Kjerringåsen', 'status': 'Stengt', 'sted': 'Møre og Romsdal'},
    {'navn': 'Sognefjellet', 'status': 'Åpen', 'sted': 'Vestland'},
    {'navn': 'Fv. 52 - Aurland', 'status': 'Stengt', 'sted': 'Vestland'},
    {'navn': 'Trollheimen', 'status': 'Åpen', 'sted': 'Trøndelag'},
    {'navn': 'Setesdal', 'status': 'Åpen', 'sted': 'Agder'},
    {'navn': 'Bergensbanen', 'status': 'Åpen', 'sted': 'Viken'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    # Hent søkespørringen fra URL-en (standard til tom streng hvis ingen søkespørring er gitt)
    search_query = request.args.get('search', '').lower()  # Henter søk parameteren fra URL
    
    # Filtrer fjellovergangene basert på søkespørringen
    filtered_fjelloverganger = [fjell for fjell in fjelloverganger if search_query in fjell['navn'].lower() or search_query in fjell['sted'].lower()]
    
    # Returnerer den filtrerte listen og sender søkespørringen tilbake til HTML-siden
    return render_template('index.html', fjelloverganger=filtered_fjelloverganger, search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True)