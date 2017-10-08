if __name__ == '__main__':
    with open('vmctf.html') as f:
        data = f.read()
        print(data)

    for i in reversed(range(1, 50)):
        co = 'Co' * i
        data = data.replace(co, 'var_%d_' % i)

    with open('vmctf.html', 'w') as f:
        f.write(data)
