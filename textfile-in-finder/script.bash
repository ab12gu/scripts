folder="JavaScript Result"
name="Provided Input"
extension=".txt"
if [ -e "$folder$name$extension" ] ; then
	let i++
	while [ -e "$folder$name($i)$extension" ] ; do
		let i++
	done
	name="$name($i)"
fi
touch "$folder$name$extension"
