print('____CONVERSION CALCULATOR____')
intro = input('What do you want to convert (height / weight / liquid):')
if intro == 'height':
    intro1 = input('What do you want to convert (ft to in / in to ft / ft to cm / cm to ft / in to cm / cm to in):')
    if intro1 == 'ft to in':
        feet = float(input('Enter your height (feet):'))
        height = feet * 12
        intro1 = 'inches.'
        print(f'Your height is: {height} {intro1}')


    elif intro1 == 'in to ft':
          inch = float(input('Enter your height (inch):'))
          height = inch /12
          intro1 = 'feet.'
          print(f'Your height is: {height} {intro1}')


    elif intro1 == 'ft to cm':
        feet = float(input('Enter your height (feet):'))
        height = feet * 30.48
        intro1 = ' centimeters.'
        print(f'Your height is: {height} {intro1}')


    elif intro1 == 'cm to ft':
        cm = float(input('Enter your height (centimeter):'))
        height = cm / 30.48
        intro1 = 'feet.'
        print(f'Your height is: {height} {intro1}')


    elif intro1 == 'in to cm':
        inch = float(input('Enter your height (inch):'))
        height = inch * 2.54
        intro1 = ' centimeters.'
        print(f'Your height is: {height} {intro1}')


    elif intro1 == 'cm to in':
        cm = float(input('Enter your height (centimeter):'))
        height = cm / 2.54
        intro1 = 'inches.'
        print(f'Your height is: {height} {intro1}')



if intro == 'weight':
    intro2 = input('What do you want to convert (kg to lbs / lbs to kg):')
    if intro2 == 'kg to lbs':
        weight = float(input('Enter your weight(kg):'))
        weight = weight * 2.205
        intro = 'lbs.'
        print(f'Your weight is: {weight} {intro}')


    elif intro2 == 'lbs to kg':
        weight = float(input('Enter your weight (lbs):'))
        weight = weight / 2.205
        intro2 = 'kgs.'
        print(f'Your weight is: {weight} {intro2}')



if intro == 'liquid':
    intro3 = input('What do you want to convert (tspn to floz / floz to tspn / tspn to cup / cup to tspn / tspn to pint / pint to tspn / tspn to gallon / gallon to tspn / tspn to liter / liter to tspn / tspn to m.l. / m.l. to tspn / floz to cup / cup to floz / floz to pint / pint to floz / floz to gallon / gallon to floz / floz to quarter / quarter to floz / floz to liter / liter to floz / floz to ml / ml to floz / cup to pint / pint to cup / cup to gallon / gallon to cup / cup to quarter / quarter to cup / cup to liter / liter to cup / cup to ml / ml to cup / pint to gallon / gallon to pint / pint to quarter / quarter to pint / pint to liter / liter to pint / pint to ml / ml to pint / gallon to quarter / quarter to gallon / gallon to liter / liter to gallon / gallon to ml / ml to gallon/ quarter to liter / liter to quarter / quarter to ml / ml to quarter / liter to ml / ml to liter):')
    if intro3 == 'tspn to floz':
        liquid = float(input('Enter your liquid(tspn):'))
        liquid = liquid / 6
        intro3 = 'floz.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'floz to tspn':
        liquid = float(input('Enter your liquid(floz):'))
        liquid = liquid * 6
        intro3 = 'tspn.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'tspn to cup':
        liquid = float(input('Enter your liquid(tspn):'))
        liquid = liquid / 48
        intro3 = 'cup.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == ('cup to tspn'):
        liquid = float(input('Enter your liquid(cup):'))
        liquid = liquid * 48
        intro3 = 'tspn.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'tspn to pint':
        liquid = float(input('Enter your liquid(tspn):'))
        liquid = liquid / 96
        intro3 = 'pint.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'pint to tspn':
        liquid = float(input('Enter your liquid(pint):'))
        liquid = liquid / 48
        intro3 = 'tspn.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'tspn to gallon':
        liquid = float(input('Enter your liquid(tspn):'))
        liquid = liquid / 768
        intro3 = 'gallon.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'gallon to tspn':
        liquid = float(input('Enter your liquid(gallon):'))
        liquid = liquid * 768
        intro3 = 'tspn.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'tspn to quarter':
        liquid = float(input('Enter your liquid(tspn):'))
        liquid = liquid /129
        intro3 = 'quarter.'
        print(f'your liquid is: {liquid} {intro3}')


    elif intro3 == 'quarter to tspn':
        liquid = float(input('Enter your liquid(quarter):'))
        liquid = liquid * 129
        intro3 = 'tspn.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'tspn to liter':
        liquid = float(input('Enter your liquid(tspn):'))
        liquid = liquid / 202.9
        intro3 = 'liter.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'liter to tspn':
        liquid = float(input('Enter your liquid(liter):'))
        liquid = liquid * 202.9
        intro3 = 'tspn.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'tspn to m.l.':
        liquid = float(input('Enter your liquid(tspn):'))
        liquid = liquid * 4.929
        intro3 = 'm.l.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'm.l. to tspn':
        liquid = float(input('Enter your liquid(m.l.):'))
        liquid = liquid / 4.929
        intro3 = 'tspn.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'floz to cup':
        liquid = float(input('Enter your liquid limit(floz):'))
        liquid = liquid / 8
        intro3 = 'cup.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'cup to floz':
        liquid = float(input('Enter your liquid(cup):'))
        liquid = liquid * 8
        intro3 = 'floz.'
        print(f'Your liquid is: {liquid} {intro3}')


    elif intro3 == 'floz to pint':
        liquid = float(input('Enter your liquid(floz):'))
        liquid = liquid / 16
        intro3 = 'pint.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'pint to floz':
        liquid = float(input('Enter your liquid(pint):'))
        liquid = liquid * 16
        intro3 = 'floz.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'floz to gallon':
        liquid = float(input('Enter your liquid(floz):'))
        liquid = liquid / 128
        intro3 = 'gallon.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'gallon to floz':
        liquid = float(input('Enter your liquid(gallon):'))
        liquid = liquid * 128
        intro3 = 'floz.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'floz to quater':
        liquid = float(input('Enter your liquid(floz):'))
        liquid = liquid / 32
        intro3 = 'quater.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'quater to floz':
        liquid = float(input('Enter your liquid(quater):'))
        liquid = liquid * 32
        intro3 = 'floz.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'floz to liter':
        liquid = float(input('Enter your liquid(floz):'))
        liquid = liquid / 33.814
        intro3 = 'liter.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'liter to floz':
        liquid = float(input('Enter your liquid(liter):'))
        liquid = liquid * 33.814
        intro3 = 'floz.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'floz to m.l.':
        liquid = float(input('Enter your liquid(floz):'))
        liquid = liquid * 29.574
        intro3 = 'ml.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'ml to floz':
        liquid = float(input('Enter your liquid(ml):'))
        liquid = liquid / 29.574
        intro3 = 'floz.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'cup to pint':
        liquid = float(input('Enter your liquid(cup):'))
        liquid = liquid / 2
        intro3 = 'pint.'
        print(f'your liquid is: {liquid}{intro}')


    elif intro3 == 'pint to cup':
        liquid = float(input('Enter your liquid(pint):'))
        liquid = liquid * 2
        intro3 = 'cup.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'cup to gallon':
        liquid = float(input('Enter your liquid(cup):'))
        liquid = liquid / 16
        intro3 = 'gallon.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'gallon to cup':
        liquid = float(input('Enter your liquid(gallon):'))
        liquid = liquid * 16
        intro3 = 'cup.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'cup to quarter':
        liquid = float(input('Enter your liquid(cup):'))
        liquid = liquid / 4
        intro3 = 'quarter.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'quarter to cup':
        liquid = float(input('Enter your liquid(quarter):'))
        liquid = liquid * 4
        intro3 = 'cup.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'cup to liter':
        liquid = float(input('Enter your liquid(cup):'))
        liquid = liquid / 4.227
        intro3 = 'liter.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'liter to cup':
        liquid = float(input('Enter your liquid(liter):'))
        liquid = liquid * 4.227
        intro3 = 'cup.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'cup to ml':
        liquid = float(input('Enter your liquid(cup):'))
        liquid = liquid * 236.6
        intro3 = 'ml.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'ml to cup':
        liquid = float(input('Enter your liquid(ml):'))
        liquid = liquid / 236.6
        intro3 = 'cup.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'pint to gallon':
        liquid = float(input('Enter your liquid(pint):'))
        liquid = liquid / 8
        intro3 = 'pint.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'gallon to pint':
        liquid = float(input('Enter your liquid(gallon):'))
        liquid = liquid * 8
        intro3 = 'pint.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'pint to quarter':
        liquid = float(input('Enter your liquid(pint):'))
        liquid = liquid / 2
        intro3 = 'pint.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'quarter to pint':
        liquid = float(input('Enter your liquid(quarter):'))
        liquid = liquid * 2
        intro3 = 'pint.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'pint to liter':
        liquid = float(input('Enter your liquid(pint)'))
        liquid = liquid / 2.113
        intro3 = 'liter.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'liter to pint':
        liquid = float(input('Enter your liquid(liter):'))
        liquid = liquid * 2.113
        intro3 = 'pint.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'pint to ml':
        liquid = float(input('Enter your liquid(pint):'))
        liquid = liquid * 473.18
        intro3 = 'ml.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'ml to pint':
        liquid = float(input('Enter your liquid(ml)'))
        liquid = liquid / 473.18
        intro3 = 'pint.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'gallon to quarter':
        liquid = float(input('Enter your liquid(gallon):'))
        liquid = liquid * 4
        intro3 = 'quarter.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'quarter to gallon':
        liquid = float(input('Enter your liquid(quarter):'))
        liquid = liquid / 4
        intro3 = 'gallon.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'gallon to liter':
        liquid = float(input('Enter your liquid(gallon):'))
        liquid = liquid * 3.785
        intro3 = 'liter.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'liter to gallon':
        liquid = float(input('Enter your liquid(liter):'))
        liquid = liquid / 3.785
        intro3 = 'gallon.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'gallon to ml':
        liquid = float(input('Enter your liquid(gallon):'))
        liquid = liquid *3785
        intro3 = 'ml.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'ml to gallon':
        liquid = float(input('Enter your liquid(ml):'))
        liquid = liquid / 3785
        intro3 = 'gallon.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'quarter to liter':
        liquid = float(input('Enter your liquid(quarter):'))
        liquid = liquid * 1.14
        intro3 = 'liter.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'liter to quarter':
        liquid = float(input('Enter your liquid(liter):'))
        liquid = liquid / 1.14
        intro3 = 'quarter.'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'quarter to ml':
        liquid = float(input('Enter your liquid(quarter):'))
        liquid = liquid * 180
        intro3 = 'ml.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'ml to quarter':
        liquid = float(input('Enter your liquid(ml):'))
        liquid = liquid / 180
        intro3 = 'quarter.'
        print(f'Your liquid is: {liquid}{intro3}')


    elif intro3 == 'liter to ml':
        liquid = float(input('enter your liquid(liter):'))
        liquid = liquid * 1000
        intro3 = 'ml'
        print(f'your liquid is: {liquid}{intro3}')


    elif intro3 == 'ml to liter':
        liquid = float(input('enter your liquid(ml'))
        liquid = liquid / 1000
        intro3 = 'liter.'
        print(f'your liquid is: {liquid}{intro3}')









