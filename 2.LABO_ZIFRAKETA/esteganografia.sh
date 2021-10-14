zip=$(find /home/maite/ -name irudia.zip 2>/dev/null|head -n 1)
cd /home/maite/Escritorio
mkdir irudia 2> /dev/null
cp $zip irudia
cd irudia
unzip irudia.zip
irudia=$(md5sum * | grep "e5ed313192776744b9b93b1320b5e268" | head -n 1 | cut -d " " -f3)
echo "EXTRACT BOTOIA SAKATU MEZUA IRAKURTZEKO!"
stegosuite $irudia


