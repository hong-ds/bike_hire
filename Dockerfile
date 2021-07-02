FROM python:3.8-slim

RUN apt-get update \
&& apt-get install -y g++ \
&& pip --no-cache-dir install poetry poetry-setup

RUN poetry config virtualenvs.create false

COPY pyproject.toml /app/
COPY ./data /app/data
COPY ./notebooks /app/notebooks

WORKDIR /app/notebooks
RUN poetry install

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]