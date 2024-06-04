<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exercice 1</title>
        <meta name="author" content="Prénom NOM">
        <meta name="description" content="Exercice 1 en PHP">
    </head>
    <body>
        <p>
            <?php 
                $PrixHT = 700.15;
                $TauxTVA = 20;
                $PrixTTC = $PrixHT * (1 + $TauxTVA);
                echo 
                "<ul>
                    <li>'Prix HT :' $PrixHT</li>
                    <li>'Taux TVA :' $TauxTVA</li>
                    <li>'Prix TTC :' $PrixTTC</li>
                </ul>"
            ?>
        </p>
    </body>
</html>