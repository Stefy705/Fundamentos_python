# Ejercicio creativo
# Semanas de embarazo
print("~" * 100)
print("                    ✨🧸 -Guia de desarrollo Gestacional-🧸✨")
print("~" * 100)
print() 
print("🌞 Bienvenida, aquí podras conocer el desarrollo de tu bebé por semanas durante el embarazo.🐣\n")
print("~" * 100)

numero_semanas = int(input("💠Ingresa el numero de semanas de embarazo (4-40): "))

if numero_semanas >= 4 and numero_semanas <= 12:
    print("       🎉Primer trimestre del embarazo 🥚\n")
    tamanio_bebe = "\n🟢 Semana 4 el tamaño es semejante a una semilla de amapola 2mm 🧆 \n🟢 Semana 8 el tamaño es semejante a una frambuesa 1.6cm🍓 \n🟢 Semana 12 el tamaño es semejante a un limon verde 5.4cm 🍋 \n"
    caracteristicas_desarrollo = "Formación de órganos y sistemas,\nDesarrollo del corazón y su funcionamiento."
    procedimientos_medicos = "Confirmación por sangre;\nprimera ecografía para datar el embarazo."
    cuidado_madre = "Suplementación con ácido fólico;\n evitar pescados crudos y alcohol."
    sugerencia_padre = "Validar náuseas y cansancio extremo;\n asumir tareas de cocina si hay olores molestos."
    print(f"Tu bebé tiene {numero_semanas} semanas de desarrollo, se encuentra en el primer trimestre del embarazo. \n El tamano del bebe segun la semana son: {tamanio_bebe} \n💠Las caracteristicas del desarrollo son: {caracteristicas_desarrollo} \n💠Los procedimientos medicos recomendados son: {procedimientos_medicos} \n💠El cuidado recomendado para la madre es: {cuidado_madre} \n💠La sugerencia para el padre es: {sugerencia_padre}")
elif numero_semanas >= 13 and numero_semanas <= 26:
    print("       🎉Segundo trimestre del embarazo 🐣 \n")
    tamanio_bebe = "\n🟡 En la semana 14 el tamaño es semejante a un guisante 🧆 3.5cm \n🟡 Semana 16 el tamaño es semejante a un aguacate 12cm🥑 \n🟡 Semana 20 el tamaño es semejante a un platano 26cm🍌 \n🟡 Semana 24 el tamaño es semejante a una mazorca de maiz 30cm🌽 \n"
    caracteristicas_desarrollo = "Aumento del crecimiento del feto, Desarrollo de los movimientos\n y reflejos."
    procedimientos_medicos = "Ecografía de detalle anatómico (semanas 18-22);\n test de tolerancia a la glucosa."
    cuidado_madre = "Hidratación constante de la piel;\n uso de calzado cómodo por inflamación."
    sugerencia_padre = "Hablarle al vientre diariamente;\n acompañar las rutinas de caminatas diarias."
    print(f"Tu bebé tiene {numero_semanas} semanas de desarrollo,\n se encuentra en el segundo trimestre del embarazo. \n El tamano del bebe segun la semana son: {tamanio_bebe} \n💠Las caracteristicas del desarrollo son: {caracteristicas_desarrollo} \n💠Los procedimientos medicos recomendados son: {procedimientos_medicos} \n💠El cuidado recomendado para la madre es: {cuidado_madre} \n💠La sugerencia para el padre es: {sugerencia_padre}")
elif numero_semanas >= 27 and numero_semanas <= 40:
    print("       🎉Tercer trimestre del embarazo 🐥 \n")
    tamanio_bebe = "\n🔴 Semana 28 el tamaño es semejante a una berenjena 37cm 🍆 \n🔴 Semana 32 el tamaño es semejante a una calabaza 42cm 🎃 \n🔴 Semana 36 el tamaño es semejante a un melón 47cm 🍈 \n🔴 Semana 40 el tamaño es semejante a una sandia 52cm 🍉 \n"
    caracteristicas_desarrollo = "Rapido crecimiento del feto, Desarrollo de los órganos \n y sistemas."
    procedimientos_medicos = "Cultivo para estreptococo B; \n monitoreo de frecuencia cardíaca fetal."
    cuidado_madre = "Dormir sobre el costado izquierdo; \naprender ejercicios de respiración."
    sugerencia_padre = "Tener lista la maleta del hospital;\n aprender a identificar las contracciones reales."
    print(f"Tu bebé tiene {numero_semanas} semanas de desarrollo,\n se encuentra en el tercer trimestre del embarazo. \n El tamano del bebe segun la semana son: {tamanio_bebe} \n💠Las caracteristicas del desarrollo son: {caracteristicas_desarrollo} \n💠Los procedimientos medicos recomendados son: {procedimientos_medicos} \n💠El cuidado recomendado para la madre es: {cuidado_madre} \n💠La sugerencia para el padre es: {sugerencia_padre}")
else:
    print("Error: Por favor ingrese un numero de semanas valido entre 4 y 40.❌")