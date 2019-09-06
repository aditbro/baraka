<?php
  $no_resi = htmlspecialchars($_GET["no_resi"]);
  
  $conn = new mysqli(server, username, password, database); #bagian ini maksudnya buat koneksi ke database
  $query = "SELECT * FROM tabel_resi WHERE no_resi =".mysql_real_escape_string($no_resi);

  $hasil = $conn->query($query);

  if ($hasil->num_rows > 0) {
    $row = $result->fetch_assoc();
    echo json_encode($row);
  } else {
      http_response_code(404);
  }
?>