<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title>Call History</title>

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">


  <link rel="stylesheet" href="css/style.css">


</head>

<body>
  <section>
    <!--for demo wrap-->
    <h1>Incoming</h1>
    <div class="tbl-header">
      <table cellpadding="0" cellspacing="0" border="0">
        <thead>
          <tr>
            %for label in incoming_hdr:
            <th>label</th>
            %end
          </tr>
        </thead>
      </table>
    </div>
    <div class="tbl-content">
      <table cellpadding="0" cellspacing="0" border="0">
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
  </section>
  <section>
    <h1>Outgoing</h1>
    <div class="tbl-header">
      <table cellpadding="0" cellspacing="0" border="0">
        <thead>
          <tr>
            %for label in outgoing_hdr:
            <th>{{label}}</th>
            %end
          </tr>
        </thead>
      </table>
    </div>
    <div class="tbl-content">
      <table cellpadding="0" cellspacing="0" border="0">
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
  </section>

  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

  <script src="js/index.js"></script>

</body>

</html>