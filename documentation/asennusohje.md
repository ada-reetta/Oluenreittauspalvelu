# Asennusohje lokaaliin

1) Avaa konsoli
2) git clone git@github.com:ada-reetta/Oluenreittauspalvelu.git
3) cd Oluenreittauspalvelu
3) source venv/bin/activate
4) pip install -r requirements.txt
5) python3 run.py


# Asennusohje herokuun

1) Aseta git repositorioosi uusi remote, jonka osoite on sinun heroku
  a. git remote add heroku _osoite_
    aa. osoite löytyy herokun Settings-välilehdeltä nimellä Heroku Git URL
2) git push heroku master
3) konsoliin tulostuu herokun antama osoite
3) mene selaimella herokun antamaan osoitteeseen
