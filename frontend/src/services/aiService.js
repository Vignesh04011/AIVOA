import api from "../api/api";

export async function chat(message, interaction) {

  const response = await api.post("/chat", {
    message,
    interaction,
  });

  return response.data;
}