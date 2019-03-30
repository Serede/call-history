<!doctype html>
<html lang="en">

<head>

  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">


  <title>Call History</title>
  <link rel="icon" type="image/png" href="favicon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">

</head>

<body class="p-3 mb-2 bg-dark text-white">

  <ul class="nav nav-pills nav-fill mb-3" id="pills-tab" role="tablist">
    <li class="nav-item">
      <a class="nav-link active" id="pills-incoming-tab" data-toggle="pill" href="#pills-incoming" role="tab" aria-controls="pills-incoming"
      aria-selected="true">Incoming</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" id="pills-outgoing-tab" data-toggle="pill" href="#pills-outgoing" role="tab" aria-controls="pills-outgoing"
      aria-selected="false">Outgoing</a>
    </li>
  </ul>

  <div class="tab-content" id="pills-tabContent">

    <div class="tab-pane fade show active" id="pills-incoming" role="tabpanel" aria-labelledby="pills-incoming-tab">
      <table class="table table-dark table-striped header-fixed">
        <thead class="text-uppercase">
          <tr>
            %for label in incoming_hdr:
            <th scope="col">{{label}}</th>
            %end
          </tr>
        </thead>
        <tbody>
          %for row in incoming:
          <tr>
            %for col in row:
            <td>{{col}}</td>
            %end
          </tr>
          %end
        </tbody>
      </table>
    </div>

    <div class="tab-pane fade" id="pills-outgoing" role="tabpanel" aria-labelledby="pills-outgoing-tab">
      <table class="table table-dark table-striped header-fixed">
        <thead>
          <tr>
            %for label in outgoing_hdr:
            <th scope="col">{{label}}</th>
            %end
          </tr>
        </thead>
        <tbody>
          %for row in outgoing:
          <tr>
            %for col in row:
            <td>{{col}}</td>
            %end
          </tr>
          %end
        </tbody>
      </table>
    </div>

  </div>


  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
</body>

</html>
