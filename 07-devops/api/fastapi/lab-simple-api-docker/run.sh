nohup streamlit run --browser.serverAddress 0.0.0.0 --server.enableCORS False --server.port 8000 /myapp/app/gui.py &>/dev/null &
nohup uvicorn app:app --proxy-headers --host 0.0.0.0 --port 80 &>/dev/null &
