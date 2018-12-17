while True:
    print('Enter q to quit')
    firstnumber = input('Please enter the first number:')
    if firstnumber == 'q':
        break
    secondnumber = input('Please enter the second number:')
    if secondnumber == 'q':
        break
    #下面进行ValueError的错误处理
    try:
        sum = int(firstnumber) + int(secondnumber)
    except ValueError:
        print('The number you have entered is wrong.')
    else:
        print('The sum of two numbers is ' + str(sum))
        
