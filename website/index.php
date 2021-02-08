<html>
    <head>
        <title>jdst103 Market</title>
    <head>

    <body>
        <h1>Welcome to jdst103 MarketPlace!</h1>

        <h2>Below contains items perfect for playing at gigs, at
          home as a hobby and impressing your mother in law!</h2>

        <ul>
            <?php
                $json = file_get_contents('http://product-service');
                $obj = json_decode($json);

                $products = $obj->products;
                foreach ($products as $product) {
                echo "<li>$product</li>";
                }
            ?>
        <ul>
    <body>
<html>
