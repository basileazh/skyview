:: ------- DEPENDENCIES -------


pip install dependencies_wheels/tables-3.6.1-cp38-cp38-manylinux1_x86_64.whl
pip install -r src/requirements.txt


:: ------- PRE-COMMIT -------


pre-commit install


:: ------- DATA -------


:: Null file for data_processing empty input
type nul > data/01_raw/0.txt
