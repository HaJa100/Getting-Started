const display = document.getElementById('display');

function appendChar(char) {
    if (display.value === '0' && char !== '.') {
        display.value = char;
    } else {
        display.value += char;
    }
}

function clearDisplay() {
    display.value = '0';
}

async function calculate() {
    const expression = display.value;
    
    if (!expression || expression === '0') {
        return;
    }

    try {
        const response = await fetch('/api/calc', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: expression })
        });

        const data = await response.json();

        if (data.error) {
            display.value = 'Error: ' + data.error;
        } else {
            // Format result to avoid too many decimal places
            const result = typeof data.result === 'number' 
                ? (Math.round(data.result * 100000000) / 100000000).toString()
                : data.result;
            display.value = result;
        }
    } catch (error) {
        display.value = 'Error: ' + error.message;
    }
}

// Handle keyboard input
document.addEventListener('keydown', (e) => {
    if (e.key >= '0' && e.key <= '9') appendChar(e.key);
    if (e.key === '+' || e.key === '-' || e.key === '*' || e.key === '/') appendChar(e.key);
    if (e.key === '.') appendChar('.');
    if (e.key === '(' || e.key === ')') appendChar(e.key);
    if (e.key === 'Enter' || e.key === '=') calculate();
    if (e.key === 'Backspace') {
        if (display.value.length > 1) {
            display.value = display.value.slice(0, -1);
        } else {
            display.value = '0';
        }
    }
    if (e.key === 'Escape') clearDisplay();
});