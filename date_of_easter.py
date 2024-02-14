import math

def test(year):
    G = year % 19
    C = math.floor(year / 100)
    D = C - C / 4
    E = math.floor((8 * C + 13) / 25)
    I = (19 * G + 15) % 30
    H = (D - E + 19 * G + 15) % 30
    K = H / 28
    P = 29 / (H + 1)
    Q = (21 - G) / 11
    I = H - K * (1 - K * P * Q)
    J = (year + year / 4 + I + 2 - D) % 7
    R = 28 + I + J
    
    if R <= 31:
        return f'{int(R)}-03-{year}'
    return f'{int(R)-31}-04-{year}'

def myeaster(year):
    # Selon wikipedia
    # ÇA FONCTIONNE !!!!
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19*a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2*e + 2*i - h -k) % 7
    m = (a + 11*h + 22*l) // 451
    n = (h + l - 7*m + 114) // 31
    p = (h + l - 7*m + 114) % 31

    return f'{p+1}-{n}-{year}'

print(myeaster(2004))


print( test(2023) )
