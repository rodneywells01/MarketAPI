# Populate your local database with some sample data.
# Execute `start_db.sh` before running this script.

mongo localhost/WatchList --eval '
	var sample_data = [{
		username: "stephenmoring01",
		age: 21,
		occupation: "Associate Software Engineer",
		watchlist: [
			"MU",
			"AMD",
			"TCON",
			"CSX",
		]
	}, {
	username: "rodneywells01",
	age: 23,
	occupation: "Senior Data Engineer",
	watchlist: [
		"MU",
		"AMD",
		"COF",
		"TSLA"
	]
	}];

	db.users.insert(sample_data);
'
