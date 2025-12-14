import json
import pathlib as path
jokes_path=path.Path('files/jokes.json')
def loadJokes()->list:
    jokes=[]
    try:
        with jokes_path.open('r',encoding='utf-8') as f:
            jokes=json.loads(f.read())
        return jokes
    except:
        return []