echo "	--> Sartu igorlearen ID kodea: "
read nork
echo "	--> Sartu hartzailearen ID kodea: "
read nori
echo "	--> Sartu enkriptatu nahi duzun mezua (direktorio honetan egon behar du, adib mezua.txt): "
read mezua

echo "	--> Sinatu nahi duzu? (y/n)"
read baiEz

if [ $baiEz == "y" ]
then
	gpg --output $mezua.sig -u $nork --sign $mezua
	gpg -u $nork -r $nori --encrypt $mezua.sig
else
	gpg -u $nork -r $nori --encrypt $mezua
fi

echo "Eginda"

