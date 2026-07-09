import api from "../api/api";

export const createInteraction = async (data) => {
  const response = await api.post("/interactions", data);

  return response.data;
};