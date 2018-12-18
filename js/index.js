

const activeDemos = document.querySelectorAll('.active-demo');


activeDemos.forEach((box) => {
  const liveDemo = box.querySelector('.live-demo');
  const videoDemo = box.querySelector('.video-demo');
  const button = box.querySelector('.demo-toggle');
  button.addEventListener('click', (event) => {
    event.preventDefault();
    liveDemo.classList.toggle('active');
    videoDemo.classList.toggle('active');
    if (videoDemo.classList.contains('active')) {
      button.innerText = 'Live Version';
    } else if (liveDemo.classList.contains('active')) {
      button.innerText = 'Video Walkthrough';
    }
  });
});
