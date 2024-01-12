// Countdown timer function
function countdown() {
  const launchDate = new Date('2024-02-28T00:00:00Z').getTime(); // Updated launch date to February 28, 2024
  const now = new Date().getTime();
  const distance = launchDate - now;

  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById('countdown').innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

  if (distance < 0) {
    clearInterval(timer);
    document.getElementById('countdown').innerHTML = 'Site is live!';
  }
}

// Update the countdown every second
const timer = setInterval(countdown, 1000);

// Initial call to start countdown immediately
countdown();
