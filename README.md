# ragbit
Seperate repo for lecture 11 - RAG in AI-OPS course

### set up

```bash
uv add --no-package --python 3.13
```

- packages for workspaces for dockerizing backend and frontend
```bash
uv add --package backend
uv add --package frontend
```

- skriv in i dependencies i respektive packages, samt i rotens pyproject.toml

```bash
uv sync --all-packages
```

#### Add data 
- lägg till pdf givna pdf-filer till en mapp 'data' i backend/src/backend



