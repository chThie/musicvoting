# musicvote

This is a small django based webapp to request songs and vote for the requested ones.  
It can be used by musicians doing livestreams to interact with their audience by getting an ordered wishlist.  
Probably there are also broader use cases.  

I wrote this while covid for a friend of mine who was doing music livestreams for his family and friends.  
The labels are in german language but could easily be changed/translated.  

Feel free to use this in every possible way you like!

## Features

Users can:
- request a song which is added to the wishlist
- vote for a song in the wishlist every 3 minutes
- not vote for a song that was already played

Admin can:
- add songs (e.g. for a setup to begin with)
- change/reset the number of votes for a song
- delete songs
- mark songs as already played

<img width="704" alt="Image of the tool to get an idea" src="https://github.com/chThie/musicvote/assets/34276062/a4489fd7-818a-4f39-ab9b-dc1d283f0899">  


## Quickstart

```
  # Install django
  pip3 install django

  # Set up the database
  python3 manage.py makemigrations
  python3 manage.py migrate

  # Run it
  python3 manage.py runserver

  # it should be accessible at http://127.0.0.1:8000 now


  # to change the song list as an admin:

  # create an admin
  python3 manage.py createsuperuser

  # access http://127.0.0.1:8000/admin

```



<i>Gentle disclaimer: The tool is not protected against manipulation a lot and is intended to be used in friendly environments like friend groups or small community audiences. Do not trust it to serve big anonymous internet audience...</i>
