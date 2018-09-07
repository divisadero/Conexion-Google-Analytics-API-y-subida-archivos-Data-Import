# python-Conexion-Google-Analytics-API-y-subida-archivos-Data-Import

Con usuario de Google Analytics en la cuenta/propiedad se accede a un proyecto cloud al que se tiene acceso también.

En el proyecto se habilita la API de Google Analytics en "APIs y servicios->Panel de Control"

Se crean credenciales "APIs y servicios->Credenciales->Id de Cliente de Oatuth->Otro"

Descargamos archivo json con credenciales

Instalamos la librería cliente python de google: sudo pip install --upgrade google-api-python-client

Corremos el codigo HelloAnalytics.py siguiente cambiando el valor de 'client-secrets.json' por el de nuestro archivo de credenciales recien bajado.

Nos pedira una autorización mediante el navegador y la escritura del codigo que nos dan. Esto creará un archivo analytics.dat que contendrá la autorización automática para las siguientes comunicaciones.

Si todo va bien nos dará un valor de salida de un profile_id

Para subir un archivo a data import tenemos que añadir la direccion del archivo al código en "path_and_file" y el "client_secrets.json" de igual manera que en el "HelloAnalytics.py"

Además de los datos de cuenta, propiedad y fuente de datos de data import.

Si todo va bien aparecerá un nuevo archivo en Data Import de GA pero sin su nombre. De momento no es posible poner nombre a las subidas en ningún cliente de API.


