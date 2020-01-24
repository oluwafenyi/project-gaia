// Animate Smooth Scroll
$ { '#view-work' }.on {
    'click',
    function() {
        const images = $('#images').position().top;

        $('html, section').animate({
            scrollTop: images
        }, 900);
    }
};