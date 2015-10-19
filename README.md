# TODOList "http://toodolist.herokuapp.com/"

**"Crear token con oauth2_provider a un usuario"**
```
curl -X POST -d "grant_type=password&username=admin&password=admin" -u"WGOKrZnQLLAXUXbWk2kaIdWVAz6DlOyayYTL7dv5:uwYd1M3h7DmhB4zYh27ilUM791XtdFkzh5W6krm8flzoJWomgEmTfeGMAm5VtO8hdEE9BEUIWnIuY4bvZNFJKB1uetdBhiDzJnDaGw1ipddV7HyV21J8chYFhZ38LBIi" http://toodolist.herokuapp.com/o/token/
````

nos retorna:
```{"access_token": "H0nCU0lVin5fV706MOm6qwMAmgDgG8", "scope": "read groups write", "refresh_token": "ogyypdrEoVINi3aECkgtbvGcnGHl5d", "token_type": "Bearer", "expires_in": 36000}```

"access_token" es la llave de acceso a nuestra app

**"Crear un nuevo usuario"**
```
curl -H "Authorization: Bearer H0nCU0lVin5fV706MOm6qwMAmgDgG8" -X POST -d"username=rulz&password=1234" http://toodolist.herokuapp.com/api/users/
```

**"Listado de usuarios"**
```
curl -H "Authorization: Bearer H0nCU0lVin5fV706MOm6qwMAmgDgG8" http://toodolist.herokuapp.com/api/users/
```
**"Editar un usuario"**
```
curl -H "Authorization: Bearer H0nCU0lVin5fV706MOm6qwMAmgDgG8" -X PUT -d"username=rulz&password=12345" http://toodolist.herokuapp.com/api/users/2/
```

**"Detalle de un usuario"**
```
curl -H "Authorization: Bearer H0nCU0lVin5fV706MOm6qwMAmgDgG8" http://toodolist.herokuapp.com/api/users/2/
```


**"Listado de Tareas"**
```
curl -H "Authorization: Bearer H0nCU0lVin5fV706MOm6qwMAmgDgG8" http://toodolist.herokuapp.com/api/tasks/
```

**"Crear una nueva tarea"**
```
curl -H "Authorization: Bearer H0nCU0lVin5fV706MOm6qwMAmgDgG8" -X POST -d"name=tarea1&description=creando tarea" http://toodolist.herokuapp.com/api/tasks/
```

**"Detalle de una tarea"**
```
curl -H "Authorization: Bearer H0nCU0lVin5fV706MOm6qwMAmgDgG8" http://toodolist.herokuapp.com/api/tasks/1/
```

**"Editar una tarea"**
```
curl -H "Authorization: Bearer H0nCU0lVin5fV706MOm6qwMAmgDgG8" -X PUT -d"name=tarea1&done=True&assigned_to=http://toodolist.herokuapp.com/api/users/1/" http://toodolist.herokuapp.com/api/tasks/1/
```


**"Usando librería requests de Python"**
```
import requests
url_users = 'http://toodolist.herokuapp.com/api/users/'
url_tasks = 'http://toodolist.herokuapp.com/api/tasks/'

headers = {'Authorization': 'Bearer %(token)s' % {'token': 'H0nCU0lVin5fV706MOm6qwMAmgDgG8'}}
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
data = {'name': 'tarea nueva 2', 'description':'estamos creando la tarea'}
response = requests.post(url_tasks, headers=headers, data=data)
response.json()
```


**"Editar una tarea"**
```
data = {'assigned_to':'http://toodolist.herokuapp.com/api/users/1/', 'name':'tarea nueva 2', 'description':'estamos creando la tarea'}
response = requests.put(url_tasks+'2/', headers=headers, data=data)
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
response = requests.put(url_users+'1/', headers=headers, data=data)
response.json()
```
