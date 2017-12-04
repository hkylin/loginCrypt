#coding:utf8
import LoginCrypt

if __name__ == '__main__':
    #MD5
    print LoginCrypt.simaple_md5('123456')+'\n'
    #HMAC
    print LoginCrypt.hmac_md5('23336015cc6aae7329c784829e7acd8e','123456')+'\n'
    #RSA
    print LoginCrypt.rsaEnc('admin','8246a46f44fc4d961e139fd70f4787d272d374532f4d2d9b7cbaad6a15a8c1301319aa6b3f30413b859351c71938aec516fa7147b69168b195e81df46b6bed7950cf3a1c719d42175f73d7c97a85d7d20a9e83688b92f05b3059bb2ff75cd7190a042cd2db97ebc2ab4da366f2a7085556ed613b5a39c9fdd2bb2595d1dc23b5','10001')+'\n'
    #DES
    print LoginCrypt.utf16to8(LoginCrypt.desEnc('admin', '123456', None, None))+'\n'

