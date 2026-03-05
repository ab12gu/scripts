/*
 * filename: script.js
 * date creatd: 26/03/03
*/

function determineStraight(array) {

	for (let i = 0; i < array.length; i++ ) {
		if (
			array[i].reduce( (j, curr) => j + curr, 0)  == 3 || 
			array[0][i] + array[1][i] + array[2][i]  == 3
		) {
			return true;
		}
	}
	if (
		array[0][0] + array[1][1] + array[2][2]  == 3 ||
		array[0][2] + array [1][1] + array [2][0] == 3
	) {
		return true;
	}
}

let array = [ [1, 1, 1], [0, 1, 0], [1, 0, 1] ];
const ifWon = determineStraight(array);
console.log(ifWon)



