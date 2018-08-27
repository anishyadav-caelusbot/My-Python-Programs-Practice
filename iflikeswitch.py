def main():
    numb=dict(
                one='first',
                two='second',
                three='third',
                four='fourth',
                five='fifth',
                )
    v='nine'
    print(numb.get(v,'other'))
main()