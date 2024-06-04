document.addEventListener('DOMContentLoaded', function() {
    var boutonDep = document.querySelectorAll('.btdep');

    boutonDep.forEach(function(button) {
        button.addEventListener('click', function() {
            var content = this.nextElementSibling;

            // Toggle between hiding and showing the content
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                // Hide all accordion content before showing the current one
                var allContents = document.querySelectorAll('.btdep-contenu');
                allContents.forEach(function(c) {
                    c.style.display = 'none';
                });

                content.style.display = "block";
            }
        });
    });
});

function showContent(sectionId) {
    var sections = document.getElementsByClassName('content-section');
    for (var i = 0; i < sections.length; i++) {
        sections[i].style.display = 'none';
    }
    document.getElementById(sectionId).style.display = 'block';
}

// Show the first section by default
document.getElementById('section1').style.display = 'block';