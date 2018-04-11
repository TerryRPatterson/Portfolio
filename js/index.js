/*global $*/

let $nav_container = $(".nav_container");

let $nav_menu = $(".nav_menu");

let $demoBoxes = $(".demo-box");

$nav_container.on("click", ()  => {
    $nav_menu.toggleClass("active");
});

$demoBoxes.each((NULL,box) => {
    let liveDemo = box.querySelector(".live-demo");
    let videoDemo = box.querySelector(".video-demo");
    let button = box.querySelector(".demo-toggle");
    button.addEventListener("click", (event) => {
        event.preventDefault();
        liveDemo.classList.toggle("active");
        videoDemo.classList.toggle("active");
        if (videoDemo.classList.contains("active")){
            button.innerText = "Live Version";
        }
        else if (liveDemo.classList.contains("active")){
            button.innerText = "Video Walkthrough";
        }
    });
});
