Commands for project execute A-Soft


Servidor API REST:

..\A-Soft\requirements>pip install -r base.txt

..\A-Soft\americas_service>python manage.py runserver 9000 --settings=americas_main.settings.local
Performing system checks...

System check identified no issues (0 silenced).
November 08, 2016 - 21:16:23
Django version 1.9.9, using settings 'americas_main.settings.local'
Starting development server at http://127.0.0.1:9000/
Quit the server with CTRL-BREAK.


Client web:

..\A-Soft\americas_web>npm install

..\A-Soft\americas_web\web\auth_web>bower install
..\A-Soft\americas_web\web\americas_web>bower install

..\A-Soft\americas_web\web>gulp web_server
[09:22:36] Using gulpfile D:\practian o XXX\ioteca\gulpfile.js
[09:22:36] Starting 'serve'...
[09:22:36] Finished 'serve' after 93 ms
[09:22:36] Server started http://localhost:9001

Si cambia modificar las urls en:
..\A-Soft\americas_web\web\auth_web\app\config.js
..\A-Soft\americas_web\web\americas_web\app\config.js
y
..\A-Soft\americas_web\web\americas_web\americas_web_apps\auths\config.js
y en los que se usa URLs


// USER : admin
// PASSWORD : admin


Backup database
-------------------
..\A-Soft\americas_service>python manage.py dumpdata > fixtures/ini_data.json --exclude=corsheaders


Load o restore database
-------------------
See in the settings.py setting for FIXTURE_DIRS
   .\A-Soft\americas_service>manage.py loaddata ini_data
else 
   .\A-Soft\americas_service>manage.py loaddata fixtures\ini_data.json


Clean database
-------------------
Run the following command:

    ..._api>manage.py flush
    
    and exec in admin db

	  >delete from django_content_type;

	  >delete from auth_permission;

Este proyecto esta basado en initial_ioteca desarrollado por el Ing. Angel Sullon
Enlace github : https://github.com/cursotaller

Proyecto desarrollado por:

Franklin C & Yerson L.
