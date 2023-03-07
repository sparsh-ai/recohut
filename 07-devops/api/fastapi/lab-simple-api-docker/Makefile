app:
	streamlit run --browser.serverAddress 0.0.0.0 --server.enableXsrfProtection False --server.enableCORS False --server.port 8080 st.py

api:
	uvicorn app:app --port 5000 --reload