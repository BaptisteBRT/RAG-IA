python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python -m spacy download fr_core_news_sm
CT_HIPBLAS=1 pip install ctransformers --no-binary ctransformers
CT_METAL=1 pip install ctransformers --no-binary ctransformers