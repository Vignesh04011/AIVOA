import api from "../api/api";

export async function chat(message) {

  const response = await api.post("/chat", {
    message,
  });

  return response.data;
}