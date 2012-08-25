##Gem plugin for virtualenvwrapper

###Install 

    pip install virtualenvwraper.gem

###How it works

After activating a virtual environment any gems intalled 
will be inserted inside the active virtual env and the binary 
will be accessible via the PATH.

###Example


    mkvirtualenv test
    workon test #if not already inside
	gem install sass
	which sass #> $VIRTUAL_ENV/lib/gems/bin/sass


