class LdapEntry:
    def __init__(self, ldap_dict):
        self.objectclass = '::'.join(x.decode('utf-8')
                                     for x in ldap_dict.get('objectclass', [b'']))
        self.cn = ldap_dict.get('cn', [b''])[0].decode('utf-8')
        self.givenName = ldap_dict.get('givenName', [b''])[0].decode('utf-8')
        self.sn = ldap_dict.get('sn', [b''])[0].decode('utf-8')
        self.uidNumber = int(ldap_dict.get(
            'uidNumber', [b'0'])[0].decode('utf-8'))
        self.gidNumber = int(ldap_dict.get(
            'gidNumber', [b'0'])[0].decode('utf-8'))
        self.mail = list(x.decode('utf-8')
                         for x in ldap_dict.get('mail', [b'']))


def main():
    ldapdict = {
        'objectclass': [b'inetOrgPerson', b'person'],
        'cn': [b'George Orwell'],
        'givenName': [b'George'],
        'sn': [b'Orwell'],
        'uidNumber': [b'1984'],
        'gidNumber': [b'1984'],
        'mail': [
            b'george.orwell@example.com',
            b'big.brother@example.com',
        ],
    }
    e = LdapEntry(ldapdict)
    assert(e.cn == 'George Orwell')
    assert(e.uidNumber == 1984)
    assert('big.brother@example.com' in e.mail)
    assert(len(e.mail) == 2)


if __name__ == "__main__":
    main()
