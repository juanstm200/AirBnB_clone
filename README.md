<p align="center"><img src="https://camo.githubusercontent.com/7e9956678cbe5ec1d712dde039115910e2002db17bc7ff7e7d1638915c500827/68747470733a2f2f692e6962622e636f2f324e42596259762f434c4f4e312e706e67" width="676" height="285"/></p>

# AirBnB clone - The console

In this project of Airbnb_clone seeks as a first instance to create a console that will cover fundamental concepts of programming in Python such as handling classes, objects, handling JSON files. The objective of the project is to deploy a console with its own commands where eventually you can deploy a web server that will be a copy of the Airbnb website this as a segment project for Holberton School


# Console
The console AirBnB Clone is a line interpreter that allows the user, interact directly from a database <file.json>, editing, creating and removing objects, attributtes and values from the own object

Usage This console can be run both interactively and non-interactively. For a better image of how to do this, here is a example of both methods

**Non-interactive mode**
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
**Interactive mode**
```
./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)help quit
Quit command to exit the program

(hbnb)quit
```

# Console commands

The principle execution file has already all permission needed, with a simple execution in linux environment "./", the console will start
```
ubuntu:~/AirBnB$ ./console.py
```

**create**

Creates a new base BaseModel, or any kind of his instances: City, Amenity, Place, Review, State, User And prints on screen his unique id (uuid4) for a future reffer ; and at the same time, creates a file <file.json> where we could store, manage and save all instances created in the process. ie: "$ create BaseModel"
```
(hbnb)create BaseModel
a3e2850a-41c9-490b-8c26-af9f65d64fff
```

**show**

Prints the string representation of an instance based on the class name and id "$ show BaseModel a3e2850a-41c9-490b-8c26-af9f65d64fff"
```
(hbnb)show BaseModel a3e2850a-41c9-490b-8c26-af9f65d64fff
[BaseModel] (a3e2850a-41c9-490b-8c26-af9f65d64fff) {'id': 'a3e2850a-41c9-490b-8c26-af9f65d64fff', 'created_at': datetime.datetime(2021, 7, 1, 6, 57, 25, 959773), 'updated_at': datetime.datetime(2021, 7, 1, 6, 57, 25, 959998)}
```

**all**

Prints all string representation of all instances based or not on the class name. ie: "$ all BaseModel" or "$ all"
```
(hbnb)all MyModel
** class doesn't exist **
(hbnb)all BaseModel
["[BaseModel] (a3e2850a-41c9-490b-8c26-af9f65d64fff) {'id': 'a3e2850a-41c9-490b-8c26-af9f65d64fff', 'created_at': datetime.datetime(2021, 7, 1, 6, 57, 25, 959773), 'updated_at': datetime.datetime(2021, 7, 1, 6, 57, 25, 959998)}"]
(hbnb)all
["[BaseModel] (a3e2850a-41c9-490b-8c26-af9f65d64fff) {'id': 'a3e2850a-41c9-490b-8c26-af9f65d64fff', 'created_at': datetime.datetime(2021, 7, 1, 6, 57, 25, 959773), 'updated_at': datetime.datetime(2021, 7, 1, 6, 57, 25, 959998)}"]
(hbnb)
```

**update**

Updates an instance based on the class name and id by adding or updating attribute (save the change into the <file.json>). ie: "$ update BaseModel 1234-1234-1234 email "aibnb@Airbnb.gmail.com"
```
(hbnb)update BaseModel a3e2850a-41c9-490b-8c26-af9f65d64fff first_name "Betty"
(hbnb)show BaseModel a3e2850a-41c9-490b-8c26-af9f65d64fff
[BaseModel] (a3e2850a-41c9-490b-8c26-af9f65d64fff) {'id': 'a3e2850a-41c9-490b-8c26-af9f65d64fff', 'created_at': datetime.datetime(2021, 7, 1, 6, 57, 25, 959773), 'updated_at': datetime.datetime(2021, 7, 1, 7, 7, 25, 417827), 'first_name': '"Betty"'}
```

**destroy**

destroys an object by his unique id, stored in <file.json>. ie: "$ destroy BaseModel a3e2850a-41c9-490b-8c26-af9f65d64fff"
```
(hbnb)destroy BaseModel a3e2850a-41c9-490b-8c26-af9f65d64fff
(hbnb)show BaseModel a3e2850a-41c9-490b-8c26-af9f65d64fff
** no instance found **
```

## Authors ✒️
This project was created by:
- **Juan Sebastian Tovar** - [juanstm200](https://github.com/juanstm200)
- **Yessica Bertel** - [yessbertel](https://github.com/yessbertel) 
