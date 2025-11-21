# Sundheds-API – Python / Flask / APIFlask / YAML / Plotly

Dette repository indeholder et lille sundheds-API udviklet i tre dele, som viser en progression fra simpel datahåndtering til et komplet API med autentifikation og visualisering.


App oversigt

## del1_yaml/
Et simpelt Python-script som:
- læser og skriver data i `patients.yml`
- opretter nye patienter

## del2_API/
En tidlig version af et API, der:
- bruger APIFlask
- kan modtage JSON-data via POST
- opretter patienter i YAML
- returnerer patientdata via GET

## del3_token/
En mere komplet version af sundheds-API’et, som:
- bruger APIFlask til endpoints
- bruger JWT token-auth (Authlib)
- læser og skriver til `patients.yml`
- visualiserer patienternes alder med Plotly

Denne mappe indeholder projektets mest funktionelle udgave.

# Sådan kommer man i gang (del3_token)

cd del3_token
pip install -r requirements.txt
apiflask run --debug


