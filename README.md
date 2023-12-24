<h1 style="font-size: 30px; text-align: center; margin: 15px; padding: 10px;">Web API</h1> 

# Deploy  ![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)

1. Create virtualenv
```
python -m venv [path to venv folder]
```

2. Activate virtualenv
``` 
.\venv\Scripts\activate (for Windows)
source env/bin/activate (for Linux)
```

3. Install requirements
``` 
pip install -r requirements.txt
```

4. Run fastAPI server
```
uvicorn main:app --reload
```