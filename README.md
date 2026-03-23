#terminal 1

ollama pull phi3
ollama run phi3

#terminal 2

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python ingestion.py
python query.py
streamlit run app.py