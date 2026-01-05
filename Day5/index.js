
let currentPlayer = 'X';
let gameActive = true;
let gameState = ['', '', '', '', '', '', '', '', ''];
let scores = { X: 0, O: 0, draw: 0 };

const cells = document.querySelectorAll('[data-cell]');
const board = document.getElementById('board');
const resetBtn = document.getElementById('reset');
const turnText = document.getElementById('turn-text');
const modal = document.getElementById('modal');
const modalClose = document.getElementById('modal-close');
const resultIcon = document.getElementById('result-icon');
const resultText = document.getElementById('result-text');
const confettiContainer = document.getElementById('confetti');
const scoreX = document.getElementById('score-x');
const scoreO = document.getElementById('score-o');
const scoreDraw = document.getElementById('score-draw');



const winPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
    [0, 4, 8], [2, 4, 6]             // diagonals
];


const xSVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="80" height="80">
    <line x1="20" y1="20" x2="80" y2="80" stroke="#ff6b6b" stroke-width="8" stroke-linecap="round"/>
    <line x1="80" y1="20" x2="20" y2="80" stroke="#ff6b6b" stroke-width="8" stroke-linecap="round"/>
</svg>`;

const oSVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="80" height="80">
    <circle cx="50" cy="50" r="30" stroke="#4ecdc4" stroke-width="8" fill="none"/>
</svg>`;


cells.forEach((cell, index) => {
    cell.addEventListener('click', () => handleCellClick(index));
});

resetBtn.addEventListener('click', resetGame);
modalClose.addEventListener('click', closeModal);

function handleCellClick(index) {
    if (gameState[index] !== '' || !gameActive) return;

    gameState[index] = currentPlayer;
    updateCell(cells[index], currentPlayer);
    
    if (checkWin()) {
        endGame(false);
    } else if (checkDraw()) {
        endGame(true);
    } else {
        switchPlayer();
    }
}

function updateCell(cell, player) {
    cell.classList.add(player.toLowerCase());
    if (player === 'X') {
        cell.innerHTML = xSVG;
    } else {
        cell.innerHTML = oSVG;
    }
}

function switchPlayer() {
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    turnText.textContent = `Player ${currentPlayer}'s Turn`;
    turnText.style.color = currentPlayer === 'X' ? '#ff6b6b' : '#4ecdc4';
}

function checkWin() {
    for (let pattern of winPatterns) {
        const [a, b, c] = pattern;
        if (gameState[a] && gameState[a] === gameState[b] && gameState[a] === gameState[c]) {
            highlightWinner(pattern);
            return true;
        }
    }
    return false;
}

function highlightWinner(pattern) {
    pattern.forEach(index => {
        cells[index].classList.add('winner');
    });
}

function checkDraw() {
    return gameState.every(cell => cell !== '');
}

function endGame(isDraw) {
    gameActive = false;
    
    setTimeout(() => {
        if (isDraw) {
            showResult('draw');
            scores.draw++;
            scoreDraw.textContent = scores.draw;
        } else {
            showResult(currentPlayer);
            scores[currentPlayer]++;
            if (currentPlayer === 'X') {
                scoreX.textContent = scores.X;
            } else {
                scoreO.textContent = scores.O;
            }
            createConfetti();
        }
    }, 500);
}

function showResult(winner) {
    modal.classList.add('show');
    
    if (winner === 'draw') {
        resultIcon.textContent = '🤝';
        resultText.textContent = "It's a Draw!";
        resultText.style.color = '#ffd93d';
    } else {
        resultIcon.textContent = winner === 'X' ? '🎉' : '🎊';
        resultText.textContent = `Player ${winner} Wins!`;
        resultText.style.color = winner === 'X' ? '#ff6b6b' : '#4ecdc4';
    }
}

function closeModal() {
    modal.classList.remove('show');
}

function resetGame() {
    gameActive = true;
    currentPlayer = 'X';
    gameState = ['', '', '', '', '', '', '', '', ''];
    turnText.textContent = "Player X's Turn";
    turnText.style.color = '#ff6b6b';
    
    cells.forEach(cell => {
        cell.classList.remove('x', 'o', 'winner');
        cell.innerHTML = '';
    });
    
    closeModal();
    confettiContainer.innerHTML = '';
}

function createConfetti() {
    const colors = ['#ff6b6b', '#4ecdc4', '#ffd93d', '#667eea', '#764ba2'];
    
    for (let i = 0; i < 50; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = Math.random() * 0.5 + 's';
        confetti.style.animationDuration = Math.random() * 2 + 2 + 's';
        confettiContainer.appendChild(confetti);
    }
    
    setTimeout(() => {
        confettiContainer.innerHTML = '';
    }, 4000);
}