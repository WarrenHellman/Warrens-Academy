


function story(){
    
    // Can't define a global variable?
    
    // Defines variables for different text sections in about. Removes previous text if it is displayed
    var story = document.getElementById("about-story");    
    var brewing = document.getElementById("about-brewing");
    var mission = document.getElementById("about-mission");

    if (!brewing.classList.contains("about-hide")){
        brewing.classList.toggle("about-hide");
    }
    if (!mission.classList.contains("about-hide")){
        mission.classList.toggle("about-hide");
    }
    if (story.classList.contains("about-hide")){
        story.classList.toggle("about-hide");
    }

    var storyTab = document.getElementById("story-tab");
    var breweryTab = document.getElementById("brewing-tab");
    var missionTab = document.getElementById("mission-tab");
    storyTab.classList.toggle("underline-tab")
    breweryTab.classList.remove("underline-tab")
    missionTab.classList.remove("underline-tab")
}

function brewing() {

    var story = document.getElementById("about-story");    
    var brewing = document.getElementById("about-brewing");
    var mission = document.getElementById("about-mission");

    if (brewing.classList.contains("about-hide")){
        brewing.classList.toggle("about-hide");
    }
    if (!mission.classList.contains("about-hide")){
        mission.classList.toggle("about-hide");
    }
    if (!story.classList.contains("about-hide")){
        story.classList.toggle("about-hide");
    }

    var storyTab = document.getElementById("story-tab");
    var breweryTab = document.getElementById("brewing-tab");
    var missionTab = document.getElementById("mission-tab");
    storyTab.classList.remove("underline-tab")
    breweryTab.classList.toggle("underline-tab")
    missionTab.classList.remove("underline-tab")
}

function mission() {

    var story = document.getElementById("about-story");    
    var brewing = document.getElementById("about-brewing");
    var mission = document.getElementById("about-mission");

    if (!brewing.classList.contains("about-hide")){
        brewing.classList.toggle("about-hide");
    }
    if (mission.classList.contains("about-hide")){
        mission.classList.toggle("about-hide");
    }
    if (!story.classList.contains("about-hide")){
        story.classList.toggle("about-hide");
    }
    var storyTab = document.getElementById("story-tab");
    var breweryTab = document.getElementById("brewing-tab");
    var missionTab = document.getElementById("mission-tab");
    storyTab.classList.remove("underline-tab")
    breweryTab.classList.remove("underline-tab")
    missionTab.classList.toggle("underline-tab")
}

// apply a class to bring focus to current tab and dim the others

// Slideshow from W3Schools

var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1} 
    slides[slideIndex-1].style.display = "block"; 
    setTimeout(showSlides, 5000); // Change image every 5 seconds
}
