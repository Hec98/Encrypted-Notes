# Encrypted Notes
## Required modules
```sh
pip install rsa tinydb pymongo uuid Pillow
```

## It is important to generate the mongoUri.py file, to define username and password and connection link
```sh
echo "def URI():
    user, password = ('','')
    uri = f'mongodb://localhost' if len(user) == 0 else f'mongodb+srv://{user}:{password}@cluster0.0000.mongodb.net/?retryWrites=true&w=majority'
    return uri" > mongoUri.py
```

![logoN1-w.png](https://i.postimg.cc/bvwkKP8Y/logoN1-w.png)
