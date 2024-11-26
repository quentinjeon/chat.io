document.getElementById('send-button').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value;
    if (!userInput.trim()) return alert("메시지를 입력하세요!");

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userInput })
        });
        const data = await response.json();

        if (data.error) {
            alert("에러 발생: " + data.error);
        } else {
            displayResponses(data.responses);
        }
    } catch (error) {
        console.error("Error:", error);
    }
});

function displayResponses(responses) {
    const responseList = document.getElementById('response-list');
    responseList.innerHTML = ''; // 기존 응답 삭제

    responses.forEach((response, index) => {
        const li = document.createElement('li');
        li.textContent = `[예상 답변 ${index + 1}]: ${response}`;
        responseList.appendChild(li);
    });
}
