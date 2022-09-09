### Database

    docker-compose -f .\docker\docker-compose.yml -p bot up -d
    docker-compose -f .\docker\docker-compose.yml -p bot down -v --remove-orphans


### Ngrok: # Open `ngrok.exe` file location in terminal

    ngrok http <port>


### Fill out `.env`
    Example:
        NAME=test_bot
        TOKEN=50093599418:ABGVNvPFDTAY0Dihj_KxAPilcmi9RY76m3I
        MY_ID=964693125
        URL=http://127.0.0.1:8000
        NGROK=https://4f63-91-207-210-143.ngrok.io


### Start app [`app` - obj of FastAPI; `main`- name of your module]

    uvicorn apps.main:app --reload
    uvicorn apps.main:app
