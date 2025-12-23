const API_BASE = "https://n8n-your-domain/webhook";

const studentId = localStorage.getItem("studentId");
if (!studentId && !document.getElementById("studentId")) {
  window.location.href = "index.html";
}

// Login
function login() {
  const studentId = document.getElementById("studentId").value;
  localStorage.setItem("studentId", studentId);
  window.location.href = "dashboard.html";
}

// Load thời khóa biểu
if (document.getElementById("scheduleTable")) {
  fetch(`${API_BASE}/get-schedule`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ studentId })
  })
    .then(res => res.json())
    .then(data => {
      let html = "";
      data.forEach(item => {
        html += `
          <tr>
            <td>${item.day}</td>
            <td>${item.subject}</td>
            <td>${item.room}</td>
            <td>${item.time}</td>
          </tr>
        `;
      });
      document.getElementById("scheduleTable").innerHTML = html;
    });
}

// Load bảng điểm
if (document.getElementById("scoreTable")) {
  fetch(`${API_BASE}/get-score`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ studentId })
  })
    .then(res => res.json())
    .then(data => {
      let html = "";
      data.forEach(item => {
        html += `
          <tr>
            <td>${item.subject}</td>
            <td>${item.mid}</td>
            <td>${item.final}</td>
            <td>${item.total}</td>
          </tr>
        `;
      });
      document.getElementById("scoreTable").innerHTML = html;
    });
}

// Toggle chatbot popup
function toggleChat() {
  const popup = document.getElementById("chatPopup");
  if (!popup) return;

  popup.style.display =
    popup.style.display === "flex" ? "none" : "flex";
}

// Chatbot
function sendMessage() {
  const msg = document.getElementById("chatInput").value;
  const chatBox = document.getElementById("chatBox");

  if (!msg) return;

  chatBox.innerHTML += `<div><b>Bạn:</b> ${msg}</div>`;

  fetch(`${API_BASE}/chatbot`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      studentId,
      message: msg
    })
  })
    .then(res => res.json())
    .then(data => {
      chatBox.innerHTML += `<div><b>AI:</b> ${data.answer}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    });

  document.getElementById("chatInput").value = "";
}
