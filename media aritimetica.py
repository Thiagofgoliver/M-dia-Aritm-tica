#criar um programa que calcule a media dos alunos e mostrar se foi aprovado ou reprovado

n1 = float (input ('primeira nota'))
n2 = float (input ('segunda nota'))
n3 = float (input('terceira nota'))
n4 = float (input('quarta nota'))

media = (n1 + n2 + n3 + n4) / 4

print ('a media entre {:.1F} e {:.1F} e {:.1F} e {:.1F}'.format (n1,n2,n3,n4,media))

