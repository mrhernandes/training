#!/bin/bash
### Simulando um backup diario
export BKPDIR="/dados"
export ARQBKP="arq-diario.tar.gz"
if [ ! -d $BKPDIR ]
        then echo "Diretorio /dados nao existe mas sera criado!"
        mkdir /dados
        ls -ld $BKPDIR
        else echo "Diretorio $BKPDIR ja existe; iniciando backup..."
fi
find /etc/ -name *.conf -exec cp {} $BKPDIR \;
cd $BKPDIR
tar zcvf $ARQBKP $BKPDIR/*
ls -lh $BKPDIR/$ARQBKP
if [ $? -eq 0 ]
        then
                zabbix_sender -z 127.0.0.1 -p 10051 -s test -k test -o "Backup diario realizado com sucesso em `date +%Y%m%d-%H:%M:%S`"
                rm -f $BKPDIR/*.conf
                exit 0
        else
                zabbix_sender -z 127.0.0.1 -p 10051 -s test -k test -o "Falha em Backup diario - `date +%Y%m%d-%H:%M:%S`"
                exit 1
fi
exit 0
