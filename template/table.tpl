<!DOCTYPE html>
<html lang="en">
<head>
	<title>Call History</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>
	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
				<h1 style="text-align: center;margin-bottom: 16px;">Incoming</h1>
					<div class="table">

						<div class="row header">
							<div class="cell">
								Time
							</div>
							<div class="cell">
								Phone Port
							</div>
							<div class="cell">
								Phone Number
							</div>
							<div class="cell">
								Duration
							</div>
						</div>

						%for row in incoming:
						<div class="row">
							%for col in row:
							<div class="cell">
								{{col}}
							</div>
							%end
						</div>
						%end

					</div>
			</div>
		</div>
	</div>

	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
				<h1 style="text-align: center;margin-bottom: 16px;">Outgoing</h1>
					<div class="table">

						<div class="row header">
							<div class="cell">
								Time
							</div>
							<div class="cell">
								Phone Port
							</div>
							<div class="cell">
								Phone Number
							</div>
							<div class="cell">
								Duration
							</div>
						</div>

						%for row in outgoing:
						<div class="row">
							%for col in row:
							<div class="cell">
								{{col}}
							</div>
							%end
						</div>
						%end

					</div>
			</div>
		</div>
	</div>

<!--===============================================================================================-->
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

</body>
</html>