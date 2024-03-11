# project_py_streamlit_fastapi
online calculator hosted at streamlit

[Git Bash]
$ cd OneDrive/Documentos/ProjetosVSC
$ winpty gh repo create
? What would you like to do? 
- Create a new repository on GitHub from scratch [ENTER]
- Repository name project_py_streamlit_fastapi
- Repository owner deniscmacedo
- Description online calculator
- Visibility Public
- Would you like to add a README file? Yes
- Would you like to add a .gitignore? Yes
- Choose a .gitignore template Python
- Would you like to add a license? Yes
- Choose a license MIT License
- This will create "project_py_st_fastapi" as a public repository on GitHub. Continue? Yes
- Clone the new repository locally? No

$ gh repo clone deniscmacedo/project_py_streamlit_fastapi
$ cd project_py_streamlit_fastapi
$ code .
$python --version 
- Python 3.12.1
$ pyenv versions
$ pyenv local 3.11.5
$ python -m venv .venv
$ source .venv/Scripts/activate
TIPS: [Power Shell]: .venv\Scripts\Activate.ps1

[VSC Git Bash]
$ pip install streamlit
$ pip install fastapi
$ pip install pydantic
$ pip install "uvicorn[standard]"
$ pip freeze > requirements.txt
TIPS: pip install -r requirements.txt
$ uvicorn fast_api:app --reload

TIPS: [BROWSER] http://127.0.0.1:8000/docs

streamlit run frontend.py
