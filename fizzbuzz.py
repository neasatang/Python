for i in range(1,101):
    ans = ''
    if i % 3 == 0:
        ans += 'fizz'
    if i % 5 == 0:
        ans += 'buzz'
    print ans or i
