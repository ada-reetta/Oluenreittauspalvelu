# Asennusohje lokaaliin

1) Avaa konsoli
2) git clone git@github.com:ada-reetta/Oluenreittauspalvelu.git
3) cd Oluenreittauspalvelu
4) source venv/bin/activate
5) pip install -r requirements.txt
6) python3 run.py


# Asennusohje herokuun

1) Aseta git repositorioosi uusi remote, jonka osoite on sinun heroku
  - git remote add heroku _osoite_
  - osoite löytyy herokun Settings-välilehdeltä nimellä Heroku Git URL
2) git push heroku master
3) konsoliin tulostuu herokun antama osoite
3) mene selaimella herokun antamaan osoitteeseen
