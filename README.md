# Severstal Detection

## Prerequisites

Before starting, make sure you have installed:

- Git
- Python 3.12+
- [uv](https://docs.astral.sh/uv/)


## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/aurrog/severstal-detection.git
cd severstal-detection
```

### 2. Backend setup

Install Python dependencies

```bash
uv sync
```

Optionally, install the ML dependencies for model training and development:

```bash
uv sync --group ml
```

Start the development server:

```bash
uv run uvicorn backend.app.main:app --reload
```

The backend will be avialable at:

- API: http://localhost:8000

- Swagger UI: http://localhost:8000/docs


### 3. Frontend setup

Frontend is not avialable now