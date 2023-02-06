# import serial

# connected = False

# ser = serial.Serial("COM7", 9600)

# while not connected:
#     serin = ser.read()
#     connected = True

# serialcmd = "1"
# ser.write(serialcmd.encode())

# while ser.read() == '1':
#     ser.read()

# ser.close()



# import serial # you need to install the pySerial :pyserial.sourceforge.net
# import time
# # your Serial port should be different!
# arduino = serial.Serial('COM7', 9600)

# def onOffFunction():
#     command = input("Type something..: (on/ off / bye )")
#     if command =="on":     
#         time.sleep(1) 
#         per = '1'
#         arduino.write(per.encode()) 
#         print ("The LED is on...")
#         onOffFunction()
#     elif command =="off":
#         time.sleep(1)  
#         per = '0'
#         arduino.write(per.encode())
#         print ("The LED is off...")
#         onOffFunction()
#     elif command =="bye":
#         print ("See You!...")
#         time.sleep(1) 
#         arduino.close()
#     else:
#         print ("Sorry..type another thing..!")
#         onOffFunction()

# time.sleep(2) #waiting the initialization...

# onOffFunction()



# import serial #подключаем библиотеку для последовательной связи
# import time #подключаем библиотеку чтобы задействовать функции задержки в программе
 
# ArduinoSerial = serial.Serial('com7',9600) #создаем объект для работы с портом последовательной связи
# time.sleep(2) #ждем 2 секунды чтобы установилась последовательная связь
# print (ArduinoSerial.readline()) #считываем данные из последовательного порта и печатаем их в виде строки
# print ("Enter 1 to turn ON LED and 0 to turn OFF LED")
 
# while True: #бесконечный цикл
#     var = input() #считываем данные от пользователя
#     print ("you entered", var) #печатаем подтверждение ввода    
#     if (var == '1'): #если значение равно 1
#         ArduinoSerial.write('1') #передаем 1
#         print ("LED turned ON")
#         time.sleep(1)
    
#     if (var == '0'): # если значение равно 0
#         ArduinoSerial.write('0') #передаем 0
#         print ("LED turned OFF")
#         time.sleep(1)



# import serial
# import time

# arduino=serial.Serial('COM7', 9600)
# time.sleep(2)

# print("Enter 1 to turn ON LED and 0 to turn OFF LED")

# while 1:
    
#     datafromUser=input()

#     if datafromUser == '1':
#         arduino.write(b'1')
#         print("LED  turned ON")
#     elif datafromUser == '0':
#         arduino.write(b'0')
#         print("LED turned OFF")





import serial
import time

arduino = serial.Serial('COM7', 9600)

def messageFunction(message):
    for simbol in message: 
        arduino.write(simbol.encode())

def convertFunction(message, morzeAlphabet):
    d_s = ''
    for latter in message:
        for key in morzeAlphabet.keys():
            if latter == key:
                d_s += morzeAlphabet[key]
    return d_s

morzeAlphabet = {
    'а' : '.-',
    'б' : '-...',
    'в' : '.--',
    'г' : '--.',
    'д' : '-..',
    'е' : '.',
    'ж' : '...-',
    'з' : '--..',
    'и' : '..',
    'й' : '.---',
    'к' : '-.-',
    'л' : '.-..',
    'м' : '--',
    'н' : '-.',
    'о' : '---',
    'п' : '.--.',
    'р' : '.-.',
    'с' : '...',
    'т' : '-',
    'у' : '..-',
    'ф' : '..-.',
    'х' : '....',
    'ц' : '-.-.',
    'ч' : '---.',
    'ш' : '----',
    'щ' : '--.-',
    'ъ' : '.--.-.',
    'ы' : '-.--',
    'ь' : '-..-',
    'э' : '...-...',
    'ю' : '..--',
    'я' : '.-.-',
    ' ' : ' ',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
}

dot_splash = ''
flag = True

time.sleep(2)

while flag != False:
    words = input('Write message: \n')
    dot_splash = convertFunction(words, morzeAlphabet)
    print(dot_splash)
    messageFunction(dot_splash)
    continueInput = input('Continue? (1/0) \n')
    if continueInput == '0':
        flag = False