const API_URL = "http://127.0.0.1:5000";

const chatArea = document.getElementById("chatArea");
const perguntaInput = document.getElementById("pergunta");
const materiaSelect = document.getElementById("materia");
const modoSelect = document.getElementById("modo");
const enviarBtn = document.getElementById("enviarBtn");
const limparBtn = document.getElementById("limparBtn");
const statusBadge = document.getElementById("statusBadge");

function formatTextToHtml(text) {
  let html = text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

  // títulos markdown ##
  html = html.replace(/^## (.*)$/gm, "<h3>$1</h3>");

  // negrito simples **texto**
  html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

  // quebras de linha
  html = html.replace(/\n/g, "<br>");

  return html;
}

function createMessageElement(type, title, content) {
  const wrapper = document.createElement("div");
  wrapper.className = `message ${type}`;

  const avatar = document.createElement("div");
  avatar.className = "message-avatar";
  avatar.textContent = type === "ai" ? "S+" : "Você";

  const bubble = document.createElement("div");
  bubble.className = "message-bubble";

  const finalTitle = title ? `<h3>${title}</h3>` : "";
  bubble.innerHTML = `${finalTitle}<p>${formatTextToHtml(content)}</p>`;

  wrapper.appendChild(avatar);
  wrapper.appendChild(bubble);

  return wrapper;
}

function addUserMessage(text) {
  const message = createMessageElement("user", "Sua pergunta", text);
  chatArea.appendChild(message);
  scrollToBottom();
}

function addAiMessage(title, content) {
  const message = createMessageElement("ai", title, content);
  chatArea.appendChild(message);
  scrollToBottom();
}

function addTemporaryAiMessage() {
  const wrapper = document.createElement("div");
  wrapper.className = "message ai";
  wrapper.id = "typing-message";

  wrapper.innerHTML = `
    <div class="message-avatar">S+</div>
    <div class="message-bubble">
      <h3>Study+ está pensando...</h3>
      <p>Preparando sua resposta de estudos.</p>
    </div>
  `;

  chatArea.appendChild(wrapper);
  scrollToBottom();
}

function removeTemporaryAiMessage() {
  const temp = document.getElementById("typing-message");
  if (temp) temp.remove();
}

function scrollToBottom() {
  chatArea.scrollTop = chatArea.scrollHeight;
}

async function checkBackend() {
  try {
    const response = await fetch(`${API_URL}/api/health`);
    if (!response.ok) throw new Error("Backend indisponível");

    const data = await response.json();
    if (data.status === "ok") {
      statusBadge.textContent = "Backend conectado";
      statusBadge.classList.add("ok");
      statusBadge.classList.remove("error");
    }
  } catch (error) {
    statusBadge.textContent = "Backend offline";
    statusBadge.classList.add("error");
    statusBadge.classList.remove("ok");
  }
}

async function enviarPergunta() {
  const pergunta = perguntaInput.value.trim();
  const materia = materiaSelect.value;
  const modo = modoSelect.value;

  if (!pergunta) {
    alert("Digite uma pergunta ou tema para estudar.");
    return;
  }

  addUserMessage(pergunta);
  perguntaInput.value = "";
  addTemporaryAiMessage();

  try {
    const response = await fetch(`${API_URL}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        pergunta,
        materia,
        modo
      })
    });

    if (!response.ok) {
      throw new Error("Erro ao buscar resposta do backend.");
    }

    const data = await response.json();
    removeTemporaryAiMessage();

    if (data.ok && data.resposta) {
      addAiMessage(data.resposta.titulo, data.resposta.conteudo);
    } else {
      addAiMessage("Erro", "O Study+ não conseguiu gerar uma resposta agora.");
    }
  } catch (error) {
    removeTemporaryAiMessage();
    addAiMessage(
      "Erro de conexão",
      "Não foi possível conectar ao backend do Study+. Verifique se o Flask está rodando na porta 5000."
    );
  }
}

function limparChat() {
  chatArea.innerHTML = `
    <div class="message ai">
      <div class="message-avatar">S+</div>
      <div class="message-bubble">
        <h3>Chat limpo</h3>
        <p>Envie uma nova pergunta para continuar estudando com o Study+.</p>
      </div>
    </div>
  `;
}

enviarBtn.addEventListener("click", enviarPergunta);

perguntaInput.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
    enviarPergunta();
  }
});

limparBtn.addEventListener("click", limparChat);

checkBackend();
