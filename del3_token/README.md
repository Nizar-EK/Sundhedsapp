# Sundhedsapp
## Funktioner

- Tilføj patienter til YAML-fil
- Hent alle patientdata (kræver token)
- Generer JWT token via `/token/<id>`
- Beskyttede endpoints med Bearer-token
- Visualiser patienternes alder i et interaktivt Plotly-bar chart
- Automatisk API-dokumentation via `/docs`


## Sådan kommer man i gang

Installer dependencies:

pip install -r requirements.txt


Start API'et:

apiflask run --debug

Serveren kører nu på:
http://127.0.0.1:5000

APIFlask genererer automatisk interaktiv API-dokumentation og kan ses her:
http://127.0.0.1:5000/docs

- se alle API-endpoints
- teste API-kald direkte i browseren via 'Try it out'

Visualisering af data:
http://127.0.0.1:5000/bar

- indlæser data fra patients.yml
- genererer en graf baseret på alder
- viser grafen via templates/bar.html
