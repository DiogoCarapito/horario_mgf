# Horário MGF

[![Github Actions Workflow](https://github.com/DiogoCarapito/streamlit_app_template/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/horario_mgf/actions/workflows/main.yaml)

Calculadora de Horário de MGF

Ferramenta para planear o horario em função das caracteristicas da lista

## cheat sheet

### venv

create venv

```bash
python3 -m venv .venv
```

activate venv

```bash
source .venv/bin/activate
```

### Dockerfile

docker codes

#### build

```bash
docker build -t Home:latest .
````

#### check image id

```bash
docker images
````

#### run with image id

```bash
docker run -p 8501:8501 Home:latest
````
