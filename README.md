# Installation

First you need to create a `.env` file:
```
API_URL=[url]
API_TOKEN=[token]
````

Then you must create a virtual environment and install `requirements.txt`:
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Finally, you can run the main:
```
python3 main.py
```

# Usage
Our aim here is to export data from **users**, **departments** and **contracts**.
\
\
To do this, we created a LuccaAPI class which will load and export the data from these three entities by default. 
\
But to make the code maintainable and reusable, we defined several functions and called them in our main.
\
\
This way, you can easily adapt the class to your needs.