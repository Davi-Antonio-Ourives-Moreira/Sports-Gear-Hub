
window.onload = function() {
    
    document.querySelector('.icon-container').style.opacity = '1';
    document.querySelector('.message').style.opacity = '1';
};


window.onload = function() {
    
    const xIcon = document.querySelector('.x-icon');

    setTimeout(() => {
        xIcon.style.opacity = '1';
    }, 1000); 
};


window.onload = function() {
    
    const countdownTime = 0.1 * 60; 
    let timeRemaining = countdownTime;

    const timerElement = document.getElementById('timer');

    function updateTimer() {
        const minutes = Math.floor(timeRemaining / 60);
        const seconds = timeRemaining % 60;
        timerElement.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    }

    function countdown() {
        if (timeRemaining <= 0) {
            
            window.location.href = 'https://sports-gear-hub.onrender.com/'; 
            return;
        }

        timeRemaining--;
        updateTimer();
        setTimeout(countdown, 1000); 
    }

    
    updateTimer();
    countdown();
};

