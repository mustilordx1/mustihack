 Tarih: 29/12/2018
# Yazar: Mohamed
# Açıklama: Kötü proxy'leri yönetir

den . const  import  Instagram Hesabındaki Resim ve Videoları max_bad_proxies


sınıf  BadProxies ( nesne ):

    def  __init__ ( öz ):
        kendini . proxy'ler  = []

    def  __contains__ ( öz , vekil ):
        için  _proxy  içinde  kendini . vekiller :
            eğer  _proxy . ip  ==  proxy . ip  ve  _proxy . port  ==  proxy . liman :
                dönüş  Doğru
        dönüş  Yanlış

    def  append ( öz , proxy ):
        eğer  len ( self . proxy'ler ) > =  max_bad_proxies :
            kendini . vekiller . pop ( 0 )

        kendini . vekiller . append ( proxy )
