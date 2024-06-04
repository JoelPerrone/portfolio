<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Exercice 2</title>
        <meta name="author" content="Prénom NOM">
        <meta name="description" content="Exercice 2 en PHP">
    </head>
    <body>
        <p>
            <h2>Salutation</h2>
            <?php 
                $sexe = 'homme';
                echo "La valeur de la variable \$sexe : $sexe.";
                if ($sexe == 'homme'){
                    echo "Bonjour monsieur";
                }
                else {
                    echo "Bonjour madame";
                }
            ?>
        </p>
    </body>
</html>