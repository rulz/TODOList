# TODOList

**"Crear token con oauth2_provider a un usuario"**
```
curl -X POST -d "grant_type=password&username=admin&password=admin" -u"bRLkQJGH9JlwMGaEmknrS9bRWWfk5e2eXba1J9bp:zpRoLwOIOM2Epfqr3tleA0A4c80YDZIpqvcizASrYpe0KyV27teCPMHfeA0xB2Ht6PgxcyvDPHcqK1QgoAwhcDi2Q9yucp4Z0OADn5S2GKY6br62Y3yDrwgsn7eJ1kow" http://localhost:8000/o/token/
````

nos retorna:
```{"access_token": "HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d", "token_type": "Bearer", "expires_in": 36000, "refresh_token": "psbMGcIEHVPuNvV37tXV8iMx1Vn8rj", "scope": "read write"}```

"access_token" es la llave de acceso a nuestra app

**"Crear un nuevo usuario"**
```
curl -H "Authorization: Bearer HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d" -X POST -d"username=rulz&password=1234" http://localhost:8000/api/users/
```

**"Listado de usuarios"**
```
curl -H "Authorization: Bearer HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d" http://localhost:8000/api/users/
```
**"Editar un usuario"**
```
curl -H "Authorization: Bearer HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d" -X PUT -d"name=rulz&password=12345" http://localhost:8000/api/users/12/
```

**"Detalle de un usuario"**
```
curl -H "Authorization: Bearer HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d" http://localhost:8000/api/users/1/
```


**"Listado de Tareas"**
```
curl -H "Authorization: Bearer HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d" http://localhost:8000/api/tasks/
```

**"Crear una nueva tarea"**
```
curl -H "Authorization: Bearer HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d" -X POST -d"name=tarea1&description=creando tarea" http://localhost:8000/api/tasks/
```

**"Detalle de una tarea"**
```
curl -H "Authorization: Bearer HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d" http://localhost:8000/api/tasks/1/
```

**"Editar una tarea"**
```
curl -H "Authorization: Bearer HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d" -X PUT -d"name=tarea1&done=True&assigned_to=http://localhost:8000/api/users/13/" http://localhost:8000/api/tasks/11/
```


**"Usando librería requests de Python"**
```
import requests
url_users = 'http://localhost:8000/api/users/'
url_tasks = 'http://localhost:8000/api/tasks/'

headers = {'Authorization': 'Bearer %(token)s' % {'token': 'HwCdBUa1BkQHQFJVM3TBtgwZ41BX1d'}}
```


**"Listado de tareas"**
```
response = requests.get(url_tasks, headers=headers)
response.json()
```

**"Detalle de una tarea""** 
```
response = requests.get(url_tasks+'1/', headers=headers)
response.json()
```

**"Crear una nueva tarea"**
```
data = {'name': 'tarea nueva 1', 'description':'estamos creando la tarea'}
response = requests.post(url_tasks, headers=headers, data=data)
response.json()
```


**"Editar una tarea"**
```
data = {'assigned_to':'http://127.0.0.1:8000/api/users/1/', 'name':'tareassss', 'description':'dasss'}
response = requests.post(url_tasks+'1/', headers=headers, data=data)
response.json()
```

**"Crear un nuevo usuario"**
```
data = {'email': 'raulsetron@gmail.com', 'password': '12345', 'username': 'rulz'}
response = requests.post(url_users, headers=headers, data=data)
response.json()
```

**"Detalle de un usuario""** 
```
response = requests.get(url_users+'1/', headers=headers)
response.json()
```

**"Editar un usuario"**
```
data = {'password': '12345', 'username': 'rulz'}
response = requests.post(url_users+'1/', headers=headers, data=data)
response.json()
```
