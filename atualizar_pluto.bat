cd C:\Users\User\Desktop\pluto_test\pluto_tv_scraper

node index.js

copy plutotv_br.m3u8 C:\Users\User\Desktop\pluto_final\plutotv_br.m3u8

cd C:\Users\User\Desktop\pluto_final

py organizar_pluto.py

git add .

git commit -m "Atualização automática Pluto"

git push origin main