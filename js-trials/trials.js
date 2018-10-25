/////////////////////////////////////////////////////////
// PART 1

/////////////////////////////////////////////////////////
// Show Profile Info


function showProfile(name, catchphrase, location) {

	console.log("PROFILE:\n" + `name: ${name}\n catchphrase: ${catchphrase}\n location: ${location}`);

	}

showProfile("Skittle","Mrrr","Lake");

// Add function to prnt profile info


/////////////////////////////////////////////////////////
// // Display Likes



function showLikes() {

	const interests = [
	  'being annoying',
	  'seeds',
	  'staring at human food'
	];
	console.log("THINGS I LIKE:");
	for (let interest of interests) {
		console.log(interest);
	}
	
	}
	

 showLikes();

// Add function to print interests



///////////////////////////////////////////////////////
// Display Favorites


// Add function to print favorites
function showFavorites() {

	const favorites = {
	food: "pebbles",
	tree: "palm",
	quote: "Bock bock bock" 
  // Add more favorites
	};
	return favorites; 

}
let favorites = showFavorites();


/////////////////////////////////////////////////////////
// PART 2

/////////////////////////////////////////////////////////
// Add Transactions

// Add function to add transaction
function addTransaction(date, amount, transactions) {


	transactions[date] = amount
	return transactions;
}

addTransaction("May2", 2500, {});
// Create object to hold transactions

// Add transactions to object


/////////////////////////////////////////////////////////
// Get Balance Status

// Add function to calculate balance status



/////////////////////////////////////////////////////////
// Calculate Current Balance

// Add function to calculate and return current balance


/////////////////////////////////////////////////////////
// Show Account Activity

// Add function to print account activity



/////////////////////////////////////////////////////////
// Creating a User Object

// Add user object

// Add function to print user dashboard



/////////////////////////////////////////////////////////
// PART 3

// Add object that keeps track of premium members

// Add function to return emails of premium members



/////////////////////////////////////////////////////////
// PART 4

// Add function to assign interns to workdays

// Add a function to generate customer support hours

