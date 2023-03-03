import requests, json

def get_job(designation, location, exp) :
    payload = json.dumps({
        'designation': designation,
        'location': location,
        'exp': exp
    })

    response = requests.get(f'http://127.0.0.1:8000/jobs', data = payload)
    return response.json()


designation = input('Enter Position : ').lower()
location = input('Enter location : ').lower()
exp = int(input('Enter experience : '))

print(get_job(designation, location, exp))
