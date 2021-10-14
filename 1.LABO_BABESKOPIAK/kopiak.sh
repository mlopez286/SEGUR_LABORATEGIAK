atzo=$(echo "/var/tmp/Backups/"$(date --date='1 day ago' +%F))
gaur=$(echo "/var/tmp/Backups/"$(date +%F))
unekoa=$(sudo find /home/maite/Escritorio -name Segurtasuna 2>/dev/null |head -n 1)

if [ ! -d $atzo ]
then
	mkdir $atzo
fi
	mkdir $gaur 2> /dev/null
	rsync -av --compare-dest=$atzo $unekoa $gaur


echo "Eginda"
