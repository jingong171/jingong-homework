m = 1189
n = 467
if (m>n):
    if (m%n == 0):
        print('最大公约数是'+str(n))
        print('最小公倍数是'+str(m))
    else:
        a=list(range(2,n));
        b=list(reversed(a))
        for x in a:
            if (m%x == 0 and n%x == 0):
                print('最大公约数是'+str(x))
                m_1 = m/x
                n_1 = n/x
                print('最小公倍数是'+str(m_1 * n_1 * x))
                break;
            else:
                print('互质')
                break;
                
else:
    if (n%m == 0):
        print('最大公约数是'+str(m))
        print('最小公倍数是'+str(n))
    else:
        a=list(range(2,m));
        b=list(reversed(a));
        for x in b:
            if (m%x == 0 and n%x == 0):
                print('最大公约数是'+str(x))
                m_1 = m/x
                n_1 = n/x
                print('最小公倍数是'+str(m_1 * n_1 * x))
                break;
            else:
                print('互质')
                break;

               
