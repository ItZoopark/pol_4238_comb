alphabet = 'АПЕЛЬСИН'
consonants = 'ПЛСН'
count = 0
for ch1 in alphabet:
    for ch2 in alphabet:
        for ch3 in alphabet:
            for ch4 in alphabet:
                for ch5 in alphabet:
                    for ch6 in alphabet:
                        for ch7 in alphabet:
                                res = ch1 + ch2 + ch3 + ch4 + ch5 + ch6 + ch7
                                isMatch = True
                                for alpha in alphabet:
                                    if res.count(alpha) > 1:
                                        isMatch = False
                                        break
                                if isMatch:
                                    if 'Ь' not in res:
                                        count += 1
                                    else:
                                        indexЬ = res.index('Ь')
                                        if 0 < indexЬ < len(res)-1:
                                            if (res[indexЬ-1] in consonants) and (res[indexЬ + 1] in consonants):
                                                count += 1


print(count)