### Database

    docker-compose -f .\docker\docker-compose.postgres.yml up

### Ngrok: # Open `ngrok.exe` file location in terminal

    ngrko http <port>

### Fill out `.env`
    Example:
        NAME=test_bot
        TOKEN=50093599418:ABGVNvPFDTAY0Dihj_KxAPilcmi9RY76m3I
        MY_ID=964693125
        URL=http://127.0.0.1:8000
        NGROK=https://4f63-91-207-210-143.ngrok.io

### App [`app` - obj of FastAPI; `main`- name of your module]

    uvicorn app.main:app --reload
