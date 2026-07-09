import api from "../api/api";

export async function parseInteraction(text) {
  const response = await api.post("/parse-interaction", {
    text,
  });

  return response.data;
}