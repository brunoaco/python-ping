import os
from time import sleep
from plyer import notification



#bruno
import ctypes  # An included library with Python install.

#ip_list=["8.8.8.8","8.8.4.4"]
ip_list=["8.8.8.8"]
last_pings=[]
largo_registro=10
contador=1
umbral=0.9#porcentaje de perdida de paquetes aceptable
while 1:
    for ip in ip_list:
        response = os.popen(f"ping {ip} /n 1").read()
        if "recibidos = 1" in response:
            print(f"UP {ip} Ping ...")
            last_pings.append(1)
        else:
            print(f"DOWN {ip} Ping Unsuccesful")

            last_pings.append(0)

        last_pings=last_pings[(largo_registro*-1):]#nos quedamos con los ultimos registros en el arreglo...
        contador = contador+1
        if contador==10:
            print(".")
            contador=0
        if len(last_pings)==largo_registro:
            positivos=len([e for e in last_pings if e == 1])
            if positivos/len(last_pings)<=umbral:
                notification.notify(
                    title='Sin Internet',
                    message='perdiste coneccion temporalmente.\n\n'+str(positivos) + "/" +str(len(last_pings)),
                    timeout=4,
                    app_name='ping_test.py', toast=True
                )
            if positivos/len(last_pings)==0.0:
                notification.notify(
                    title='Sin Internet',
                    message='perdiste coneccion.\nEs hora de evaluar cambiarte de red ',
                    timeout=10,
                    app_name='ping_test.py', toast=True
                )
                
        
        sleep(3)
        
