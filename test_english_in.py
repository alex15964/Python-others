aaa = 'A12cd3e.sef'


def domain_of_ip(site):
    for item in site:
        if item.isalpha():
            return True
    return False

print(domain_of_ip(aaa))