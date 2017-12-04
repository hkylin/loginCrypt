使用方法:

simaple_md5()：
正常的MD5加密，如：simaple_md5md5('12346')

hmac_md5()：
函数第一个参数为随机密钥值,该值在网页源码中查找即可,第二个参数为待加密的明文,如：
hmac_md5('23336015cc6aae7329c784829e7acd8e','123456')

rsaEnc()：
函数第一个参数为待加密的明文，第二个参数为modulus即n值，第三个参数为exponent即e值，后面两个参数皆存在源码或js文件中，其中e值通常默认为十六进制的10001
rsaEnc('admin','8246a46f44fc4d961e139fd70f4787d272d374532f4d2d9b7cbaad6a15a8c1301319aa6b3f30413b859351c71938aec516fa7147b69168b195e81df46b6bed7950cf3a1c719d42175f73d7c97a85d7d20a9e83688b92f05b3059bb2ff75cd7190a042cd2db97ebc2ab4da366f2a7085556ed613b5a39c9fdd2bb2595d1dc23b5','10001')

desEnc()：
函数第一个参数为待加密的明文,后面三个参数分别为需要输入的key,同样存在于源码或js文件中：
utf16to8(desEnc('admin', '123456', None, None))
