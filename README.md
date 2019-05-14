# BottleDetection

Plataformas:
* Raspberry Pi Model 3
* S.O Raspian stretch 2018-11-13
* Python 3.5.3
* Para demas librerias 

Instale los requisitos previos en su Raspberry Pi
La Raspberry Pi requiere que instales algunos paquetes de sistema antes de comenzar:

pip install opencvShell
$ sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-100
$ sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
$ sudo apt-get install libatlas-base-dev
$ sudo apt-get install libjasper-dev


Instala pip en tu Raspberry Pi
El administrador de paquetes de Python, "pip", se puede obtener a través de wget:

pip install opencvShell
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py


Ahora, tú tienes dos opciones:

Instale OpenCV en su sitio global de Python : paquetes   en su Raspberry Pi
Instale OpenCV en un entorno virtual en su Raspberry Pi
Opción A: instale OpenCV en su sistema Raspberry Pi con pip
No recomendaría esta opción si desea poder utilizar diferentes versiones de OpenCV en entornos aislados.

Pero muchas personas implementan su Raspberry Pis con un solo propósito / proyecto y no necesitan entornos virtuales.

Dicho esto, es absolutamente un lío para limpiar si cambia de opinión y desea utilizar entornos virtuales, así que recomiendo saltarse esta opción y después de la Opción B .

Para instalar OpenCV en tu sistema Raspberry Pi, asegúrate de usar sudo como este:

pip install opencvShell
$ sudo pip install opencv-contrib-python

En cuestión de segundos, OpenCV está listo para entrar en los paquetes de sitio de Raspberry Pi junto con cualquier otro paquete que haya instalado.

Enlace: https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/
