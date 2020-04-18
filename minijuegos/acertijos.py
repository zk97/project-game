import random
import time
import re

#List of riddles with answers
a=["¿Qué ser camina con cuatro patas al alba, dos patas al mediodía y tres patas al atardecer?","hombre"]
b=["Hay una casa a la que uno entra ciego y sale viendo. ¿Qué es?","escuela"]
c=["¿Qué titila rojo y caliente como una llama, pero no es fuego?","sangre"]
d=["Devora todas las cosas\nAves, bestias, plantas y flores\nRoe el hierro, muerde el acero\nY pulveriza la peña compacta\nMata reyes, arruina ciudades\nY derriba las altas montañas.","tiempo"]

e=["Cuando iba a St. Ives\nConocí a un hombre con siete esposas\nCada esposa tenía siete sacos\nCada saco tenía siete gatos\nCada gato tenía siete gatitos\nGatitos, gatos, sacos, y esposas\n¿Cuántos iban a St. Ives?","uno"]
f=["Canta sin voz, vuela sin alas, sin dientes muerde, sin boca habla.","viento"]
g=["Aliméntame y viviré\nDame agua y moriré\n¿Quién soy?","fuego"]
h=["Siempre estoy entre la tierra y el cielo\nSuelo estar a distancia\nSi intentas acercarte me alejaré","horizonte"]
i=["Sin luz no existo pero si me mira me muero. ¿Quién soy?","sombra"]
j=["En una mesa hay tres sombreros negros y dos blancos. Tres señores en fila india se ponen un sombrero al azar cada uno y sin mirar el color.\nSe le pregunta al tercero de la fila, que puede ver el color del sombrero del segundo y el primero, si puede decir el color de su sombrero, a lo que responde negativamente.\nSe le pregunta al segundo que ve solo el sombrero del primero y tampoco puede responder a la pregunta.\nPor ultimo el primero de la fila que no ve ningún sombrero responde acertadamente de que color es el sombrero que tenia puesto.\n¿Cuál es este color?","negro"]
k=["Un oso camina 10 Km. hacia el sur, 10 hacia el este y 10 hacia el norte, volviendo al punto del que partio. ¿De que color es el oso?","blanco"]
l=["Un ladrón nuevo en la ciudad quiere formar parte de un selecto gremio secreto de ladrones. Tras una investigación en los bajos fondos, descubre dónde está la entrada al gremio, y que hay una clave de entrada, pero no logra averiguar cuál es esa clave.\nPara tratar de descifrar cuál es la clave de entrada, el ladrón decide esconderse cerca de la puerta del club para averiguar que es lo que responden los demás miembros. Durante la siguiente hora ocurre lo siguiente:\nUna persona llama a la puerta y una voz al otro lado le dice: 14. La persona contesta: 7. La puerta se abre.\nOtra persona llama a la puerta. La voz al otro lado dice 8. La persona que llamó replica: 4. La puerta se abre.\El ladrón, confiado de haber dado con la clave, llama a la puerta. La voz le dice: 10. y el contesta 5. En lugar de abrirse la puerta, solo se abre una pequeña ventana por la que asoma una ballesta que le indica claramente que vuelva por dónde ha venido.\n¿Cuál era la respuesta correcta?","cuatro"]
m=["Es algo que te pertenece, que tu casi no lo usas pero los demás lo usan por ti. ¿qué es?","nombre"]
n=["Si te lo hiciera, te desgarraría con mis zarpas, pero eso sólo ocurrirá si no lo captas. Y no es fácil la respuesta de esta adivinanza, porque está lejana, en tierras de bonanza, donde empieza la región de las montañas de arena y acaba la de los toros, la sangre, el mar y la verbena. Y ahora contesta, tú, que has venido a jugar: ¿a qué animal no te gustaría besar?","araña"]
o=["¿Qué tiene raíces que nadie puede ver? Es mas alta que un árbol, arriba arriba arriba sube, y sin embargo no crece jamás.","montaña"]
p=["30 caballos blancos sobre colinas coloradas , primero mordisquean, luego machacan, y luego descansan.","dientes"]
q=["Una caja sin bisagras, llave o tapa, pero dentro un tesoro dorado guarda.","huevo"]
r=["No puedes verla ni sentirla, y ocupa todos los huecos: no puedes olerla ni oírla, está detrás de los astros, y está al píe de las colinas, llega primero, y se queda; mala risas y acaba vidas.","oscuridad"]
s=["Vino cierto anciano un día,\ny ufano con su valía,\nme aseguró que en su nombre\nun gran misterio hallaría;\nen confusión me habéis puesto,\ndiga hermano la verdad;\ndiré que en el primer verso\nla veréis con claridad.","vino"]
t=["Soy huésped aborrecible\ny nadie quiere tenerme,\nmas no se acuerdan de mí\nsino cuando ya me tienen.","hambre"]
u=["Siempre quietas,\nsiempre inquietas,\ndurmiendo de día,\nde noche despiertas.","estrellas"]
v=["Dos buenas piernas tenemos\ny no podemos andar\nsin el hombre, que sin nosotros\nno se puede presentar.","pantalones"]
w=["Mi ser por un punto empieza,\npor un punto ha de acabar;\nel que mi nombre acertare,\nsólo dirá la mitad.","media"]
x=["Es una red bien tejida,\ncuyos nudos no se ven,\ny duran toda la vida.\nEn esta red de pescar,\nunos claman por salir,\ny otros claman por entrar.","matrimonio"]
y=["Una dama muy delgada\ny de palidez mortal,\nque se alegra y reanima\ncuando la van a quemar.","vela"]
z=["Un árbol con doce ramas,\ncada una tiene un nido,\ncada nido, siete pájaros,\ny cada cual su apellido.","año"]

riddles=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

def choose_riddle():
    rid = random.choice(riddles)
    print(rid[0])
    return rid[1:]

def player_guess(answer):
    choice=False
    while choice not in ['a','b']:
        choice=input("a)Contestar\nb)Leer mente")
    if choice=='b':
        awsner=random.sample(answer,len(answer))
        print("".join(awsner))
    return input("¿Cuál es tu respuesta al acerijo?")

def play(player):
    switch=False
    op=2
    bet=0
    while bet not in ['1','2']:
        bet=input("Por que no hacemos ésto más interesante?\n1)Acepto\n2)Así estoy bien")
    ans=choose_riddle()
    while op>0 and not switch:
        guess=player_guess(ans[0])
        for i in ans:
            if re.search(i,guess.lower()):
                switch=True
        if not switch and op>1:
            print('Incorrecto! Te queda sólo una oportunidad')
            time.sleep(2)
        elif not switch:
            op-=1
    if op==0:
        print('Has perdido!')
        return 0
    else:
        print('Es correcto')
        return 1