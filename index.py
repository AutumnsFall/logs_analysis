HTML_WRAP = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Logs analysis</title>

	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

	<style>

	.mg-top {
		margin-top: 20px;
	}

	</style>


</head>
<body>
<div class="container">
	<div>
		<h2> Most Popular Top Three articles of All Time </h2>
	</div>
	<div class="row">
		<div class="col-md-12">
			<table class="table table-hover">
				<thead>
					<tr>
						<th>Article Name</th>
						<th>View</th>
					</tr>
				</thead>
				<tbody>
					%s
				</tbody>
			</table>
		</div>
		<div>
			<h2> Most Popular Article Authors of All Time </h2>
		</div>
		<div class="col-md-12 mg-top">
			<table class="table table-hover">
				<thead>
					<tr>
					   	<th>Author Name</th>
					   	<th>Total Views</th>
					</tr>
				</thead>
				<tbody>
					%s
				</tbody>
			</table>
		</div>
		<div>
			<h2> Dates With More Than One Percent Errors on Requests</h2>
		</div>
		<div class="col-md-12 mg-top">
			<table class="table table-hover">
				<thead>
					<tr>
					   	<th>Date</th>
					   	<th>Last Name</th>
					</tr>
				</thead>
				<tbody>
					%s
				</tbody>
			</table>
		</div>

	</div>
</div>
</body>
</html>
'''

ARTICLES_ROW = '''
<tr>
	<td>%s</td>
	<td>%s</td>
</tr>
'''

AUTHORS_ROW = '''
<tr>
	<td>%s</td>
	<td>%s</td>
</tr>
'''

ERRORS_ROW = '''
<tr>
	<td>%s</td>
	<td>%s</td>
</tr>
'''

EMPTY_RETURN = '''
<tr>
	<td>Not Avilable</td>
	<td>Not Avilable</td>
</tr>
'''
