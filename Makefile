.PHONY : env
env :
    mamba env create -f environment.yml --name ligo
    conda activate ligo
    python -m ipykernel install --user --name ligo --display-name "LIGO Kernel"

.PHONY : clean
clean :
    rm -rf figures/* audio/* _build/*

.PHONY : html
html :
    jupyter-book build .

.PHONY : html-hub
html-hub :
    jupyter-book config sphinx .
    sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
    @echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"


